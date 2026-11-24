BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes, unless the shed is <strong>freestanding</strong>, <strong>10 m² or less</strong> and <strong>2.4 m or lower</strong>. Even small exempt sheds must still meet the building rules, local laws and planning policies.</p>
<p>Planning approval isn't needed if the shed meets the R-Codes deemed-to-comply rules.</p>

<h2>Size and height</h2>
<p>The City's outbuildings policy (LP.01) sets the limits by lot size. For example, on lots up to <strong>600 m²</strong>:</p>
<div class="table-wrap"><table>
<thead><tr><th>Limit</th><th>Lots up to 600 m²</th></tr></thead><tbody>
<tr><td>Floor area</td><td>Up to 10% of the site</td></tr>
<tr><td>Wall height</td><td>2.4 m</td></tr>
<tr><td>Ridge height</td><td>4.2 m</td></tr>
</tbody></table></div>
<p>Bigger lots get bigger limits. Check the policy for your lot size. Check yours with the <a href="/shed-size-checker">shed size checker</a>.</p>

<h2>Where it can go</h2>
<ul>
<li><strong>Not in the front yard.</strong> It must sit behind the R-Codes front setback.</li>
<li><strong>Corner lots:</strong> at least 1.5 m from the secondary street.</li>
<li><strong>On the boundary:</strong> a nil setback may be allowed to up to two boundaries, if stormwater stays on your lot and the total boundary wall length meets the City's policy and the R-Codes.</li>
<li><strong>Open space:</strong> you must keep the R-Codes minimum open space.</li>
<li><strong>Fire separation:</strong> the building code's fire separation rules apply and must be shown in your application.</li>
</ul>
<p>Check drainage easements with the City's Engineering Services first.</p>

<h2>What to send</h2>
<ul>
<li><strong>BA1:</strong> a Certificate of Design Compliance and the plans it lists. Decided within 10 working days.</li>
<li><strong>BA2:</strong> a 1:200 site plan with boundaries, other buildings and floor level, 1:100 floor plans and elevations, and structural details. Decided within 25 working days.</li>
</ul>
<p>Owner-builders can build sheds. A shed worth over $20,000 needs owner-builder approval or a registered builder under the City's sheet. Building Services is on 1300 422 664. See <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a> and <a href="/shed-site-plan">shed site plans</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in the City of Canning?",
     "Yes, unless it's freestanding, 10 m² or less and no more than 2.4 m high."),
    ("How big can a shed be in Canning?",
     "It depends on lot size. On lots up to 600 m², up to 10% of the site, with 2.4 m walls and a 4.2 m ridge."),
    ("Can a shed go on the boundary in Canning?",
     "Often yes, on up to two boundaries, if stormwater stays on your lot and the boundary walls meet the City's policy and the R-Codes."),
    ("Can I put a shed in my front yard in Canning?",
     "No. Sheds must sit behind the R-Codes front setback."),
]


def page(S):
    return {"path": "city-of-canning-shed-rules.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "City of Canning shed rules: the 10% size limit, heights, boundary walls and what to send.",
            "title": "City of Canning Shed Rules (2026)",
            "desc": "City of Canning shed rules: when you need a building permit, size and height limits by lot size, front and corner setbacks, building on the boundary, and what to send with a BA1 or BA2.",
            "eyebrow": "Council guide", "h1": "City of Canning shed rules", "crumb": "Canning shed rules",
            "answer": "<p>In the City of Canning, a shed needs a <strong>building permit</strong> unless it's freestanding, 10 m² or less and 2.4 m or lower. On lots up to 600 m², a shed can cover up to <strong>10%</strong> of the site with <strong>2.4 m</strong> walls and a <strong>4.2 m</strong> ridge. It can't go in the front yard.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-size-checker", "Shed size checker"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Building information sheet: sheds and outbuildings (BIS-06), City of Canning", "https://cdn.canning.wa.gov.au/media/05upmym1/bis-06-information-sheet-sheds-and-outbuildings.pdf")]}
