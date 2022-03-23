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
        for image in images:
            found = False
            for image_file in image_files:
                if image in str(image_file):
                    copy_path = str(image_file).replace(source, target)
                    if verbose > 0:
                        print(f"Copying: '{image_file}' to '{copy_path}")
                    found = True
                    if not dryrun:
                        img = Path(image_file).open("rb").read()
                        path = Path(copy_path)
                        path.parent.mkdir(exist_ok=True, parents=True)
                        path.open("wb").write(img)
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
        src = img["src"]
        images.append(src)
    return images


def template_sidebar(inner_html: str) -> str:
    open = """
<div metal:use-macro="load: ../shared/layout.html">
<div metal:fill-slot="content" tal:omit-tag="True">
<div class="sidebar-inner">
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
    div_toc_tag = soup.find("div", attrs={"class": "toc"}).extract()
    div_toc_tag.name = "div"
    div_toc_tag["class"] = "sticky-xl-top"
    div_sticky_lg_top = soup.new_tag("div")
    div_sticky_lg_top["class"] = "sticky-lg-top"
    div_sticky_lg_top.insert(0, div_toc_tag)
    div_sticky_md_top = soup.new_tag("div")
    div_sticky_md_top["class"] = "sticky-md-top"
    div_sticky_md_top.insert(0, div_sticky_lg_top)
    div_sticky_sm_top = soup.new_tag("div")
    div_sticky_sm_top["class"] = "sticky-sm-top"
    div_sticky_sm_top.insert(0, div_sticky_md_top)
    aside = soup.new_tag("aside")
    aside["class"] = "sidebar"
    aside.insert(0, div_sticky_sm_top)
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


def md2html(md_file: str, verbose: int) -> str:
    try:
        if verbose > 0:
            print(f"Reading: {md_file}")
        md = Path(md_file).open("r", encoding="utf-8").read()
        md = md.replace(".md", "")
        md = md.replace("/templates/", "/")
        if '[TOC]' in md:
            html = str(sidebar_html(md))
        else:
            html = str(basic_html(md)).replace("<html><body>", "").replace("</body></html>", "").strip()
        return html
    except IOError as ex:
        logger.error(f"{ex} - {md_file}")
    except AttributeError as ex:
        logger.error(f"{ex} - {md_file}")


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
help_ignore = "Ignore markdown file (may repeat for multiple files)."
help_markdown = "Full path to markdown file (may repeat for multiple files)."
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
@click.option("-e", "--extension", default=None, help=help_extensions)
@click.option("-v", "--verbose", count=True, help=help_verbose)
@click.option("-d", "--dryrun", is_flag=True, default=False, help=help_dryrun)
def main(source: str, target: str, ignore: tuple, markdown: tuple, extension: tuple, verbose: int, dryrun: bool):
    """
        Build (and deploy) HTML from MD

        \b
            SOURCE: Path to markdown root directory.
            TARGET: Path to html root directory.
    """
    if extension is None:
        extension = ("png", "svg", "jpg", "jpeg")

    image_files = get_image_files(source, extension)

    if len(markdown) > 0:
        md_files = markdown
    else:
        md_files = get_md_files(source, ignore)

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
