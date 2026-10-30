#!/usr/bin/env python3
"""Render each site's favicon to PNG sizes and a favicon.ico: python3 make_icons.py
(uses Node Playwright to draw the SVG at 512 px, writes img/fav-<key>-<size>.png and img/fav-<key>.ico)."""
import json
import os
import subprocess

from PIL import Image

import icons
from sites import SITES

HERE = os.path.dirname(os.path.abspath(__file__))
JS = """
const { chromium } = require('playwright');
(async () => {
  const jobs = JSON.parse(process.argv[1]);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 512, height: 512 } });
  for (const [svg, out] of jobs) {
    await p.setContent('<html><body style="margin:0;background:transparent">' + svg + '</body></html>');
    await p.screenshot({ path: out, omitBackground: true });
  }
  await b.close();
})();
"""

jobs = []
for key, site in SITES.items():
    svg = icons.favicon(site["accent"]).replace("<svg ", '<svg width="512" height="512" ', 1)
    jobs.append([svg, os.path.join(HERE, "img", "fav-%s-512.png" % key)])
subprocess.run(["node", "-e", JS, json.dumps(jobs)], check=True)
for key in SITES:
    big = Image.open(os.path.join(HERE, "img", "fav-%s-512.png" % key)).convert("RGBA")
    for size in (48, 96, 180, 192):
        big.resize((size, size), Image.LANCZOS).save(os.path.join(HERE, "img", "fav-%s-%d.png" % (key, size)))
    big.save(os.path.join(HERE, "img", "fav-%s.ico" % key), sizes=[(16, 16), (32, 32), (48, 48)])
print("icons done")
