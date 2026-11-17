BODY = """
<h2>How long you can stay</h2>
<p>Since <strong>1 September 2024</strong>, the City of Kwinana treats a tiny home on wheels like a caravan. What you need depends on how long someone lives in it:</p>
<div class="table-wrap"><table>
<thead><tr><th>Stay</th><th>What you need</th></tr></thead><tbody>
<tr><td>Up to 5 nights</td><td>The landowner's OK only</td></tr>
<tr><td>More than 5 nights, up to 24 months</td><td>The landowner's OK and approval from the City</td></tr>
<tr><td>Longer than 24 months</td><td>Apply to the City again</td></tr>
</tbody></table></div>
<p>It works on land in any zone except commercial and industrial, and it doesn't change your rates.</p>

<h2>The main rules</h2>
<ul>
<li><strong>Only one</strong> caravan or tiny home on wheels per property. More than one counts as a caravan park.</li>
<li>It must stay on its trailer, be towable and be licensed for the road.</li>
<li>At least <strong>900 mm</strong> from the boundary with any neighbouring lot and <strong>1.8 m</strong> from the house.</li>
<li>In residential zones, place it at the back if it's easy to get to, or at least <strong>2 m</strong> from the front boundary. Not on the verge and not blocking parking.</li>
<li>A smoke alarm and an RCD (safety switch) are needed.</li>
<li>Easy access to power, drinking water, hot water, a flushing toilet, shower, basin, kitchen sink, stove, laundry and a washing line. These can be in the main house. Wastewater must go to sewer or an approved septic or treatment system.</li>
<li>One extra parking bay, and no more than 6 unrelated people living on the property.</li>
<li>In bushfire-prone areas, keep <strong>3 m</strong> of cleared space around it.</li>
<li>No short-stay letting such as Airbnb. Private renting for more than 3 months is allowed with a management plan.</li>
</ul>

<h2>How to apply</h2>
<p>Apply to the City's <strong>Environmental Health</strong> team with the documents it lists, such as a site plan showing setbacks, proof you can use the land, and proof of the smoke alarm and RCD. The City aims to decide within <strong>14 business days</strong>. If approved for more than 12 months, expect an inspection after 12 months. The City can cancel the approval if the rules aren't followed. Call the City on (08) 9439 0250 to check your lot.</p>
<p>Read the <a href="/tiny-home-on-wheels-rules-wa">WA tiny home on wheels rules</a>, what <a href="/tiny-home-services">services a tiny home needs</a>, or whether you can have <a href="/more-than-one-tiny-home">more than one tiny home</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in the City of Kwinana?",
     "Yes, with the landowner's OK and the City's approval for stays over 5 nights. Approval lasts up to 24 months, then you re-apply."),
    ("How many tiny homes can I have on my property in Kwinana?",
     "One. More than one caravan or tiny home on wheels counts as a caravan park."),
    ("Can I rent out a tiny home on wheels in Kwinana?",
     "Not as short-stay or Airbnb. Private renting for more than 3 months is allowed with a management plan."),
    ("How close to the boundary can a tiny home be in Kwinana?",
     "At least 900 mm from the boundary with any neighbouring lot and 1.8 m from the house."),
]


def page(S):
    return {"path": "city-of-kwinana-tiny-homes.html", "published": "2026-11-18", "type": "Council guide", "icon": "pin",
            "card": "City of Kwinana tiny home on wheels rules: stay limits, setbacks, services and how to apply.",
            "title": "City of Kwinana Tiny Home Rules (2026)",
            "desc": "City of Kwinana tiny home on wheels rules: 5 nights with owner's OK, up to 24 months with City approval, one per lot, 900 mm setbacks, services and how to apply.",
            "eyebrow": "Council guide", "h1": "City of Kwinana tiny home rules", "crumb": "City of Kwinana tiny homes",
            "answer": "<p>In Kwinana, someone can stay in a tiny home on wheels for up to <strong>5 nights</strong> with the landowner's OK. For longer, up to <strong>24 months</strong>, you also need the City's approval. Only <strong>one</strong> is allowed per property, it must stay on its trailer, and it needs proper services and <strong>900 mm</strong> boundary setbacks.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules WA"), ("/tiny-home-services", "Tiny home services"), ("/more-than-one-tiny-home", "More than one tiny home")],
            "sources": [("Temporary accommodation, City of Kwinana", "https://www.kwinana.wa.gov.au/property-and-pets/building-and-renovating-(residential)/temporary-accommodation"),
                        ("FAQs: temporary accommodation, City of Kwinana", "https://www.kwinana.wa.gov.au/council/documents,-publications-and-forms/publications-and-forms-(all)/information-sheets-and-guides/2024/faqs-%E2%80%93-temporary-accommodation")]}
