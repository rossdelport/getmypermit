BODY = """
<h2>Building permit</h2>
<p>The City of South Perth lists carports among the structures that need a building permit. Lodge a BA1 (certified by a private building surveyor) or a BA2 (checked by the City).</p>

<h2>Street setback</h2>
<p>South Perth's Local Planning Policy 1.1 (Residential Development, last changed August 2025) changes some R-Codes rules. A carport normally follows the usual primary street setback for your zoning. It can come forward by up to <strong>half</strong> that setback if:</p>
<ul>
<li>the carport and its posts are at least <strong>0.5 m</strong> from the side boundaries,</li>
<li>it's no wider than <strong>60%</strong> of the lot frontage,</li>
<li>it has <strong>no walls</strong> in the part that sits inside the street setback,</li>
<li>you can see clearly between the house and the street, and</li>
<li>it has <strong>no enclosed storeroom</strong>.</li>
</ul>
<p>The 0.5 m side gap and the storeroom rule are extras South Perth adds on top of the R-Codes. Work out your numbers with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>.</p>

<h2>Garages are set back further</h2>
<p>For most houses (R-Codes Part B), the policy sets garages <strong>5.0 m</strong> from the primary street, instead of the usual 4.5 m. A garage joined to the house can be closer if it sits at least 0.5 m behind the front of the house. See <a href="/carport-vs-garage">carport vs garage</a>.</p>

<h2>Side and rear boundaries</h2>
<p>Under the R-Codes, a carport can usually have its posts on the boundary if it's no more than <strong>10 m</strong> long and <strong>2.7 m</strong> high, sits behind the street setback, and its roof, eaves and gutters are at least <strong>450 mm</strong> from the boundary. The building code has its own fire rules too. See <a href="/carport-on-boundary">carports on the boundary</a>.</p>

<h2>If you can't meet these rules</h2>
<p>A carport that doesn't meet the policy and the R-Codes needs planning (development) approval before the building permit. Call the City on 9474 0777.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in South Perth?",
     "Yes. The City of South Perth lists carports as needing a building permit."),
    ("How close to the street can a carport be in South Perth?",
     "Up to half the usual primary street setback, if it's 0.5 m from side boundaries, no wider than 60% of the frontage, has no walls in the setback, keeps a clear view and has no enclosed storeroom."),
    ("Can a South Perth carport have a storeroom?",
     "Not if you want the reduced street setback. The policy says the carport must not include an enclosed storeroom."),
    ("How far back must a garage be in South Perth?",
     "Usually 5.0 m from the primary street for most houses, or closer if the garage joins the house and sits 0.5 m behind its front."),
]


def page(S):
    return {"path": "city-of-south-perth-carport-rules.html", "published": "2026-11-28", "type": "Council guide", "icon": "pin",
            "card": "City of South Perth carport rules: the 50% street setback cut, 0.5 m side gap, no storerooms and 5 m garages.",
            "title": "City of South Perth Carport Rules (2026)",
            "desc": "City of South Perth carport rules: building permits, how far forward a carport can go under Local Planning Policy 1.1, the 0.5 m side gap and 60% frontage limit, garage setbacks and boundary posts.",
            "eyebrow": "Council guide", "h1": "City of South Perth carport rules", "crumb": "South Perth carport rules",
            "answer": "<p>In the City of South Perth, a carport needs a <strong>building permit</strong>. It can come forward by up to <strong>half</strong> the usual street setback if it's <strong>0.5 m</strong> from the side boundaries, no wider than <strong>60%</strong> of the frontage, has no walls in the setback, keeps a clear view and has no storeroom.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-on-boundary", "Carport on the boundary"), ("/carport-vs-garage", "Carport vs garage")],
            "sources": [("Building approvals, City of South Perth", "https://southperth.wa.gov.au/development/building/building-approvals"),
                        ("Local Planning Policy 1.1: residential development (modified 26 Aug 2025), City of South Perth", "https://southperth.wa.gov.au/docs/default-source/6-about-us/council/policies-delegations/environment-(built-and-natural)/local-planning-policy---residential-development.pdf?sfvrsn=74aca9bd_10")]}
