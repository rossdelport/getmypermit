BODY = """
<h2>The key point: a tiny home on footings <em>is</em> a granny flat</h2>
<p>In WA the law doesn't have a separate category for "tiny homes". What matters is whether it has wheels:</p>
<ul>
<li><strong>On wheels</strong>, it is treated as a <strong>caravan</strong>, under the Caravan Parks and Camping Grounds rules.</li>
<li><strong>On footings</strong> on a lot that already has a house, it is an <strong>ancillary dwelling</strong>, which is a granny flat. On an empty lot it is a single house.</li>
</ul>
<p>So the real choice is between a granny flat (built on site or delivered as a fixed tiny home) and a tiny home on wheels.</p>

<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Granny flat (or fixed tiny home)</th><th>Tiny home on wheels</th></tr></thead><tbody>
<tr><td>What the law calls it</td><td>Ancillary dwelling</td><td>Caravan</td></tr>
<tr><td>Size limit</td><td>70 m&sup2; internal floor area to skip planning approval</td><td>Road limits: 2.5 m wide, 4.3 m high without a transport permit</td></tr>
<tr><td>Building permit</td><td>Yes</td><td>No (it is a vehicle), but it must be roadworthy</td></tr>
<tr><td>Planning approval</td><td>Not needed if it meets all the standard R-Codes rules on a residential lot</td><td>Not a planning matter; approval comes under the caravan rules</td></tr>
<tr><td>How long you can live in it</td><td>Permanently</td><td>Up to 5 nights with the owner's OK; up to 24 months with council approval, then re-apply</td></tr>
<tr><td>Can you rent it out?</td><td>Yes, to anyone</td><td>Only within what the council approval allows; permanent letting generally needs a licensed caravan park</td></tr>
<tr><td>Services</td><td>Connected to power, water and sewer or septic like a house</td><td>Council can require power, water, sewage and cooking facilities as approval conditions</td></tr>
<tr><td>Adds value to the property?</td><td>Yes, it is a permanent improvement</td><td>No, it stays a vehicle you can sell or move</td></tr>
<tr><td>Can you take it with you?</td><td>No</td><td>Yes</td></tr>
</tbody></table></div>

<h2>When a granny flat is the better choice</h2>
<ul>
<li>Someone will live in it long term, such as a parent or an adult child.</li>
<li>You want rental income with no time limit on approval.</li>
<li>You want to add lasting value to the property.</li>
<li>Your lot fits a 70 m&sup2; flat within the standard setbacks, so you can skip planning approval.</li>
</ul>

<h2>When a tiny home on wheels is the better choice</h2>
<ul>
<li>You need somewhere to live <strong>while you build</strong> your main house.</li>
<li>The need is temporary, such as a family member staying for a year.</li>
<li>You might move, and want to take the home with you.</li>
<li>You can't fit a granny flat within the setbacks on your lot.</li>
</ul>

<h2>The middle option</h2>
<p>Some people buy a tiny home on a trailer and later take the wheels off and put it on footings. At that point it becomes a dwelling and needs a <strong>building permit</strong> like any granny flat. It must meet the building code: a proper kitchen, bathroom and laundry, ceiling heights, energy efficiency, engineering and a bushfire report if the lot is bushfire-prone. Many trailer-built tiny homes need changes to pass, so check before you buy if this is the plan.</p>
"""

FAQS = [
    ("Is a tiny home a granny flat in WA?",
     "A tiny home on footings on a lot with a house is legally an ancillary dwelling, which is a granny flat. A tiny home on wheels is treated as a caravan instead."),
    ("Can I live in a tiny home on wheels in my backyard in WA?",
     "For up to 5 nights with the owner's permission. For longer, you need approval from your council, which can be given for up to 24 months at a time and can come with conditions on power, water and sewage."),
    ("Which is cheaper to approve, a granny flat or a tiny home?",
     "A tiny home on wheels needs no building permit, so approval is simpler and cheaper, but it is time-limited. A granny flat needs a building permit and is permanent."),
    ("Can I rent out a tiny home on wheels?",
     "Only within what your council approval allows. Ongoing rental of a caravan is generally limited to licensed caravan parks, while a granny flat can be rented to anyone."),
]


def page(S):
    return {"path": "granny-flat-vs-tiny-home.html", "published": "2026-10-30", "type": "Comparison", "icon": "tiny",
            "card": "Granny flat or tiny home on wheels? How WA treats each, how long you can live in them, renting, and which suits you.",
            "title": "Granny Flat vs Tiny Home in WA: Approvals, Living and Renting Compared",
            "desc": "In WA a tiny home on footings is legally a granny flat; on wheels it is a caravan. Approvals, how long you can live in each, renting and costs compared.",
            "eyebrow": "Comparison", "h1": "Granny flat vs tiny home", "crumb": "Granny flat vs tiny home",
            "answer": "<p>In WA a <strong>tiny home on footings is legally a granny flat</strong>: it needs a building permit and can be lived in and rented permanently. A <strong>tiny home on wheels is a caravan</strong>: no building permit, but you can only live in it for <strong>5 nights</strong> with the owner's OK, or up to <strong>24 months</strong> with council approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-no-planning-approval", "Granny flat with no planning approval"), ("https://tinyhomepermit.com.au/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels: WA rules")],
            "sources": [("Temporary accommodation and camping outside of caravan parks (WA Government, updated June 2026)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Tiny homes (Shire of Mundaring)", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx"),
                        ("Permits, orders and schemes: vehicle size limits (Main Roads WA)", "https://www.mainroads.wa.gov.au/heavy-vehicles/permit-order-scheme/")]}
