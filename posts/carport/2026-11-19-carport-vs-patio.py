BODY = """
<h2>What's the difference?</h2>
<p>The R-Codes define a <strong>carport</strong> as an open structure for parking one or more vehicles, with no door. A <strong>patio</strong> is an open structure with a solid (waterproof) roof, attached to the house or not. They can look the same, so councils go by what it's for and where it sits.</p>

<h2>Approvals side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Carport</th><th>Patio</th></tr></thead><tbody>
<tr><td>Building permit</td><td>Usually yes</td><td>Usually yes</td></tr>
<tr><td>Permit exemption</td><td>Freestanding, up to 10 m² and 2.4 m high</td><td>Freestanding, up to 10 m² and 2.4 m high</td></tr>
<tr><td>In the front setback</td><td>Can usually come forward by up to half the front setback, if no wider than 60% of the frontage and open to the street</td><td>No special rule, so a patio in the front setback usually needs planning approval</td></tr>
<tr><td>On a side or rear boundary</td><td>Posts can be on the boundary if no more than 10 m long and 2.7 m high, behind the front setback, with roof and gutters 450 mm back</td><td>Same rule as a carport</td></tr>
<tr><td>Adding a door</td><td>A solid door turns it into a garage, with different rules</td><td>Enclosing it can turn it into a room, with different rules</td></tr>
</tbody></table></div>
<p>These come from the R-Codes (Volume 1, April 2026, clauses 5.1.3 and 5.2.1). Local policies can change them, so councils vary.</p>

<h2>Which should you apply for?</h2>
<p>Apply for what you'll actually use it for. If you'll park under it, call it a carport, because the carport rules let it sit closer to the street. If it's for outdoor living behind the house, call it a patio. Mislabelling it can cause trouble later, for example when you sell.</p>
<p>Compare a <a href="/carport-vs-garage">carport and a garage</a>, read about a <a href="/carport-in-front-setback">carport in the front setback</a>, or see the rules for a <a href="/carport-on-boundary">carport on the boundary</a>.</p>
"""

FAQS = [
    ("What's the difference between a carport and a patio in WA?",
     "A carport is an open structure for parking vehicles, with no door. A patio is an open structure with a solid roof, used for outdoor living."),
    ("Do carports and patios both need a building permit?",
     "Usually yes. Only freestanding ones up to 10 m² and 2.4 m high are exempt."),
    ("Can a patio go in the front setback like a carport?",
     "Not under the same rule. Carports have a special front setback rule. A patio in the front setback usually needs planning approval."),
    ("Can I use my patio as a carport?",
     "If you'll park under it, it should be approved as a carport, which has its own front setback and width rules."),
]


def page(S):
    return {"path": "carport-vs-patio.html", "published": "2026-11-19", "type": "Comparison", "icon": "carport",
            "card": "Carport vs patio in WA: definitions, building permits, front setback and boundary rules compared.",
            "title": "Carport vs Patio: Approvals Compared in WA (2026)",
            "desc": "Carport vs patio in WA: how the R-Codes define each, building permit rules, the carport front setback concession, boundary setbacks, and which to apply for.",
            "eyebrow": "Comparison", "h1": "Carport vs patio: approvals compared", "crumb": "Carport vs patio",
            "answer": "<p>Both usually need a <strong>building permit</strong> and follow the same side boundary rules. The big difference is the front yard: a <strong>carport</strong> can usually come forward into the front setback if it's no wider than <strong>60%</strong> of the frontage and open to the street. A <strong>patio</strong> doesn't get that rule.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-vs-garage", "Carport vs garage"), ("/carport-in-front-setback", "Carport in the front setback"), ("/carport-on-boundary", "Carport on the boundary")],
            "sources": [("Residential Design Codes Volume 1 (April 2026)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Do I need a permit?, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit")]}
