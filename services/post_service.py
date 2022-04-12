#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: post_service

:Synopsis:

:Author:
    servilla

:Created:
    4/6/22
"""
from pathlib import Path

import fastapi_chameleon
from bs4 import BeautifulSoup

from services.clipper import clip
from services.literal import Literal


class PostCardObject:
    def __init__(
            self,
            name: str = None,
            title: str = None,
            thumbnail: str = None,
            date: str = None,
            author: str = None,
            description: str = None
    ):
        self.name = name
        self.title = title
        self.thumbnail = thumbnail
        self.date = date
        self.author = author
        self.description = description


def make_postcard_object(file: str, clip_len: int, img_picker: str) -> PostCardObject:
    name = Path(file).stem
    fd = Path(file).open("r", encoding="utf-8").read()
    soup = BeautifulSoup(fd, "lxml")
    title = soup.find("h2").get_text()
    paras = soup.find_all("p")
    date = paras[0].get_text()
    author = paras[1].get_text()
    h3s = soup.find_all("h3")
    description = None
    for h3 in h3s:
        if h3.get_text() == "Description":
            p = h3.findNext("p").get_text()
            if p is not None:
                description = p if clip_len is None else clip(p, clip_len)

    image = soup.find("img", id=img_picker)
    if image is None:
        image = soup.find("img")
    thumbnail = None if image is None else image["src"]

    return PostCardObject(
        name=name,
        title=title,
        thumbnail=thumbnail,
        date=date,
        author=author,
        description=description
    )


def get_post_html(post_type: str, name: str) -> Literal:
    template_path = fastapi_chameleon.engine.template_path
    post_file = f"{template_path}/{post_type}/{name}.html"
    with Path(post_file).open("r", encoding="utf-8") as f:
        html = f.read()
    return Literal(html)


def get_postcard_objects(post_type: str, clip_len: int, img_picker: str) -> list:
    postcard_objects = []
    template_path = fastapi_chameleon.engine.template_path
    posts_path = f"{template_path}/{post_type}"
    if Path(posts_path).is_dir():
        for post in sorted(Path(posts_path).rglob(f"{post_type}-*.*.html"), reverse=True):
            if post.is_file():
                fd = f"{posts_path}/{post.name}"
                pco = make_postcard_object(fd, clip_len, img_picker)
                postcard_objects.append(pco)
    return postcard_objects
