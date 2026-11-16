BODY = """
<h2>First, check if it's really unapproved</h2>
<p>Ask your council for a <strong>plan search</strong> (building records search). If there's an approved plan for the patio, you don't need to do anything. If there isn't, or the patio is different from what was approved, it's treated as unauthorised.</p>
<p>Also check whether it needed approval at all. A freestanding patio no bigger than 10 m² and no taller than 2.4 m usually didn't need a building permit. An <strong>attached</strong> patio usually did, whatever its size.</p>

<h2>You can't get a building permit after the fact</h2>
<p>A building permit can only be issued <strong>before</strong> work starts. For a patio that's already built, the process is a <strong>building approval certificate</strong> instead. In WA, building without a required permit is an offence, with fines of up to $50,000 for a first offence, so it's worth fixing.</p>

<h2>Step by step</h2>
<ol>
<li><strong>Get as-built plans.</strong> A site plan and elevations showing the patio as it stands now, with setbacks to the boundaries.</li>
<li><strong>Get it checked by a registered building surveyor.</strong> They inspect it and, if it complies, sign a <strong>BA18 Certificate of Building Compliance</strong>. They may ask for an engineer's report on the posts, beams and footings.</li>
<li><strong>Fix anything that doesn't comply.</strong> This could be extra bracing, bigger footings, or changes near the boundary.</li>
<li><strong>Get planning approval if needed.</strong> If the patio breaks the R-Codes or a local policy (for example, it's in the front setback or too close to a boundary), your council may need a retrospective planning application first.</li>
<li><strong>Lodge a BA13 with the council.</strong> Send the BA13 application for a building approval certificate, the BA18, the plans and the fees.</li>
</ol>

<h2>Fees</h2>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA13 application for unauthorised work</td><td>0.38% of the patio's current value, at least $121</td></tr>
<tr><td>Building Services Levy for unauthorised work</td><td>0.274% of the value (Rockingham lists a $123.30 minimum)</td></tr>
<tr><td>Building surveyor for the BA18</td><td>Set by the surveyor. Rockingham charges at least $400.</td></tr>
</tbody></table></div>
<p>These fees are higher than for a normal building permit, which is why approval before you build is cheaper.</p>
<p>Councils vary, so ask yours what they need. See the <a href="/patio-approval-checker">patio approval checker</a>, <a href="/patio-plans-for-council">what goes on patio plans</a> and the <a href="/patio-approval-cost-perth">cost of patio approval</a>.</p>
"""

FAQS = [
    ("Can I get council approval for a patio that's already built?",
     "Usually yes. You can't get a building permit after the fact, but you can apply for a building approval certificate (BA13) with a BA18 from a registered building surveyor."),
    ("What is a BA18?",
     "A Certificate of Building Compliance, signed by a registered building surveyor, saying the existing patio meets the building standards."),
    ("How much does retrospective patio approval cost?",
     "The BA13 fee is 0.38% of the patio's value (at least $121), plus a 0.274% levy and the building surveyor's fee."),
    ("What if my patio doesn't comply?",
     "You may need to change it, for example adding bracing or moving it back from a boundary, before it can be approved. The council can also order it removed."),
]


def page(S):
    return {"path": "existing-patio-approval.html", "published": "2026-11-17", "type": "How-to guide", "icon": "pergola",
            "card": "How to get council approval for a patio that was built without a permit: BA13, BA18 and fees.",
            "title": "How to Get an Existing Patio Approved in WA (BA13 + BA18)",
            "desc": "Built a patio without approval? How to get it approved in WA: plan search, as-built plans, BA18 from a building surveyor, BA13 to council, and the fees.",
            "eyebrow": "How-to guide", "h1": "How to get an existing patio approved", "crumb": "Existing patio approval",
            "answer": "<p>You can't get a building permit for a patio that's already built. Instead, a registered building surveyor checks it and signs a <strong>BA18</strong>, then you lodge a <strong>BA13</strong> (building approval certificate) with your council. The fee is <strong>0.38%</strong> of the patio's value (at least $121) plus a levy.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-plans-for-council", "Patio plans for council"), ("/patio-approval-cost-perth", "Patio approval cost")],
            "sources": [("Building approvals: forms and fees, WA Government (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Industry Bulletin 157: BA18 Certificate of Building Compliance, Building and Energy", "https://www.wa.gov.au/system/files/2024-10/ib_157_-_updated_ba18_-_certificate_of_building_compliance_for_building_surveyors_0.pdf"),
                        ("Unauthorised work, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work"),
                        ("Unapproved buildings and structures, City of Belmont", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/unapproved-buildings-and-structures"),
                        ("Building Services fee sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/d92d0adf-466c-4d62-bb92-fc64ccf62f7d/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Building-Services-Fee-Sheet.pdf?language=en")]}
