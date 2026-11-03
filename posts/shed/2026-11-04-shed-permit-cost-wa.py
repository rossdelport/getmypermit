BODY = """
<h2>Council fees for a shed</h2>
<p>The building permit fee is set by the state, so it's the same at every WA council. For a BA2 (the usual homeowner application) it's <strong>0.32%</strong> of the value of the work, at least $121. You also pay the Building Services Levy: $61.65 for work up to $45,000.</p>
<div class="table-wrap"><table>
<thead><tr><th>Shed value (incl. GST, labour and slab)</th><th>BA2 fee</th><th>Levy</th><th>Total</th></tr></thead><tbody>
<tr><td>$10,000</td><td>$121</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$20,000</td><td>$121</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$40,000</td><td>$128</td><td>$61.65</td><td>$189.65</td></tr>
<tr><td>$60,000</td><td>$192</td><td>$82.20</td><td>$274.20</td></tr>
</tbody></table></div>
<p>The value must include everything: the kit, slab, labour, services, fees and the builder's margin. Councils can reject an application if the value looks too low.</p>

<h2>Extra council charges</h2>
<ul>
<li><strong>Planning approval</strong>, only if your shed breaks the outbuilding rules (too big, too tall or too close to a boundary): $147 for work up to $50,000 at councils like Melville.</li>
<li><strong>Verge bonds</strong>, at some councils. Wanneroo charges a $140 admin fee with every building permit, plus a $2,200 refundable bond if the work is worth $20,000 or more. Melville charges a $1,900 bond plus a $100 inspection fee for work over $20,000.</li>
</ul>

<h2>Other costs to budget for</h2>
<ul>
<li><strong>Plans and engineering.</strong> Most shed kit suppliers include these with the kit. Check before you buy.</li>
<li><strong>Registered builder.</strong> Since 1 July 2026, a shed worth less than $50,000 doesn't need a registered builder, and you can build it yourself without owner-builder approval.</li>
<li><strong>Home indemnity insurance</strong> is required for permit work worth more than $20,000.</li>
</ul>

<h2>Small sheds cost nothing</h2>
<p>A freestanding shed of <strong>10 m² or less</strong> and no higher than <strong>2.4 m</strong> doesn't need a building permit at all.</p>
"""

FAQS = [
    ("How much is a shed permit in WA?",
     "For a BA2, 0.32% of the value of the work, at least $121, plus the $61.65 Building Services Levy for work up to $45,000. A $20,000 shed costs $182.65 in permit fee and levy."),
    ("Is the shed permit fee different at each council?",
     "No, the permit fee and levy are set by the state. Extras like verge bonds and planning fees differ between councils."),
    ("Do I need to pay for planning approval for a shed?",
     "Only if the shed doesn't meet your council's outbuilding rules. At councils like Melville, the fee is $147 for work up to $50,000."),
    ("Does a small shed need a permit?",
     "Not if it's freestanding, 10 m² or less and no higher than 2.4 m."),
]


def page(S):
    return {"path": "shed-permit-cost-wa.html", "published": "2026-11-04", "type": "Cost guide", "icon": "price",
            "card": "Council fees for a shed permit at different values, plus verge bonds and planning fees.",
            "title": "Shed Permit Cost in WA (2026): Council Fees Explained",
            "desc": "What a shed building permit costs in WA in 2026: the 0.32% BA2 fee, the Building Services Levy, worked examples, verge bonds, planning fees and when a shed is free.",
            "eyebrow": "Cost guide", "h1": "Shed permit cost in WA (2026)", "crumb": "Shed permit cost",
            "answer": "<p>A shed permit costs <strong>0.32%</strong> of the value of the work (at least $121) plus a <strong>$61.65</strong> levy for work up to $45,000. For most backyard sheds that's <strong>$182.65</strong> in council fees. Some councils add a verge bond, and planning approval is $147 if you need it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/shed-vs-garage", "Shed vs garage approvals")],
            "sources": [("Building approvals: fees and Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Building or renovating your home: Class 10a threshold (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Building a shed or outbuilding (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Street and Verge Bond fees, patios information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit")]}
