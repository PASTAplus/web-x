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


def template(inner_html: str) -> str:
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


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("docmap", nargs=1, required=True)
def main(docmap: str):
    """
        Build (and deploy) HTML from MD

        \b
            DOCMAP: Path to JSON file containing one or more source Markdown files with
                    corresponding target HTML files.
    """

    with open(docmap, "r") as f:
        maps = json.loads(f.read())

    for map in maps:
        try:
            with open(map, "r") as f:
                md = f.read()
            inner_html = markdown.markdown(md, extensions=[TocExtension(marker='[TOC]', toc_depth='2-6')])
            html = template(inner_html)
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
            lines = soup.prettify().split("\n")
            doc = lines[2:-2]
            with open(maps[map], "w") as f:
                for line in doc:
                    f.write(line[2:] + "\n")
        except IOError as ex:
            logger.error(ex)

    return 0


if __name__ == '__main__':
    main()
