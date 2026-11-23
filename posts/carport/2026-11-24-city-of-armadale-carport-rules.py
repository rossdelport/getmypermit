BODY = """
<h2>Do you need a building permit?</h2>
<p>Almost always. The City of Armadale only lets a carport skip the permit if it's <strong>freestanding</strong>, under <strong>10 m²</strong> and no higher than <strong>2.4 m</strong>. Any carport <strong>attached</strong> to the house or another structure needs a permit, whatever its size. Get the permit before any work starts.</p>

<h2>Planning approval and setbacks</h2>
<p>Setbacks come from the R-Codes and the City's local planning policies, so they depend on your lot. If your carport doesn't meet them, you may need <strong>planning approval first</strong>, before the building permit can be issued. Call the City on 9394 5000 if you're not sure.</p>

<h2>Who can build it</h2>
<p>If the work is worth <strong>$50,000 or more</strong>, you need a registered builder or owner-builder approval from the state. Most carports cost less than that.</p>

<h2>What to send</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Details</th></tr></thead><tbody>
<tr><td>Form</td><td>BA1 (certified) or BA2 (uncertified), filled in fully and signed by the builder and the applicant</td></tr>
<tr><td>Certificate of Design Compliance</td><td>BA1 only, from a registered building surveyor</td></tr>
<tr><td>Site plan at 1:200</td><td>Carport spot, other buildings, setbacks, fire separation, septic tanks if any, and landscaping and paving in the front setback</td></tr>
<tr><td>Plans at 1:100</td><td>Floor plan, elevations and a cross-section</td></tr>
<tr><td>Structural engineer's certification</td><td>Needed</td></tr>
<tr><td>Planning approval</td><td>If needed</td></tr>
<tr><td>Fees</td><td>See the City's fees sheet. A training levy receipt is only needed for work over $100,000</td></tr>
</tbody></table></div>

<h2>Timeframes and after the build</h2>
<ul>
<li>BA1: up to <strong>10 business days</strong>. BA2: up to <strong>25 business days</strong>.</li>
<li>The permit lasts <strong>2 years</strong>. You can apply for more time.</li>
<li>The builder must send a <strong>BA7 notice of completion</strong> within 7 days of finishing.</li>
</ul>
<p>You can apply online on the City's website. See <a href="/attached-vs-freestanding-carport">attached vs freestanding carports</a>, <a href="/carport-in-front-setback">carports in the front setback</a> and <a href="/carport-site-plan">carport site plans</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in Armadale?",
     "Yes, unless it's freestanding, under 10 m² and no higher than 2.4 m. All attached carports need a permit."),
    ("Does a carport need planning approval in Armadale?",
     "Only if it doesn't meet the R-Codes or the City's planning policies. If it does need it, get planning approval before the building permit."),
    ("How long is an Armadale building permit valid?",
     "Two years from the date it's granted. You can apply to extend it."),
    ("Can I build my own carport in Armadale?",
     "Yes. You only need a registered builder or owner-builder approval if the work is worth $50,000 or more."),
]


def page(S):
    return {"path": "city-of-armadale-carport-rules.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Armadale carport rules: when you need a permit, planning approval and what to send.",
            "title": "City of Armadale Carport Rules (2026)",
            "desc": "City of Armadale carport rules: when a building permit is needed, planning approval and setbacks, the $50,000 builder rule, what to send, timeframes and the 2-year permit.",
            "eyebrow": "Council guide", "h1": "City of Armadale carport rules", "crumb": "Armadale carport rules",
            "answer": "<p>In the City of Armadale nearly every carport needs a <strong>building permit</strong>. Only freestanding ones under <strong>10 m²</strong> and 2.4 m high are exempt. Setbacks follow the R-Codes and local policies, and you may need planning approval first. The City decides in 10 business days (BA1) or 25 (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/attached-vs-freestanding-carport", "Attached vs freestanding carport"), ("/carport-in-front-setback", "Carport in the front setback"), ("/carport-site-plan", "Carport site plan")],
            "sources": [("Building information sheet: carport (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/3EU0cVeb0fudwwQOKbJCdI/ea1bbd43bb7a65ea28bdc751a4d39505/Building_Services_Information_Sheet_-_Carport_-_June_2026.PDF")]}
