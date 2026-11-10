BODY = """
<h2>Approvals you need</h2>
<p>The City of Wanneroo says a <strong>building permit is always required</strong> for a granny flat (ancillary dwelling). Planning approval <strong>may</strong> be needed too. If it is, it must be granted before the building permit is issued.</p>
<p>Under the state R-Codes, a granny flat on a residential lot doesn't need planning approval if it meets all the deemed-to-comply rules, including:</p>
<ul>
<li>No more than <strong>70 m²</strong> internal floor area</li>
<li>Behind the street setback line</li>
<li>Parking: one extra bay on most house lots, unless you're close to a frequent train or bus service</li>
<li>Leaves the house enough open space and outdoor living area</li>
<li>Meets the other R-Codes rules for single houses, such as setbacks and privacy</li>
</ul>

<h2>Wanneroo's own policy: bigger flats on big lots</h2>
<p>Wanneroo has a Local Planning Policy for granny flats (LPP 2.6). Its main extra is size:</p>
<div class="table-wrap"><table>
<thead><tr><th>Lot</th><th>Size the City may consider</th></tr></thead><tbody>
<tr><td>Most residential lots</td><td>Up to 70 m² (the R-Codes limit)</td></tr>
<tr><td>Lots over 4,000 m²</td><td>Up to <strong>100 m²</strong>, if it stays subsidiary to the main house</td></tr>
<tr><td>Lots over 4,000 m² with special needs</td><td>Up to <strong>110 m²</strong> where residents have accessibility or medical needs and it's built to the Liveable Housing Design Guidelines "Silver Level"</td></tr>
</tbody></table></div>
<p>Anything over 70 m² isn't deemed-to-comply, so it goes through planning approval. The policy says the larger size helps interpret the R-Codes' design principles; it doesn't change the 70 m² deemed-to-comply rule.</p>

<h2>Rural and other non-R-Code land</h2>
<p>Where the R-Codes don't apply, such as some rural zones, Wanneroo's policy says:</p>
<ul>
<li>The granny flat must go with a single house that exists or is built at the same time</li>
<li>Only <strong>one</strong> granny flat per lot</li>
<li>Materials, colours and bulk shouldn't spoil the street or neighbours' outlook</li>
</ul>

<h2>What counts as a granny flat</h2>
<p>The policy says a granny flat is self-contained: it should have a bathroom, toilet, kitchen and laundry. It can be detached, attached, or built into the house. Games rooms, sleep-outs and pool rooms that can't be lived in separately aren't granny flats.</p>

<h2>How to apply</h2>
<p>Wanneroo prefers online lodgement. Use its Certified (BA1) or Uncertified (BA2) residential building checklist, and its DA Checklist if you need planning approval. Already built without approval? The City has a separate Unauthorised Works checklist. Call 9405 5000 with questions.</p>
<p>Read the full <a href="/granny-flat-rules-wa">granny flat rules in WA</a>, check <a href="/granny-flat-parking">granny flat parking</a>, or compare with the <a href="/city-of-joondalup-granny-flat-rules">City of Joondalup granny flat rules</a>.</p>
"""

FAQS = [
    ("Do I need approval for a granny flat in Wanneroo?",
     "A building permit is always required. Planning approval is only needed if the granny flat doesn't meet all the R-Codes deemed-to-comply rules, such as the 70 m² limit."),
    ("How big can a granny flat be in Wanneroo?",
     "70 m² on most lots. On lots over 4,000 m², the City's policy lets it consider up to 100 m², or 110 m² for residents with accessibility or medical needs. Over 70 m² needs planning approval."),
    ("Can I have two granny flats in Wanneroo?",
     "Usually no. Wanneroo's policy allows only one granny flat per lot where the R-Codes don't apply. Under the R-Codes, a granny flat goes with one house, and the higher-density rules allow one per site."),
    ("Does a Wanneroo granny flat need a laundry?",
     "The City's policy says a self-contained granny flat should include a bathroom, toilet, kitchen and laundry."),
]


def page(S):
    return {"path": "city-of-wanneroo-granny-flat-rules.html", "published": "2026-11-11", "type": "Council guide", "icon": "pin",
            "card": "Permits, the 70 m² rule, Wanneroo's 100 m² option on big lots, and how to apply.",
            "title": "City of Wanneroo Granny Flat Rules (2026)",
            "desc": "City of Wanneroo granny flat rules: building permit always needed, 70 m² deemed-to-comply, up to 100 m² on lots over 4,000 m² under LPP 2.6, and how to apply.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo granny flat rules", "crumb": "City of Wanneroo granny flat rules",
            "answer": "<p>In Wanneroo a granny flat <strong>always needs a building permit</strong>. It skips planning approval if it meets the R-Codes, including the <strong>70 m²</strong> limit. On lots over <strong>4,000 m²</strong>, the City's policy lets it consider up to <strong>100 m²</strong>, through planning approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-parking", "Granny flat parking"), ("/city-of-joondalup-granny-flat-rules", "City of Joondalup granny flat rules")],
            "sources": [("What approvals do I need? Ancillary dwelling (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/directory_record/111/ancillary_accommodation_granny_flat"),
                        ("Local Planning Policy 2.6 Ancillary Accommodation (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/100/ancillary_accommodation_-_lpp_26.pdf"),
                        ("State Planning Policy 7.3 R-Codes Volume 1, April 2026 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
