"""Daily guides and tools.

Each piece lives in posts/<site key>/<YYYY-MM-DD>-<slug>.py and defines page(S), returning an article page dict
with these extra keys: "published" (YYYY-MM-DD), "type" (Free tool, Question answer, Council guide, How-to guide,
Comparison, Cost guide), "card" (one-line summary for the guides list), "icon" (a name from icons.py) and
optionally "updated" (YYYY-MM-DD) and "sources" [(title, url)].
"""
import datetime
import glob
import importlib.util
import os

import build as b

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = ("/guides", "Guides")


def nice(iso):
    d = datetime.date.fromisoformat(iso)
    return "%d %s" % (d.day, d.strftime("%B %Y"))


def load(key, S):
    out = []
    for f in sorted(glob.glob(os.path.join(HERE, "posts", key, "*.py"))):
        spec = importlib.util.spec_from_file_location("post_" + os.path.basename(f)[:-3].replace("-", "_"), f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        p = mod.page(S)
        p.setdefault("kind", "article")
        p["parent"] = PARENT
        out.append(p)
    return sorted(out, key=lambda p: (p["published"], p["path"]), reverse=True)


def post_cards(posts):
    out = '<div class="grid g3">'
    for p in posts:
        out += ('<a class="card" href="/%s"><div class="icon">%s</div><p class="meta">%s &middot; %s</p><h3>%s</h3><p>%s</p>'
                '<span class="more">%s &rarr;</span></a>') % (
            p["path"].replace(".html", ""), b.icons.get(p.get("icon", "doc"), 22), p["type"], nice(p["published"]),
            p["h1"], p["card"], "Use the tool" if p["type"] == "Free tool" else "Read more")
    return out + "</div>"


def hub(S, posts, core):
    """guides.html: the site's core guides first, then every daily piece, newest first."""
    tools = [p for p in posts if p["type"] == "Free tool"]
    body = """
<section class="page-hero"><div class="wrap"><div class="ph-inner">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span>Guides</nav>
  <p class="eyebrow">Guides and free tools</p>
  <h1>%s guides and free tools</h1>
  <p class="lead">Plain-English answers about %s approvals in Western Australia, checked against the official rules. New guides are added every week.</p>
</div></div></section>""" % (S["short"] if S["key"] != "gmp" else "Building permit", S["short"].lower() if S["key"] != "gmp" else "building permit and council")
    if core:
        body += b.section(b.intro("Start here", "The essentials") + b.cards([("doc", t, d, h) for h, t, d in core], cols=3), "section tight")
    if tools:
        body += b.section(b.intro("Free tools", "Check it yourself in a minute") + post_cards(tools), "section tight")
    if posts:
        body += b.section(b.intro("Latest", "All guides, newest first") + post_cards(posts), "section tight")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "guides.html", "title": "%s Guides and Free Tools | WA" % S["name"],
            "desc": "Free tools and plain-English guides to %s approvals in Perth and Western Australia, checked against the official rules." % (
                S["short"].lower() if S["key"] != "gmp" else "building permits and council"),
            "h1": "Guides", "crumb": "Guides", "body": body,
            "updated": posts[0]["published"] if posts else None}


def latest(S, posts, n=3):
    if not posts:
        return ""
    return b.section(b.intro("New guides", "Latest guides and tools") + post_cards(posts[:n]) +
                     '<p style="margin-top:22px"><a class="btn btn-line" href="/guides">See all guides and tools</a></p>', "section tight")
