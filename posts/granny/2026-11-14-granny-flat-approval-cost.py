BODY = """
<h2>The council and state fees</h2>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Rate</th></tr></thead><tbody>
<tr><td>Building permit, BA2 (council checks the plans)</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>Building permit, BA1 (private surveyor checks first)</td><td>0.19% of the value, at least $121, plus the surveyor's fee</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 up to $45,000; 0.137% of the value above that</td></tr>
<tr><td>Construction Training Fund levy</td><td>0.2% for work over $100,000, paid directly to the fund</td></tr>
<tr><td>Planning approval, if needed ($50,000 to $500,000)</td><td>Up to 0.382% of the cost</td></tr>
</tbody></table></div>

<h2>Worked examples</h2>
<div class="table-wrap"><table>
<thead><tr><th>Granny flat value (incl. GST)</th><th>BA2 fee</th><th>Levy</th><th>CTF levy</th><th>Total, no planning approval</th></tr></thead><tbody>
<tr><td>$120,000</td><td>$384.00</td><td>$164.40</td><td>$240.00</td><td>$788.40</td></tr>
<tr><td>$150,000</td><td>$480.00</td><td>$205.50</td><td>$300.00</td><td>$985.50</td></tr>
<tr><td>$200,000</td><td>$640.00</td><td>$274.00</td><td>$400.00</td><td>$1,314.00</td></tr>
</tbody></table></div>
<p>If you also need planning approval, add up to 0.382% of the cost, for example up to <strong>$573</strong> on a $150,000 granny flat (City of Joondalup's fee schedule).</p>

<h2>Do you need planning approval?</h2>
<p>Usually not. Most granny flats up to <strong>70 m²</strong> that meet the R-Codes' deemed-to-comply rules skip planning approval, so you only pay the building permit fees. Planning approval is needed if the granny flat breaks a rule, such as a setback, or the land isn't zoned residential.</p>

<h2>Other costs to budget for</h2>
<ul>
<li><strong>Plans and engineering</strong> for the application</li>
<li><strong>Verge bond</strong>, which some councils charge on bigger jobs (for example $1,900 plus a $100 inspection fee at Melville, for work over $20,000)</li>
<li><strong>Home indemnity insurance</strong>, which a registered builder usually arranges for home building work over $20,000</li>
<li><strong>Retrospective approval</strong> if the granny flat is already built: Joondalup adds a penalty of twice the planning fee</li>
</ul>
<p>Read <a href="/granny-flat-building-permit">does a granny flat need a building permit?</a>, <a href="/granny-flat-cost-perth">granny flat costs in Perth</a> or <a href="/granny-flat-approval-process">the granny flat approval process</a>.</p>
"""

FAQS = [
    ("How much does granny flat approval cost in WA?",
     "For a $150,000 granny flat with no planning approval, about $985 in state fees: $480 BA2 fee, $205.50 Building Services Levy and $300 Construction Training Fund levy."),
    ("Do I need to pay for planning approval for a granny flat?",
     "Usually not. Most granny flats up to 70 m² that meet the R-Codes don't need it. If yours does, the fee is up to 0.382% of the cost for work from $50,000 to $500,000."),
    ("Is a BA1 or BA2 cheaper for a granny flat?",
     "The council fee for a BA1 is lower (0.19% vs 0.32%), but you also pay a private building surveyor."),
    ("What is the Construction Training Fund levy?",
     "A 0.2% levy on building work over $100,000. Since 1 July 2026 it's paid directly to the fund, and councils ask for the receipt."),
]


def page(S):
    return {"path": "granny-flat-approval-cost.html", "published": "2026-11-14", "type": "Cost guide", "icon": "price",
            "card": "The building permit fees, levies and planning fees for a WA granny flat, with worked examples.",
            "title": "Granny Flat Approval Cost in WA (2026 Fees)",
            "desc": "Granny flat approval cost in WA in 2026: BA2 0.32%, Building Services Levy 0.137%, CTF levy 0.2%, and planning approval if needed. Worked examples.",
            "eyebrow": "Cost guide", "h1": "How much does granny flat approval cost?",
            "crumb": "Granny flat approval cost",
            "answer": "<p>For a <strong>$150,000</strong> granny flat that doesn't need planning approval, the state fees come to about <strong>$985</strong>: the 0.32% BA2 permit fee, the 0.137% Building Services Levy and the 0.2% Construction Training Fund levy. Plans, engineering and any planning approval cost extra.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-building-permit", "Granny flat building permit"), ("/granny-flat-cost-perth", "Granny flat cost in Perth"), ("/granny-flat-approval-process", "Granny flat approval process")],
            "sources": [("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Planning services fees and charges 2025/26 (City of Joondalup)", "https://www.joondalup.wa.gov.au/awcontent/Web/Documents/Budget,%20Fees%20and%20Financial%20Reports/Planning-Services-fees-and-charges-2025_26.pdf"),
                        ("Building a shed or outbuilding (fees), City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding")]}
