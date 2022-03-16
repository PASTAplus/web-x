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
import json

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
    inner_html = markdown.markdown(md, extensions=[TocExtension(marker='[TOC]', toc_depth='2-6')])
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
    inner_html = markdown.markdown(md)
    html = template_basic(inner_html)
    soup = BeautifulSoup(html, "lxml")
    return soup


def md2html(md_file: str, html_file: str, verbose: int, dryrun: bool):
    try:
        if verbose > 0:
            print(f"Reading: {md_file}")
        with open(md_file, "r") as f:
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
help_lines = (
                 "Line number (0-based) of mapping to execute - may repeat (e.g., -l 1 -l 3)."
                 " Must be used with a DOCMAP file."
)
help_md = "Full path to markdown file. Must be used with --html."
help_html = "Full path to html file. Must be used with --markdown."
help_verbose = "Send output to standard out (-v or -vv for increasing output)."
help_dryrun = "Dry-run only, no output written."


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("docmap", nargs=1, required=False)
@click.option("-l", "--lines", type=int, multiple=True, help=help_lines)
@click.option("--md", default=None, help=help_md)
@click.option("--html", default=None, help=help_html)
@click.option("-v", "--verbose", count=True, help=help_verbose)
@click.option("-d", "--dryrun", is_flag=True, default=False, help=help_dryrun)
def main(docmap: str, lines: tuple, md: str, html: str, verbose: int, dryrun: bool):
    """
        Build (and deploy) HTML from MD

        \b
            DOCMAP: Path to JSON file containing one or more source Markdown files with
                    corresponding target HTML files.
    """

    if docmap is not None:
        try:
            with open(docmap, "r") as f:
                maps = json.loads(f.read())
            for i, map in enumerate(maps):
                if len(lines) == 0:
                    md2html(map, maps[map], verbose, dryrun)
                elif i in lines:
                    md2html(map, maps[map], verbose, dryrun)
        except (FileNotFoundError, IOError) as ex:
            logger.error(ex)
    elif md is not None and html is not None:
        md2html(md, html, verbose, dryrun)
    else:
        print("No DOCMAP or markdown file to process, try -h or --help for help - bye!")

    return 0


if __name__ == '__main__':
    main()
