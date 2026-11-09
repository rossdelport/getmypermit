BODY = """
<h2>The rule is about size, not bedrooms</h2>
<p>WA's R-Codes don't set a maximum number of bedrooms for a granny flat (the official name is "ancillary dwelling"). What they limit is the size: <strong>70 m²</strong> of internal floor area if you want to skip planning approval. The state's own explanatory guidelines say 70 m² "allows for a single or two-bedroom dwelling".</p>

<h2>Fitting two bedrooms into 70 m²</h2>
<p>The 70 m² is measured from the inside face of the walls, so the wall thickness doesn't count against you. Even so, two bedrooms, a bathroom, a kitchen and a living area is a tight fit. Good designs usually:</p>
<ul>
<li>combine the kitchen, living and dining into one open space</li>
<li>keep hallways short or skip them</li>
<li>put the laundry inside the bathroom</li>
<li>use built-in robes instead of walk-in ones</li>
</ul>
<p>Check your design with the <a href="/granny-flat-size-calculator">granny flat 70 m² calculator</a>.</p>

<h2>What else the rules expect</h2>
<ul>
<li><strong>A kitchen and bathroom.</strong> A granny flat is self-contained, so a separate kitchen and bathroom are generally expected. The guidelines say a laundry isn't essential for planning.</li>
<li><strong>Setbacks, site cover, height and privacy.</strong> It must meet the deemed-to-comply rules for your lot, as well as the size limit.</li>
<li><strong>Parking.</strong> On most house lots, one extra parking bay is needed unless you're within an 800 m walk of a train station or 250 m of a high-frequency bus stop.</li>
<li><strong>No separate title.</strong> A granny flat can't be subdivided off as its own lot.</li>
</ul>

<h2>Going over 70 m²</h2>
<p>A bigger flat isn't automatically refused, but it no longer meets the deemed-to-comply rules. That means you need planning approval, and councils vary in what they'll accept.</p>

<h2>A building permit is still needed</h2>
<p>Whatever the number of bedrooms, the state is clear: you still need a building permit from your council, and the flat must meet the National Construction Code. See the full <a href="/granny-flat-approval-process">granny flat approval process</a> or the <a href="/granny-flat-rules-wa">granny flat rules in WA</a>.</p>
"""

FAQS = [
    ("Can a granny flat have 2 bedrooms in WA?",
     "Yes. The R-Codes limit the size, not the bedrooms. WA's explanatory guidelines say the 70 m² limit allows for a single or two-bedroom dwelling."),
    ("Can a granny flat have 3 bedrooms in WA?",
     "There's no bedroom limit, but fitting three bedrooms plus a kitchen, bathroom and living area into 70 m² is very hard. A bigger flat needs planning approval."),
    ("How is the 70 m² granny flat size measured?",
     "As internal floor area, measured from the finished inside surface of the walls."),
    ("Does a two-bedroom granny flat need extra parking?",
     "On most house lots, yes: one extra bay, unless you're close to a train station or high-frequency bus stop. Higher-density lots don't need one."),
    ("Does a two-bedroom granny flat need a building permit?",
     "Yes. Every granny flat needs a building permit and must meet the National Construction Code, even when planning approval isn't needed."),
]


def page(S):
    return {"path": "two-bedroom-granny-flat-rules.html", "published": "2026-11-07", "type": "Question answer", "icon": "granny",
            "card": "Yes, if it fits in 70 m². How the space splits, and what else the rules expect.",
            "title": "Can a Granny Flat Have 2 Bedrooms in WA?",
            "desc": "Two-bedroom granny flats in WA: the 70 m² limit, how it's measured, fitting two bedrooms in, parking, and why you still need a building permit.",
            "eyebrow": "Question answer", "h1": "Can a granny flat have 2 bedrooms in WA?", "crumb": "Two-bedroom granny flats",
            "answer": "<p><strong>Yes.</strong> WA's rules limit a granny flat's size, not its bedrooms. To skip planning approval it must be <strong>70 m² or less</strong> inside the walls, and the state's guidelines say that's enough for a single or two-bedroom flat. You still need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-size-calculator", "Granny flat 70 m² calculator"), ("/granny-flat-approval-process", "Granny flat approval process"), ("/granny-flat-rules-wa", "Granny flat rules in WA")],
            "sources": [("Granny flats info sheet (WA Planning)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("R-Codes Volume 1 Explanatory Guidelines 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-04/r-codes-vol-1-explanatory-guideline_2024-mar2024.pdf")]}
