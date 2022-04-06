#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: build.py

:Synopsis:

:Author:
    servilla

:Created:
    2/20/22
"""
from pathlib import Path
import platform

from bs4 import BeautifulSoup
import click
import daiquiri
import markdown
from markdown.extensions.toc import TocExtension
import logging
import os

cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/build.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


def safe_image_copy(source: str, target: str, image_files: list, images: list, verbose: int, dryrun: bool):
    if not Path(target).exists() and not Path(target).is_dir():
        msg = f"The target '{target}' either does not exist or is not a directory - bye!"
        raise IOError(msg)
    else:
        os = platform.system()
        for image in images:
            found = False
            if os == "Windows":
                image = image.replace("/", "\\")
            for image_file in image_files:
                if image in str(image_file):
                    found = True
                    copy_path = str(image_file).replace(source, target)
                    if verbose > 0:
                        print(f"Copying: '{image_file}' to '{copy_path}")
                    if not dryrun:
                        img = Path(image_file).open("rb").read()
                        path = Path(copy_path)
                        path.parent.mkdir(exist_ok=True, parents=True)
                        path.open("wb").write(img)
                    break
            if not found:
                msg = f"Image '{image}' not found in '{source}'!"
                raise FileNotFoundError(msg)


def safe_html_write(target: str, html_file: str, html: str, verbose: int, dryrun: bool):
    if not Path(target).exists() and not Path(target).is_dir():
        msg = f"The target '{target}' either does not exist or is not a directory - bye!"
        raise IOError(msg)
    else:
        if verbose > 0:
            print(f"Writing: {html_file}")
        if verbose == 2:
            print(html)
        if not dryrun:
            path = Path(html_file)
            path.parent.mkdir(exist_ok=True, parents=True)
            path.open("w", encoding="utf-8").write(html)


def get_md_files(source: str, ignore: tuple) -> list:
    files = []
    if Path(source).is_dir():
        for obj in Path(source).rglob("*.md"):
            if Path(obj).is_file() and Path(obj).name not in ignore:
                files.append(obj)
    else:
        msg = f"Source '{source}' is not a directory!"
        raise IOError(msg)
    return files


def get_image_files(source: str, extensions: tuple) -> list:
    files = []
    if Path(source).is_dir():
        for extension in extensions:
            ext = f"*.{extension.lower()}"
            for obj in Path(source).rglob(ext):
                if Path(obj).is_file():
                    files.append(obj)
            ext = f"*.{extension.upper()}"
            for obj in Path(source).rglob(ext):
                if Path(obj).is_file():
                    files.append(obj)
    else:
        msg = f"Source '{source}' is not a directory!"
        raise IOError(msg)
    return files


def get_html_images(html: str) -> list:
    images = []
    soup = BeautifulSoup(html, "lxml")
    imgs = soup.find_all("img")
    for img in imgs:
        src: str = img["src"]
        if src.startswith("/static/images/"):
            images.append(src)
    return images


def template_sidebar(inner_html: str) -> str:
    open = """
<div metal:use-macro="load: ../shared/layout.html">
<div metal:fill-slot="content" tal:omit-tag="True">
<div class="container">
<main class="main-tutorial">
"""

    close = """
</main>
</div>
</div>
</div>
</div>
"""
    return open + inner_html + close


def sidebar_html(md: str) -> BeautifulSoup:
    inner_html = markdown.markdown(
        md,
        extensions=[TocExtension(marker='[TOC]', toc_depth='2-6'), 'tables', 'fenced_code']
    )
    html = template_sidebar(inner_html)
    soup = BeautifulSoup(html, "lxml")
    toc = soup.find("div", attrs={"class": "toc"}).extract()
    h1 = soup.find("h1")
    h1_a = soup.new_tag(
        "a",
        attrs={"href": "#", "class": "d-flex align-items-center mb-2 link-dark text-decoration-none"}
    )
    h1_span = soup.new_tag("span", attrs={"class": "fs-5 fw-semibold"})
    h1_span.string = h1.get_text()
    h1_a.insert(0, h1_span)
    toc.insert(1, h1_a)
    for tag in toc.find_all('ul'):
        if 'ul' in tag.name:
            tag['class'] = 'fw-normal'
    ul_tag = toc.find('ul')  # Class of the first <ul> is different
    ul_tag['class'] = "btn-toggle-nav"
    for li in toc.find_all('li'):
        for a in li.find_all('a'):
            a['class'] = 'link-dark rounded'
    toc["class"] = "flex-shrink-0 py-5 px-1 bg-white sticky-top"
    aside = soup.new_tag("aside")
    aside["class"] = "sidebar-aside"
    aside.insert(0, toc)
    main_tag = soup.find("main")
    main_tag.insert_before(aside)
    return soup


def template_basic(inner_html: str) -> str:
    open = """
<div metal:use-macro="load: ../shared/layout.html">
<div metal:fill-slot="content" tal:omit-tag="True">
<main class="main-tutorial">
"""

    close = """
</main>
</div>
</div>
"""
    return open + inner_html + close


def basic_html(md: str) -> BeautifulSoup:
    inner_html = markdown.markdown(md, extensions=['tables', 'fenced_code'])
    html = template_basic(inner_html)
    soup = BeautifulSoup(html, "lxml")
    return soup


def template_featured_data(inner_html: str) -> str:
    open = '<main class="main-tutorial">\n'
    close = "\n</main>"
    return open + inner_html + close


def featured_data_html(md: str) -> BeautifulSoup:
    inner_html = markdown.markdown(md, extensions=['tables', 'fenced_code'])
    html = template_featured_data(inner_html)
    soup = BeautifulSoup(html, "lxml")
    return soup


def template_news(inner_html: str) -> str:
    open = '<main class="main-tutorial">\n'
    close = "\n</main>"
    return open + inner_html + close


def news_html(md: str) -> BeautifulSoup:
    inner_html = markdown.markdown(md, extensions=['tables', 'fenced_code'])
    html = template_news(inner_html)
    soup = BeautifulSoup(html, "lxml")
    return soup


def md2html(md_file: str, verbose: int) -> str:
    try:
        if verbose > 0:
            print(f"Reading: {md_file}")
        md = Path(md_file).open("r", encoding="utf-8").read()
        md = md.replace(".md", "")
        md = md.replace("/templates/", "/")
        if "[TOC]" in md:
            html = str(sidebar_html(md))
        elif "# Featured Data" in md:
            html = str(featured_data_html(md))
        elif "# News" in md:
            html = str(featured_data_html(md))
        else:
            html = str(basic_html(md))
        return html
    except IOError as ex:
        logger.error(f"{ex} - {md_file}")
    except AttributeError as ex:
        logger.error(f"{ex} - {md_file}")


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
help_ignore = "Ignore markdown file (may repeat for multiple files)."
help_markdown = "Full path to markdown file (may repeat for multiple files; cannot be used with --file)."
help_file = "File containing markdown files to be processes one per line (cannot be used with --markdown)."
help_extensions = (
    "Extension of image files to copy (may repeat for multiple extensions; default is "
    "png, svg, jpg, and jpeg)."
)
help_verbose = "Send output to standard out (-v or -vv for increasing output)."
help_dryrun = "Dry-run only, no output written."


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("source", nargs=1, required=True)
@click.argument("target", nargs=1, required=True)
@click.option("-i", "--ignore", type=str, multiple=True, help=help_ignore)
@click.option("-m", "--markdown", type=str, multiple=True, help=help_markdown)
@click.option("-f", "--file", type=str, default=None, help=help_file)
@click.option("-e", "--extension", default=None, help=help_extensions)
@click.option("-v", "--verbose", count=True, help=help_verbose)
@click.option("-d", "--dryrun", is_flag=True, default=False, help=help_dryrun)
def main(source: str, target: str, ignore: tuple, markdown: tuple, file: str, extension: tuple, verbose: int, dryrun: bool):
    """
        Build (and deploy) HTML from MD

        \b
            SOURCE: Path to markdown root directory.
            TARGET: Path to html root directory.
    """
    if extension is None:
        extension = ("png", "svg", "jpg", "jpeg")

    image_files = get_image_files(source, extension)
    md_files = get_md_files(source, ignore)

    if file is not None and len(markdown) > 0:
        msg = "Cannot use options --markdown and --file together - bye!"
        logger.error(msg)
        return 1

    if file is not None and Path(file).exists():
        markdown = (Path(file).open("r", encoding="utf-8").read()).split("\n")

    if len(markdown) > 0:
        keepers = []
        for markdown_file in markdown:
            at_least_one_match = False
            for md_file in md_files:
                if markdown_file == md_file.name:
                    at_least_one_match = True
                    keepers.append(md_file)
            if not at_least_one_match:
                logger.warn(f"No matches found for '{markdown_file}' in '{source}'.")
        md_files = keepers

    for md_file in md_files:
        html_file = str(md_file).replace(source, target).replace(".md", ".html")
        html = md2html(md_file, verbose).replace("<html><body>", "").replace("</body></html>", "").strip()
        images = get_html_images(html)
        safe_html_write(target, html_file, html, verbose, dryrun)
        try:
            safe_image_copy(source, target, image_files, images, verbose, dryrun)
        except FileNotFoundError as ex:
            logger.error(ex)
            msg = f"The above error occurred when building '{html_file}'!"
            logger.error(msg)

    return 0


if __name__ == '__main__':
    main()
