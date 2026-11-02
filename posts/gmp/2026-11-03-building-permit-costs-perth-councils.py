BODY = """
<h2>The fee is the same at every council</h2>
<p>Building permit fees are set by the state's Building Regulations 2012, not by each council. So a BA2 for a $30,000 patio costs the same in Joondalup as it does in Rockingham. What changes between councils are the <strong>extras</strong>, like verge bonds and planning fees.</p>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA2 (uncertified) application</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>BA1 (certified) application, houses and Class 10</td><td>0.19% of the value, at least $121</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000; 0.137% of the value above that</td></tr>
<tr><td>Construction Training Fund levy</td><td>0.2% of the value, only for work over $100,000</td></tr>
</tbody></table></div>
<p>The value is the full cost of the work including GST: materials, labour, services, fees, overheads and profit.</p>

<h2>What you'll pay for a BA2</h2>
<div class="table-wrap"><table>
<thead><tr><th>Value of work</th><th>BA2 fee</th><th>Levy</th><th>CTF</th><th>Total to council</th></tr></thead><tbody>
<tr><td>$20,000 (shed, patio, carport)</td><td>$121</td><td>$61.65</td><td>None</td><td>$182.65</td></tr>
<tr><td>$45,000</td><td>$144</td><td>$61.65</td><td>None</td><td>$205.65</td></tr>
<tr><td>$60,000 (large garage)</td><td>$192</td><td>$82.20</td><td>None</td><td>$274.20</td></tr>
<tr><td>$150,000 (granny flat)</td><td>$480</td><td>$205.50</td><td>$300</td><td>$985.50</td></tr>
</tbody></table></div>
<p>A BA1 costs less in council fees (for example $285 instead of $480 at $150,000), but you also pay a private building surveyor.</p>

<h2>Extras that vary by council</h2>
<div class="table-wrap"><table>
<thead><tr><th>Council</th><th>Extra charge</th></tr></thead><tbody>
<tr><td>City of Wanneroo</td><td>Street and Verge Bond with every building permit: $140 admin fee, plus a $2,200 refundable bond if the work is worth $20,000 or more</td></tr>
<tr><td>City of Melville</td><td>Verge bond of $1,900 plus a $100 inspection fee for work over $20,000</td></tr>
<tr><td>City of Stirling</td><td>$110 to amend a permit or the builder's details (BA19)</td></tr>
</tbody></table></div>
<p>Other councils have their own verge, crossover and inspection charges, listed in their yearly fees and charges schedule.</p>

<h2>If you need planning approval too</h2>
<p>Planning (development) approval is a separate fee. At councils we've checked, such as Subiaco and Melville, it's <strong>$147</strong> for work up to $50,000. It's only needed when your project doesn't meet the standard planning rules, or is in a heritage area.</p>
"""

FAQS = [
    ("How much is a building permit in WA?",
     "For a BA2, 0.32% of the value of the work, at least $121, plus the Building Services Levy ($61.65 for work up to $45,000). A $20,000 shed or patio costs $182.65 in permit fee and levy."),
    ("Are building permit fees different at each Perth council?",
     "No. The permit fees and the levy are set by the state, so they're the same everywhere. Extras like verge bonds, planning fees and inspection fees vary by council."),
    ("What is the Building Services Levy?",
     "A state levy collected with your building permit: $61.65 for work up to $45,000, or 0.137% of the value above that."),
    ("When do I pay the Construction Training Fund levy?",
     "Only for work over $100,000 that starts on or after 1 July 2026. It's 0.2% of the value."),
]


def page(S):
    return {"path": "building-permit-costs-perth-councils.html", "published": "2026-11-03", "type": "Cost guide", "icon": "price",
            "card": "The state-set permit fees, worked examples, and the extra charges that differ by council.",
            "title": "Building Permit Costs at Perth Councils (2026)",
            "desc": "What a building permit costs at Perth councils in 2026: BA1 and BA2 fees, the Building Services Levy, CTF levy, worked examples, and verge bonds at Wanneroo, Melville and more.",
            "eyebrow": "Cost guide", "h1": "Building permit costs at Perth councils (2026)", "crumb": "Building permit costs",
            "answer": "<p>The building permit fee is set by the state, so it's <strong>the same at every Perth council</strong>: 0.32% of the value for a BA2 (at least $121), plus a $61.65 levy for work up to $45,000. A $20,000 shed or patio costs <strong>$182.65</strong>. Councils differ only on extras, like verge bonds.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/ba1-vs-ba2", "BA1 vs BA2"), ("/how-to-fill-in-a-ba2-form", "How to fill in a BA2 form"), ("/do-i-need-approval", "Do I need council approval?")],
            "sources": [("Building approvals: fees and Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy"),
                        ("Patios information sheet, verge bond (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Building a shed or outbuilding (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Building documents (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/building-advice/building-documents")]}
