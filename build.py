#!/usr/bin/env python3
"""Builds the GetMyPermit family of static sites (plain HTML for GitHub Pages).

Usage: python3 build.py OUT_ROOT
Writes OUT_ROOT/<repo>/... for every site in sites.py. Edit the content modules, then rebuild.
"""
import html
import json
import os
import shutil
import sys

from sites import SITES, PHONE, PHONE_TEL, UPDATED, UPDATED_ISO, ORG_ID, QUOTE_URL
import icons
import prices

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600&display=swap"
CSS_VER = "8"
INDEXNOW_KEY = "cb48ff159a951fc036db20a5d5d446f6"


def esc(s):
    return html.escape(s, quote=True)


def url(site, path):
    path = "" if path in ("index.html", "") else path.replace(".html", "")
    return "https://%s/%s" % (site["domain"], path)


def quote_link(site, permit=None):
    permit = permit or site["permit"]
    if site["key"] == "gmp":
        return "/quote" + ("?permit=" + permit if permit else "")
    return "%s?permit=%s&from=%s" % (QUOTE_URL, permit, site["domain"])


# ---------- building blocks used by the content modules ----------

def ticks(items):
    return '<ul class="ticks">' + "".join(
        "<li>%s%s</li>" % (icons.get("check", 16), t) for t in items) + "</ul>"


def hero(site, eyebrow, h1, lead, tick_items, float_title, float_sub, second=None, img=None, alt=""):
    second = second or ('<a class="btn btn-line" href="#check">Do I need a permit?</a>')
    img = img or site["image"]
    return """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">%s</p>
      <h1>%s</h1>
      <p class="lead">%s</p>
      <div class="cta-row">
        <a class="btn btn-accent" href="%s">Get my fixed price <span class="arr">&rarr;</span></a>
        %s
      </div>
      <p class="micro">Free &middot; Takes 2 minutes &middot; No obligation &middot; Reply within 1 business day</p>
      %s
    </div>
    <div class="hero-media">
      <picture>
        <source media="(max-width: 700px)" srcset="/img/%s-800.webp">
        <img src="/img/%s-1600.webp" width="1600" height="893" alt="%s" fetchpriority="high">
      </picture>
      <div class="float-card"><div class="dot">%s</div><div><strong>%s</strong><span>%s</span></div></div>
    </div>
  </div>
</section>""" % (eyebrow, h1, lead, quote_link(site), second,
                 ticks([prices.hero_tick(site) if t.startswith("Fixed price") else t for t in tick_items]), img, img, esc(alt),
                 icons.get("doc", 20), float_title, float_sub)


def section(inner, cls="section", sid=None):
    return '<section class="%s"%s><div class="wrap">%s</div></section>' % (cls, ' id="%s"' % sid if sid else "", inner)


def intro(eyebrow, title, text="", center=False):
    return '<div class="intro%s"><p class="eyebrow">%s</p><h2>%s</h2>%s</div>' % (
        " center" if center else "", eyebrow, title, "<p>%s</p>" % text if text else "")


def steps(items):
    out = '<div class="steps">'
    for i, (t, d) in enumerate(items, 1):
        out += '<div class="step"><span class="n">%02d</span><h3>%s</h3><p>%s</p></div>' % (i, t, d)
    return out + "</div>"


def cards(items, cols=3):
    """items: (icon, title, text, href or None)"""
    out = '<div class="grid g%d">' % cols
    for ic, t, d, href in items:
        inner = '<div class="icon">%s</div><h3>%s</h3><p>%s</p>' % (icons.get(ic, 22), t, d)
        if href:
            out += '<a class="card" href="%s">%s<span class="more">Read more &rarr;</span></a>' % (href, inner)
        else:
            out += '<div class="card">%s</div>' % inner
    return out + "</div>"


def stats(items):
    return '<div class="stats">' + "".join(
        '<div class="stat"><strong>%s</strong><span>%s</span></div>' % s for s in items) + "</div>"


def split(img, alt, inner, flip=False):
    pic = '<img src="/img/%s-800.webp" width="800" height="446" alt="%s" loading="lazy">' % (img, esc(alt))
    a, b = (inner, pic) if not flip else (pic, inner)
    return '<div class="split"><div>%s</div><div>%s</div></div>' % (a, b)


def checks(items):
    return '<ul class="checks">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"


def faq_block(faqs):
    return '<div class="faq">' + "".join(
        '<div class="faq-item"><h3>%s</h3><p>%s</p></div>' % (q, a) for q, a in faqs) + "</div>"


def checker(site, tree, title="Do I need a permit?", sub="Answer a few quick questions. It takes about 20 seconds."):
    cid = "checker-" + site["key"]
    return """
<div class="checker" data-checker-root="%s" id="check-tool">
  <h3>%s</h3>
  <p style="color:var(--muted);font-size:15px">%s</p>
  <div class="progress"><i></i></div>
  <div class="checker-body" aria-live="polite"><noscript><p>Turn on JavaScript to use the checker, or <a href="%s">ask us</a> and we will tell you for free.</p></noscript></div>
</div>
<script type="application/json" id="%s">%s</script>""" % (cid, title, sub, quote_link(site), cid, json.dumps(tree))


def band(site, title, text, second=None):
    second = second if second is not None else '<a class="btn btn-line" href="tel:%s">Call %s</a>' % (PHONE_TEL, PHONE)
    return """
<section class="band"><div class="wrap">
  <h2>%s</h2><p>%s</p>
  <div class="cta-row"><a class="btn btn-accent" href="%s">Get my fixed price <span class="arr">&rarr;</span></a>%s</div>
  <p class="ps"><strong>P.S.</strong> Not sure you even need a permit? Ask anyway. If you don't, we'll tell you, and it costs nothing.</p>
</div></section>""" % (title, text, quote_link(site), second)


# ---------- page shell ----------

def logo(site, cls=""):
    return '<a class="logo %s" href="/" aria-label="%s home">%s<b>%s</b></a>' % (
        cls, esc(site["name"]), icons.mark(site["accent"]), site["logo"])


def header(site, path):
    links = ""
    for href, label in site["nav"]:
        cur = ' aria-current="page"' if href.strip("/") == path.replace(".html", "") else ""
        links += '<a href="%s"%s>%s</a>' % (href, cur, label)
    return """<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar">
  %s
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">%s<a href="/pricing">Prices</a><a class="btn btn-ink btn-sm" href="%s">Get my price</a></nav>
</div></header>""" % (logo(site), links, quote_link(site))


def footer(site):
    col2 = "".join('<li><a href="%s">%s</a></li>' % l for l in site["foot_links"])
    if site["key"] == "gmp":
        fam = "".join('<li><a href="https://%s/">%s</a></li>' % (s["domain"], s["short"]) for s in SITES.values() if s["key"] != "gmp")
        fam += '<li><a href="https://poolcouncilapproval.com.au/">Pools and spas</a></li>'
        col3 = "<h4>Our permit sites</h4><ul>%s</ul>" % fam
        about = "GetMyPermit handles council paperwork for sheds, patios, carports, granny flats, tiny homes and pools across Perth and Western Australia."
    else:
        col3 = """<h4>Part of GetMyPermit</h4><ul>
<li><a href="https://getmypermit.com.au/">All permit types</a></li>
<li><a href="https://getmypermit.com.au/do-i-need-approval">Do I need approval?</a></li>
<li><a href="https://getmypermit.com.au/how-it-works">How it works</a></li>
<li><a href="https://getmypermit.com.au/permit-jargon">Permit jargon buster</a></li>
<li><a href="https://getmypermit.com.au/about">About us</a></li></ul>"""
        about = site["foot_about"]
    return """
<footer class="foot"><div class="wrap">
  <div class="foot-grid">
    <div>%s<p>%s</p></div>
    <div><h4>Guides</h4><ul>%s</ul></div>
    <div>%s</div>
    <div><h4>Talk to us</h4><ul>
      <li><a href="tel:%s">%s</a></li>
      <li><a href="%s">Get a quote</a></li>
      <li><a href="/pricing">Prices</a></li>
      <li>Perth and Western Australia</li></ul></div>
  </div>
  <p class="legal">We are a permit paperwork service. We prepare and lodge applications for you, working with registered building surveyors, draftspeople and engineers where a job needs them. We are not a council and we are not building surveyors. Rules differ between councils, so every job is checked against your council's own requirements.</p>
  <div class="foot-bottom"><span>&copy; 2026 %s</span><span><a href="https://getmypermit.com.au/privacy">Privacy</a></span></div>
</div></footer>
<div class="mcta"><a class="btn btn-accent" href="%s">Get my price</a><a class="btn btn-ink" href="tel:%s">Call</a></div>
<script src="/assets/site.js?v=%s" defer></script>""" % (
        logo(site, "light"), about, col2, col3, PHONE_TEL, PHONE, quote_link(site), site["name"],
        quote_link(site), PHONE_TEL, CSS_VER)


def org_node():
    return {
        "@type": ["Organization", "ProfessionalService"], "@id": ORG_ID, "name": "GetMyPermit",
        "url": "https://getmypermit.com.au/", "telephone": "+61 400 369 865",
        "logo": "https://getmypermit.com.au/favicon-192.png", "image": "https://getmypermit.com.au/og.jpg",
        "areaServed": {"@type": "State", "name": "Western Australia"},
        "address": {"@type": "PostalAddress", "addressRegion": "WA", "addressCountry": "AU"},
        "description": "Building permit and council approval paperwork for sheds, patios, pergolas, carports, granny flats, tiny homes and pools in Perth and Western Australia.",
    }


def jsonld(site, page):
    u = url(site, page["path"])
    graph = []
    site_id = "https://%s/#website" % site["domain"]
    graph.append({"@type": "WebSite", "@id": site_id, "url": "https://%s/" % site["domain"], "name": site["name"],
                  "publisher": {"@id": ORG_ID}})
    if site["key"] == "gmp":
        graph.append(org_node())
    else:
        o = org_node()
        graph.append({"@type": "Organization", "@id": ORG_ID, "name": o["name"], "url": o["url"], "telephone": o["telephone"]})
        graph.append({"@type": "Service", "@id": "https://%s/#service" % site["domain"], "name": site["service"],
                      "serviceType": site["service"], "provider": {"@id": ORG_ID},
                      "areaServed": {"@type": "State", "name": "Western Australia"}, "url": "https://%s/" % site["domain"],
                      "offers": prices.offers(site)})
    wp = {"@type": "WebPage", "@id": u + "#page", "url": u, "name": page["title"], "description": page["desc"],
          "isPartOf": {"@id": site_id}, "dateModified": page_iso(page), "inLanguage": "en-AU",
          "primaryImageOfPage": {"@type": "ImageObject", "url": "https://%s/img/%s-1600.webp" % (site["domain"], page.get("img", site["image"]))}}
    graph.append(wp)
    if page.get("published"):
        graph.append({"@type": "Article", "@id": u + "#article", "headline": strip(page["h1"]), "description": page["desc"],
                      "datePublished": page["published"], "dateModified": page_iso(page), "inLanguage": "en-AU",
                      "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "mainEntityOfPage": {"@id": u + "#page"},
                      "image": "https://%s/img/%s-1600.webp" % (site["domain"], page.get("img", site["image"]))})
    if page["path"] != "index.html":
        crumbs = [("Home", "https://%s/" % site["domain"])]
        if page.get("parent"):
            crumbs.append((page["parent"][1], url(site, page["parent"][0].strip("/") + ".html")))
        crumbs.append((page.get("crumb", page["h1"]), u))
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "item": h} for i, (n, h) in enumerate(crumbs, 1)]})
    if page.get("faqs"):
        graph.append({"@type": "FAQPage", "@id": u + "#faq", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in page["faqs"]]})
    graph += page.get("ld", [])
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("&rsquo;", "'").replace("&amp;", "&")


def head(site, page):
    u = url(site, page["path"])
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else '<meta name="robots" content="max-image-preview:large">'
    return """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
%s
<meta name="theme-color" content="#fbfaf7">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="https://%s/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%s">
<link rel="stylesheet" href="/assets/site.css?v=%s">
<style>:root{--accent:%s}</style>
<script type="application/ld+json">%s</script>
</head>
<body>
""" % (esc(page["title"]), esc(page["desc"]), u, robots, esc(site["name"]), esc(page["title"]), esc(page["desc"]), u,
       site["domain"], FONTS, CSS_VER, site["accent"], jsonld(site, page))


def nice_date(iso):
    import datetime
    d = datetime.date.fromisoformat(iso)
    return "%d %s" % (d.day, d.strftime("%B %Y"))


def page_iso(page):
    return page.get("updated") or page.get("published") or UPDATED_ISO


def dates_line(page):
    if page.get("published") and page.get("updated") and page["updated"] != page["published"]:
        return "Published %s &middot; Last updated %s" % (nice_date(page["published"]), nice_date(page["updated"]))
    return "Last updated %s" % nice_date(page_iso(page))


def parent_crumb(page):
    if not page.get("parent"):
        return ""
    return '<a href="%s">%s</a><span>/</span>' % page["parent"]


def sources_block(page):
    if not page.get("sources"):
        return ""
    return '<h2>Sources</h2><ul class="sources">%s</ul>' % "".join(
        '<li><a href="%s" rel="noopener">%s</a></li>' % (u, t) for t, u in page["sources"])


def article(site, page):
    """Inner page: answer first, prose with a sticky quote card, FAQs, then the CTA band."""
    related = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in page.get("related", []))
    faqs = ""
    if page.get("faqs"):
        faqs = section('<div class="ph-inner">%s%s</div>' % (intro("Questions", "Common questions"), faq_block(page["faqs"])), "section tight")
    return """
<main id="main">
<section class="page-hero"><div class="wrap"><div class="ph-inner">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span>%s%s</nav>
  <p class="eyebrow">%s</p>
  <h1>%s</h1>
  <div class="answer"><span class="label">Short answer</span>%s</div>
  <p class="updated">%s</p>
</div></div></section>
<section class="content"><div class="wrap">
  <article class="prose">%s%s</article>
  <aside class="aside"><div class="aside-card">
    <h3>%s</h3><p>%s</p>
    <p class="aside-price">%s <a href="/pricing">See prices</a></p>
    <a class="btn btn-accent" href="%s">Get my fixed price</a>
    <p class="micro">Free, takes 2 minutes, no obligation. Approved, or your money back.</p>
    <a class="btn btn-line" href="tel:%s" style="margin-top:10px">Call %s</a>
    %s
  </div></aside>
</div></section>
%s
%s
</main>""" % (parent_crumb(page), esc(page.get("crumb", page["h1"])), page["eyebrow"], page["h1"], page["answer"], dates_line(page),
             page["body"], sources_block(page),
             site["aside_title"], site["aside_text"], prices.from_price(site), quote_link(site, page.get("permit")), PHONE_TEL, PHONE,
             '<ul class="aside-list">%s</ul>' % related if related else "",
             faqs, band(site, page.get("band_title", site["band_title"]), page.get("band_text", site["band_text"])))


def render(site, page):
    if page.get("kind") == "article":
        main = article(site, page)
    else:
        main = '<main id="main">%s</main>' % page["body"]
    if not page.get("noprices") and page["path"] not in ("404.html", "thanks.html", "privacy.html", "quote.html"):
        cut = main.rfind('<section class="band">')
        cut = cut if cut > 0 else main.rfind("</main>")
        main = main[:cut] + prices.section(site) + "\n" + main[cut:]
    return head(site, page) + header(site, page["path"]) + main + footer(site) + "\n</body>\n</html>\n"


# ---------- site files ----------

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def build_site(site, out):
    for p in site["pages"]:
        write(os.path.join(out, p["path"]), render(site, p))
    write(os.path.join(out, "CNAME"), site["domain"] + "\n")
    write(os.path.join(out, ".nojekyll"), "")
    write(os.path.join(out, "favicon.svg"), icons.favicon(site["accent"]))
    write(os.path.join(out, "robots.txt"), """User-agent: *
Allow: /

# Search and AI assistants are welcome to read every page.
User-agent: Googlebot
User-agent: Bingbot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: Google-Extended
User-agent: Applebot
Allow: /

Sitemap: https://%s/sitemap.xml
""" % site["domain"])
    urls = "".join("<url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (url(site, p["path"]), page_iso(p))
                   for p in site["pages"] if not p.get("noindex") and p["path"] != "404.html")
    write(os.path.join(out, "sitemap.xml"),
          '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    lines = ["# %s" % site["name"], "", "> %s" % site["llms"], "", "## Pages", ""]
    for p in site["pages"]:
        if not p.get("noindex") and p["path"] != "404.html":
            lines.append("- [%s](%s): %s" % (strip(p["h1"]), url(site, p["path"]), p["desc"]))
    lines += ["", "## Contact", "", "- Phone: %s" % PHONE, "- Quote form: %s" % QUOTE_URL, ""]
    write(os.path.join(out, "llms.txt"), "\n".join(lines))
    write(os.path.join(out, INDEXNOW_KEY + ".txt"), INDEXNOW_KEY)
    # Runs on GitHub after each push: tells Bing (and so Copilot and ChatGPT search) which pages changed.
    os.makedirs(os.path.join(out, ".github", "workflows"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "assets", "indexnow.yml"), os.path.join(out, ".github", "workflows", "indexnow.yml"))
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "assets", "site.css"), os.path.join(out, "assets", "site.css"))
    shutil.copy(os.path.join(HERE, "assets", "site.js"), os.path.join(out, "assets", "site.js"))
    img_dir = os.path.join(out, "img")
    os.makedirs(img_dir, exist_ok=True)
    for name in site["images"]:
        for size in ("1600", "800"):
            shutil.copy(os.path.join(HERE, "img", "%s-%s.webp" % (name, size)), img_dir)
    shutil.copy(os.path.join(HERE, "img", "og-%s.jpg" % site["image"]), os.path.join(out, "og.jpg"))
    shutil.copy(os.path.join(HERE, "img", "fav-%s-180.png" % site["key"]), os.path.join(out, "apple-touch-icon.png"))
    shutil.copy(os.path.join(HERE, "img", "fav-%s.ico" % site["key"]), os.path.join(out, "favicon.ico"))
    for size in ("48", "96", "192"):
        shutil.copy(os.path.join(HERE, "img", "fav-%s-%s.png" % (site["key"], size)), os.path.join(out, "favicon-%s.png" % size))


if __name__ == "__main__":
    root = sys.argv[1]
    for s in SITES.values():
        build_site(s, os.path.join(root, s["repo"]))
        print("built", s["domain"], len(s["pages"]), "pages")


def answer_check(site, eyebrow, title, answer_html, points, tree, check_title="Do I need a permit?"):
    """Two columns: the plain answer and key rules on the left, the checker on the right."""
    left = '<p class="eyebrow">%s</p><h2>%s</h2><div class="answer" style="margin-top:8px"><span class="label">Short answer</span>%s</div>%s' % (
        eyebrow, title, answer_html, checks(points))
    return section('<div class="split" style="align-items:start"><div>%s</div><div>%s</div></div>' % (left, checker(site, tree, check_title)),
                   "section white", "check")


def guides(items):
    """Links to the site's guide pages: (href, title, text, icon)."""
    return cards([(ic, t, d, h) for h, t, d, ic in items], cols=3)


def prose_section(html_text, cls="section", sid=None):
    return section('<div class="narrow prose">%s</div>' % html_text, cls, sid)
