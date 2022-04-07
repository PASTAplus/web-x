#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: featured_service

:Synopsis:

:Author:
    servilla

:Created:
    4/5/22
"""
from pathlib import Path

import fastapi_chameleon

from services.literal import Literal
from services.grid_object import GridObject


def get_html(name: str) -> Literal:
    template_path = fastapi_chameleon.engine.template_path
    featured_file = f"{template_path}/featured/{name}.html"
    with Path(featured_file).open("r") as f:
        html = f.read()
    return Literal(html)


def get_grid_objects() -> list:
    grid_objects = []
    template_path = fastapi_chameleon.engine.template_path
    featured_path = f"{template_path}/featured"
    if Path(featured_path).is_dir():
        for obj in Path(featured_path).rglob("featured-*.*.html"):
            if Path(obj).is_file():
                go = GridObject(name=obj.stem, leader="This is a leader...", thumbnail="/featured/data/x.png");
                grid_objects.append(go)
    return grid_objects
