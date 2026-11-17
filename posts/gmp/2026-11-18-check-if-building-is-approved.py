BODY = """
<h2>Why it matters</h2>
<p>In WA there's no "7-year rule" that makes old unapproved work legal. If the council has no record of a building permit for a patio, shed, carport or extension, it's treated as <strong>unauthorised</strong>, no matter how long it's been there. That can cause problems when you sell, insure or renovate.</p>

<h2>Four ways to check</h2>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What to do</th></tr></thead><tbody>
<tr><td>1. Ask the seller</td><td>Ask for copies of the building permit and the approved plans. Owners often keep them with the house papers.</td></tr>
<tr><td>2. Request a plan search</td><td>Most Perth councils let you request copies of past plans and permits for a property. For example, the City of Stirling has an archived plans request, and the City of Bayswater has a plan search request form.</td></tr>
<tr><td>3. Get the owner's OK</td><td>If you're not the owner, councils usually need the owner's written permission before they release plans. Stirling asks for this.</td></tr>
<tr><td>4. Compare plans to the site</td><td>Check that what was approved matches what's actually built: size, position and setbacks.</td></tr>
</tbody></table></div>
<p>Each council has its own form and fee, and some take a few weeks, so ask early if you're buying.</p>

<h2>If there's no approval</h2>
<p>You can usually fix it with a <strong>Certificate of Building Approval</strong>. This is lodged with a <strong>BA13</strong> form and a <strong>BA18</strong> inspection certificate from a registered building surveyor or engineer. Some structures also need retrospective planning approval first. Councils vary, so check with yours.</p>
<p>Read about <a href="/retrospective-approval">retrospective approval</a>, why the <a href="/seven-year-rule-wa">7-year rule is a myth</a>, or what a <a href="/certificate-of-building-compliance">Certificate of Building Compliance</a> is.</p>
"""

FAQS = [
    ("How do I find out if a patio or shed was approved in WA?",
     "Ask the seller for the permit and plans, or request a plan search from the local council. If there's no record, the council treats it as unauthorised."),
    ("Can I see the building plans for a house I'm buying?",
     "Usually yes, but councils normally need the owner's written permission before they release plans to a buyer or agent."),
    ("Does unapproved work become legal after 7 years in WA?",
     "No. There's no time limit that makes unapproved building work legal in WA."),
    ("How do I fix a building with no approval?",
     "Usually with a BA13 application for a Certificate of Building Approval, backed by a BA18 inspection certificate. Some structures also need retrospective planning approval."),
]


def page(S):
    return {"path": "check-if-building-is-approved.html", "published": "2026-11-18", "type": "Question answer", "icon": "pin",
            "card": "How to check if a patio, shed or extension was approved, and what to do if it wasn't.",
            "title": "How to Check if a Building Is Approved in WA (2026)",
            "desc": "How to check if a patio, shed, carport or extension has council approval in WA: ask the seller, request a plan search, and what to do if there's no permit.",
            "eyebrow": "Question answer", "h1": "How do I check if a building is approved?", "crumb": "Check if a building is approved",
            "answer": "<p>Ask the owner for the <strong>building permit and approved plans</strong>, or request a <strong>plan search</strong> from the local council. Councils usually need the owner's written permission to release plans. If there's no record, the work is treated as <strong>unauthorised</strong>. There's no 7-year rule in WA.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-approval", "Retrospective approval"), ("/seven-year-rule-wa", "The 7-year rule myth"), ("/certificate-of-building-compliance", "Certificate of Building Compliance")],
            "sources": [("Request archived plans, City of Stirling", "https://www.stirling.wa.gov.au/developing-property/planning-advice/request-archived-plans"),
                        ("Plan search request form, City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/forms/2024/plan-search-request-form"),
                        ("Unauthorised work, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work")]}
