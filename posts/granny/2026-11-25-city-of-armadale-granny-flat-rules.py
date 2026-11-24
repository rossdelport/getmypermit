BODY = """
<h2>The main rules</h2>
<ul>
<li><strong>Size:</strong> up to <strong>70 m²</strong>, not counting open verandahs or carports.</li>
<li><strong>How many:</strong> one granny flat per property.</li>
<li><strong>Type:</strong> detached, attached, or built into the house.</li>
<li><strong>Permit:</strong> a building permit is <strong>always</strong> needed before work starts. Health or planning approval may be needed first.</li>
</ul>

<h2>Who can build it</h2>
<p>If the work is worth <strong>$20,000 or more</strong>, you need a registered builder or owner-builder approval. A registered builder must also get a <strong>home indemnity insurance</strong> certificate for a granny flat over $20,000. Owner-builders don't need one at this stage.</p>

<h2>What to send</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Details</th></tr></thead><tbody>
<tr><td>Form</td><td>BA1 or BA2, filled in fully, signed by the builder and applicant</td></tr>
<tr><td>Certificate of Design Compliance</td><td>BA1 only</td></tr>
<tr><td>Site plan at 1:200</td><td>Granny flat, other buildings, boundary distances, septic tanks if any, a <strong>2 m x 2 m tree planting area</strong>, and landscaping and paving in the front setback</td></tr>
<tr><td>Plans at 1:100</td><td>Floor plan, elevations and cross-sections</td></tr>
<tr><td>Reports</td><td>Structural engineer's certification, specifications, energy efficiency report and termite treatment</td></tr>
<tr><td>If needed</td><td>BAL assessment, health approval, planning approval, home indemnity insurance</td></tr>
<tr><td>Over $100,000</td><td>Construction Training Fund levy receipt</td></tr>
</tbody></table></div>

<h2>Timeframes</h2>
<ul>
<li>BA1 (certified by a private building surveyor): up to <strong>10 business days</strong>.</li>
<li>BA2 (checked by the City): up to <strong>25 business days</strong>.</li>
<li>The permit lasts <strong>2 years</strong>, and the builder sends a BA7 within 7 days of finishing.</li>
</ul>
<p>Call Building Services on 9394 5000. See <a href="/granny-flat-building-permit">the granny flat building permit</a>, <a href="/granny-flat-approval-process">the approval process</a> and <a href="/choosing-a-granny-flat-builder">choosing a builder</a>.</p>
"""

FAQS = [
    ("How big can a granny flat be in the City of Armadale?",
     "Up to 70 m², not counting open verandahs or carports. Only one is allowed per property."),
    ("Do I need a building permit for a granny flat in Armadale?",
     "Yes, always, before any work starts. Health or planning approval may also be needed first."),
    ("Do I need a registered builder for a granny flat in Armadale?",
     "If the work is worth $20,000 or more, you need a registered builder or owner-builder approval."),
    ("What does Armadale want on a granny flat site plan?",
     "The granny flat, other buildings, distances to boundaries, septic tanks if any, a 2 m x 2 m tree planting area, and landscaping and paving in the front setback."),
]


def page(S):
    return {"path": "city-of-armadale-granny-flat-rules.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "City of Armadale granny flat rules: the 70 m² limit, builder rules, what to send and timeframes.",
            "title": "City of Armadale Granny Flat Rules (2026)",
            "desc": "City of Armadale granny flat (ancillary dwelling) rules: the 70 m² limit, one per lot, the $20,000 builder rule and home indemnity insurance, the full checklist and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Armadale granny flat rules", "crumb": "Armadale granny flat rules",
            "answer": "<p>In the City of Armadale you can build <strong>one granny flat</strong> up to <strong>70 m²</strong> per property. A <strong>building permit</strong> is always needed, and work worth $20,000 or more needs a registered builder or owner-builder approval. The City decides in 10 business days (BA1) or 25 (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-building-permit", "Granny flat building permit"), ("/granny-flat-approval-process", "Granny flat approval process"), ("/choosing-a-granny-flat-builder", "Choosing a granny flat builder")],
            "sources": [("Building information sheet: ancillary dwelling (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/40qQCMMHfyFz2fsz5rVvUq/618c3f6d9bd14b993fc41cc80e977718/Building_Services_Information_Sheet_-_Ancillary_Dwelling_-_June_2026.PDF")]}
