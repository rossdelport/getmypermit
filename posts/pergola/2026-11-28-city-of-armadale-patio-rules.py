BODY = """
<h2>Patio, pergola or shade sail?</h2>
<p>The City of Armadale treats these differently:</p>
<ul>
<li><strong>Patio:</strong> open on at least two sides, with a waterproof roof.</li>
<li><strong>Pergola:</strong> open sided, with a roof that lets water through, such as shade cloth or lattice.</li>
<li><strong>Shade sail:</strong> fabric with an open weave, tensioned between anchor points.</li>
</ul>
<p>Not sure which you have? See <a href="/pergola-vs-patio">pergola vs patio</a>.</p>

<h2>When you need a building permit</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No permit needed if it is…</th></tr></thead><tbody>
<tr><td>Patio</td><td>Less than <strong>10 m²</strong>, freestanding and no higher than 2.4 m</td></tr>
<tr><td>Pergola or shade sail</td><td>Less than <strong>20 m²</strong>, freestanding and no higher than 2.4 m</td></tr>
<tr><td>Anything attached to the house or another structure</td><td>Always needs a permit, whatever the size</td></tr>
</tbody></table></div>
<p>Check yours with the <a href="/patio-approval-checker">patio approval checker</a>. For sails, see <a href="/shade-sail-approval-wa">shade sail approval</a>.</p>

<h2>Setbacks and planning</h2>
<p>Setbacks follow the City's local planning policies and the R-Codes. Planning approval may be needed before a building permit can be issued. For pergolas and sails, the City asks that the cover is placed so water doesn't run off onto the neighbours.</p>

<h2>Who can build it</h2>
<p>A registered builder or owner-builder approval is needed if the work costs <strong>$50,000 or more</strong>.</p>

<h2>How long it takes</h2>
<ul>
<li><strong>Certified (BA1):</strong> up to 10 business days.</li>
<li><strong>Uncertified (BA2):</strong> up to 25 business days.</li>
</ul>
<p>The permit lasts 2 years. The builder lodges a BA7 notice of completion within 7 days of finishing.</p>

<h2>What to send</h2>
<ul>
<li>A BA1 or BA2 form, signed by the builder and the applicant, and the fees.</li>
<li>A site plan at 1:200 showing the patio, existing buildings, setbacks, fire separation, septic tanks (if any), and landscaping and hard surfaces in the street setback.</li>
<li>A floor plan, elevations and cross-section at 1:100.</li>
<li>A structural engineer's certificate, and planning approval if needed.</li>
</ul>
<p>Call the City on 9394 5000.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Armadale?",
     "Yes, unless it's less than 10 m², freestanding and no higher than 2.4 m. A patio attached to the house always needs one."),
    ("Do I need a permit for a pergola in Armadale?",
     "Not if it's less than 20 m², freestanding and no higher than 2.4 m. An attached pergola always needs a permit."),
    ("How long does a patio permit take in Armadale?",
     "Up to 10 business days for a certified application and up to 25 for an uncertified one, unless the City asks for more information."),
    ("How long is an Armadale building permit valid?",
     "Two years from the date it's granted. You can apply for an extension if you need more time."),
]


def page(S):
    return {"path": "city-of-armadale-patio-rules.html", "published": "2026-11-28", "type": "Council guide", "icon": "pin",
            "card": "City of Armadale patio rules: 10 m² patio and 20 m² pergola exemptions, timeframes and what to send.",
            "title": "City of Armadale Patio and Pergola Rules (2026)",
            "desc": "City of Armadale patio, pergola and shade sail rules: when you need a building permit, the 10 m² patio and 20 m² pergola exemptions, attached structures, timeframes and what to send.",
            "eyebrow": "Council guide", "h1": "City of Armadale patio rules", "crumb": "Armadale patio rules",
            "answer": "<p>In the City of Armadale, a patio needs a <strong>building permit</strong> unless it's under <strong>10 m²</strong>, freestanding and no higher than 2.4 m. Pergolas and shade sails get a bigger exemption of under <strong>20 m²</strong>. Anything attached to the house always needs a permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/pergola-vs-patio", "Pergola vs patio"), ("/shade-sail-approval-wa", "Shade sail approval")],
            "sources": [("Building information sheet: patio (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/4E7ZUSssqgrJ1Ls0ghHDbZ/b16529f20dc3850d04175e79a1adbeb8/Building_Services_Information_Sheet_-_Patio_-_June_2026.PDF"),
                        ("Building information sheet: pergola or shade sail (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/141VjCqJ0SthcUK4ZRiASt/a96070e9bca78fc7d834f96c17f17262/Building_Services_Information_Sheet_-_Pergola_Shade_Sail_-_June_2026.PDF")]}
