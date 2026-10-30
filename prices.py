"""Our public price list. Change a price here and every site, page and quote tile updates on the next build."""
import build as b

# key: (name, price shown, short note)
COUNCIL_IN = "Total price. Council fees included."
COUNCIL_EXTRA = "Plus council fees, which depend on the build value. We show you the exact amount before you pay."
ITEMS = {
    "shed": ("Shed or outbuilding", "$990", COUNCIL_IN),
    "garage": ("Garage", "$1,190", COUNCIL_IN),
    "carport": ("Carport", "$990", COUNCIL_IN),
    "pergola": ("Pergola or patio", "$990", COUNCIL_IN),
    "deck": ("Deck", "$1,190", COUNCIL_IN),
    "retaining-wall": ("Retaining wall", "$1,690", "Walls up to 1 m high. Standard engineering and council fees included."),
    "pool": ("Pool or spa", "$1,500", COUNCIL_IN),
    "granny-flat": ("Granny flat, your builder's plans", "$2,950", COUNCIL_EXTRA),
    "granny-design": ("Granny flat, we draw the plans", "from $6,950", COUNCIL_EXTRA),
    "tiny-wheels": ("Tiny home on wheels", "$1,450", "Council application for living in it. Council fees included."),
    "tiny-slab": ("Tiny home on a slab", "$2,450", COUNCIL_EXTRA),
    "retrospective": ("Already built: site check", "$495", "Comes off your approval price. Approvals from $1,950 plus council fees."),
    "bal": ("BAL (bushfire) assessment", "$595", "Done by an accredited assessor. $495 when added to another job."),
    "fast": ("Fast track", "+$550", "Certified application, decided in about 10 business days instead of 25. Add to any job."),
    "partner": ("Builders and suppliers", "10 to 15% off", "Partner rates for regular work, invoiced monthly."),
}

SITE_ITEMS = {
    "gmp": list(ITEMS),
    "shed": ["shed", "garage", "retrospective", "fast"],
    "pergola": ["pergola", "deck", "retrospective", "fast"],
    "carport": ["carport", "retrospective", "fast"],
    "granny": ["granny-flat", "granny-design", "bal"],
    "tiny": ["tiny-wheels", "tiny-slab", "bal"],
}

# Price shown on the quote form tiles (tile key -> short price).
TILE_PRICE = {"shed": "$990", "garage": "$1,190", "carport": "$990", "pergola": "$990", "deck": "$1,190",
              "granny-flat": "from $2,950", "tiny-home": "from $1,450", "pool": "$1,500", "retaining-wall": "$1,690",
              "retrospective": "from $495", "bal": "$595", "partner": "10 to 15% off"}

INCLUDED = ["Site plan and drawings", "Application forms and owner consent", "Lodging with your council",
            "Council fees and levies (unless a price says otherwise)", "Answering council's questions until your permit is issued"]
EXTRA = ["Planning approval, if your council asks for it", "Custom engineering if your kit doesn't come with it (+$450)",
         "Heritage areas, or fixing something that already exists", "Travel outside the Perth metro area"]


def link(key, site):
    if key == "pool":
        return "https://poolcouncilapproval.com.au/"
    if key == "partner":
        return "https://getmypermit.com.au/for-builders" if site["key"] != "gmp" else "/for-builders"
    tile = {"granny-design": "granny-flat", "tiny-wheels": "tiny-home", "tiny-slab": "tiny-home", "fast": None}.get(key, key)
    return b.quote_link(site, tile)


def cards(site):
    out = '<div class="price-grid">'
    for k in SITE_ITEMS[site["key"]]:
        name, price, note = ITEMS[k]
        out += '<a class="price-card" href="%s"><span class="pc-name">%s</span><strong class="pc-price">%s</strong><span class="pc-note">%s</span></a>' % (
            link(k, site), name, price, note)
    return out + "</div>"


def lists():
    return '<div class="price-lists"><div><h3>Always included</h3>%s</div><div><h3>Only if your job needs it</h3>%s<p class="pc-small">We tell you about any of these before you pay anything. Council fees are included for jobs worth up to $50,000.</p></div></div>' % (
        b.ticks(INCLUDED), '<ul class="pc-extra">' + "".join("<li>%s</li>" % e for e in EXTRA) + "</ul>")


def section(site):
    """The price strip shown on every page."""
    more = '<p class="center" style="margin-top:22px"><a href="/pricing">See what\'s included &rarr;</a></p>'
    return b.section(b.intro("Prices", "Our prices, upfront", "One total price, with council fees included. No surprises.", True)
                     + cards(site) + more, "section white", "prices")


def page(site):
    body = """
<section class="page-hero"><div class="wrap narrow">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span>Prices</nav>
  <p class="eyebrow">Prices</p>
  <h1>Our prices, upfront</h1>
  <p class="lead">Most permit services won't tell you a price until you call, and then council fees are added on top. Our prices are the total, with council fees included, so you know the cost before you start.</p>
</div></section>"""
    body += b.section(cards(site) + lists(), "section", "prices")
    body += b.band(site, site["band_title"], site["band_text"])
    return {"path": "pricing.html", "title": "Prices | %s" % site["name"],
            "desc": "Upfront, fixed prices for %s in Perth and WA, with council fees included. %s from %s." % (
                site["short"].lower() if site["key"] != "gmp" else "building permits and council approvals",
                ITEMS[SITE_ITEMS[site["key"]][0]][0], ITEMS[SITE_ITEMS[site["key"]][0]][1].replace("from ", "")),
            "h1": "Our prices, upfront", "crumb": "Prices", "body": body, "noprices": True}


def from_price(site):
    """The headline price for a site, e.g. 'From $990, council fees included.'"""
    k = SITE_ITEMS[site["key"]][0]
    if site["key"] == "gmp":
        return "Sheds, patios and carports from $990 all in, council fees included."
    name, price, note = ITEMS[k]
    return "%s permits from %s%s." % (name.split(",")[0], price.replace("from ", ""),
                                      ", council fees included" if note == COUNCIL_IN or "Council fees included" in note else " plus council fees")


def offers(site):
    out = []
    for k in SITE_ITEMS[site["key"]]:
        name, price, _ = ITEMS[k]
        num = price.replace("from ", "").replace("$", "").replace(",", "")
        if num.isdigit():
            out.append({"@type": "Offer", "name": name, "price": num, "priceCurrency": "AUD"})
    return out


def hero_tick(site):
    """Short price for the hero, in place of 'Fixed price up front'."""
    name, price, note = ITEMS[SITE_ITEMS[site["key"]][0]]
    price = price.replace("from ", "")
    if site["key"] == "gmp" or site["key"] in ("granny", "tiny"):
        return "From %s%s" % (price, ", council fees included" if "included" in note else "")
    return "%s, council fees included" % price
