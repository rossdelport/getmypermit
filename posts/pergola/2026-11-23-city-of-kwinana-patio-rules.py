BODY = """
<h2>When you need a building permit</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>Permit needed if</th></tr></thead><tbody>
<tr><td>Patio (solid roof, like Colorbond or polycarbonate)</td><td>It's attached to another structure, over 10 m², or over 2.4 m high</td></tr>
<tr><td>Pergola or shade sail (open or shade-cloth roof)</td><td>It's over 20 m² or over 2.4 m high</td></tr>
</tbody></table></div>
<p>So almost every attached patio in Kwinana needs a permit. A small freestanding patio can skip it if it's 10 m² or less, 2.4 m high or less, and not in a high-wind region. The City suggests keeping a freestanding patio at least <strong>900 mm</strong> from the house and <strong>500 mm</strong> from the boundary.</p>
<p>Kwinana treats a pergola or shade sail with a solid roof as a patio.</p>

<h2>Planning approval</h2>
<p>A permit-free patio may still need planning approval, for example if it doesn't meet the R-Codes. If it does, you must get planning approval <strong>before</strong> you lodge the building permit. Call Building Services if you're not sure.</p>

<h2>What to send</h2>
<ul>
<li>A BA1 or BA2 form signed by all owners and the builder.</li>
<li>A site plan (at least 1:200) showing the house and other buildings, setbacks from boundaries, patio size, and post and downpipe spots.</li>
<li>Elevations and a cross-section (at least 1:100) certified by a structural engineer, showing roof pitch, footings, how it fixes to the house, roof sheeting and heights.</li>
<li>A floor plan (at least 1:100).</li>
<li>For steel frames: engineer details of member sizes, bracing, wind load and fixings. For timber: footing and post connection details and the timber type.</li>
</ul>
<p>With a BA1 (certified by a private building surveyor) the City has <strong>10 business days</strong> to decide. With a BA2 it has <strong>25 business days</strong>. You can apply online through Kwinana Connect, or call Building Services on 9439 0208.</p>
<p>See <a href="/attached-vs-freestanding-patio">attached vs freestanding</a>, <a href="/patio-plans-for-council">patio plans for council</a> and <a href="/shade-sail-approval-wa">shade sail approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in Kwinana?",
     "Yes, if it's attached to the house or another structure, over 10 m², or over 2.4 m high. Only small freestanding patios are exempt."),
    ("Do I need a permit for a pergola in Kwinana?",
     "Only if it's over 20 m² or over 2.4 m high. A pergola with a solid roof counts as a patio."),
    ("How long does the City of Kwinana take?",
     "10 business days for a certified (BA1) application and 25 business days for an uncertified (BA2) one."),
    ("Does my patio need engineering in Kwinana?",
     "Yes. Elevations and cross-sections must be certified by a practising structural engineer."),
]


def page(S):
    return {"path": "city-of-kwinana-patio-rules.html", "published": "2026-11-23", "type": "Council guide", "icon": "pin",
            "card": "City of Kwinana patio rules: when you need a permit, the 10 m² and 20 m² limits and what to send.",
            "title": "City of Kwinana Patio and Pergola Rules (2026)",
            "desc": "City of Kwinana patio and pergola rules: when a building permit is needed, the 10 m² patio and 20 m² pergola limits, planning approval, what to send and how long it takes.",
            "eyebrow": "Council guide", "h1": "City of Kwinana patio and pergola rules", "crumb": "Kwinana patio rules",
            "answer": "<p>In the City of Kwinana, a <strong>patio</strong> needs a building permit if it's attached to another structure, over <strong>10 m²</strong> or over <strong>2.4 m</strong> high. A <strong>pergola or shade sail</strong> needs one if it's over <strong>20 m²</strong> or 2.4 m high. Plans must be certified by a structural engineer.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/attached-vs-freestanding-patio", "Attached vs freestanding patio"), ("/patio-plans-for-council", "Patio plans for council"), ("/shade-sail-approval-wa", "Shade sail approval")],
            "sources": [("Sheds, patios, pergolas and shade sails building permits, City of Kwinana", "https://www.kwinana.wa.gov.au/property-and-pets/building-and-renovating-(residential)/sheds,-patios,-pergolas-and-shade-sails"),
                        ("Information sheet: patios, City of Kwinana", "https://www.kwinana.wa.gov.au/council/documents,-publications-and-forms/publications-and-forms-(all)/information-sheets-and-guides/2020/information-sheet-patios")]}
