BODY = """
<h2>Two kinds of tiny home</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Tiny home on wheels</th><th>Tiny home not on wheels</th></tr></thead><tbody>
<tr><td>Treated as</td><td>A caravan</td><td>A building (a house or granny flat)</td></tr>
<tr><td>Up to 5 nights</td><td>Fine with the landowner's OK</td><td>Needs a building permit before anyone lives in it</td></tr>
<tr><td>Over 5 nights, up to 24 months</td><td>Written approval from the Shire or the Minister</td><td>As above</td></tr>
<tr><td>Permanent</td><td>Only in a licensed caravan park</td><td>Yes, once approved</td></tr>
</tbody></table></div>

<h2>Fixed tiny homes: building rules</h2>
<p>A tiny home not on wheels needs a <strong>building permit</strong>, and may need planning approval too. In Dardanup, the permit application must be <strong>certified by a private building surveyor</strong> (a BA1). It must meet the building code and the Shire's health local laws, including:</p>
<ul>
<li>a kitchen, bathroom and laundry,</li>
<li>ceilings at least 2.4 m in living rooms and bedrooms, and 2.1 m in bathrooms, toilets, laundries and kitchens,</li>
<li>connection to sewer or an approved on-site wastewater system,</li>
<li>power, water and hot water, with compliance for electrical, plumbing and any gas work,</li>
<li>smoke alarms, ventilation, light and energy efficiency,</li>
<li>termite protection and bushfire construction if in a bushfire prone area, and</li>
<li>engineer certification of the structure, including how it's fixed to the ground.</li>
</ul>

<h2>Planning rules</h2>
<p>Fixed tiny homes must meet the Shire's Local Planning Scheme No. 9 and its policies, whether used as a house or a granny flat. That covers the R-Codes, setbacks or building envelopes, services and bushfire rules.</p>
<p>Check before you buy. Call the Shire on (08) 9724 0000. See <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>, <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules</a> and <a href="/tiny-home-services">connecting services</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in Dardanup?",
     "Yes, for up to 5 nights with the landowner's OK. For longer, up to 24 months, you need written approval from the Shire or the Minister. Permanent living is only allowed in a licensed caravan park."),
    ("Does a fixed tiny home need a permit in Dardanup?",
     "Yes. It needs a building permit, certified by a private building surveyor, and it may need planning approval too."),
    ("What ceiling height does a tiny home need in Dardanup?",
     "At least 2.4 m in living rooms and bedrooms, and 2.1 m in bathrooms, toilets, laundries and kitchens."),
    ("Does a tiny home need a kitchen and bathroom in Dardanup?",
     "Yes. A fixed tiny home must have a kitchen, bathroom and laundry."),
]


def page(S):
    return {"path": "shire-of-dardanup-tiny-homes.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "Shire of Dardanup tiny home rules: wheels vs fixed, the 5-night and 24-month rules and building standards.",
            "title": "Shire of Dardanup Tiny Home Rules (2026)",
            "desc": "Shire of Dardanup tiny home rules: tiny homes on wheels (5 nights, up to 24 months with approval), fixed tiny homes needing a certified building permit, ceiling heights, services and planning.",
            "eyebrow": "Council guide", "h1": "Shire of Dardanup tiny home rules", "crumb": "Dardanup tiny homes",
            "answer": "<p>In the Shire of Dardanup, a <strong>tiny home on wheels</strong> counts as a caravan. You can stay up to <strong>5 nights</strong> with the owner's OK, or up to <strong>24 months</strong> with written approval. A <strong>fixed tiny home</strong> needs a building permit certified by a private building surveyor.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/fixed-tiny-home-permit", "Fixed tiny home permit"), ("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/tiny-home-services", "Tiny home services")],
            "sources": [("Tiny homes, Shire of Dardanup", "https://www.dardanup.wa.gov.au/development-and-planning/building/tiny-homes.aspx")]}
