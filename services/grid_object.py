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
    def __init__(self, name: str = None, leader: str = None, thumbnail: str = None):
        self._name = name
        self._leader = leader
        self._thumbnail = thumbnail

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def leader(self):
        return self._leader

    @leader.setter
    def leader(self, leader):
        self._leader = leader

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        self._thumbnail = thumbnail
