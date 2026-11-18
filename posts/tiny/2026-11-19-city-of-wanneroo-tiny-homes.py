BODY = """
<h2>Tiny homes on wheels: Wanneroo is strict</h2>
<p>Under WA law, councils can approve someone living in a caravan or tiny home on wheels on private land for up to 24 months. The City of Wanneroo sets much tighter limits in its Temporary Camping Guideline:</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>City of Wanneroo</th></tr></thead><tbody>
<tr><td>How long</td><td>Up to <strong>3 months</strong> in any 12 months</td></tr>
<tr><td>Who can stay</td><td>Only <strong>family members</strong> of the property owner</td></tr>
<tr><td>Owner</td><td>Must live in the house on the property at the same time</td></tr>
<tr><td>Type</td><td>A registered, roadworthy caravan or vehicle with its own toilet, shower and cooking</td></tr>
<tr><td>Vacant residential land</td><td>Usually not approved</td></tr>
</tbody></table></div>

<h2>Conditions</h2>
<ul>
<li>Connected to drinking water.</li>
<li>Toilet waste emptied into a toilet or sewer, and grey water into sewer or a proper system, safely.</li>
<li>A smoke alarm, fire blanket and dry powder fire extinguisher inside.</li>
<li>Parked on a hard surface inside your boundaries, meeting the City's setbacks.</li>
<li><strong>No generators</strong> for power, and noise rules apply.</li>
</ul>
<p>The City can cancel approval if the rules aren't followed. Apply to the City's Health Services using the online temporary camping licence form.</p>

<h2>Living in it while you build</h2>
<p>On <strong>Rural, Rural Resource, Rural Residential and Landscape Enhancement</strong> land, the owner and close family can live on site for <strong>12 months</strong> while building a house. You need the house's approvals first, the slab must be down, and wastewater approval must be in place. The time can be extended if the house is nearly finished.</p>

<h2>Want to stay longer?</h2>
<p>For permanent living, a tiny home usually has to be approved as a building, such as a granny flat, with a building permit. In a case reported by the ABC in October 2025, the City treated a tiny home in a front yard as an ancillary dwelling (granny flat) rather than a tiny home on wheels. Ask the City early. Councils vary a lot on tiny homes.</p>
<p>Read the <a href="/tiny-home-on-wheels-rules-wa">WA tiny home on wheels rules</a>, about <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a>, or the <a href="/fixed-tiny-home-permit">fixed tiny home permit</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in the City of Wanneroo?",
     "Only short term. Wanneroo approves up to 3 months in any 12 months, for family members of the owner, while the owner lives in the house."),
    ("Can I rent out a tiny home on wheels in Wanneroo?",
     "No. Wanneroo's temporary camping approval is only for family members of the property owner."),
    ("Can I live in a caravan while building a house in Wanneroo?",
     "On rural-type zones, yes, for 12 months once the house is approved and the slab is down. It can be extended if the house is nearly finished."),
    ("How do I keep a tiny home in Wanneroo long term?",
     "You'd usually need it approved as a building, such as a granny flat, with a building permit. Ask the City first."),
]


def page(S):
    return {"path": "city-of-wanneroo-tiny-homes.html", "published": "2026-11-19", "type": "Council guide", "icon": "pin",
            "card": "City of Wanneroo tiny home rules: 3 months in 12, family only, and living on site while you build.",
            "title": "City of Wanneroo Tiny Home Rules (2026)",
            "desc": "City of Wanneroo tiny home on wheels rules: up to 3 months in 12, family members only, conditions, living on rural land while building, and long-term options.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo tiny home rules", "crumb": "City of Wanneroo tiny homes",
            "answer": "<p>The City of Wanneroo only approves living in a tiny home on wheels for up to <strong>3 months in any 12 months</strong>, for <strong>family members</strong> of the owner, while the owner lives in the house. On rural-type land you can live on site for <strong>12 months</strong> while building a house. Long term, a tiny home usually needs approval as a building.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules WA"), ("/live-in-caravan-on-own-land-wa", "Live in a caravan on your land"), ("/fixed-tiny-home-permit", "Fixed tiny home permit")],
            "sources": [("Temporary camping, City of Wanneroo", "https://www.wanneroo.wa.gov.au/community-and-safety/public-health/temporary-camping"),
                        ("Tiny home dream shattered as council orders removal, ABC News (26 Oct 2025)", "https://www.abc.net.au/news/2025-10-26/tiny-home-dream-shattered-for-woman-with-epilepsy-by-council/105922162"),
                        ("Tiny House Fact Sheet, Government of Western Australia", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf")]}
