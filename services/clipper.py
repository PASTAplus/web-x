#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: clipper

:Synopsis:

:Author:
    servilla

:Created:
    4/7/22
"""


def clip(sentence: str, length: int) -> str:
    clipped = ""
    if sentence is not None:
        words = sentence.split()
        for word in words:
            if len(clipped) + len(word) < length - 3:
                clipped = " ".join([clipped, word])
            else:
                clipped += "..."
                break
    return clipped.strip()
