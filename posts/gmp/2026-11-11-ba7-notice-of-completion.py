BODY = """
<h2>What the BA7 is for</h2>
<p>A building permit doesn't end when the last screw goes in. Under section 33 of the Building Act, the builder named on the permit must tell the council the work is finished. That notice is <strong>form BA7, Notice of completion</strong>. It closes off the permit on the council's records.</p>

<h2>The key rules</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Detail</th></tr></thead><tbody>
<tr><td>Who lodges it</td><td>The builder or demolition contractor named on the permit. If you're the owner-builder, or you built a small Class 10 job yourself, that's you.</td></tr>
<tr><td>When</td><td>Within <strong>7 days</strong> of finishing the work, or the stage of work the permit covered</td></tr>
<tr><td>Where</td><td>The permit authority, usually your council</td></tr>
<tr><td>Fee</td><td>None listed on the form</td></tr>
<tr><td>Penalty for not lodging</td><td>Up to <strong>$10,000</strong></td></tr>
</tbody></table></div>

<h2>What goes on the form</h2>
<p>The current BA7 (approved 17 July 2026) is two pages:</p>
<ol>
<li><strong>Property</strong>: the address or lot number, and the permit number</li>
<li><strong>Details</strong>: whether it's building or demolition work (or a stage), the date of completion, the <strong>final value of the contract</strong>, and whether it includes a pool, spa or pool barrier</li>
<li><strong>Builder</strong>: name, registration, licence or owner-builder approval number, and contact details</li>
<li><strong>Notification</strong>: you sign to say you're the builder on the permit, the work is finished, and you've attached a certificate for each inspection or test listed on the permit</li>
<li><strong>Inspections and tests</strong>: dates and types, with the certificates attached</li>
</ol>

<h2>Common questions councils get</h2>
<ul>
<li><strong>What inspections?</strong> Only those listed on your permit. New pools also have their safety barrier inspected by the council.</li>
<li><strong>Does it let me move in?</strong> Houses, granny flats and outbuildings (Class 1 and 10) don't need an occupancy permit. For Class 2 to 9 buildings, the form says the BA7 doesn't authorise occupancy.</li>
<li><strong>The builder changed halfway?</strong> That's a different form: the BA8, Notice of cessation.</li>
</ul>
<p>Some councils, such as Gosnells, remind owners that the BA7 is still needed even when other steps are done. Councils vary in how they accept it, so check your council's website.</p>
<p>Not sure which form you need at the start? See <a href="/which-ba-form">which BA form do I need?</a>, the <a href="/permit-jargon">permit jargon guide</a>, or <a href="/how-to-fill-in-a-ba2-form">how to fill in a BA2</a>.</p>
"""

FAQS = [
    ("What is a BA7 in WA?",
     "A BA7 is the Notice of completion. The builder named on the building or demolition permit lodges it with the council to say the work is finished."),
    ("How long do I have to lodge a BA7?",
     "Within 7 days of finishing the work, or the stage of work, that the permit covered."),
    ("What happens if I don't lodge a BA7?",
     "Not lodging it can bring a penalty of up to $10,000."),
    ("Who signs the BA7?",
     "The builder or demolition contractor named on the permit. For owner-builders, that's the owner."),
    ("Does a BA7 let me occupy a building?",
     "It doesn't authorise occupancy of a Class 2 to 9 building that needs an occupancy permit. Houses and outbuildings don't need one."),
]


def page(S):
    return {"path": "ba7-notice-of-completion.html", "published": "2026-11-11", "type": "Question answer", "icon": "doc",
            "card": "The form that closes off your permit: who lodges it, the 7-day rule and the $10,000 penalty.",
            "title": "What Is a BA7 Notice of Completion? (WA 2026)",
            "desc": "The BA7 notice of completion in WA: who lodges it, the 7-day deadline, what goes on the form, inspection certificates and the $10,000 penalty.",
            "eyebrow": "Question answer", "h1": "What is a BA7 notice of completion?", "crumb": "BA7 notice of completion",
            "answer": "<p>The <strong>BA7</strong> is the form the builder named on your permit lodges with the council when the work is finished. It must go in within <strong>7 days</strong> of completion, with certificates for any inspections or tests the permit listed. Not lodging it can bring a penalty of up to <strong>$10,000</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/permit-jargon", "Permit jargon guide"), ("/how-to-fill-in-a-ba2-form", "How to fill in a BA2")],
            "sources": [("Form BA7 Notice of completion, approved 17 July 2026 (Building Commissioner)", "https://www.wa.gov.au/media/54192/download?inline"),
                        ("Occupying a building (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Occupying-a-building")]}
