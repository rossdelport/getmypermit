BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes, unless the shed is freestanding, <strong>under 10 m²</strong> and <strong>2.4 m or lower</strong>, and it meets the setback rules. Only <strong>one</strong> small exempt shed is allowed per lot. A garage <strong>always</strong> needs a building permit.</p>
<p>Planning approval may not be needed, depending on your zoning, site cover, the shed's size and height, and any special conditions. Ask a City planning officer to confirm.</p>

<h2>How big can it be?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Lot size</th><th>Total shed area allowed</th></tr></thead><tbody>
<tr><td>Under 600 m²</td><td>Up to 10% of the lot (500 m² lot = 50 m²)</td></tr>
<tr><td>Over 600 m²</td><td>60 m², plus 2.5 m² for every 100 m² over 600 m² (800 m² lot = 65 m²)</td></tr>
</tbody></table></div>
<p>The limit is the <strong>combined</strong> area of all sheds and outbuildings on the lot. Try the <a href="/shed-size-checker">shed size checker</a>.</p>

<h2>Height</h2>
<ul>
<li>Walls: generally up to <strong>3.0 m</strong>.</li>
<li>Walls in zincalume, unpainted fibre cement or similar: up to <strong>2.4 m</strong>.</li>
<li>Roof: generally up to <strong>4.2 m</strong>.</li>
</ul>

<h2>Setbacks and other rules</h2>
<p>Setbacks come from the City's planning scheme, the R-Codes, local planning policies and any detailed area plan. Different density zones can have different setbacks, and some zones also need minimum open space. Check your zoning on the City's online map, and confirm setbacks with Building Services. See <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>
<ul>
<li>Sheds generally aren't allowed on <strong>vacant</strong> residential lots.</li>
<li>Bigger sheds or reduced setbacks usually need a development application and neighbour consultation, approved <strong>before</strong> the building permit.</li>
</ul>

<h2>What to send</h2>
<ul>
<li>A BA1 (with a Certificate of Design Compliance) or BA2 form.</li>
<li>A site plan at 1:200 or better, with setbacks to boundaries and all buildings, pools and retaining walls, and ground levels.</li>
<li>Floor plan, section and elevations at 1:100 or better.</li>
<li>Construction details and how the shed is anchored, such as footings. See <a href="/shed-site-plan">shed site plans</a>.</li>
</ul>
<p>Lodge online via "Building Lodgements" on the City's website. Building Services is on 9550 3777.</p>
"""

FAQS = [
    ("What size shed can I build without a permit in Mandurah?",
     "A freestanding shed under 10 m² and no more than 2.4 m high, that meets the setbacks. Only one is allowed per lot."),
    ("How big can a shed be in Mandurah?",
     "On lots under 600 m², up to 10% of the lot. On bigger lots, 60 m² plus 2.5 m² for every 100 m² over 600 m², counting all sheds together."),
    ("How high can a shed be in Mandurah?",
     "Walls generally up to 3.0 m, or 2.4 m if finished in zincalume or unpainted fibre cement. The roof is generally limited to 4.2 m."),
    ("Can I put a shed on a vacant block in Mandurah?",
     "Generally not. The City says sheds are generally not permitted on vacant residential lots."),
]


def page(S):
    return {"path": "city-of-mandurah-shed-rules.html", "published": "2026-11-26", "type": "Council guide", "icon": "pin",
            "card": "City of Mandurah shed rules: the permit-free size, the lot-size formula, wall heights and what to send.",
            "title": "City of Mandurah Shed Rules (2026)",
            "desc": "City of Mandurah shed rules: when you need a building permit, the one-exempt-shed rule, maximum shed area by lot size, wall and roof heights, vacant lots and what to send.",
            "eyebrow": "Council guide", "h1": "City of Mandurah shed rules", "crumb": "Mandurah shed rules",
            "answer": "<p>In the City of Mandurah, a shed needs a <strong>building permit</strong> unless it's freestanding, under 10 m² and 2.4 m or lower (one per lot). Total shed area is capped at <strong>10%</strong> of lots under 600 m², or <strong>60 m² plus 2.5 m² per extra 100 m²</strong> on bigger lots. Walls are generally limited to 3.0 m.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Sheds, free standing garages and outbuildings information sheet (2026-03), City of Mandurah", "https://www.mandurah.wa.gov.au/getContentAsset/e65afc06-4ab1-4822-8d73-3bf9e23779ed/8c05e2a8-714e-41ec-a13c-ec89cb576508/Sheds%20and%20Garages%20Information%20Sheet.pdf?language=en"),
                        ("Do I need approval?, City of Mandurah", "https://www.mandurah.wa.gov.au/my-home-property-and-rates/building-and-improving-your-home/do-i-need-approval")]}
