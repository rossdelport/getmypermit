BODY = """
<h2>What the BA2 is</h2>
<p>The BA2 is the state's <strong>application for a building permit, uncertified</strong>. "Uncertified" means no private building surveyor has checked your plans yet, so your council does that check. It can only be used for a house (Class 1a) and Class 10 structures: garages, carports, sheds, patios, fences, retaining walls, pools and the like. Council has up to 25 business days to decide.</p>
<p>The form has six parts. Here's what goes in each.</p>

<h2>Part 1: Property</h2>
<p>The street address of the land being built on. Use the <strong>lot number</strong> if there's no street number yet. Add the certificate of title volume and folio if you know them (they're on your rates notice or title). Tick whether the lot is vacant.</p>

<h2>Part 2: Details of the building work</h2>
<ul>
<li><strong>Description.</strong> Plain words, such as "Freestanding steel shed 6 m x 6 m" or "Patio attached to rear of house".</li>
<li><strong>BCA class.</strong> Class 1a for a house or granny flat. Class 10a for a garage, carport or shed. Class 10b for a fence, retaining wall or pool.</li>
<li><strong>Type of work and structure.</strong> New or alteration, and whether it is detached or attached.</li>
<li><strong>Estimated value of the work, including GST.</strong> This sets your fee (0.32%, at least $121), so make it realistic. Include labour, materials and services; councils can reject an application if the value looks wrong.</li>
<li><strong>Floor area, lot area and main materials</strong> for the floor, walls, roof and frame.</li>
<li><strong>Alternative solution.</strong> Tick "No" unless an engineer or designer has used a performance solution instead of the standard building code method.</li>
</ul>

<h2>Part 3: Owner details</h2>
<p>Name, address, email and phone for <strong>every</strong> owner on the title. Each owner signs. If there are several owners, attach a list with each name and signature. If someone signs for an owner, attach their written authority.</p>

<h2>Part 4: Builder details</h2>
<p>Who will build it, and which type of builder they are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Builder type</th><th>When it applies</th></tr></thead><tbody>
<tr><td>Registered building contractor</td><td>Give their registration number</td></tr>
<tr><td>Approved owner-builder</td><td>Attach the owner-builder approval and give its number</td></tr>
<tr><td>Other</td><td>Work under $20,000, or where a registered builder isn't required</td></tr>
</tbody></table></div>
<p>The Shire of Harvey's 2026 checklist, for example, asks for owner-builder approval when work is over $20,000 for a house, or over $50,000 for a shed, carport or patio. The builder signs this part.</p>

<h2>Part 5: Applicant</h2>
<p>Tick owner, builder or other. If someone else is lodging for you (such as a permit service), their details go here.</p>

<h2>Part 6: Statement by the applicant</h2>
<p>Two questions about your neighbours: does the work <strong>encroach</strong> on other land, and could it <strong>adversely affect</strong> other land (for example footings or a wall right on the boundary)? If yes, attach the neighbour's signed consent on a <strong>BA20</strong>, or a court order. The applicant then signs.</p>

<h2>What to attach</h2>
<ul>
<li>Site plan (usually at least 1:200) showing the distances to every boundary and other buildings</li>
<li>Floor plan, elevations and sections (usually at least 1:100) with all dimensions</li>
<li>Construction details and structural engineering</li>
<li>Energy efficiency report (houses and habitable additions only)</li>
<li>Bushfire (BAL) report, if the lot is bushfire-prone</li>
<li>Construction Training Fund receipt, for work over $100,000</li>
<li>Planning approval, if your project needed it</li>
</ul>
<p>Check your council's BA2 checklist too, as some ask for extra items such as a verge bond application.</p>
"""

FAQS = [
    ("Who signs the BA2 form?",
     "Every owner on the title signs Part 3, the builder signs Part 4 and the applicant signs Part 6. If someone signs for an owner, attach their written authority."),
    ("Can I fill in a BA2 myself?",
     "Yes. Owners often lodge their own BA2. The form itself is simple; the drawings, engineering and council's questions are the harder part."),
    ("What value do I put on the BA2?",
     "The full estimated cost of the work including GST, labour, materials and services. The fee is 0.32% of this value, at least $121, and councils can reject an application if the value is too low."),
    ("Can I use a BA2 for a commercial building?",
     "No. The BA2 is only for houses (Class 1a) and Class 10 structures such as sheds, carports, patios, fences and pools. Other buildings need a certified BA1."),
]


def page(S):
    return {"path": "how-to-fill-in-a-ba2-form.html", "published": "2026-11-01", "type": "How-to guide", "icon": "doc",
            "card": "The BA2 building permit form, part by part: what to write, who signs, and what to attach.",
            "title": "How to Fill In a BA2 Form (WA Uncertified Building Permit)",
            "desc": "A part-by-part guide to the WA BA2 form: property, building work, value, owners, builder type, neighbour consent, signatures and the documents to attach.",
            "eyebrow": "How-to guide", "h1": "How to fill in a BA2 form", "crumb": "How to fill in a BA2",
            "answer": "<p>The BA2 has six parts: <strong>the property, the building work, the owners, the builder, the applicant and a statement</strong> about neighbours. Give an honest value including GST (it sets the fee), get every owner and the builder to sign, and attach the site plan, drawings and engineering. Council then has up to 25 business days to decide.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/city-of-stirling-building-permits", "City of Stirling building permits"), ("/do-i-need-approval", "Do I need council approval?")],
            "sources": [("Form BA2: Application for building permit, uncertified (Building Commissioner)", "https://www.narembeen.wa.gov.au/documents/10324/ba2-application-for-a-building-permit-uncertified"),
                        ("BA2 application checklist, July 2026 (Shire of Harvey)", "https://www.harvey.wa.gov.au/wp-content/uploads/2026/07/BA2-Class-1-and-10-Building-Permit-Application-Checklist-as-at-06.07.2026.pdf"),
                        ("Outbuildings information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/360/outbuildings_-_information_sheet.pdf"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf")]}
