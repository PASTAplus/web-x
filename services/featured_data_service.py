#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: featured_data_service

:Synopsis:

:Author:
    servilla

:Created:
    4/5/22
"""
from pathlib import Path

import fastapi_chameleon

from services.literal import Literal


def get_html(name: str) -> Literal:
    template_path = fastapi_chameleon.engine.template_path
    featured_file = f"{template_path}/featured/{name}.html"
    with Path(featured_file).open("r") as f:
        html = f.read()
    return Literal(html)
