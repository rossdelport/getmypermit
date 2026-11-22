BODY = """
<h2>The short version</h2>
<p>In WA, building work that needs a permit and is worth over <strong>$20,000</strong> (or <strong>$50,000</strong> for sheds, carports and garages) must be done by a <strong>registered builder</strong> or by you as an approved <strong>owner-builder</strong>. Both are legal. The difference is who carries the risk.</p>

<div class="table-wrap"><table>
<thead><tr><th></th><th>Owner-builder</th><th>Registered builder</th></tr></thead><tbody>
<tr><td>Who manages the job</td><td>You: trades, quality, safety and inspections</td><td>The builder</td></tr>
<tr><td>Approval before the permit</td><td>Owner-builder approval from the state, usually 6 to 8 weeks</td><td>None for you. The builder is already registered</td></tr>
<tr><td>Who signs the permit form</td><td>You, as the builder</td><td>The builder and all owners</td></tr>
<tr><td>Fixing faults</td><td>You, for at least 7 years</td><td>The builder</td></tr>
<tr><td>How often</td><td>Usually once every 6 years, unless a waiver is granted</td><td>No limit</td></tr>
<tr><td>Selling within 7 years</td><td>You need home indemnity insurance for the buyer</td><td>The builder's insurance covers it</td></tr>
</tbody></table></div>

<h2>When owner-building makes sense</h2>
<ul>
<li>You have time to run the job and are happy to manage trades.</li>
<li>You plan to <strong>live in the home</strong> (or use the shed or carport yourself) and not sell or rent it straight away. This is a rule for owner-builders.</li>
<li>You have done an owner-builder course, or already have building industry registration, plus a white card.</li>
</ul>

<h2>When a registered builder is the better pick</h2>
<ul>
<li>You may sell within 7 years. Owner-builders stay responsible for faults and must arrange home indemnity insurance before selling.</li>
<li>The land is owned by a company or trust. Owner-builders must be individuals.</li>
<li>You have owner-built in the last 6 years and don't have a waiver.</li>
<li>You need the work started soon, and can't wait 6 to 8 weeks for owner-builder approval.</li>
</ul>

<h2>What doesn't change</h2>
<p>Either way you still need a building permit, and planning approval if the work doesn't meet the R-Codes. Licensed work like electrical and plumbing must still be done by licensed trades. Hiring trades doesn't take away an owner-builder's legal duties.</p>
<p>Check if you need approval with the <a href="/owner-builder-checker">owner-builder checker</a>, see <a href="/which-ba-form">which BA form you need</a>, or read about <a href="/structural-engineer-cost-perth">engineer costs in Perth</a>.</p>
"""

FAQS = [
    ("Is it cheaper to be an owner-builder in WA?",
     "It can be, because you aren't paying a builder's margin. But you take on the builder's risks, including fixing faults for at least 7 years, and you must manage every trade yourself."),
    ("How long does owner-builder approval take in WA?",
     "Usually about 6 to 8 weeks. Once it's granted, you have 6 months to apply for your building permit."),
    ("Can I sell a house I owner-built?",
     "Yes, but if you sell within 7 years of the building permit, you need home indemnity insurance that covers the buyer for the rest of that 7 years."),
    ("How often can I be an owner-builder?",
     "Usually once every 6 years. You can apply to have that rule waived."),
    ("Do I need owner-builder approval for a shed?",
     "Only if a permit is needed and the work is worth more than $50,000. Below that, you can usually build it yourself with just a building permit."),
]


def page(S):
    return {"path": "owner-builder-vs-registered-builder.html", "published": "2026-11-23", "type": "Comparison", "icon": "doc",
            "card": "Owner-builder or registered builder in WA? Who carries the risk, the 7-year rule and when each makes sense.",
            "title": "Owner Builder vs Registered Builder in WA (2026)",
            "desc": "Owner-builder vs registered builder in WA: who manages the job, the 6 to 8 week approval, the 7-year fault rule, selling with home indemnity insurance and when each is the better pick.",
            "eyebrow": "Comparison", "h1": "Owner-builder vs registered builder in WA", "crumb": "Owner-builder vs registered builder",
            "answer": "<p>Both are legal in WA. An <strong>owner-builder</strong> saves the builder's margin but runs the job, needs state approval first (usually <strong>6 to 8 weeks</strong>) and stays responsible for faults for <strong>7 years</strong>. A <strong>registered builder</strong> carries that risk for you. You need one or the other for permit work over $20,000 ($50,000 for sheds and carports).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/owner-builder-checker", "Owner-builder checker"), ("/which-ba-form", "Which BA form do I need?"), ("/structural-engineer-cost-perth", "Structural engineer cost in Perth")],
            "sources": [("Owner-builder approval, Department of Local Government, Industry Regulation and Safety", "https://www.wa.gov.au/organisation/service-delivery/owner-builder-approval")]}
