#!/usr/bin/env python3
"""Build every site: python3 make.py OUT_ROOT [keys]  (writes OUT_ROOT/<repo>/)."""
import importlib
import os
import sys

import build
import posts
from sites import SITES

SKIP = ("index.html", "404.html", "quote.html", "thanks.html", "privacy.html", "about.html")


def assemble(key):
    site = SITES[key]
    pages = importlib.import_module("content_" + key).pages(site)
    daily = posts.load(key, site)
    core = [("/" + p["path"].replace(".html", ""), build.strip(p["h1"]), p["desc"]) for p in pages
            if p["path"] not in SKIP and not p.get("noindex")]
    home = next(p for p in pages if p["path"] == "index.html")
    cut = home["body"].rfind('<section class="band">')
    if daily and cut > 0:
        home["body"] = home["body"][:cut] + posts.latest(site, daily) + "\n" + home["body"][cut:]
        home["updated"] = daily[0]["published"]
    return pages + daily + [posts.hub(site, daily, core)]


if __name__ == "__main__":
    root = sys.argv[1]
    only = sys.argv[2:] or list(SITES)
    for key in only:
        site = SITES[key]
        site["pages"] = assemble(key)
        build.build_site(site, os.path.join(root, site["repo"]))
        print("built", site["domain"], len(site["pages"]), "pages")
