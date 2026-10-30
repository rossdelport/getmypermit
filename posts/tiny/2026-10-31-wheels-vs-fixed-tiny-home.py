BODY = """
<h2>The legal difference in one line</h2>
<p>In WA, a tiny home <strong>on wheels is a caravan</strong>, covered by the Caravan Parks and Camping Grounds rules. A tiny home <strong>on footings is a building</strong>: a single house on an empty lot, or an ancillary dwelling (granny flat) on a lot that already has a house. Everything else follows from that.</p>

<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>On wheels</th><th>Fixed (on footings)</th></tr></thead><tbody>
<tr><td>What the law calls it</td><td>Caravan</td><td>Single house or ancillary dwelling</td></tr>
<tr><td>Approval to live in it</td><td>Up to 5 nights: landowner's OK. Longer: council approval, up to 24 months at a time</td><td>Building permit before it is placed; planning approval if it doesn't meet the standard rules</td></tr>
<tr><td>How long you can stay</td><td>Time-limited; re-apply when the approval ends</td><td>Permanently</td></tr>
<tr><td>Building code</td><td>Doesn't apply as a building, but it must be roadworthy</td><td>Must meet the building code, including energy efficiency and bushfire rules if the lot is bushfire-prone</td></tr>
<tr><td>Size limits</td><td>2.5 m wide and 4.3 m high to tow without a permit</td><td>Planning rules; 70 m&sup2; internal floor area to skip planning approval as a granny flat</td></tr>
<tr><td>Services</td><td>Council can require power, water, sewage and cooking facilities as conditions</td><td>Connected like any house by licensed trades</td></tr>
<tr><td>Can you move it?</td><td>Yes</td><td>Not easily</td></tr>
</tbody></table></div>

<h2>Choose wheels if</h2>
<ul>
<li>You need somewhere to live <strong>while building</strong> your main house. Councils such as the Shire of Mundaring allow this for up to 2 years.</li>
<li>Your plans are short-term or might change.</li>
<li>You want to take the home with you when you move.</li>
</ul>

<h2>Choose fixed if</h2>
<ul>
<li>You want to live there <strong>for good</strong>, without re-applying.</li>
<li>You want to rent it out long-term, or add lasting value to the property.</li>
<li>Your lot already has a house and the tiny home fits within the 70 m&sup2; granny flat rules.</li>
</ul>

<h2>Switching from wheels to fixed later</h2>
<p>Many people start on wheels and plan to fix the home down later. Once it goes on footings it needs a <strong>building permit</strong> and must meet the building code like any new house. Homes built as trailers often need changes to pass, such as insulation, ceiling heights and the energy efficiency rating. If that's your plan, choose a builder who designs to the building code from the start.</p>
"""

FAQS = [
    ("Is a tiny home on wheels a caravan in WA?",
     "Yes. On wheels, it is treated as a caravan under the Caravan Parks and Camping Grounds rules. You can stay up to 5 nights with the landowner's OK, or up to 24 months at a time with council approval."),
    ("Does a fixed tiny home need a building permit?",
     "Yes. On footings it is a building: a single house on an empty lot or an ancillary dwelling (granny flat) on a lot with a house. It needs a building permit and must meet the building code."),
    ("Which is easier to get approved?",
     "A tiny home on wheels needs no building permit, so it is simpler, but the approval is time-limited. A fixed tiny home takes more paperwork once, then it can stay permanently."),
    ("Can I take the wheels off my tiny home?",
     "Yes, but it then becomes a building and needs a building permit before it is fixed down. It must meet the building code, which many trailer-built homes need changes to pass."),
]


def page(S):
    return {"path": "wheels-vs-fixed-tiny-home.html", "published": "2026-10-31", "type": "Comparison", "icon": "tiny",
            "card": "On wheels it's a caravan; on footings it's a house. Approvals, time limits, the building code and which to choose.",
            "title": "Tiny Home on Wheels vs Fixed Tiny Home in WA: Which Approval?",
            "desc": "In WA a tiny home on wheels is a caravan and a fixed tiny home is a house. Approvals, how long you can stay, the building code, size limits and which suits you.",
            "eyebrow": "Comparison", "h1": "Tiny home on wheels vs fixed tiny home", "crumb": "Wheels vs fixed",
            "answer": "<p>On wheels, a tiny home is a <strong>caravan</strong>: no building permit, but you can only live in it for <strong>5 nights</strong> with the landowner's OK, or <strong>up to 24 months</strong> at a time with council approval. On footings, it's a <strong>building</strong>: it needs a building permit and must meet the building code, but you can live in it permanently.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels: WA rules"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/moving-a-tiny-home", "Moving a tiny home onto your land")],
            "sources": [("Temporary accommodation and camping outside of caravan parks (WA Government, updated June 2026)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Tiny homes (Shire of Mundaring)", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx"),
                        ("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Permits, orders and schemes: vehicle size limits (Main Roads WA)", "https://www.mainroads.wa.gov.au/heavy-vehicles/permit-order-scheme/")]}
