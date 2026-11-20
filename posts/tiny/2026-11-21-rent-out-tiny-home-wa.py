BODY = """
<h2>It depends on wheels or fixed</h2>
<div class="table-wrap"><table>
<thead><tr><th>Your tiny home</th><th>Short stays (Airbnb)</th><th>Longer rental</th></tr></thead><tbody>
<tr><td>On wheels (a caravan)</td><td>Usually <strong>not</strong> on a normal house lot. Mundaring allows it only in an approved caravan park, and Kwinana doesn't allow short-stay letting</td><td>Some councils allow it with approval. Kwinana allows private renting over 3 months with a management plan</td></tr>
<tr><td>Fixed and approved as a dwelling or granny flat</td><td>Possible. Must be registered on the state short-stay register</td><td>Usually yes, like any rental home</td></tr>
</tbody></table></div>

<h2>Tiny homes on wheels</h2>
<p>Councils usually treat a tiny home on wheels as a <strong>caravan</strong>. Caravans can't be lived in permanently outside a licensed caravan park, and staying on private land beyond a short visit needs council approval. Councils treat paid stays as a <strong>land use</strong>: the Shire of Bridgetown-Greenbushes says short-term renting of a tiny home needs development approval, plus building and health approvals. Ask your council before you list it.</p>

<h2>Fixed tiny homes and granny flats</h2>
<p>If your tiny home is approved as a building (for example a granny flat), you can usually rent it out. For stays under 3 months:</p>
<ul>
<li>It must be on the state <strong>Short-Term Rental Accommodation (STRA) Register</strong> before you advertise or take bookings, and the registration number must be shown in the ad.</li>
<li>If you live in the main house, it's <strong>hosted</strong> and doesn't need planning approval.</li>
<li>If nobody lives on site (<strong>unhosted</strong>) in Perth, you need planning approval once you rent it for more than <strong>90 nights</strong> in 12 months.</li>
<li>Registration lasts 12 months, and penalties apply for not registering.</li>
</ul>
<p>Read the <a href="/city-of-kwinana-tiny-homes">City of Kwinana tiny home rules</a>, the <a href="/shire-of-mundaring-tiny-homes">Shire of Mundaring rules</a>, or <a href="/wheels-vs-fixed-tiny-home">wheels vs fixed</a>.</p>
"""

FAQS = [
    ("Can I Airbnb a tiny home on wheels in Perth?",
     "Usually not on a normal house lot. A tiny home on wheels is a caravan, and councils such as Mundaring only allow it in an approved caravan park. Ask your council first."),
    ("Do I need to register a tiny home on Airbnb in WA?",
     "If it's approved as a dwelling, such as a granny flat, yes. It must be on the STRA Register before you advertise or take bookings."),
    ("Do I need planning approval to rent out a granny flat as a short stay?",
     "Not if you live in the main house (hosted). If unhosted in Perth, only once you rent it for more than 90 nights in 12 months."),
    ("Can I rent my tiny home long term?",
     "Some councils allow it. Kwinana allows private renting of a tiny home on wheels for more than 3 months with a management plan, as part of its approval."),
]


def page(S):
    return {"path": "rent-out-tiny-home-wa.html", "published": "2026-11-21", "type": "Question answer", "icon": "tiny",
            "card": "Can you rent out a tiny home in WA? Airbnb, caravans, the STRA register and the 90-night rule.",
            "title": "Can I Rent Out a Tiny Home in WA? (Airbnb Rules 2026)",
            "desc": "Renting out a tiny home in WA: why tiny homes on wheels usually can't be an Airbnb on a house lot, the STRA register, hosted vs unhosted, and the 90-night rule in Perth.",
            "eyebrow": "Question answer", "h1": "Can I rent out a tiny home in WA?", "crumb": "Renting out a tiny home",
            "answer": "<p>A tiny home <strong>on wheels</strong> is a caravan, so it usually <strong>can't</strong> be a short-stay rental on a normal house lot without council approval. A <strong>fixed</strong> tiny home approved as a dwelling or granny flat can be, but it must be on the state <strong>STRA Register</strong>, and in Perth an unhosted one needs planning approval past <strong>90 nights</strong> a year.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/city-of-kwinana-tiny-homes", "City of Kwinana tiny homes"), ("/shire-of-mundaring-tiny-homes", "Shire of Mundaring tiny homes"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home")],
            "sources": [("STRA Register FAQs, Government of WA", "https://www.wa.gov.au/organisation/department-of-local-government-industry-regulation-and-safety/short-term-rental-accommodation-register-frequently-asked-questions"),
                        ("Tiny homes, caravans and short-term accommodation, Shire of Bridgetown-Greenbushes", "https://www.bridgetown.wa.gov.au/tiny-homes-caravans-and-short-term-accommodation.aspx"),
                        ("Tiny homes, Shire of Mundaring", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx"),
                        ("Temporary accommodation, City of Kwinana", "https://www.kwinana.wa.gov.au/property-and-pets/building-and-renovating-(residential)/temporary-accommodation")]}
