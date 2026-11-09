BODY = """
<h2>Short answer: location isn't banned, setbacks decide it</h2>
<p>WA's R-Codes define a granny flat (ancillary dwelling) as a self-contained home on the same lot as the main house. It can be attached, integrated or detached. Nothing in that definition says it must be at the back. What matters is whether it meets the same rules as any other building on your lot, especially the <strong>street setback</strong>.</p>

<h2>The rules that apply at the front</h2>
<p>To skip planning approval, a granny flat must meet all the deemed-to-comply rules, including:</p>
<ul>
<li><strong>Street setback.</strong> It must sit back from the street as far as your R-Code requires. In Joondalup's R20 areas, for example, buildings need an average street setback of 6 m.</li>
<li><strong>Size.</strong> No more than 70 m² of internal floor area.</li>
<li><strong>Looks.</strong> Joondalup requires the flat to match the colour, roof pitch and materials of the main house. This matters more when it's visible from the street.</li>
<li><strong>Open space, height and privacy.</strong> As for any building on the lot.</li>
<li><strong>Parking.</strong> The R-Codes ask for one extra car bay for the flat on most house lots (single houses R40 and below), unless you're within an 800 m walk of a train station or 250 m of a high-frequency bus stop.</li>
</ul>
<p>A front granny flat can also make it harder to fit the driveway, parking and front garden the rules expect, so plan these together.</p>

<h2>Corner lots</h2>
<p>A corner lot has a secondary street with a smaller setback, often 1.5 m to 2 m depending on the R-Code. That can make a flat on the side street easier to fit than one at the very front.</p>

<h2>If it doesn't fit the rules</h2>
<p>You can apply for planning approval. The council looks at how it affects the streetscape, neighbours and parking. Councils vary in how they treat granny flats in the front setback, so ask early.</p>

<h2>Watch out for old council rules</h2>
<p>Some older council documents still say a granny flat must be for family members only, or need a 450 m² lot. The state's 2024 R-Codes changes removed the lot size minimum and allow anyone to live in a granny flat, including tenants. Make sure you're reading current rules.</p>

<h2>You still need a building permit</h2>
<p>Wherever it goes, every granny flat needs a building permit. See the <a href="/granny-flat-approval-process">granny flat approval process</a>, check your design with the <a href="/granny-flat-size-calculator">70 m² calculator</a>, or read the <a href="/granny-flat-rules-wa">granny flat rules in WA</a>.</p>
"""

FAQS = [
    ("Can I build a granny flat at the front of my property in WA?",
     "Yes, if it meets the street setback and other R-Code rules for your lot. If it doesn't, you can apply for planning approval. Councils vary in how they assess front granny flats."),
    ("How far from the street does a granny flat need to be?",
     "The same street setback as other buildings on your lot, set by your R-Code. In Joondalup's R20 areas, buildings need an average street setback of 6 m."),
    ("Does a granny flat have to match the house?",
     "In Joondalup, yes: it must match the colour, roof pitch and materials of the main house to skip planning approval. Check your council's rules."),
    ("Can a granny flat go on the side street of a corner lot?",
     "Often that's easier, because secondary street setbacks are smaller, often 1.5 m to 2 m depending on the R-Code."),
    ("Does a front granny flat need extra parking?",
     "Usually. The R-Codes ask for one extra bay on most house lots, unless you're close to a train station or high-frequency bus stop."),
]


def page(S):
    return {"path": "granny-flat-at-the-front.html", "published": "2026-11-08", "type": "Question answer", "icon": "granny",
            "card": "Front granny flats are allowed if they meet the street setback and design rules.",
            "title": "Can a Granny Flat Go at the Front of Your Property in WA?",
            "desc": "Putting a granny flat at the front of your block in WA: street setbacks, matching the house, parking, corner lots, and when you need planning approval.",
            "eyebrow": "Question answer", "h1": "Can a granny flat go at the front of your property?", "crumb": "Granny flat at the front",
            "answer": "<p><strong>Yes, if it meets the rules.</strong> WA's R-Codes don't require a granny flat to be at the back. It must meet the same <strong>street setback</strong> as other buildings on your lot, be <strong>70 m² or less</strong>, and in councils like Joondalup match the main house. If it can't, you can apply for planning approval. You always need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-approval-process", "Granny flat approval process"), ("/granny-flat-size-calculator", "Granny flat 70 m² calculator"), ("/granny-flat-rules-wa", "Granny flat rules in WA")],
            "sources": [("Granny flat or ancillary dwelling (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/granny-flat-or-ancillary-dwelling"),
                        ("Granny flats info sheet (WA Planning)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Patio, pergola or shade sails: R-Code setbacks (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails")]}
