BODY = """
<h2>Yes, every granny flat needs a building permit</h2>
<p>The 2024 changes made granny flats easier, but only on the <strong>planning</strong> side. The state's granny flat info sheet says you still need a <strong>building permit</strong>, and the granny flat must meet the National Construction Code. The City of Wanneroo and the City of Joondalup both say a building permit is always required.</p>

<h2>Planning approval vs building permit</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Planning approval</th><th>Building permit</th></tr></thead><tbody>
<tr><td>Needed?</td><td>Usually not, if it meets the deemed-to-comply rules</td><td>Always</td></tr>
<tr><td>What it checks</td><td>Size (70 m²), setbacks, site cover, height, privacy</td><td>Structure, fire safety, energy, plumbing and the building code</td></tr>
<tr><td>Time limit</td><td>60 days, or 90 with consultation</td><td>10 business days (BA1) or 25 (BA2)</td></tr>
</tbody></table></div>
<p>If your granny flat needs planning approval, it must come first. Wanneroo says the planning approval must be granted before the building permit.</p>

<h2>BA1 or BA2?</h2>
<ul>
<li><strong>BA2 (uncertified):</strong> the council checks the plans. Allowed for houses and Class 10 buildings, so a granny flat can use it. Decision within 25 business days.</li>
<li><strong>BA1 (certified):</strong> a private building surveyor checks the plans first and issues a Certificate of Design Compliance. Decision within 10 business days.</li>
</ul>
<p>Wanneroo has separate BA1 and BA2 checklists for residential buildings.</p>

<h2>Who can build it</h2>
<p>The state says there are <strong>no special exemptions</strong> for prefab or kit homes. A habitable building worth more than <strong>$20,000</strong> that needs a permit must be built by a <strong>registered builder</strong> or an <strong>approved owner-builder</strong>. Electrical and plumbing work must be done by licensed trades.</p>

<h2>State fees</h2>
<p>A BA2 costs 0.32% of the value and a BA1 0.19% (plus the surveyor), at least $121. The Building Services Levy is 0.137% above $45,000, and the Construction Training Fund levy is 0.2% for work over $100,000. Use the fee calculator on <a href="https://getmypermit.com.au/building-permit-fee-calculator">GetMyPermit</a> to work it out.</p>
<p>Read <a href="/granny-flat-approval-process">the granny flat approval process</a>, <a href="/granny-flat-rules-wa">granny flat rules in WA</a>, or <a href="/city-of-wanneroo-granny-flat-rules">City of Wanneroo granny flat rules</a>.</p>
"""

FAQS = [
    ("Do I need a building permit for a granny flat in WA?",
     "Yes. The state's granny flat info sheet says a building permit is still needed, and councils such as Wanneroo and Joondalup say it's always required."),
    ("Do I need planning approval for a granny flat?",
     "Usually not, if it's 70 m² or less and meets the R-Codes deemed-to-comply rules. If it doesn't, planning approval comes first."),
    ("Can I build a granny flat as an owner-builder?",
     "Yes, if you're an approved owner-builder. Otherwise a habitable building over $20,000 must be built by a registered builder."),
    ("Does a kit or transportable granny flat need a permit?",
     "Yes. The state says there are no specific exemptions for prefabricated buildings."),
]


def page(S):
    return {"path": "granny-flat-building-permit.html", "published": "2026-11-12", "type": "Question", "icon": "doc",
            "card": "Why every granny flat still needs a building permit, BA1 vs BA2, and who can build it.",
            "title": "Do I Need a Building Permit for a Granny Flat? (WA)",
            "desc": "Yes: every WA granny flat needs a building permit, even when planning approval isn't needed. BA1 vs BA2, time limits, fees, and who can build it.",
            "eyebrow": "Question", "h1": "Do I need a building permit for a granny flat?",
            "crumb": "Granny flat building permit",
            "answer": "<p><strong>Yes.</strong> Since 2024 most granny flats up to <strong>70 m²</strong> don't need <strong>planning</strong> approval, but every granny flat still needs a <strong>building permit</strong> and must meet the National Construction Code. Councils such as Wanneroo and Joondalup confirm this.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-approval-process", "Granny flat approval process"), ("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/city-of-wanneroo-granny-flat-rules", "City of Wanneroo granny flat rules")],
            "sources": [("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Ancillary accommodation (granny flat), City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/111/ancillary_accommodation_granny_flat"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
