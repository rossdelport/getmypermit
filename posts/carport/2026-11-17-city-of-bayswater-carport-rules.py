BODY = """
<h2>Building permit</h2>
<p>Like other Perth councils, the City of Bayswater only exempts a freestanding structure that's no bigger than <strong>10 m²</strong> and no taller than <strong>2.4 m</strong>. Almost every carport is bigger, so expect to need a building permit. You can lodge a <strong>BA1</strong> (certified, with a Certificate of Design Compliance from a private building surveyor) or a <strong>BA2</strong> (uncertified). The City has <strong>25 business days</strong> to decide a BA2.</p>

<h2>Carports in the front setback</h2>
<p>Bayswater's Residential Development Policy (adopted September 2026) changes the standard R-Codes rule. A carport can be as close as <strong>1.5 m</strong> to the front boundary if:</p>
<div class="table-wrap"><table>
<thead><tr><th>Requirement</th><th>Limit</th></tr></thead><tbody>
<tr><td>Width</td><td>No more than 60% of the lot frontage</td></tr>
<tr><td>Sides</td><td>Open on all sides</td></tr>
<tr><td>Height</td><td>No more than 3.5 m</td></tr>
</tbody></table></div>
<p>If your carport meets these and the other R-Codes rules, you usually won't need planning approval. If not, you'll need a development application first. The City runs a <strong>fast track</strong> service for simple applications such as carports.</p>

<h2>Character Protection Areas</h2>
<p>Parts of <strong>Maylands North, Mount Lawley and Bayswater</strong> are Character Protection Areas with stricter carport rules:</p>
<ul>
<li>Parking must be at the <strong>rear, off the right of way</strong>, if there is one you can use. If not, from a side street, and only then from the front street.</li>
<li>A carport in the street setback must be <strong>open on all sides</strong> (except where it meets the house) and simple, so it doesn't hide the house.</li>
<li>Lots with a frontage of <strong>12 m or less</strong> can only have a single-width carport.</li>
<li>Roofs should be flat or low-pitch skillion, lining up with the house verandah. Posts no wider than 90 × 90 mm.</li>
<li><strong>No roller doors, tilt doors or solid gates</strong> on a carport in the street setback.</li>
<li>If there's already a garage, no carport is allowed in the front setback.</li>
</ul>
<p>Heritage-listed places and heritage areas have their own rules, so check your lot on the City's online map.</p>
<p>Work out your setback with the <a href="/front-setback-carport-calculator">front setback calculator</a>, read about a <a href="/carport-corner-block">carport on a corner block</a>, or compare <a href="/flat-vs-gable-carport">flat and gable carports</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in the City of Bayswater?",
     "Yes, almost always. Only freestanding structures up to 10 m² and 2.4 m high are exempt from a building permit."),
    ("How close to the front boundary can a carport be in Bayswater?",
     "1.5 m, if it's open on all sides, no wider than 60% of the frontage and no taller than 3.5 m."),
    ("Can I put a roller door on a carport in a Bayswater Character Protection Area?",
     "Not if the carport is in the street setback. Roller doors, tilt doors and solid gates aren't permitted there."),
    ("How long does Bayswater take to approve a carport?",
     "Up to 25 business days for an uncertified BA2 building permit. Planning approval, if needed, comes first."),
]


def page(S):
    return {"path": "city-of-bayswater-carport-rules.html", "published": "2026-11-17", "type": "Council guide", "icon": "pin",
            "card": "Bayswater's 1.5 m carport setback rule, building permits and Character Protection Area limits.",
            "title": "City of Bayswater Carport Rules (2026)",
            "desc": "City of Bayswater carport rules: building permit, the 1.5 m front setback rule (60% width, open sides, 3.5 m high), and Character Protection Area limits.",
            "eyebrow": "Council guide", "h1": "City of Bayswater carport rules", "crumb": "Bayswater carport rules",
            "answer": "<p>In Bayswater, almost every carport needs a <strong>building permit</strong>. Since September 2026, a carport can sit <strong>1.5 m</strong> from the front boundary if it's open on all sides, no wider than <strong>60%</strong> of the frontage and no taller than <strong>3.5 m</strong>. Character Protection Areas have stricter rules, including no roller doors in the street setback.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback calculator"), ("/carport-corner-block", "Carport on a corner block"), ("/flat-vs-gable-carport", "Flat vs gable carport")],
            "sources": [("Residential Development Policy (September 2026), City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/policies/2026/residential-development-policy"),
                        ("Character Protection Areas Policy, City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/policies/2025/character-protection-areas-policy"),
                        ("Sheds, pergolas and outdoor structures, City of Bayswater", "https://www.bayswater.wa.gov.au/home-and-property/renovating-your-home-or-property/sheds,-pergolas-and-outdoor-structures"),
                        ("Fast track development application, City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/forms/2026/fast-track-development-application-self-assessment")]}
