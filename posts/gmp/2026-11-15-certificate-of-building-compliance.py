BODY = """
<h2>What a BA18 is</h2>
<p>A <strong>certificate of building compliance</strong> (form BA18) is a signed statement from a <strong>registered building surveyor</strong>. For work that was built without a permit, it says the building <strong>substantially complies</strong> with each building standard that applies to it. It must come with plans and specifications that show how it complies.</p>
<p>The current form is dated <strong>2 November 2023</strong> in its footer. You can find it on the state's building approval forms page.</p>

<h2>When you need one</h2>
<p>You need a BA18 when you're asking council to approve work that's already been built without a permit:</p>
<div class="table-wrap"><table>
<thead><tr><th>Type of building</th><th>Form you lodge with council</th><th>Needs a BA18?</th></tr></thead><tbody>
<tr><td>Class 1 and 10: houses, extensions, patios, sheds, carports, pools</td><td>BA13 building approval certificate</td><td>Yes</td></tr>
<tr><td>Class 2 to 9: units, shops, offices, factories</td><td>BA9 occupancy permit</td><td>Yes</td></tr>
</tbody></table></div>

<h2>Step by step</h2>
<ol>
<li><strong>Check what's approved.</strong> Ask council for a plan search of your property. Anything with no approval record is treated as unauthorised. The City of Rockingham, for example, charges $60 for a full set of residential plans.</li>
<li><strong>Check if planning approval is needed first.</strong> Some councils need a retrospective planning or R-Codes approval before they'll issue the building approval. Rockingham says this for rural and special residential lots, and that lots zoned R2 to R80 may need an R-Codes application.</li>
<li><strong>Engage a registered building surveyor.</strong> They'll tell you what inspections and documents they need. A BA18 usually includes a site inspection.</li>
<li><strong>Gather the documents.</strong> Usually as-built plans (floor plan, elevations, sections, construction details), specifications and, where needed, an engineer's certificate for the structure.</li>
<li><strong>Get the BA18 signed.</strong> The surveyor checks the work against the building standards and signs the certificate.</li>
<li><strong>Lodge with council.</strong> Submit the BA13 (or BA9), the BA18 and every document listed on the BA18, and pay the fees.</li>
<li><strong>Council decides.</strong> If approved, council issues a building approval certificate (BA14), which lets the structure stay.</li>
</ol>

<h2>Who can issue it</h2>
<p>Councils vary. The Shire of Mundaring says only a <strong>private</strong> building surveyor can issue a BA18. The City of Gosnells and the City of Rockingham offer a certification service and may be engaged to provide one. Rockingham's fee sheet lists a BA18 at a <strong>minimum of $400 for the first 3 hours, then $110 an hour</strong>. A list of registered building surveyors is on the state's Building and Energy website.</p>

<h2>Council fees for the BA13</h2>
<p>These are set by the state, so they're usually the same at every council:</p>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Rate</th></tr></thead><tbody>
<tr><td>BA13 for unauthorised Class 1 and 10 work</td><td>0.38% of the value, minimum $121</td></tr>
<tr><td>Building services levy for unauthorised work</td><td>0.274% of the value, minimum $123.30</td></tr>
</tbody></table></div>
<p>That's about double the levy you'd pay if you got a permit first. See <a href="/retrospective-approval-cost">retrospective approval cost</a> for worked examples.</p>

<h2>If the work doesn't comply</h2>
<p>Lodging doesn't guarantee approval. Council can ask for work to be done to bring it up to standard, refuse the application, or take action to have it removed. Building without a permit can carry fines of up to $50,000 for a first offence. There's no "7-year rule" that makes old work legal: read <a href="/seven-year-rule-wa">is there a 7-year rule in WA?</a></p>
<p>Not sure which form you need? Use the <a href="/which-ba-form">which BA form checker</a>.</p>
"""

FAQS = [
    ("What is a BA18 in WA?",
     "A certificate of building compliance signed by a registered building surveyor. For unauthorised work, it states the building substantially complies with each building standard that applies, with plans and specifications showing how."),
    ("Who can issue a BA18 certificate?",
     "A registered building surveyor. Councils vary: Mundaring says only a private surveyor can issue one, while Gosnells and Rockingham offer a certification service."),
    ("How much does a BA18 cost?",
     "Private surveyors set their own prices. The City of Rockingham lists a minimum of $400 for the first 3 hours, then $110 an hour. Council's BA13 fee and levy are on top."),
    ("Do I need a BA18 for an unapproved patio or shed?",
     "Yes. To get retrospective approval for Class 1 or 10 work like a patio or shed, you lodge a BA13 with a BA18 attached."),
]


def page(S):
    return {"path": "certificate-of-building-compliance.html", "published": "2026-11-15", "type": "How-to guide", "icon": "check",
            "card": "What a BA18 is, when you need one, who can issue it and the steps to get one.",
            "title": "How to Get a Certificate of Building Compliance (BA18) in WA",
            "desc": "How to get a BA18 certificate of building compliance in WA: when you need one, who can issue it, documents, council fees and the steps to retrospective approval.",
            "eyebrow": "How-to guide", "h1": "How to get a certificate of building compliance (BA18)", "crumb": "BA18 certificate",
            "answer": "<p>A <strong>BA18</strong> is a certificate from a <strong>registered building surveyor</strong> saying work built without a permit substantially complies with the building standards. You lodge it with a <strong>BA13</strong> (houses, sheds, patios) or <strong>BA9</strong> (other buildings) to get retrospective approval from council.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-approval-cost", "Retrospective approval cost"), ("/seven-year-rule-wa", "Is there a 7-year rule in WA?"), ("/which-ba-form", "Which BA form do I need?")],
            "sources": [("Industry Bulletin 157: Updated BA18, Building and Energy", "https://www.wa.gov.au/system/files/2024-10/ib_157_-_updated_ba18_-_certificate_of_building_compliance_for_building_surveyors_0.pdf"),
                        ("Unauthorised work, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work"),
                        ("Unauthorised buildings, Shire of Mundaring", "https://www.mundaring.wa.gov.au/plan-build/understanding-regulations-approvals-and-permits/unauthorised-buildings.aspx"),
                        ("Unauthorised building work and Building Services fee sheet, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/building-applications-and-permits")]}
