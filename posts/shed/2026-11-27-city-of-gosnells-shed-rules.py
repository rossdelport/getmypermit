BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes, unless the shed is <strong>freestanding</strong>, <strong>10 m² or less</strong> and <strong>2.4 m or lower</strong>. A garage follows the same rule in Gosnells. Exempt sheds must still meet the building code and the R-Codes.</p>

<h2>Size and height</h2>
<div class="table-wrap"><table>
<thead><tr><th>Limit</th><th>Rule</th></tr></thead><tbody>
<tr><td>Wall height</td><td>2.4 m</td></tr>
<tr><td>Roof height</td><td>4.2 m</td></tr>
<tr><td>Total area of all sheds</td><td>60 m² or 10% of the lot, whichever is less</td></tr>
</tbody></table></div>
<p>So on a 450 m² lot, the most you can have is 45 m² of sheds in total. Bigger sheds can be considered with a development application under the City's Local Planning Policy 2.2 (Outbuildings and Sea Containers). Check with the <a href="/shed-size-checker">shed size checker</a>.</p>

<h2>Setbacks</h2>
<div class="table-wrap"><table>
<thead><tr><th>Boundary</th><th>Minimum setback</th></tr></thead><tbody>
<tr><td>Side and rear, walls up to 9 m long</td><td>1 m</td></tr>
<tr><td>Side and rear, walls over 9 m long</td><td>1.5 m</td></tr>
<tr><td>Secondary street</td><td>1.5 m</td></tr>
</tbody></table></div>
<p>A smaller setback can be considered with a development application, the fee and comments from your neighbours. <strong>Easements can't be built over.</strong> If there's a 2 m easement across the back, the shed must be at least 2 m from the rear boundary. See <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>

<h2>What to send</h2>
<ul>
<li>A BA2 form and the fees.</li>
<li>A site plan at 1:200 or better with street names, lot and house numbers, lot size, the shed's size and position, and setbacks to all boundaries.</li>
<li>At least one elevation at 1:100 or better.</li>
<li>Structural details: beams, purlins, columns, connections, footings, slab thickness and roof sheeting.</li>
<li>At least 2 m head clearance from the paving to the underside of the main beam.</li>
</ul>
<p>See <a href="/shed-site-plan">shed site plans</a>. Call Building Services on 9397 3000.</p>
"""

FAQS = [
    ("What size shed can I build without a permit in Gosnells?",
     "A freestanding shed of 10 m² or less and no more than 2.4 m high."),
    ("How big can a shed be in the City of Gosnells?",
     "All sheds on a lot together can't exceed 60 m² or 10% of the lot area, whichever is less, unless approved through a development application."),
    ("How far from the fence does a shed need to be in Gosnells?",
     "At least 1 m from side and rear boundaries for walls up to 9 m long, 1.5 m for longer walls, and 1.5 m from a secondary street."),
    ("Can I build a shed over an easement in Gosnells?",
     "No. Setbacks set by easements can't be varied, so the shed must stay clear of the easement."),
]


def page(S):
    return {"path": "city-of-gosnells-shed-rules.html", "published": "2026-11-27", "type": "Council guide", "icon": "pin",
            "card": "City of Gosnells shed rules: the 60 m² or 10% limit, 1 m setbacks, easements and what to send.",
            "title": "City of Gosnells Shed Rules (2026)",
            "desc": "City of Gosnells shed rules: when you need a building permit, the 60 m² or 10% area limit, 2.4 m walls and 4.2 m roof, side and rear setbacks, easements and what to send with your BA2.",
            "eyebrow": "Council guide", "h1": "City of Gosnells shed rules", "crumb": "Gosnells shed rules",
            "answer": "<p>In the City of Gosnells, a shed needs a <strong>building permit</strong> unless it's freestanding, 10 m² or less and 2.4 m or lower. All sheds together are capped at <strong>60 m² or 10%</strong> of the lot, whichever is less, with <strong>2.4 m</strong> walls and a <strong>4.2 m</strong> roof. Keep at least <strong>1 m</strong> from side and rear boundaries.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Shed/garage on residential properties (version 26/03/2026), City of Gosnells", "https://www.gosnells.wa.gov.au/files/assets/public/v/3/documents/ecm/9148508.pdf")]}
