# GetMyPermit site builder

Builds all six sites (plain HTML for GitHub Pages) from one design and six content files.

- `sites.py`: domains, accent colours, menus, phone, quote email.
- `content_<site>.py`: every page's words, FAQs and checker questions. Edit these to change content.
- `build.py`: the page shell (head, header, footer, JSON-LD, sitemap, robots, llms.txt) and building blocks.
- `assets/site.css`, `assets/site.js`: the shared design and the checker / quote form code.
- `img/`: hero photos (webp) and social images.
- `posts/<site key>/<YYYY-MM-DD>-<slug>.py`: the daily guides and tools (one file each, defines `page(S)`). `posts.py` adds them to the Guides page, the home page's Latest section, the sitemap and llms.txt automatically.
- `plan_data.py`: the content calendar (what to publish each day on each site, with the search data behind it).

Build: `python3 make.py OUT_DIR [site keys]`, then copy `OUT_DIR/<repo>/` into each repo's `gh-pages` branch and push.
Each repo serves from its `gh-pages` branch with a CNAME file. Keys: gmp, shed, pergola, carport, granny, tiny.
