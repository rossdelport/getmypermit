BODY = """
<h2>What the BA1 is</h2>
<p>The BA1 is the state's <strong>application for a building permit, certified</strong>. "Certified" means a private registered building surveyor has already checked your plans and signed a <strong>Certificate of Design Compliance</strong> (form BA3). You lodge the BA1 and the certificate with your council, which then issues the permit.</p>
<p>The current form was approved by the Building Commissioner on 17 July 2026 and has six parts.</p>

<h2>Part 1: The property</h2>
<p>The street address (or lot number if there's no street number), and the certificate of title volume and folio if you know them. You also say if the lot is vacant.</p>

<h2>Part 2: The building work</h2>
<ul>
<li>A short description of the work and what the building will be used for</li>
<li>The building class, copied from the Certificate of Design Compliance (for example Class 1 for a house, Class 10 for a shed, garage, carport, patio or pool)</li>
<li>The type of work: new, addition, fit-out, relocation or change of use</li>
<li>For Class 10, which type: pool, garage, patio, carport, shed, fence or wall, retaining wall, water tank or other</li>
<li>The <strong>estimated value including GST</strong>. Your permit fee is worked out from this</li>
<li>Floor area, lot area, number of storeys, and the main materials</li>
<li>Whether a "performance solution" is proposed (a way of meeting the building code other than the standard rules). Your surveyor will know</li>
</ul>

<h2>Part 3: The owner</h2>
<p>Name, address and contact details. The form says the <strong>owner's signature is not needed for Class 1 or Class 10</strong> buildings. If there are several owners, attach a list.</p>

<h2>Part 4: The builder</h2>
<p>Tick the type of builder:</p>
<ul>
<li>A registered building contractor (give the registration number)</li>
<li>An approved owner-builder (attach the approval and give its number)</li>
<li>Public authority</li>
<li>Other: work under $20,000, or where a registered builder isn't needed</li>
</ul>
<p>The builder signs this part.</p>

<h2>Part 5: The applicant</h2>
<p>Who is lodging it: the owner, the builder or someone else (such as a drafter or permit service).</p>

<h2>Part 6: The statement</h2>
<p>The applicant signs to confirm that all required information is attached, any other approvals (like planning approval) have been obtained, and whether the work goes over or affects the neighbour's land. If it does, attach the neighbour's consent (form BA20) or a court order.</p>

<h2>What to lodge with it</h2>
<p>Councils publish their own checklists. The City of Bayswater's, for example, lists:</p>
<ul>
<li>The completed BA1 and the Certificate of Design Compliance with all documents it refers to</li>
<li>Site plan, floor plans and elevations</li>
<li>The permit fee and Building Services Levy</li>
<li>Home indemnity insurance for work over $20,000 (not needed for things like carports, patios, sheds and pools, or owner-builders)</li>
<li>A Construction Training Fund levy receipt for work over $100,000</li>
<li>Proof that planning conditions have been met</li>
</ul>

<h2>Fees and timing</h2>
<p>The BA1 permit fee is 0.19% of the value for houses and Class 10 structures, at least $121, plus the Building Services Levy ($61.65 up to $45,000). Councils usually decide a BA1 within <strong>10 business days</strong> of a complete application. Not sure whether a BA1 or BA2 suits you? See <a href="/ba1-vs-ba2">BA1 vs BA2</a>, or read <a href="/how-to-fill-in-a-ba2-form">how to fill in a BA2</a>. Work out the fee with the <a href="/building-permit-fee-calculator">fee calculator</a>.</p>
"""

FAQS = [
    ("What is a BA1 form in WA?",
     "It's the application for a certified building permit. You lodge it with a Certificate of Design Compliance (BA3) from a private registered building surveyor."),
    ("Does the owner need to sign the BA1?",
     "Not for Class 1 or Class 10 buildings, such as houses, sheds, garages, carports, patios and pools. The form says the owner's signature isn't required for these."),
    ("What do I need to lodge with a BA1?",
     "The Certificate of Design Compliance and the documents it refers to, plans, fees, and where needed home indemnity insurance, the CTF levy receipt and proof planning conditions are met. Councils have their own checklists."),
    ("How much is a BA1 building permit?",
     "0.19% of the value of the work for houses and Class 10 structures, at least $121, plus the Building Services Levy of $61.65 for work up to $45,000."),
    ("How long does a BA1 take?",
     "Councils have 10 business days to decide a complete BA1 application."),
]


def page(S):
    return {"path": "how-to-fill-in-a-ba1-form.html", "published": "2026-11-08", "type": "How-to guide", "icon": "doc",
            "card": "The six parts of the certified permit form, what to attach, and the fees.",
            "title": "How to Fill In a BA1 Form (WA Certified Permit)",
            "desc": "How to fill in the WA BA1 certified building permit form, part by part: property, work details, owner, builder, applicant and statement, plus what to attach.",
            "eyebrow": "How-to guide", "h1": "How to fill in a BA1 form", "crumb": "How to fill in a BA1",
            "answer": "<p>The BA1 has six parts: the property, the building work (including its value with GST), the owner, the builder, the applicant, and a signed statement. Attach the <strong>Certificate of Design Compliance</strong> from a private building surveyor, your plans and the fees. The owner doesn't need to sign for houses or Class 10 structures.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/ba1-vs-ba2", "BA1 vs BA2"), ("/how-to-fill-in-a-ba2-form", "How to fill in a BA2 form"), ("/building-permit-fee-calculator", "Building permit fee calculator")],
            "sources": [("Form BA1: Application for building permit, certified (Building and Energy)", "https://www.wa.gov.au/media/54115/download?inline"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Certified application checklist (City of Bayswater)", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/forms/2026/form-ba1-certified-application-checklist")]}
