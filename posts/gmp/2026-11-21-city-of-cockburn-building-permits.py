BODY = """
<h2>BA1 or BA2?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private building surveyor, who issues a Certificate of Design Compliance (BA3) first</td><td>The City's building surveyors</td></tr>
<tr><td>What it can be used for</td><td>Any building. Must be used for Classes 2 to 9 (shops, offices, apartments)</td><td>Houses (Class 1) and sheds, garages, carports, patios, pools and retaining walls (Class 10)</td></tr>
<tr><td>City's decision time</td><td>10 business days</td><td>25 business days</td></tr>
</tbody></table></div>
<p>If the City asks for more information, you have <strong>21 calendar days</strong> to send it. If you don't, the City can refuse the application and keep the fee.</p>

<h2>What Cockburn says needs a permit</h2>
<p>The City's checklist lists new work, alterations and additions, pools and spas and their fences, patios (including "pergolas" with a metal roof), sheds, shade sails, boundary retaining walls, screen walls and front fences. Lightweight dividing fences usually don't need one. Small exempt work is listed in the state Building Regulations 2012.</p>

<h2>What to have ready</h2>
<ul>
<li>The BA1 or BA2 form, with fees paid when you lodge.</li>
<li>A Construction Training Fund levy form or receipt if the work is over $20,000.</li>
<li>A registered builder's details, or owner-builder approval, if needed. For a house that's work over <strong>$20,000</strong>. Since 1 July 2026, for a shed, garage or carport it's <strong>$50,000</strong>.</li>
<li>Any other approvals first: planning approval, Water Corporation, a septic system (City Health Services) or a new crossover.</li>
<li>A <strong>BA20</strong> neighbour consent if the work affects their land, for example removing a dividing fence, digging to the boundary, or a boundary or retaining wall within 600 mm of it. Skipping it can mean a fine of $5,000 to $25,000.</li>
<li>Plans: a site plan at 1:200 with levels, sewer and easements, plus floor plans, elevations and sections at 1:100.</li>
<li>Engineering, termite and energy details where they apply, and a BAL report (under 12 months old) in bushfire-prone areas.</li>
</ul>

<h2>After you build</h2>
<p>The builder named on the permit must lodge a <strong>BA7 notice of completion</strong> within <strong>7 days</strong> of finishing, with a copy of any inspection certificates. Cockburn accepts it by email.</p>
<p>Not sure if you need a permit? The City offers <strong>free pre-lodgement meetings</strong> at its Spearwood office; book on 9411 3608.</p>
<p>See <a href="/which-ba-form">which BA form you need</a>, use the <a href="/owner-builder-checker">owner-builder checker</a>, or read about the <a href="/ba7-notice-of-completion">BA7 notice of completion</a>.</p>
"""

FAQS = [
    ("How long does a building permit take in the City of Cockburn?",
     "10 business days for a certified BA1 and 25 business days for an uncertified BA2, once the City has everything it needs."),
    ("Can I lodge a BA2 in Cockburn?",
     "Yes, for a house (Class 1) or a Class 10 structure such as a shed, patio, carport, pool or retaining wall. Other buildings need a BA1."),
    ("Does Cockburn give free building advice?",
     "Yes. The City offers free pre-lodgement meetings at its Spearwood office. Call 9411 3608 to book."),
    ("What happens if I don't send the extra information in time?",
     "You have 21 calendar days. After that, the City can refuse the application and keep the fee."),
]


def page(S):
    return {"path": "city-of-cockburn-building-permits.html", "published": "2026-11-21", "type": "Council guide", "icon": "pin",
            "card": "City of Cockburn building permits: BA1 vs BA2, timeframes, the checklist and free advice.",
            "title": "City of Cockburn Building Permits (2026)",
            "desc": "City of Cockburn building permits: BA1 (10 days) vs BA2 (25 days), what needs a permit, the documents to lodge, neighbour consent, the BA7 and free advice.",
            "eyebrow": "Council guide", "h1": "City of Cockburn building permits", "crumb": "City of Cockburn building permits",
            "answer": "<p>The City of Cockburn decides a certified <strong>BA1</strong> in <strong>10 business days</strong> and an uncertified <strong>BA2</strong> in <strong>25 business days</strong>. Houses, sheds, patios, carports and pools can use a BA2. If the City asks for more information you have <strong>21 days</strong>, and it offers <strong>free pre-lodgement meetings</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/owner-builder-checker", "Owner-builder checker"), ("/ba7-notice-of-completion", "BA7 notice of completion")],
            "sources": [("Building Permit Application, City of Cockburn", "https://www.cockburn.wa.gov.au/Building-Planning-and-Roads/Applications-and-Permits/Building-permit"),
                        ("Building permit submission checklist (Class 1 and 10), City of Cockburn", "https://www.cockburn.wa.gov.au/getattachment/0fe70f8e-9b97-4c89-a87e-434a63b4a1b1/ECM_9666000_v2_BP-Submission-Checklist-Class-1-10-March-2020-pdf.aspx")]}
