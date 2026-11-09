BODY = """
<h2>What you pay for</h2>
<p>In WA you can't get a building permit after the work is built. Instead you apply for a <strong>building approval certificate</strong> (form BA13 for houses, sheds, patios, carports and other Class 1 and 10 work). The cost comes in four parts:</p>
<div class="table-wrap"><table>
<thead><tr><th>Cost</th><th>Who sets it</th><th>Amount</th></tr></thead><tbody>
<tr><td>Council application fee (BA13)</td><td>State regulations</td><td><strong>0.38%</strong> of the value of the work, minimum <strong>$121</strong></td></tr>
<tr><td>Building Services Levy</td><td>State</td><td><strong>0.274%</strong> of the value of the work</td></tr>
<tr><td>Certificate of building compliance (BA18)</td><td>Private building surveyor</td><td>Their own fee</td></tr>
<tr><td>As-built drawings and engineer's check</td><td>Drafter and engineer</td><td>Their own fees</td></tr>
</tbody></table></div>
<p>The state also sets the value used for these fees: for unauthorised work, it's the <strong>current value</strong> of the work as decided by the council, not what you paid.</p>

<h2>How it compares with getting a permit first</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Permit before building (BA2)</th><th>Approval after building (BA13)</th></tr></thead><tbody>
<tr><td>Council fee</td><td>0.32%, minimum $121</td><td>0.38%, minimum $121</td></tr>
<tr><td>Building Services Levy</td><td>0.137% (or $61.65 for work of $45,000 or less)</td><td>0.274%</td></tr>
<tr><td>Inspection of finished work</td><td>Not needed</td><td>Needed (BA18)</td></tr>
</tbody></table></div>

<h2>Council fee examples</h2>
<div class="table-wrap"><table>
<thead><tr><th>Value of the work</th><th>BA13 fee (0.38%, min $121)</th></tr></thead><tbody>
<tr><td>$10,000 patio</td><td>$121</td></tr>
<tr><td>$30,000 shed</td><td>$121</td></tr>
<tr><td>$40,000 carport and patio</td><td>$152</td></tr>
<tr><td>$80,000 granny flat</td><td>$304</td></tr>
</tbody></table></div>
<p>Add the levy on top. Some councils also charge extra items such as a verge bond or inspection fees, so check your council's fee schedule.</p>

<h2>The cost that can hurt most</h2>
<p>The fees are small next to the cost of <strong>changes</strong>. If the surveyor finds the work doesn't meet the building rules, you may need to fix it before the certificate is issued. A council can also refuse the application and ask for the work to be removed. Fines for building without a permit can reach <strong>$50,000</strong> for a first offence.</p>
<p>Read how the process works on <a href="/retrospective-approval">retrospective approval</a>, why old work never becomes legal in <a href="/seven-year-rule-wa">is there a 7-year rule?</a>, or estimate normal permit fees with the <a href="/building-permit-fee-calculator">building permit fee calculator</a>.</p>
"""

FAQS = [
    ("How much does retrospective approval cost in WA?",
     "The council fee for a building approval certificate (BA13) is 0.38% of the value of the work, with a minimum of $121. The Building Services Levy is 0.274%. On top of that you pay a private building surveyor for the inspection and certificate (BA18), and often a drafter and engineer."),
    ("Is retrospective approval more expensive than a normal permit?",
     "Yes. The council fee is 0.38% instead of 0.32% for an uncertified permit, the levy rate is double (0.274% instead of 0.137%), and you also need a surveyor to inspect the finished work."),
    ("What value is used to work out the fee?",
     "For unauthorised work, the state says it's the current value of the work as decided by the council."),
    ("Can a council refuse retrospective approval?",
     "Yes. If the work can't be shown to meet the building standards, the council can refuse and ask for changes or removal."),
]


def page(S):
    return {"path": "retrospective-approval-cost.html", "published": "2026-11-10", "type": "Cost guide", "icon": "retro",
            "card": "The BA13 fee, the doubled levy, surveyor costs and worked examples.",
            "title": "Retrospective Approval Cost in WA (2026)",
            "desc": "What retrospective building approval costs in WA: the 0.38% BA13 fee (min $121), the 0.274% levy, surveyor and drawing costs, with worked examples.",
            "eyebrow": "Cost guide", "h1": "How much does retrospective approval cost in WA?", "crumb": "Retrospective approval cost",
            "answer": "<p>The council fee for a building approval certificate (BA13) is <strong>0.38%</strong> of the value of the work, minimum <strong>$121</strong>, plus a Building Services Levy of <strong>0.274%</strong>. You also pay a private building surveyor to inspect the work, and often a drafter and engineer. Both state rates are higher than for a permit taken out before building.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-approval", "Retrospective approval"), ("/seven-year-rule-wa", "Is there a 7-year rule?"), ("/building-permit-fee-calculator", "Building permit fee calculator")],
            "sources": [("Building approvals: fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Unauthorised work (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work"),
                        ("Unapproved buildings and structures (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/unapproved-buildings-and-structures")]}
