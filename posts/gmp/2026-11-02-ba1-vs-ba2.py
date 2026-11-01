BODY = """
<h2>The short version</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private registered building surveyor, before you lodge</td><td>Your council, after you lodge</td></tr>
<tr><td>What you lodge with it</td><td>A Certificate of Design Compliance (form BA3) from the surveyor</td><td>Plans, engineering and the council's checklist items</td></tr>
<tr><td>What it can be used for</td><td>Any type of building</td><td>Only houses (Class 1a) and Class 10 structures such as sheds, garages, carports, patios, fences, retaining walls and pools</td></tr>
<tr><td>Council's time limit</td><td>10 business days</td><td>25 business days</td></tr>
<tr><td>Council's fee</td><td>0.19% of the value, at least $121</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>Extra cost</td><td>The private surveyor's fee</td><td>None</td></tr>
</tbody></table></div>

<h2>What "certified" means</h2>
<p>With a BA1, a private building surveyor checks your plans against the building code first and signs a <strong>Certificate of Design Compliance</strong> (BA3). Council then mainly checks the paperwork, which is why it only has 10 business days. With a BA2, council's own surveyors do the technical check, so it gets up to 25 business days and charges a higher fee.</p>

<h2>Council fees compared</h2>
<p>The fee is set by the state's Building Regulations, so it's the same at every WA council. On top of it, the Building Services Levy is $61.65 for work up to $45,000.</p>
<div class="table-wrap"><table>
<thead><tr><th>Value of work</th><th>BA1 fee</th><th>BA2 fee</th></tr></thead><tbody>
<tr><td>$20,000 (shed or patio)</td><td>$121 (minimum)</td><td>$121 (minimum)</td></tr>
<tr><td>$50,000 (garage)</td><td>$121 (minimum)</td><td>$160</td></tr>
<tr><td>$150,000 (granny flat)</td><td>$285</td><td>$480</td></tr>
</tbody></table></div>
<p>For most backyard jobs the council fee is about the same either way. The bigger difference is the surveyor's fee (BA1) against the longer wait (BA2).</p>

<h2>Which one should you use?</h2>
<ul>
<li><strong>BA2</strong> suits most homeowners building a shed, carport, patio, pool or granny flat who don't mind waiting up to five weeks. It's cheaper because there's no surveyor to pay.</li>
<li><strong>BA1</strong> suits builders, anyone in a hurry, and any building that isn't a house or Class 10 structure (where it's the only option).</li>
</ul>
<p>Either way, you'll need drawings and engineering, and council can ask for more information, which pauses the clock.</p>
"""

FAQS = [
    ("What is the difference between a BA1 and a BA2?",
     "A BA1 is a certified application: a private building surveyor checks the plans first and issues a Certificate of Design Compliance (BA3). A BA2 is uncertified: your council does that check. BA1 has a 10 business day limit and a 0.19% fee; BA2 has 25 business days and 0.32%."),
    ("Is a BA1 faster than a BA2?",
     "Council's time limit is shorter (10 business days against 25), but you need to add the time the private surveyor takes to issue the Certificate of Design Compliance."),
    ("Can I use a BA2 for a granny flat?",
     "Yes. A granny flat is a Class 1a dwelling, so a BA2 can be used. Commercial and other building classes need a BA1."),
    ("Are BA1 and BA2 fees the same at every council?",
     "Yes. The fees are set by the Building Regulations 2012: 0.19% for a BA1 and 0.32% for a BA2, both with a $121 minimum, plus the Building Services Levy."),
]


def page(S):
    return {"path": "ba1-vs-ba2.html", "published": "2026-11-02", "type": "Comparison", "icon": "doc",
            "card": "Certified or uncertified? Who checks your plans, how long it takes and what it costs.",
            "title": "BA1 vs BA2: Certified or Uncertified Building Permit (WA)",
            "desc": "BA1 vs BA2 compared: who checks the plans, the 10 vs 25 business day limits, the 0.19% vs 0.32% fees, what each can be used for, and which suits your job.",
            "eyebrow": "Comparison", "h1": "BA1 vs BA2: which permit application?", "crumb": "BA1 vs BA2",
            "answer": "<p>A <strong>BA1</strong> is checked by a private building surveyor first, so council decides within <strong>10 business days</strong> and charges 0.19%. A <strong>BA2</strong> is checked by council, takes up to <strong>25 business days</strong> and charges 0.32% (both at least $121). BA2 only covers houses and Class 10 structures like sheds, carports and patios.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/how-to-fill-in-a-ba2-form", "How to fill in a BA2 form"), ("/do-i-need-approval", "Do I need council approval?")],
            "sources": [("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Form BA2: Application for building permit, uncertified (Building Commissioner)", "https://www.narembeen.wa.gov.au/documents/10324/ba2-application-for-a-building-permit-uncertified"),
                        ("Building documents and timeframes (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/building-advice/building-documents")]}
