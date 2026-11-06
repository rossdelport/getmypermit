BODY = """
<h2>Tiny home on wheels: it's temporary accommodation</h2>
<p>In WA a tiny home on wheels is treated like a caravan. Under the state rules you can stay in one on private land for up to <strong>5 nights</strong> with the landowner's OK. For longer, you need council approval, which can be given for up to <strong>24 months</strong> at a time.</p>
<p>The City of Swan has an "Application to reside in temporary accommodation" form for this. It lists caravans, tiny homes on wheels, and buses or similar temporary structures. It's handled by the City's Health Services team.</p>

<h2>What the City of Swan asks for</h2>
<ul>
<li>A plan of the inside layout of the tiny home</li>
<li>A site plan showing where it will sit, how close it is to other buildings, and how close it is to houses next door</li>
<li>How wastewater will be handled: connection to sewer, to an existing septic system, or to a new one</li>
<li>Where the drinking water comes from: scheme water, or a tank (with its size)</li>
<li>A description of the power supply</li>
<li>Where the bathroom facilities are. These must include a toilet, shower, wash trough and kitchen sink</li>
<li>A copy of the vehicle registration</li>
<li>A bushfire plan, if the property is in a bushfire-prone area</li>
</ul>
<p>If you're the person who'll live in it but not the owner, the landowner also signs to support the application.</p>

<h2>Registration matters</h2>
<p>The City says it will only approve temporary accommodation for <strong>licensed (registered) vehicles</strong>. If the registration details aren't known yet, it gives a conditional approval until you provide them. So keep your tiny home's trailer registered.</p>

<h2>Bushfire-prone land</h2>
<p>Much of the Swan Valley and hills area is bushfire-prone. On these properties you must sign an acknowledgement that the tiny home isn't designed to withstand a bushfire, and agree to leave early if a fire threatens. You can check your property on the DFES bushfire-prone areas map.</p>

<h2>Fees and how to lodge</h2>
<p>There's a fee for the temporary licence under the Caravan Parks and Camping Grounds Act, paid before the application is processed. You can lodge the form in person at 2 Midland Square, Midland or at a City of Swan library, by mail, or by email. The form also covers renewing an existing approval.</p>

<h2>Fixed tiny home: it's a building</h2>
<p>If your tiny home sits on footings without wheels, it's a building. It needs a building permit and must meet the National Construction Code, like any home. See <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>, and check which one yours is with the <a href="/caravan-or-building-checker">caravan or building checker</a>. For the state-wide rules, read <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules in WA</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home in the City of Swan?",
     "Yes, with approval. Up to 5 nights needs only the landowner's OK. Longer stays need the City's approval for temporary accommodation, for up to 24 months at a time."),
    ("What do I need to apply for a tiny home in the City of Swan?",
     "A layout plan, a site plan, details of wastewater, drinking water and power, the location of a toilet, shower, wash trough and kitchen sink, a copy of the vehicle registration, and a bushfire plan if needed."),
    ("Does my tiny home need to be registered in the City of Swan?",
     "Yes. The City only approves temporary accommodation for licensed vehicles. If the registration isn't known yet, it gives a conditional approval."),
    ("Is there a fee for tiny home approval in the City of Swan?",
     "Yes. There's a fee for the temporary licence under the Caravan Parks and Camping Grounds Act, paid before the application is processed."),
    ("Does a tiny home without wheels need a building permit in the City of Swan?",
     "Yes. A fixed tiny home is a building, so it needs a building permit and must meet the National Construction Code."),
]


def page(S):
    return {"path": "city-of-swan-tiny-homes.html", "published": "2026-11-07", "type": "Council guide", "icon": "pin",
            "card": "The City of Swan's temporary accommodation form: what it asks for and the rules.",
            "title": "City of Swan Tiny Home Rules (2026)",
            "desc": "Living in a tiny home in the City of Swan: the temporary accommodation application, what you need, registration, bushfire rules, and fixed tiny homes.",
            "eyebrow": "Council guide", "h1": "City of Swan tiny home rules", "crumb": "City of Swan tiny homes",
            "answer": "<p>A tiny home on wheels counts as temporary accommodation. Up to <strong>5 nights</strong> needs only the landowner's OK. For longer, apply to the City of Swan on its temporary accommodation form, with plans, water, wastewater and power details, and the <strong>vehicle registration</strong>. Approval can be for up to <strong>24 months</strong>. A tiny home without wheels needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules in WA"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/caravan-or-building-checker", "Caravan or building checker")],
            "sources": [("Application to reside in temporary accommodation (City of Swan)", "https://www.swan.wa.gov.au/awcontent/Web/Documents/Services%20and%20Community/Public%20health/W-AP-Temporary-Accommodation-Application-Form.pdf"),
                        ("Temporary accommodation and camping outside of caravan parks (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks")]}
