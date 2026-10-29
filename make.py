#!/usr/bin/env python3
"""Build every site: python3 make.py OUT_ROOT  (writes OUT_ROOT/<repo>/)."""
import os
import sys

import build
from sites import SITES
import importlib

if __name__ == "__main__":
    root = sys.argv[1]
    only = sys.argv[2:] or list(SITES)
    for key in only:
        site = SITES[key]
        site["pages"] = importlib.import_module("content_" + key).pages(site)
        build.build_site(site, os.path.join(root, site["repo"]))
        print("built", site["domain"], len(site["pages"]), "pages")
