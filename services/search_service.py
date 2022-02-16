#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: search_service

:Synopsis:

:Author:
    servilla

:Created:
    2/13/22
"""
import pickle
from urllib.parse import urlparse

import aiohttp
import daiquiri
import starlette.status as status

import bugle.index.load as load
from bugle.index.index import Index
from bugle.index.webpage import WebPage


from config import Config


logger = daiquiri.getLogger(__name__)


def search_on_terms(terms: str) -> list:
    pages = []

    with open(f"{Config.CACHE}/index.pkl", "rb") as f:
        index = pickle.load(f)

    hits = index.search(terms, rank=True)
    term_list = terms.split()
    for hit in hits:
        webpage: WebPage = hit[0]
        parse = urlparse(webpage.url)
        pages.append(
            {
                "url": webpage.url,
                "path": parse.path,
                "terms": ",".join([_ for _ in term_list if _ in webpage.fulltext.lower()])
            }
        )
    return pages
