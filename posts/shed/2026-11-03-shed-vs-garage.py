BODY = """
<h2>The difference in planning terms</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Shed (outbuilding)</th><th>Garage</th></tr></thead><tbody>
<tr><td>What it is</td><td>A detached building that isn't lived in</td><td>The R-Codes define a garage as a roofed structure for vehicles, other than a carport, <strong>attached to the house</strong></td></tr>
<tr><td>Building class</td><td>Class 10a</td><td>Class 10a</td></tr>
<tr><td>Building permit</td><td>Yes, unless 10 m² or less and 2.4 m or lower</td><td>Yes</td></tr>
<tr><td>Main planning rules</td><td>Size limits (often 60 m² or 10% of the lot), wall 2.4 m, ridge 4.2 m, 1 m from boundaries</td><td>Street setback (4.5 m at Stirling, or closer if 0.5 m behind the house), boundary walls, minimum sizes</td></tr>
<tr><td>Registered builder</td><td>Not needed under $50,000</td><td>Not needed under $50,000</td></tr>
</tbody></table></div>

<h2>What both need</h2>
<p>Both are Class 10a buildings under the building code, so the building permit process is the same: plans, engineering, a BA1 or BA2 application, and council fees of 0.32% of the value for a BA2 (at least $121). Since <strong>1 July 2026</strong>, a Class 10a building worth <strong>less than $50,000</strong> doesn't have to be built by a registered builder, and you can build it yourself without owner-builder approval.</p>

<h2>Sheds: the outbuilding rules</h2>
<p>At councils like Wanneroo and Melville, a shed skips planning approval if it's no more than 60 m² or 10% of the lot, walls are no higher than 2.4 m and the ridge no higher than 4.2 m, and it's at least 1 m from side and rear boundaries. Go bigger or taller and you'll need planning approval.</p>

<h2>Garages: the street and boundary rules</h2>
<p>At the City of Stirling, a garage can be as close as <strong>4.5 m</strong> to the front boundary, or closer if it's at least 0.5 m behind the front of the house. A garage wall can go on the side boundary on R20 lots and above, but must sit behind the primary street setback (6 m on R20 and R25, 4 m on R30 and R40). Minimum size is 5.4 m long and 2.4 m wide for a single, or 4.8 m wide for a double.</p>

<h2>Freestanding garages</h2>
<p>A garage that isn't attached to the house doesn't fit the R-Codes garage definition. Ask your council whether it will assess yours under its garage rules or its outbuilding (shed) rules, as this changes the size and height limits.</p>
"""

FAQS = [
    ("Do sheds and garages need the same permit?",
     "Both are Class 10a buildings and need a building permit, apart from small sheds of 10 m² or less and 2.4 m or lower. The planning rules are different: sheds follow outbuilding rules and garages follow street setback and boundary wall rules."),
    ("Do I need a registered builder for a garage in WA?",
     "Not if it's worth less than $50,000. From 1 July 2026, Class 10a buildings like garages, sheds, carports and patios under $50,000 don't need a registered builder."),
    ("How close to the street can a garage be?",
     "At the City of Stirling, 4.5 m from the front boundary, or closer if the garage is at least 0.5 m behind the front of the house."),
    ("Is a freestanding garage a shed?",
     "It doesn't fit the R-Codes garage definition, which covers garages attached to the house. Ask your council which rules it will use."),
]


def page(S):
    return {"path": "shed-vs-garage.html", "published": "2026-11-03", "type": "Comparison", "icon": "garage",
            "card": "Both need a building permit, but the planning rules are different. Here's how they compare.",
            "title": "Shed vs Garage: What Approvals Each Needs (WA)",
            "desc": "Shed vs garage approvals in WA: building permits, outbuilding size and height limits, garage street setbacks and boundary walls, and the $50,000 registered builder threshold.",
            "eyebrow": "Comparison", "h1": "Shed vs garage: what approvals each needs", "crumb": "Shed vs garage",
            "answer": "<p>Both are Class 10a buildings and need a <strong>building permit</strong> (except sheds of 10 m² or less and 2.4 m or lower). The difference is planning: sheds follow the <strong>outbuilding rules</strong> (size, height, 1 m from boundaries), while garages follow <strong>street setback and boundary wall</strong> rules.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/garage-building-permit", "Garage building permits"), ("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/shed-size-checker", "Shed size checker")],
            "sources": [("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Building or renovating your home: Class 10a threshold (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Outbuildings information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/360/outbuildings_-_information_sheet.pdf"),
                        ("Building a shed or outbuilding (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding")]}
