BODY = """
<h2>Why there's no real "small carport" exemption</h2>
<p>The WA Building Regulations exempt small freestanding structures from a building permit: <strong>10 m&sup2; or less and no taller than 2.4 m</strong>. Some websites say a carport can use this. On paper it can, but look at the size of a car space:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Size</th><th>Area</th></tr></thead><tbody>
<tr><td>Exemption limit</td><td>e.g. 3.2 m x 3.1 m</td><td>10 m&sup2;</td></tr>
<tr><td>Minimum car space (City of Stirling)</td><td>5.4 m x 2.4 m</td><td>about 13 m&sup2;</td></tr>
</tbody></table></div>
<p>A real car won't fit under a 10 m&sup2; roof. That's why councils like Stirling and Wanneroo simply say a carport <strong>always needs a building permit</strong>. The exemption also only covers freestanding structures, and most carports are fixed to the house.</p>

<h2>What size avoids planning approval?</h2>
<p>This is the question that matters more. Planning approval isn't about a size limit; it's about whether the carport meets the standard rules for your lot. Most carports skip it if they:</p>
<ul>
<li>Take up no more than <strong>60% of the lot's frontage</strong>.</li>
<li>Keep a clear view between the house and the street (open sides, no solid doors).</li>
<li>Sit at least the reduced street setback. At Wanneroo, the normal setback (6 m at R20, 4 m at R30 to R40) can be halved for a carport that meets the frontage, open-sides and matching-materials rules.</li>
<li>Aren't on a heritage-listed property or in a heritage area.</li>
</ul>
<p>Posts on a side boundary can also be allowed. Wanneroo accepts this for carports no longer than 10 m and no higher than 2.7 m, with the roof set 500 mm back. <a href="/carport-in-front-setback">More on carports in the front setback</a>.</p>

<h2>So what should you do?</h2>
<p>Plan on a building permit for any carport you can park a car under. For most, the council fees are about $183 in total. If yours is in the front setback or near the boundary, check the planning rules before you buy a kit, because that's where carports get refused.</p>
"""

FAQS = [
    ("What size carport can you build without council approval in WA?",
     "Effectively none. The building permit exemption only covers freestanding structures up to 10 m&sup2; and 2.4 m high, which is too small to park a car under. Councils such as Stirling and Wanneroo say every carport needs a building permit."),
    ("Does a carport need planning approval?",
     "Not if it meets the standard planning rules: within 60% of the frontage, open to views from the street, at the right setback and not on a heritage property. Otherwise it needs planning approval first."),
    ("Can a carport be built on the boundary in WA?",
     "Often, yes. The City of Wanneroo, for example, allows carport posts on the boundary if the carport is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back from the boundary."),
    ("What is the minimum size for a carport?",
     "The City of Stirling's minimum car space is 5.4 m long and 2.4 m wide, about 13 m&sup2;. That's already bigger than the 10 m&sup2; permit exemption."),
]


def page(S):
    return {"path": "carport-size-without-approval.html", "published": "2026-10-31", "type": "Question answer", "icon": "carport",
            "card": "The 10 m² exemption explained, why it doesn't fit a car, and the size rules that decide planning approval.",
            "title": "What Size Carport Can You Build Without Council Approval in WA?",
            "desc": "In WA the permit exemption stops at 10 m² and 2.4 m high, too small for a car, so every real carport needs a building permit. The size rules for planning approval explained.",
            "eyebrow": "Question answer", "h1": "What size carport can you build without approval?", "crumb": "Carport size without approval",
            "answer": "<p>Effectively <strong>none</strong>. The exemption only covers freestanding structures up to <strong>10 m&sup2; and 2.4 m high</strong>, and a car space is at least about 13 m&sup2;. So every carport you can park under needs a <strong>building permit</strong>. Planning approval is different: most carports skip it if they stay within 60% of the frontage, keep views to the street and meet the setbacks.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/carport-in-front-setback", "Carports in the front setback"), ("/carport-approval-cost-perth", "Carport approval cost")],
            "sources": [("Do I need a permit? Exempt structures (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf")]}
