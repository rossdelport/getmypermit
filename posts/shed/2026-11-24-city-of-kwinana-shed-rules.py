BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes, if the shed is over <strong>10 m²</strong> or over <strong>2.4 m</strong> high. A freestanding shed that's 10 m² or less and 2.4 m or lower doesn't need one. The City notes that most sheds and other outbuildings will need a building permit, planning approval, or both.</p>

<h2>Setbacks</h2>
<p>For a shed with walls up to <strong>2.7 m</strong> high and no longer than <strong>9 m</strong>:</p>
<div class="table-wrap"><table>
<thead><tr><th>Boundary</th><th>Usual setback</th><th>Can it be less?</th></tr></thead><tbody>
<tr><td>Side and rear</td><td>1 m</td><td>Yes, if it doesn't affect next door. You'll need your neighbour's comments in writing</td></tr>
<tr><td>Secondary street (corner lots)</td><td>1.5 m</td><td>Yes, if it doesn't affect next door or the street. Neighbour comments needed</td></tr>
</tbody></table></div>
<p>If a neighbour objects, Building Services will look at whether the objection is valid. Sheds usually go beside or behind the house. Bigger or taller sheds, different ground levels and R-Code rules can change these numbers, so councils vary even within the same suburb.</p>

<h2>Other rules</h2>
<ul>
<li>All stormwater must be kept on your own lot.</li>
<li>If the shed needs planning approval, get it before you lodge the building permit.</li>
</ul>

<h2>How to apply</h2>
<p>Apply online through Kwinana Connect under "Planning, Building, Health Applications". Send a BA1 (certified by a private building surveyor, 10 business days) or a BA2 (checked by the City, 25 business days), with a site plan, shed plans and engineering. Call Building Services on (08) 9439 0208 if you're not sure.</p>
<p>See <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>, <a href="/garden-shed-approval">garden shed approval</a> and <a href="/shed-site-plan">drawing a shed site plan</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in Kwinana?",
     "Yes, if it's over 10 m² or over 2.4 m high. Smaller freestanding sheds don't need a building permit."),
    ("How close to the fence can a shed be in Kwinana?",
     "Usually 1 m from side and rear boundaries, and 1.5 m from a secondary street, for walls up to 2.7 m high and 9 m long. It can be less with your neighbour's written comments."),
    ("How do I apply for a shed permit in Kwinana?",
     "Online through Kwinana Connect, using a BA1 or BA2 form with your site plan and shed plans."),
    ("Does a shed need planning approval in Kwinana?",
     "Sometimes. Many outbuildings need planning approval as well as a building permit, so check with the City before you lodge."),
]


def page(S):
    return {"path": "city-of-kwinana-shed-rules.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Kwinana shed rules: the 10 m² limit, 1 m setbacks, neighbour comments and how to apply.",
            "title": "City of Kwinana Shed Rules (2026)",
            "desc": "City of Kwinana shed rules: when you need a building permit, side, rear and corner setbacks, reducing setbacks with neighbour comments, stormwater and applying through Kwinana Connect.",
            "eyebrow": "Council guide", "h1": "City of Kwinana shed rules", "crumb": "Kwinana shed rules",
            "answer": "<p>In the City of Kwinana, a shed needs a <strong>building permit</strong> if it's over <strong>10 m²</strong> or <strong>2.4 m</strong> high. Sheds with walls up to 2.7 m and 9 m long usually sit <strong>1 m</strong> from side and rear boundaries (1.5 m from a secondary street), or closer with your neighbour's written comments.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/garden-shed-approval", "Garden shed approval"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Sheds, patios, pergolas and shade sails building permits, City of Kwinana", "https://www.kwinana.wa.gov.au/property-and-pets/building-and-renovating-(residential)/sheds,-patios,-pergolas-and-shade-sails"),
                        ("Building information note: sheds and other Class 10a structures, City of Kwinana", "https://www.kwinana.wa.gov.au/council/documents,-publications-and-forms/publications-and-forms-(all)/information-sheets-and-guides/2020/building-information-note-sheds-and-other-bca-clas")]}
