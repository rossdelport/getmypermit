BODY = """
<h2>Do you need a building permit?</h2>
<p>The City of Wanneroo calls a patio "an unenclosed structure covered in a water-impermeable material". Gazebos and thatched structures count as patios too.</p>
<ul>
<li><strong>No building permit</strong> if the patio is freestanding, <strong>10 m² or less</strong> and <strong>2.4 m or lower</strong>.</li>
<li><strong>Every attached patio</strong> needs a building permit, whatever its size.</li>
</ul>
<p>You only need planning approval (a development application) if the patio doesn't meet the standard R-Codes rules below.</p>

<h2>Setbacks</h2>
<div class="table-wrap"><table>
<thead><tr><th>Where</th><th>Rule</th></tr></thead><tbody>
<tr><td>Side and rear boundary</td><td>1 m to the post for a patio 14 m long or less; 1.5 m if longer (the length includes structures next to it)</td></tr>
<tr><td>Posts on the boundary</td><td>Allowed if the patio is no longer than 10 m and no higher than 2.7 m, the roof is 500 mm back from the boundary, and it's behind the front setback</td></tr>
<tr><td>Front of the house</td><td>Can come forward to half the street setback: 3 m from the boundary on R20, 2 m on R30</td></tr>
<tr><td>Secondary street (corner lots)</td><td>1.5 m</td></tr>
<tr><td>Eaves</td><td>Can project up to 0.75 m into a setback</td></tr>
<tr><td>Building code fire separation</td><td>900 mm from the patio roof to the boundary, or 900 mm between a freestanding patio and the house</td></tr>
</tbody></table></div>
<p>These apply to most R20 and R30 lots. Estates with a Local Development Plan can have different rules.</p>

<h2>What to lodge</h2>
<ul>
<li>BA2 building permit application</li>
<li>Site plan at 1:200 with levels, setbacks, any septic system and a north point</li>
<li>Elevations and sections at 1:100</li>
<li>Construction details, including how it connects to the roof and the footings</li>
<li>Structural engineer's details</li>
<li>Street and Verge Bond application</li>
<li>Planning approval, if you needed one</li>
</ul>

<h2>Fees</h2>
<p>The building permit is 0.32% of the value (at least $121), plus the $61.65 Building Services Levy for work up to $45,000. Wanneroo also charges a <strong>$140</strong> verge bond admin fee. If the work is worth <strong>$20,000 or more</strong>, add a <strong>$2,200</strong> refundable bond.</p>

<h2>Contact</h2>
<p>City of Wanneroo, phone <strong>(08) 9405 5000</strong>.</p>
"""

FAQS = [
    ("Do I need council approval for a patio in Wanneroo?",
     "Every attached patio needs a building permit. A freestanding patio doesn't if it's 10 m² or less and 2.4 m or lower. Planning approval is only needed if the patio doesn't meet the standard R-Codes rules."),
    ("How close to the boundary can a patio be in Wanneroo?",
     "1 m to the post if the patio is 14 m long or less, or 1.5 m if longer. Posts can go on the boundary if the patio is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back."),
    ("What is the Wanneroo verge bond for a patio?",
     "A $140 admin fee with every building permit, plus a $2,200 refundable bond if the work is worth $20,000 or more."),
    ("Can a patio go in front of the house in Wanneroo?",
     "Yes, up to half the street setback: 3 m from the front boundary on an R20 lot or 2 m on R30, if it meets the other R-Codes rules."),
]


def page(S):
    return {"path": "city-of-wanneroo-patio-rules.html", "published": "2026-11-02", "type": "Council guide", "icon": "pergola",
            "card": "When Wanneroo patios need a permit, the boundary setbacks, what to lodge and the verge bond.",
            "title": "City of Wanneroo Patio Rules: Permits, Setbacks and Fees",
            "desc": "City of Wanneroo patio rules: when you need a building permit, side and front setbacks, posts on the boundary, what to lodge, and the $140 verge bond and $2,200 bond.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo patio rules", "crumb": "Wanneroo patio rules",
            "answer": "<p>In Wanneroo, <strong>every attached patio needs a building permit</strong>. A freestanding one doesn't if it's 10 m² or less and 2.4 m or lower. Keep posts <strong>1 m</strong> from the side boundary (1.5 m if over 14 m long), or on the boundary if no longer than 10 m and no higher than 2.7 m. Expect a $140 verge bond fee too.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/patio-approval-checker", "Patio approval checker"), ("/patio-approval-cost-perth", "Patio approval cost in Perth")],
            "sources": [("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
