BODY = """
<h2>Step 1: Measure your frontage</h2>
<p>The key number is the width of your lot along the street (the frontage). Under the R-Codes (Volume 1, April 2026, clause 5.2.1 C1.2), a carport can sit closer to the street, by up to <strong>half</strong> the normal front setback, only if it's no wider than <strong>60%</strong> of the frontage.</p>
<div class="table-wrap"><table>
<thead><tr><th>Frontage</th><th>Widest carport for the reduced setback</th></tr></thead><tbody>
<tr><td>8 m</td><td>4.8 m</td></tr>
<tr><td>10 m</td><td>6.0 m</td></tr>
<tr><td>12 m</td><td>7.2 m</td></tr>
<tr><td>15 m</td><td>9.0 m</td></tr>
</tbody></table></div>
<p>So a 6 m wide double carport needs a frontage of at least <strong>10 m</strong> to use the reduced setback. The carport must also leave a clear view between the house and the street, and match the house in roof pitch, colours and materials.</p>

<h2>Step 2: Check the driveway</h2>
<ul>
<li>A driveway is usually <strong>3 m to 6 m</strong> wide at the street boundary.</li>
<li>It should be at least <strong>0.5 m</strong> from the side boundary and from any street pole.</li>
<li>Walls, fences and posts within <strong>1.5 m</strong> of where the driveway meets the street must be no higher than <strong>0.75 m</strong>, so drivers can see.</li>
</ul>
<p>These come from R-Codes clauses 5.3.5 and 5.2.5.</p>

<h2>Step 3: Pick the option that fits</h2>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>When it works</th></tr></thead><tbody>
<tr><td>Double carport in the reduced setback</td><td>Width is 60% of frontage or less</td></tr>
<tr><td>Double carport further back</td><td>Wider carport, set back to the full front setback</td></tr>
<tr><td>Tandem carport (one car behind the other)</td><td>Narrow lots where a double won't fit</td></tr>
<tr><td>Carport off a rear lane</td><td>Lots with a right of way at the back</td></tr>
</tbody></table></div>
<p>Some areas are stricter. For example, in the City of Bayswater's Character Protection Areas, lots with a frontage of 12 m or less can only have a single carport. If your design doesn't meet the standard rules, you can still apply for planning approval. Councils vary. Almost every carport also needs a building permit.</p>
<p>Work out your setback with the <a href="/front-setback-carport-calculator">front setback calculator</a>, read about a <a href="/carport-in-front-setback">carport in the front setback</a>, or see what goes on a <a href="/carport-site-plan">carport site plan</a>.</p>
"""

FAQS = [
    ("Can I fit a double carport on a narrow lot in Perth?",
     "Often yes. To sit closer to the street, the carport can be no wider than 60% of the lot frontage. A 6 m double carport needs about a 10 m frontage."),
    ("How wide can my carport be on a 10 m frontage?",
     "Up to 6 m if you want to use the reduced front setback. A wider carport has to meet the full front setback."),
    ("How wide can my driveway be?",
     "Under the R-Codes, usually between 3 m and 6 m at the street boundary, and at least 0.5 m from the side boundary."),
    ("What if a double carport won't fit?",
     "Consider a tandem carport, setting the carport further back, using a rear lane, or applying for planning approval."),
]


def page(S):
    return {"path": "double-carport-narrow-lot.html", "published": "2026-11-18", "type": "How-to guide", "icon": "plan",
            "card": "How to fit a double carport on a narrow Perth lot: the 60% frontage rule and driveway limits.",
            "title": "Double Carport on a Narrow Lot in Perth (2026)",
            "desc": "How to fit a double carport on a narrow Perth lot: the 60% of frontage rule, driveway width and sightline limits, and options when a double won't fit.",
            "eyebrow": "How-to guide", "h1": "How to fit a double carport on a narrow lot", "crumb": "Double carport on a narrow lot",
            "answer": "<p>Measure your street frontage. Under the R-Codes, a carport can sit closer to the street only if it's no wider than <strong>60% of the frontage</strong>, so a 6 m double carport needs about <strong>10 m</strong> of frontage. If it's wider, set it back further, go tandem or use a rear lane. You'll usually also need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback calculator"), ("/carport-in-front-setback", "Carport in the front setback"), ("/carport-site-plan", "Carport site plan")],
            "sources": [("Residential Design Codes Volume 1 (April 2026), clauses 5.2.1, 5.2.5 and 5.3.5", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Character Protection Areas Policy, City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/policies/2025/character-protection-areas-policy")]}
