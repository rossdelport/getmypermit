BODY = """
<h2>The legal difference is the roof</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Pergola</th><th>Patio</th></tr></thead><tbody>
<tr><td>Definition</td><td>An open structure with no roof, though it can have a covering of <strong>open-weave, permeable</strong> material (Building Regulations 2012)</td><td>An unenclosed structure covered in a <strong>water-impermeable</strong> material (R-Codes)</td></tr>
<tr><td>Typical build</td><td>Open beams or slats, shade cloth, climbing plants</td><td>Metal, polycarbonate or other solid roof</td></tr>
<tr><td>Building permit exemption</td><td>Built with a house: 20 m² or less and 2.4 m or lower</td><td>Freestanding: 10 m² or less and 2.4 m or lower</td></tr>
<tr><td>Attached to the house</td><td>Exempt within the limits above</td><td>Needs a building permit at any size (for example at Wanneroo)</td></tr>
<tr><td>Counts as a "building" in the R-Codes</td><td>No, pergolas are excluded</td><td>Yes</td></tr>
</tbody></table></div>

<h2>Why it matters</h2>
<p>Calling something a pergola doesn't make it one. What counts is whether the top lets water through. Add a solid roof to a pergola and, legally, it's now a patio. That brings the smaller 10 m² exemption limit and, if it's attached, the need for a building permit. See <a href="/roof-on-pergola-approval">putting a roof on a pergola</a>.</p>
<p>Shade sails follow the same idea. The Town of Victoria Park, for example, treats an impermeable (vinyl) shade sail as a verandah and a permeable one as a pergola.</p>

<h2>Planning rules</h2>
<p>The R-Codes' definition of a "building" leaves pergolas out, but includes patios. Patios have to meet setbacks; at Wanneroo, for example, 1 m from the side boundary to the post for a patio up to 14 m long. Check your council's rules for pergolas too, especially near boundaries or in the front yard.</p>

<h2>Louvre roofs</h2>
<p>Opening louvre roofs sit between the two. They're watertight when closed, so ask your council how it classifies yours before you build.</p>
"""

FAQS = [
    ("What is the difference between a pergola and a patio in WA?",
     "The roof. A pergola has no roof, or only an open-weave permeable covering like shade cloth. A patio has a water-impermeable roof, such as metal or polycarbonate."),
    ("Does a pergola need a permit in WA?",
     "A pergola built with a house doesn't need a building permit if it's 20 m² or less and 2.4 m or lower. Bigger or taller ones do."),
    ("Does a patio need a permit in WA?",
     "A freestanding patio doesn't if it's 10 m² or less and 2.4 m or lower. Councils such as Wanneroo require a building permit for every attached patio."),
    ("If I add a roof to my pergola, is it a patio?",
     "Yes. Once the covering is water-impermeable, it meets the definition of a patio and the patio rules apply."),
]


def page(S):
    return {"path": "pergola-vs-patio.html", "published": "2026-11-04", "type": "Comparison", "icon": "pergola",
            "card": "It all comes down to the roof. How the permit rules differ for pergolas and patios.",
            "title": "Pergola vs Patio: the Real Difference (WA Permit Rules)",
            "desc": "Pergola vs patio in WA: the legal definitions, why the roof decides it, the 20 m² and 10 m² permit exemptions, attached patios, shade sails and louvre roofs.",
            "eyebrow": "Comparison", "h1": "Pergola vs patio: the real difference", "crumb": "Pergola vs patio",
            "answer": "<p>It's the <strong>roof</strong>. A pergola is open or has a permeable covering like shade cloth. A patio has a solid, waterproof roof. That changes the permit rules: a pergola with a house is exempt up to <strong>20 m²</strong>, but a freestanding patio only up to <strong>10 m²</strong> (both 2.4 m high or less).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("/roof-on-pergola-approval", "Putting a roof on a pergola"), ("/patio-approval-checker", "Patio approval checker")],
            "sources": [("Do I need a building permit? (Town of Victoria Park)", "https://www.victoriapark.wa.gov.au/Profiles/vicpark/Assets/ClientData/Documents/Develop_and_Build/Building/Building_information_and_FAQs/Do-I-need-a-Building-Permit.pdf"),
                        ("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Tiny houses fact sheet, R-Codes definition of a building (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf")]}
