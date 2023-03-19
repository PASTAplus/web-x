#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: literal

:Synopsis:

:Author:
    servilla

:Created:
    4/5/22
"""


class Literal(object):
    def __init__(self, s):
        self.s = s

    def __html__(self):
        return self.s
