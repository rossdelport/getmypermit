BODY = """
<h2>Patio, pergola or shade sail?</h2>
<ul>
<li><strong>Patio:</strong> a roof that water can't get through, like Colorbond sheeting.</li>
<li><strong>Pergola:</strong> an open structure with a roof that lets water through, like shade cloth.</li>
<li><strong>Shade sail:</strong> an open structure with a cover that lets water through.</li>
</ul>
<p>Not sure which you have? See <a href="/pergola-vs-patio">pergola vs patio</a>.</p>

<h2>When you don't need a building permit</h2>
<p>In the City of Bayswater, you only skip the permit if <strong>all</strong> of these apply:</p>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>Max area</th><th>Max height</th><th>Attached to anything?</th></tr></thead><tbody>
<tr><td>Patio</td><td>10 m²</td><td>2.4 m</td><td>No</td></tr>
<tr><td>Pergola</td><td>20 m²</td><td>2.4 m</td><td>No</td></tr>
<tr><td>Shade sail</td><td>20 m²</td><td>2.4 m</td><td>No</td></tr>
</tbody></table></div>
<p>So a patio attached to your house always needs a building permit, whatever its size. Check yours with the <a href="/patio-approval-checker">patio approval checker</a>.</p>

<h2>How to apply</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private registered building surveyor, who issues a Certificate of Design Compliance</td><td>The City's building surveyors</td></tr>
<tr><td>City decides within</td><td>10 business days</td><td>25 business days</td></tr>
</tbody></table></div>
<p>Fees must be paid when you lodge, or the City won't accept the application.</p>

<h2>Already built without a permit?</h2>
<p>You can apply for retrospective approval. To see what's already approved on a property, you can lodge a plan search request with the City. See <a href="/existing-patio-approval">approval for an existing patio</a>.</p>
<p>Planning rules (R-Codes, character areas) can still apply even when no building permit is needed. Call the City on 08 9272 0622.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Bayswater?",
     "Yes, unless it's 10 m² or less, no more than 2.4 m high and not attached to any other structure."),
    ("Do I need a permit for a pergola in Bayswater?",
     "Not if it's 20 m² or less, no more than 2.4 m high and not attached to anything."),
    ("Does an attached patio need a permit in Bayswater?",
     "Yes. To be exempt a patio must not be attached to any other structure, so a patio fixed to the house needs a building permit."),
    ("How long does Bayswater take to approve a patio?",
     "Up to 10 business days for a certified (BA1) application and up to 25 business days for an uncertified (BA2) one."),
]


def page(S):
    return {"path": "city-of-bayswater-patio-rules.html", "published": "2026-11-26", "type": "Council guide", "icon": "pin",
            "card": "City of Bayswater patio rules: permit-free limits for patios, pergolas and shade sails, and how to apply.",
            "title": "City of Bayswater Patio and Pergola Rules (2026)",
            "desc": "City of Bayswater patio, pergola and shade sail rules: the size, height and not-attached tests for skipping a permit, BA1 vs BA2 timeframes and retrospective approval.",
            "eyebrow": "Council guide", "h1": "City of Bayswater patio and pergola rules", "crumb": "Bayswater patio rules",
            "answer": "<p>In the City of Bayswater, a <strong>patio</strong> needs a building permit unless it's <strong>10 m²</strong> or less, 2.4 m or lower and <strong>not attached</strong> to anything. Pergolas and shade sails get a <strong>20 m²</strong> limit. The City decides in 10 business days (BA1) or 25 (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/pergola-vs-patio", "Pergola vs patio"), ("/existing-patio-approval", "Approval for an existing patio")],
            "sources": [("Sheds, pergolas and outdoor structures, City of Bayswater", "https://www.bayswater.wa.gov.au/home-and-property/renovating-your-home-or-property/sheds,-pergolas-and-outdoor-structures")]}
