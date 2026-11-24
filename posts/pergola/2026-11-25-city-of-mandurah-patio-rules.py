BODY = """
<h2>Patio, pergola or shade sail?</h2>
<p>The City of Mandurah calls a structure with a <strong>water-resistant roof</strong>, open on two or more sides, a patio. An open frame with a permeable roof (or no roof) is a pergola. A shade sail is fabric stretched between anchor points.</p>

<h2>When you need a building permit</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Patio</td><td>Freestanding, 10 m² or less and 2.4 m high or less</td></tr>
<tr><td>Pergola</td><td>Freestanding, 20 m² or less and 2.4 m high or less</td></tr>
<tr><td>Shade sail</td><td>Freestanding, 10 m² or less and 2.4 m high or less</td></tr>
</tbody></table></div>
<p>Anything bigger, or attached to the house, needs a permit.</p>

<h2>Planning approval</h2>
<ul>
<li><strong>Patios:</strong> usually not needed if the patio meets the R-Codes deemed-to-comply rules. The City offers a deemed-to-comply check for a fee.</li>
<li><strong>Pergolas and shade sails:</strong> generally not needed, unless you're on the canals.</li>
</ul>
<p>Setbacks come from the City's planning scheme, the R-Codes, local planning policies and any detailed area plan for your estate. You must also keep the minimum open space and outdoor living area. If anything doesn't meet these rules, you need <strong>development approval first</strong>, before the building permit can be decided.</p>

<h2>What to send</h2>
<ul>
<li>A BA1 (with a Certificate of Design Compliance) or a BA2 form.</li>
<li>A site plan at 1:200 or better, showing setbacks to boundaries and all buildings, pools and retaining walls, plus existing and new ground levels.</li>
<li>A floor plan, section and elevations at 1:100 or better.</li>
<li>Construction details: materials, sizes, spans and spacing.</li>
<li>How it connects to the house and how it's anchored, such as footings.</li>
</ul>
<p>The City prefers online lodgement through "Building Lodgements" on its website. Building Services is on 9550 3777. See the <a href="/patio-approval-checker">patio approval checker</a>, <a href="/shade-sail-approval-wa">shade sail approval</a> and <a href="/patio-plans-for-council">patio plans for council</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in Mandurah?",
     "Yes, unless it's freestanding, 10 m² or less and no more than 2.4 m high."),
    ("Do I need a permit for a pergola in Mandurah?",
     "Not if it's freestanding, 20 m² or less and no more than 2.4 m high."),
    ("Does a patio need planning approval in Mandurah?",
     "Usually not, if it meets the R-Codes deemed-to-comply rules. If it doesn't, you need development approval before the building permit."),
    ("Do canal homes in Mandurah have extra rules?",
     "Yes. Pergolas and shade sails generally don't need planning approval, except on the canals, so check with a planning officer."),
]


def page(S):
    return {"path": "city-of-mandurah-patio-rules.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "City of Mandurah patio rules: permit limits for patios, pergolas and shade sails, planning and what to send.",
            "title": "City of Mandurah Patio and Pergola Rules (2026)",
            "desc": "City of Mandurah patio, pergola and shade sail rules: when a building permit is needed, planning approval and the canals, setbacks and open space, and what to send.",
            "eyebrow": "Council guide", "h1": "City of Mandurah patio and pergola rules", "crumb": "Mandurah patio rules",
            "answer": "<p>In the City of Mandurah, a <strong>patio</strong> needs a building permit unless it's freestanding, <strong>10 m²</strong> or less and 2.4 m or lower. Freestanding <strong>pergolas</strong> up to <strong>20 m²</strong> and 2.4 m are exempt. Planning approval usually isn't needed if you meet the R-Codes, but canal lots can differ.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/shade-sail-approval-wa", "Shade sail approval"), ("/patio-plans-for-council", "Patio plans for council")],
            "sources": [("Do I need approval?, City of Mandurah", "https://www.mandurah.wa.gov.au/my-home-property-and-rates/building-and-improving-your-home/do-i-need-approval"),
                        ("Patios and carports information sheet, City of Mandurah", "https://www.mandurah.wa.gov.au/getContentAsset/6bcb0b1b-fe5e-4f49-92fc-d295c942b2d7/8c05e2a8-714e-41ec-a13c-ec89cb576508/Patios%20and%20Carports%20Information%20Sheet.pdf?language=en")]}
