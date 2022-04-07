#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: __init__

:Synopsis:

:Author:
    servilla

:Created:
    4/7/22
"""
import logging
import os
import sys

import daiquiri

sys.path.insert(0, os.path.abspath(".."))

cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/tests.log"
daiquiri.setup(
    level=logging.INFO, outputs=(daiquiri.output.File(logfile), "stdout",)
)


def main():
    return 0


if __name__ == "__main__":
    main()