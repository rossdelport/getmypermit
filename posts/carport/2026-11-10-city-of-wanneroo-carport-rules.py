BODY = """
<h2>Do I need approval?</h2>
<p>The City of Wanneroo says a <strong>building permit is always required</strong> for a carport. You only need planning approval (a development application) as well if your carport doesn't meet the R-Codes, for example if it's too close to the street. If planning approval is needed, it must be granted before the building permit is issued.</p>
<p>A carport is a roofed structure for vehicles that stays open, except where it touches the house or a boundary on one side. A door is allowed only if you can see through it. Add a solid door and it's a garage.</p>

<h2>Wanneroo's carport setbacks</h2>
<p>These come from the City's carport information sheet (July 2025) and apply to most lots coded R20 or R30:</p>
<div class="table-wrap"><table>
<thead><tr><th>Setback</th><th>Rule</th></tr></thead><tbody>
<tr><td>Primary street</td><td>6 m on an R20 lot, 4 m on R30 or R40. Can be halved if the carport is no wider than 60% of the frontage, keeps a clear view between house and street, and matches the house.</td></tr>
<tr><td>Secondary street (corner lots)</td><td>1.5 m</td></tr>
<tr><td>Side boundary</td><td>1 m to the post if the carport is 14 m long or less; 1.5 m if longer</td></tr>
<tr><td>On the boundary</td><td>Posts can sit on the boundary, with the roof, eaves and gutters at least 500 mm back, if the carport is no more than 10 m long and 2.7 m high and is behind the primary street setback</td></tr>
<tr><td>Eaves</td><td>Can project no more than 0.75 m into a setback</td></tr>
</tbody></table></div>
<p>Rules can differ on other zonings or where a Local Development Plan or Structure Plan applies. The R-Codes were also updated in April 2026, so check your lot with the City before you design.</p>

<h2>Building code distances</h2>
<p>Separate from planning, the building code says a carport must be <strong>900 mm</strong> from a side boundary or another building on the lot. This can drop to <strong>500 mm</strong> if the carport has two or more open sides (at least a third of its perimeter open), a polycarbonate or non-combustible roof, non-combustible linings, and doesn't hold up any part of the house.</p>

<h2>What to lodge</h2>
<p>For an uncertified application (BA2), Wanneroo asks for:</p>
<ul>
<li>A site plan at 1:200 with spot levels, finished floor level, setbacks to boundaries and buildings (including retaining walls), septic systems and a north point</li>
<li>Floor plan, elevations and sections at 1:100</li>
<li>Construction details and a structural engineer's details</li>
<li>A bushfire (BAL) report if needed</li>
<li>A Street and Verge Bond Permit application, which comes with every building permit</li>
</ul>
<p>For a certified application (BA1), lodge the Certificate of Design Compliance and the documents it refers to. The City prefers online lodgement. Already built without a permit? Wanneroo has a separate checklist for unauthorised works.</p>
<p>Check your front setback with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>, read about <a href="/carport-on-boundary">building a carport on the boundary</a>, or see <a href="/carport-council-approval">carport council approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in Wanneroo?",
     "Yes. The City of Wanneroo says a building permit is always required for a carport. Planning approval is only needed as well if the carport doesn't meet the R-Codes."),
    ("How close to the street can a carport be in Wanneroo?",
     "The City's July 2025 sheet says 6 m on an R20 lot and 4 m on R30 or R40, halved if the carport is no wider than 60% of the frontage, keeps a view to the street and matches the house."),
    ("Can I build a carport on the boundary in Wanneroo?",
     "Yes, the posts can sit on the boundary if the carport is no more than 10 m long and 2.7 m high, behind the street setback, with the roof, eaves and gutters at least 500 mm back."),
    ("Do I need a verge bond for a carport in Wanneroo?",
     "You need to apply for a Street and Verge Bond Permit with every building permit. It has a non-refundable admin fee, and a bond depending on the value of the work."),
]


def page(S):
    return {"path": "city-of-wanneroo-carport-rules.html", "published": "2026-11-10", "type": "Council guide", "icon": "pin",
            "card": "Street and side setbacks, boundary posts, building code distances and what to lodge in Wanneroo.",
            "title": "City of Wanneroo Carport Rules (2026)",
            "desc": "City of Wanneroo carport rules: building permit always needed, 6 m / 4 m street setbacks, posts on the boundary, 900 mm building code rule and what to lodge.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo carport rules", "crumb": "City of Wanneroo carport rules",
            "answer": "<p>In Wanneroo a carport <strong>always needs a building permit</strong>. The City's sheet sets a <strong>6 m</strong> street setback on R20 lots (4 m on R30 or R40), which can be halved if the carport is no wider than 60% of the frontage. Posts can go on the side boundary if it's no more than <strong>10 m</strong> long and <strong>2.7 m</strong> high.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-on-boundary", "Carport on the boundary"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("What approvals do I need? Carports (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/directory_record/115/carports")]}
