BODY = """
<h2>Why a roof changes everything</h2>
<p>The WA Building Regulations define a pergola as <strong>"an open structure that does not have a roof"</strong>, though it may have a covering of open-weave, permeable material such as shade cloth. Add solid sheeting and, legally, it's no longer a pergola. It becomes a <strong>patio</strong> (or verandah, if it's attached to the house), and different rules apply.</p>

<h2>Building permit: before and after</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Open pergola</th><th>With a solid roof (patio)</th></tr></thead><tbody>
<tr><td>Exempt from a building permit if</td><td>Built with a house, 20 m&sup2; or less, 2.4 m high or less, and not in wind region C or D</td><td>Freestanding, 10 m&sup2; or less, 2.4 m high or less</td></tr>
<tr><td>Attached to the house</td><td>Exempt within the limits above</td><td><strong>Permit needed</strong>, any size</td></tr>
</tbody></table></div>
<p>So a 4 m x 4 m (16 m&sup2;) open pergola off the back of the house is usually exempt. Put a solid roof on it and it needs a building permit, because it's both attached and over 10 m&sup2;.</p>

<h2>Which "roofs" count</h2>
<div class="table-wrap"><table>
<thead><tr><th>Covering</th><th>Treated as</th></tr></thead><tbody>
<tr><td>Shade cloth or other permeable fabric</td><td>Still a pergola</td></tr>
<tr><td>Vinyl or other waterproof shade sail</td><td>A verandah (roofed)</td></tr>
<tr><td>Polycarbonate, metal sheeting, insulated panels</td><td>A roof: now a patio or verandah</td></tr>
<tr><td>Opening louvre roof</td><td>Not clearly covered by the definition. Because it can close watertight, ask your council before treating it as exempt</td></tr>
</tbody></table></div>

<h2>The planning side</h2>
<p>The R-Codes treat an unroofed pergola more leniently than a roofed patio. A patio is "an unenclosed structure covered in a water impermeable material", and it counts towards things like setbacks and, on some lots, open space. A pergola that sat happily near the fence may be too close once it's roofed. The City of Wanneroo, for example, asks patios to be 1 m from the boundary, or allows posts on the boundary only if the patio is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back.</p>

<h2>The structure itself</h2>
<p>A roof adds weight and, more importantly, <strong>wind uplift</strong>. Posts, beams and footings sized for an open pergola often aren't enough for a roof. The building permit application needs engineering for the roofed structure, so expect upgraded footings or tie-downs.</p>

<h2>Already added a roof without a permit?</h2>
<p>It can be approved afterwards with a building approval certificate. A registered building surveyor inspects it, and the council fee is 0.38% of the value, at least $121.</p>
"""

FAQS = [
    ("Can I put a roof on my pergola without council approval?",
     "Usually not. Once it has a solid roof it is legally a patio or verandah, and those need a building permit unless they are freestanding, 10 m&sup2; or less and 2.4 m high or less."),
    ("Does shade cloth count as a roof?",
     "No. A permeable shade cloth keeps it a pergola. A waterproof covering such as vinyl, polycarbonate or metal sheeting makes it a roofed structure."),
    ("Do louvre roofs need council approval?",
     "The definition doesn't clearly cover them. Because louvres can close watertight, check with your council before treating one as an exempt pergola."),
    ("Will my pergola posts take a roof?",
     "Often not. A roof adds weight and wind uplift, so the footings and frame usually need an engineer's check and may need upgrading."),
]


def page(S):
    return {"path": "roof-on-pergola-approval.html", "published": "2026-11-01", "type": "Question answer", "icon": "pergola",
            "card": "A solid roof turns a pergola into a patio. When that needs a permit, which coverings count, and the planning catch.",
            "title": "Do I Need Approval to Put a Roof on My Pergola? (WA)",
            "desc": "In WA a pergola has no roof by definition. Adding a solid roof makes it a patio, which usually needs a building permit. Shade cloth, louvres, setbacks and engineering explained.",
            "eyebrow": "Question answer", "h1": "Do I need approval to put a roof on my pergola?", "crumb": "Roof on a pergola",
            "answer": "<p><strong>Usually yes.</strong> In WA a pergola is an open structure with <strong>no roof</strong>. Add a solid roof (polycarbonate, metal or a waterproof sail) and it becomes a <strong>patio or verandah</strong>, which needs a building permit unless it's freestanding, 10 m&sup2; or less and 2.4 m high or less. Shade cloth doesn't count as a roof.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("/patio-approval-checker", "Patio approval checker"), ("/patio-building-permit", "Patio building permits")],
            "sources": [("Building Regulations 2012: definition of pergola (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_42729.pdf"),
                        ("Do I need a building permit? Pergolas, shade sails and verandahs (Town of Victoria Park)", "https://www.victoriapark.wa.gov.au/Profiles/vicpark/Assets/ClientData/Documents/Develop_and_Build/Building/Building_information_and_FAQs/Do-I-need-a-Building-Permit.pdf"),
                        ("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf")]}
