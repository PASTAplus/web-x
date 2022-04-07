#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: grid_object

:Synopsis:

:Author:
    servilla

:Created:
    4/6/22
"""


class GridObject:
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
