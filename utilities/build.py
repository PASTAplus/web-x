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


def get_html_images(s: BeautifulSoup) -> list:
    images = []
    imgs = s.find_all("img")
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
    images = get_html_images(soup)
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
    images = get_html_images(soup)
    return soup


def md2html(md_file: str, html_file: str, verbose: int, dryrun: bool):
    try:
        if verbose > 0:
            print(f"Reading: {md_file}")
        with open(md_file, "r", encoding="utf-8") as f:
            md = f.read()
            md = md.replace(".md", "")
            md = md.replace("/templates/", "/")
        if '[TOC]' in md:
            _ = str(sidebar_html(md))
        else:
            _ = str(basic_html(md))
        html = _.replace("<html><body>", "").replace("</body></html>", "").strip()
        if verbose > 0:
            print(f"Writing: {html_file}")
        if verbose == 2:
            print(html)
        if not dryrun:
            with open(html_file, "w") as f:
                f.write(html.strip())
    except IOError as ex:
        logger.error(f"{ex} - {md_file}")
    except AttributeError as ex:
        logger.error(f"{ex} - {md_file}")


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
help_ignore = "Ignore markdown file (may repeat for multiple files)."
help_md = "Full path to markdown file. Must be used with --html."
help_html = "Full path to html file. Must be used with --md."
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
@click.option("--md", default=None, help=help_md)
@click.option("--html", default=None, help=help_html)
@click.option("-e", "--extension", default=None, help=help_extensions)
@click.option("-v", "--verbose", count=True, help=help_verbose)
@click.option("-d", "--dryrun", is_flag=True, default=False, help=help_dryrun)
def main(source: str, target: str, ignore: tuple, md: str, html: str, extension: tuple, verbose: int, dryrun: bool):
    """
        Build (and deploy) HTML from MD

        \b
            SOURCE: Path to markdown root directory.
            TARGET: Path to html root directory.
    """

    md_files = get_md_files(source, ignore)
    for md_file in md_files:
        print(md_file)
    #     md2html(md, html, verbose, dryrun)

    if extension is None:
        extension = ("png", "svg", "jpg", "jpeg")

    image_files = get_image_files(source, extension)
    for image_file in image_files:
        print(image_file)

    return 0


if __name__ == '__main__':
    main()
