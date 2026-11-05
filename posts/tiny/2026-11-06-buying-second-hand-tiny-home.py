BODY = """
<h2>Step 1: Work out what you're actually buying</h2>
<p>In WA, a tiny home on wheels that's fitted out to live in is usually treated as a <strong>caravan</strong>, not a building. That means no building permit, but council rules on how long you can live in it. A tiny home without wheels (or with them taken off) is a <strong>building</strong> and needs a building permit like any home.</p>
<p>So before anything else, ask: is it on a road-going trailer, or is it a cabin that needs a truck and crane? The answer changes every check that follows.</p>

<h2>Step 2: Check it's not carrying someone else's debt</h2>
<p>Do a <strong>PPSR search</strong> on the trailer's VIN or chassis number. It costs <strong>$2</strong> online and covers caravans and trailers. It shows if a lender has a security interest recorded against it, which means it could be repossessed even after you've paid.</p>
<ul>
<li>Search on the day you buy, or the day before.</li>
<li>Keep the search certificate.</li>
<li>A PPSR search doesn't show who owns it or how much is owed, so check the seller's ID and paperwork too.</li>
<li>You can't search by number plate. You need the VIN or chassis number.</li>
</ul>
<p>Buying from a licensed dealer generally protects you from repossession. Buying privately, the search matters much more.</p>

<h2>Step 3: Match the numbers</h2>
<p>Photograph the VIN or chassis number on the frame and compare it with the registration papers, the seller's receipt and any build documents. If anything doesn't match, stop until it's explained in writing.</p>

<h2>Step 4: Ask for the build pack</h2>
<ul>
<li>Original invoice, plans and builder details</li>
<li>Trailer engineering and weight records (tare and maximum weight)</li>
<li>Electrical, gas and plumbing certificates</li>
<li>Records of any changes since it was built</li>
</ul>
<p>Missing paperwork isn't always a deal-breaker, but price in the cost of inspections to fill the gaps.</p>

<h2>Step 5: Inspect beyond the styling</h2>
<p>Look for water damage (stains, soft floors, musty smells), rust on the chassis, and worn tyres, brakes and bearings. Get a qualified person to check the electrics and gas. A light switch working doesn't mean the wiring is safe.</p>

<h2>Step 6: Check you can legally live in it where you want</h2>
<p>This is where many buyers get caught. In WA you can usually stay in a caravan on private land for a short time with the owner's OK. Longer stays need council approval, for up to 24 months at a time. Councils can set conditions like power, water and sewerage. Ask your council <strong>before</strong> you buy, not after.</p>
<p>Learn more in <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules in WA</a> and <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a>. Planning to take the wheels off? See <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>.</p>

<h2>Step 7: Plan the move</h2>
<p>Get a written quote for transport, including any permits, the route and access into your block. See <a href="/moving-a-tiny-home">moving a tiny home</a>.</p>
"""

FAQS = [
    ("What should I check before buying a second-hand tiny home?",
     "Do a $2 PPSR search on the VIN, match the VIN with the paperwork, ask for the build and certificate records, inspect for water damage and trailer wear, and confirm with your council that you can live in it on your land."),
    ("How do I check if a used tiny home has finance owing?",
     "Do a PPSR search on its VIN or chassis number. It costs $2 online and shows if a security interest is recorded. Search on the day you buy or the day before."),
    ("Does a second-hand tiny home on wheels need a building permit in WA?",
     "Usually not, because a tiny home on wheels fitted for living is treated as a caravan. But council rules limit how long you can live in it, and a home without wheels needs a building permit."),
    ("Can I live in a second-hand tiny home on my land in WA?",
     "Short stays are usually fine with the landowner's OK. Longer stays need council approval, for up to 24 months at a time. Ask your council before you buy."),
    ("Does a PPSR search show who owns the tiny home?",
     "No. It shows recorded security interests and may show stolen or written-off status, but not the owner or ownership history."),
]


def page(S):
    return {"path": "buying-second-hand-tiny-home.html", "published": "2026-11-06", "type": "How-to guide", "icon": "tiny",
            "card": "Seven checks before you pay: debts, paperwork, condition and council rules.",
            "title": "How to Buy a Second-Hand Tiny Home Safely (WA)",
            "desc": "Buying a used tiny home in WA? Seven checks before you pay: a $2 PPSR search, VIN and paperwork, inspection, and whether council will let you live in it.",
            "eyebrow": "How-to guide", "h1": "How to buy a second-hand tiny home safely", "crumb": "Buying a used tiny home",
            "answer": "<p>Before you pay: do a <strong>$2 PPSR search</strong> on the VIN to check for finance owing, match the VIN with the paperwork, get the build and safety certificates, and have it inspected. Most importantly, ask your council <strong>before</strong> you buy whether you can live in it on your land, and for how long.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules in WA"), ("/moving-a-tiny-home", "Moving a tiny home"), ("/tiny-home-prices-perth", "Tiny home prices in Perth")],
            "sources": [("Do a used car or vehicle search (PPSR)", "https://www.ppsr.gov.au/searching/do-used-car-or-vehicle-search"),
                        ("Tiny House Fact Sheet (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Buying a second-hand tiny home in Australia: checklist (Tiny Modular Directory)", "https://www.tinymodulardirectory.com.au/blog/buying-second-hand-tiny-home-australia/")]}
