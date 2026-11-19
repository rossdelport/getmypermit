BODY = """
<h2>What doesn't need a permit</h2>
<div class="table-wrap"><table>
<thead><tr><th>Work</th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Patio, shed or gazebo</td><td>Freestanding, up to 10 m² and 2.4 m high</td></tr>
<tr><td>Pergola or shade sail with a house</td><td>Up to 20 m² and 2.4 m high</td></tr>
<tr><td>Colorbond dividing fence</td><td>Up to 2 m high and not forward of the house</td></tr>
<tr><td>Rainwater tank</td><td>Up to 5,000 litres</td></tr>
<tr><td>Solar panels or hot water system on the house</td><td>Usually exempt</td></tr>
<tr><td>Demolishing a patio, shed or pool</td><td>Up to 40 m²</td></tr>
</tbody></table></div>
<p>Pools and spas 300 mm or deeper always need a permit. Being exempt from a building permit doesn't mean you can skip planning approval or the building rules.</p>

<h2>How to apply</h2>
<ul>
<li><strong>BA1 (certified):</strong> for any building, with a Certificate of Design Compliance (BA3) from a registered building surveyor. The City has <strong>10 business days</strong> to decide. The City also offers its own certification service.</li>
<li><strong>BA2 (uncertified):</strong> only for houses (Class 1a) and sheds, patios and carports (Class 10). The City checks the plans and has <strong>25 business days</strong>.</li>
</ul>
<p>Lodge online through the City's portal with one copy of each document, plus a verge permit application if you'll use the verge. Incomplete applications aren't accepted. If the City asks for more information, you have <strong>21 days</strong> to provide it.</p>

<h2>Before you lodge</h2>
<p>Any other approvals must already be in place: planning approval if needed, health approval for a septic system, and owner-builder approval if you're managing work over <strong>$20,000</strong> on a house (or over <strong>$50,000</strong> for a shed, patio or carport) without a registered builder.</p>
<p>Planning approval is only needed for a house or minor structure if it breaks the R-Codes' standard rules, a local development plan or a local planning policy. The City decides within 60 days, or 90 with neighbour comment.</p>

<h2>After you build</h2>
<p>Lodge a <strong>BA7 notice of completion</strong> within <strong>7 days</strong> of finishing, with proof of any inspections the permit asked for. There are penalties if you don't.</p>
<p>See <a href="/which-ba-form">which BA form you need</a>, use the <a href="/building-permit-fee-calculator">building permit fee calculator</a>, or read about the <a href="/ba7-notice-of-completion">BA7 notice of completion</a>.</p>
"""

FAQS = [
    ("How long does the City of Gosnells take to approve a building permit?",
     "10 business days for a certified BA1, or 25 business days for an uncertified BA2, once the application is complete."),
    ("What can I build in Gosnells without a permit?",
     "A freestanding patio, shed or gazebo up to 10 m² and 2.4 m high, an open pergola with a house up to 20 m², a dividing fence up to 2 m, and a rainwater tank up to 5,000 litres, among others."),
    ("Can I use a BA2 in Gosnells?",
     "Yes, for a house (Class 1a) or a shed, patio or carport (Class 10). Other buildings need a certified BA1."),
    ("When do I lodge the BA7 in Gosnells?",
     "Within 7 days of finishing the work, with proof of any required inspections."),
]


def page(S):
    return {"path": "city-of-gosnells-building-permits.html", "published": "2026-11-20", "type": "Council guide", "icon": "pin",
            "card": "City of Gosnells building permits: exemptions, BA1 vs BA2, timeframes and what to have ready.",
            "title": "City of Gosnells Building Permits (2026)",
            "desc": "City of Gosnells building permits: what's exempt, BA1 (10 days) vs BA2 (25 days), lodging online, owner-builder limits, planning approval and the BA7.",
            "eyebrow": "Council guide", "h1": "City of Gosnells building permits", "crumb": "City of Gosnells building permits",
            "answer": "<p>The City of Gosnells decides a certified <strong>BA1</strong> in <strong>10 business days</strong> and an uncertified <strong>BA2</strong> in <strong>25 business days</strong>. Small freestanding structures up to <strong>10 m²</strong> and <strong>2.4 m</strong> are exempt. Lodge online, and have planning, health and owner-builder approvals sorted first if you need them.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/building-permit-fee-calculator", "Building permit fee calculator"), ("/ba7-notice-of-completion", "BA7 notice of completion")],
            "sources": [("Building Permits, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits"),
                        ("Do I need a permit?, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Development approval, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Development-approval")]}
