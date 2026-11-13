BODY = """
<h2>What needs a building permit in Joondalup</h2>
<div class="table-wrap"><table>
<thead><tr><th>Project</th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Shed</td><td>Freestanding, 10 m² or less, 2.4 m or less, installed to the maker's instructions</td></tr>
<tr><td>Patio or louvre roof</td><td>Standalone, 10 m² or less, 2.4 m or less</td></tr>
<tr><td>Pergola</td><td>20 m² or less and 2.4 m or less</td></tr>
<tr><td>Shade sail</td><td>Standalone, 20 m² or less, 2.4 m or less (attached sails always need one)</td></tr>
<tr><td>Carport, garage, granny flat</td><td>Always needs a building permit</td></tr>
</tbody></table></div>
<p>If your project also needs planning approval, Joondalup says the building permit can only be issued <strong>after</strong> planning approval.</p>

<h2>How to apply</h2>
<ol>
<li><strong>Check planning first.</strong> Most sheds, patios and pergolas on house lots don't need planning approval if they meet the R-Codes and city policy.</li>
<li><strong>Pick certified or uncertified.</strong> A certified application (BA1) comes with a Certificate of Design Compliance from a private building surveyor. For an uncertified one (BA2), the City checks the plans.</li>
<li><strong>Use the right checklist.</strong> Joondalup has checklists for each project type, listing the plans and documents it needs.</li>
<li><strong>Lodge online</strong> through the City's portal (preferred) or by mail. You'll get an invoice for the fee.</li>
<li><strong>Answer any questions.</strong> If something is missing, you usually have <strong>21 days</strong> to supply it.</li>
</ol>
<p>Once the application is complete, the City decides a certified application within <strong>10 working days</strong> and an uncertified one within <strong>25 working days</strong>. When the work is finished, the builder must lodge a <strong>BA7</strong> notice of completion within 7 days.</p>

<h2>Fees</h2>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Amount</th></tr></thead><tbody>
<tr><td>Building permit, certified, house or Class 10</td><td>0.19% of the value, at least $121</td></tr>
<tr><td>Building permit, uncertified</td><td>0.32% of the value, at least $121 (state rate)</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000</td></tr>
<tr><td>Planning approval, work up to $50,000</td><td>Up to $147</td></tr>
<tr><td>Planning approval, $50,000 to $500,000</td><td>Up to 0.382% of the cost</td></tr>
<tr><td>Planning approval for work already done</td><td>An extra penalty of twice the normal fee</td></tr>
<tr><td>Deemed-to-comply check</td><td>$295</td></tr>
<tr><td>Written planning advice</td><td>$73</td></tr>
</tbody></table></div>
<p>Compare with <a href="/city-of-wanneroo-building-permits">City of Wanneroo building permits</a>, see <a href="/which-ba-form">which BA form you need</a>, or use the <a href="/approval-timeline-calculator">approval timeline calculator</a>.</p>
"""

FAQS = [
    ("How long does a building permit take in Joondalup?",
     "Once the application is complete, 10 working days for a certified (BA1) application and 25 working days for an uncertified (BA2) one."),
    ("Do I need a permit for a small shed in Joondalup?",
     "Not if it's freestanding, 10 m² or less, 2.4 m or less, and installed to the manufacturer's instructions."),
    ("How much does planning approval cost in Joondalup?",
     "Up to $147 for work up to $50,000, and up to 0.382% of the cost from $50,000 to $500,000. Work already done attracts an extra penalty of twice the fee."),
    ("Can I lodge a building permit online in Joondalup?",
     "Yes. The City prefers online lodgement through its portal. You can also lodge by mail."),
]


def page(S):
    return {"path": "city-of-joondalup-building-permits.html", "published": "2026-11-14", "type": "Council guide", "icon": "pin",
            "card": "What needs a permit in the City of Joondalup, how to apply, timeframes and fees.",
            "title": "City of Joondalup Building Permits Guide (2026)",
            "desc": "City of Joondalup building permits: which sheds, patios, pergolas and shade sails need one, how to apply online, 10 or 25 working days, and fees.",
            "eyebrow": "Council guide", "h1": "City of Joondalup building permits",
            "crumb": "Joondalup building permits",
            "answer": "<p>In Joondalup, small freestanding sheds and patios up to <strong>10 m²</strong> and <strong>2.4 m</strong>, and pergolas up to <strong>20 m²</strong>, usually don't need a building permit. Most other projects do. Lodge online; the City decides in <strong>10 working days</strong> (certified) or <strong>25</strong> (uncertified).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/city-of-wanneroo-building-permits", "City of Wanneroo building permits"), ("/which-ba-form", "Which BA form do I need?"), ("/approval-timeline-calculator", "Approval timeline calculator")],
            "sources": [("Requirements for building applications, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/property-and-land-development/requirements-for-building-applications"),
                        ("Patio, pergola or shade sails, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails"),
                        ("Outbuilding (shed), City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)"),
                        ("Planning services fees and charges 2025/26 (City of Joondalup)", "https://www.joondalup.wa.gov.au/awcontent/Web/Documents/Budget,%20Fees%20and%20Financial%20Reports/Planning-Services-fees-and-charges-2025_26.pdf")]}
