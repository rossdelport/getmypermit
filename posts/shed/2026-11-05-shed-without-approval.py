BODY = """
<h2>Why it matters</h2>
<p>Building and Energy says owners must make sure a building permit is obtained before work starts, and <strong>penalties apply</strong> if it isn't. Most sheds need one: anything bigger than <strong>10 m²</strong> or taller than <strong>2.4 m</strong>. A shed that also breaks the planning rules (too big, too tall or too close to a boundary) can need planning approval as well.</p>

<h2>Your options if it's already built</h2>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>What it involves</th></tr></thead><tbody>
<tr><td><strong>Get it approved after the fact</strong></td><td>Apply for a <strong>building approval certificate</strong> (form BA13) with a <strong>certificate of building compliance</strong> (BA18) from a registered building surveyor, who inspects the shed</td></tr>
<tr><td><strong>Take it down</strong></td><td>A shed of 40 m² or less, with no asbestos and not on a heritage property, can be removed without a demolition permit</td></tr>
<tr><td><strong>Make it smaller</strong></td><td>A freestanding shed cut down to 10 m² or less and 2.4 m or lower no longer needs a building permit</td></tr>
</tbody></table></div>

<h2>What retrospective approval costs</h2>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA13 for unauthorised work</td><td>0.38% of the value of the work, at least $121</td></tr>
<tr><td>Building Services Levy for unauthorised work</td><td>0.274% of the value of the work</td></tr>
<tr><td>Building surveyor</td><td>Their own fee for inspecting and certifying</td></tr>
</tbody></table></div>
<p>For a $20,000 shed that's $121 plus $54.80 levy, plus the surveyor. The value used is the current value of the work, as decided by council. If the shed also needs planning approval, that's a separate application.</p>

<h2>What if it doesn't meet the rules?</h2>
<p>The surveyor certifies that the shed meets the building standards. If it doesn't, it may need changes before it can be approved. Council can also refuse planning approval for a shed that's too big or too close to a boundary.</p>
<p>We can check your shed and tell you which option fits: see <a href="/retrospective-shed-approval">retrospective shed approval</a>.</p>
"""

FAQS = [
    ("What happens if I build a shed without a permit in WA?",
     "Owners must make sure a permit is obtained before building, and penalties apply if it isn't. You can fix it by getting a building approval certificate (BA13) with a building surveyor's certificate of building compliance (BA18), or by removing the shed."),
    ("Can I get a shed approved after it's built?",
     "Yes, with a building approval certificate (BA13). A registered building surveyor inspects the shed and issues a certificate of building compliance (BA18)."),
    ("How much does retrospective shed approval cost?",
     "The BA13 fee is 0.38% of the value (at least $121) plus a 0.274% levy, plus the building surveyor's fee."),
    ("Do I need a permit to remove an unapproved shed?",
     "Not if it's 40 m² or less, has no asbestos and the property isn't heritage-listed."),
]


def page(S):
    return {"path": "shed-without-approval.html", "published": "2026-11-05", "type": "Question answer", "icon": "shed",
            "card": "Penalties, how to get it approved after the fact, and what that costs.",
            "title": "What Happens If You Build a Shed Without Approval? (WA)",
            "desc": "Built a shed without a permit in WA? The penalties, your three options, how retrospective approval with a BA13 and BA18 works, and what it costs.",
            "eyebrow": "Question answer", "h1": "What happens if you build a shed without approval?", "crumb": "Shed without approval",
            "answer": "<p>Owners must get a building permit before building, and <strong>penalties apply</strong> if they don't. You can fix it with a <strong>building approval certificate</strong> (BA13), backed by a building surveyor's inspection (BA18). It costs <strong>0.38%</strong> of the value (at least $121) plus a 0.274% levy and the surveyor's fee. Or take it down.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-shed-approval", "Retrospective shed approval"), ("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/how-to-get-a-shed-permit", "How to get a shed permit")],
            "sources": [("Building or renovating your home (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit")]}
