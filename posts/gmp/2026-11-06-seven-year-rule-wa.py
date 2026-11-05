BODY = """
<h2>The short version</h2>
<p>There is no rule in Western Australia that makes unapproved building work legal after 7 years, or after any number of years. It's an offence under the <em>Building Act 2011</em> to do building work without a permit unless the work is exempt. That covers small things too, like patios, sheds, fences, retaining walls, pools and spas.</p>
<p>If council has no approval on file for a building, it treats that building as unauthorised, however old it is.</p>

<h2>Where does the "7 years" idea come from?</h2>
<p>It usually gets mixed up with a real WA rule about <strong>owner-builders</strong>. An owner-builder is responsible for their building work for at least <strong>seven years</strong>. If they sell the home within seven years of the building permit, they need home indemnity insurance that covers the next owners for the rest of that time.</p>
<p>That rule is about who fixes faults. It has nothing to do with whether unapproved work becomes legal. Rules in other states are different too, so advice from interstate often doesn't apply here.</p>

<h2>What you can do about old unapproved work</h2>
<p>A council can't issue a building permit after the work is done. Instead, you apply for one of these:</p>
<div class="table-wrap"><table>
<thead><tr><th>Building</th><th>What you apply for</th></tr></thead><tbody>
<tr><td>Houses, extensions, patios, sheds, carports, pools (Class 1 and 10)</td><td><strong>Building approval certificate</strong> (form BA13)</td></tr>
<tr><td>Units, shops and other buildings (Class 2 to 9)</td><td><strong>Occupancy permit</strong> (form BA9)</td></tr>
</tbody></table></div>
<p>Both need a <strong>certificate of building compliance</strong> (form BA18) from a registered building surveyor. The surveyor inspects the work and confirms it substantially meets the building standards, using as-built plans and documents.</p>

<h2>What it costs</h2>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA13 for unauthorised work</td><td>0.38% of the value of the work, at least $121</td></tr>
<tr><td>Building Services Levy for unauthorised work</td><td>0.274% of the value of the work</td></tr>
<tr><td>Building surveyor (BA18)</td><td>Their own fee</td></tr>
</tbody></table></div>
<p>If the work also broke the planning rules (for example it's too close to a boundary), a separate planning application may be needed as well. Councils vary on this.</p>

<h2>What if it doesn't comply?</h2>
<p>Applying doesn't guarantee approval. If the work doesn't meet the standards, council may ask for changes first. If the changes aren't made, or the work is badly non-compliant, council can refuse and take action to have it removed. Fines under the Building Act go up to $50,000 for a first offence.</p>

<h2>Buying a home with old extensions?</h2>
<p>Ask the council for a <strong>plan search</strong> before you buy. It shows which buildings on the lot are approved. Anything without a record is treated as unauthorised, and becomes your problem once you own it.</p>
<p>See <a href="/retrospective-approval">retrospective approval</a> for how we handle this, or <a href="/what-doesnt-need-a-building-permit">what doesn't need a building permit</a> to check if your work was exempt in the first place.</p>
"""

FAQS = [
    ("Is there a 7-year rule for unapproved buildings in WA?",
     "No. WA has no rule that makes unapproved work legal after 7 years or any other time. It stays unauthorised until it's approved with a building approval certificate (BA13) or occupancy permit (BA9)."),
    ("Do I need a building permit after 7 years?",
     "You can't get a building permit after the work is done. Instead you apply for a building approval certificate (BA13) with a building surveyor's certificate of building compliance (BA18)."),
    ("What is the 7-year rule for owner-builders in WA?",
     "Owner-builders are responsible for their work for at least seven years. If they sell within seven years of the permit, they need home indemnity insurance that covers the buyers for the rest of that period."),
    ("Can council make me remove an old unapproved structure?",
     "Yes. If the work is badly non-compliant or required changes aren't made, council can refuse approval and take action to have it removed."),
    ("How do I check if a building on a property is approved?",
     "Ask the council for a plan search. If council has no approval record for a building, it's treated as unauthorised."),
]


def page(S):
    return {"path": "seven-year-rule-wa.html", "published": "2026-11-06", "type": "Question answer", "icon": "clock",
            "card": "Why old unapproved work never becomes legal on its own, and how to fix it.",
            "title": "Is There a 7-Year Rule for Unapproved Buildings in WA?",
            "desc": "No, WA has no 7-year rule. Unapproved work stays unauthorised until it's approved. Where the myth comes from, the BA13 and BA18 fix, and what it costs.",
            "eyebrow": "Question answer", "h1": "Is there a 7-year rule for unapproved buildings in WA?", "crumb": "The 7-year rule",
            "answer": "<p><strong>No.</strong> In WA, unapproved building work doesn't become legal after 7 years or any other time. It stays unauthorised until you get a <strong>building approval certificate</strong> (BA13), backed by a building surveyor's inspection (BA18). The \"7 years\" idea usually comes from the owner-builder rule, which is about fixing faults, not approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-approval", "Retrospective approval"), ("/what-doesnt-need-a-building-permit", "What doesn't need a building permit"), ("/which-ba-form", "Which BA form do I need?")],
            "sources": [("Unauthorised work (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work"),
                        ("Unapproved buildings and structures (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/unapproved-buildings-and-structures"),
                        ("Owner-builder approval (Building and Energy)", "https://www.wa.gov.au/organisation/service-delivery/owner-builder-approval"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
