#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: package_service

:Synopsis:

:Author:
    servilla

:Created:
    5/25/21
"""
import datetime
from typing import List, Optional


def package_count() -> int:
    return 274_000


def latest_packages(limit: int = 5) -> List:
    return [
               {'id': "edi.12.3"},
               {'id': "edi.423.1"},
               {'id': "knb-lter-cap.22.4"},
               {'id': "edi.1001.3"},
               {'id': "knb-lter-knz.44.2"},
               {'id': "knb-lter-jrn.232934213.1"},
               {'id': "edi.32.1"},
               {'id': "knb-lter-sev.2.17"},
           ][:limit]
