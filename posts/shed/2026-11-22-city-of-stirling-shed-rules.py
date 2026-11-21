BODY = """
<h2>The two ways to skip planning approval</h2>
<p>The City of Stirling says a shed doesn't need planning approval if it fits <strong>one</strong> of these two groups:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>A. One small shed</th><th>B. Larger or more than one shed</th></tr></thead><tbody>
<tr><td>How many</td><td>Only one shed on the lot</td><td>Any number</td></tr>
<tr><td>Size</td><td>Up to 10 m²</td><td>Up to 60 m² in total, or 10% of the lot, whichever is less</td></tr>
<tr><td>Height</td><td>Walls and ridge up to 2.7 m</td><td>Walls up to 2.4 m, ridge up to 4.2 m</td></tr>
<tr><td>Boundaries</td><td>Can sit on up to two boundaries (600 mm or closer)</td><td>1 m from boundaries, or 1.5 m if a wall is longer than 14 m</td></tr>
<tr><td>Both groups</td><td colspan="2">Not in the front or side street setback area, and the lot keeps its open space and outdoor living area</td></tr>
</tbody></table></div>

<h2>Street setback and open space by R-Code</h2>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Street setback area (no shed)</th><th>Open space</th><th>Outdoor living area</th></tr></thead><tbody>
<tr><td>R10 / R12.5</td><td>7.5 m</td><td>60% / 55%</td><td>No minimum</td></tr>
<tr><td>R20 / R25</td><td>6 m</td><td>50%</td><td>30 m²</td></tr>
<tr><td>R30</td><td>4 m</td><td>45%</td><td>24 m²</td></tr>
<tr><td>R40</td><td>4 m</td><td>45%</td><td>20 m²</td></tr>
<tr><td>R50 / R60</td><td>2 m</td><td>40%</td><td>16 m²</td></tr>
</tbody></table></div>
<p>Look up your R-Code by typing your address into the City's Address and Application Assistant.</p>

<h2>Heritage areas always need approval</h2>
<p>Every shed in the <strong>Mount Lawley, Menora and Inglewood</strong> Heritage Protection Area, or on a heritage-listed property, needs planning approval and must follow the City's character guidelines (LPP 3.1).</p>

<h2>Do you need a building permit?</h2>
<p>Not for a freestanding shed of <strong>10 m² or less</strong> and <strong>2.4 m or less</strong> high (outside cyclone wind regions). Anything bigger needs a building permit.</p>
<p>The City's own example: a 27 m² shed on a 220 m² R40 lot is over 10% of the lot, so it needs both planning approval and a building permit.</p>

<h2>If you need planning approval</h2>
<ul>
<li>An application form signed by every owner, plus the fee.</li>
<li>A certificate of title issued in the last 6 months.</li>
<li>A 1:200 site plan, plus 1:100 floor plans and elevations showing heights and ground levels.</li>
</ul>
<p>You don't need your neighbour's approval to apply. The City has 60 days to decide, but sheds are usually faster. Strata lots may also need strata approval. Call the City on 9205 8555.</p>
<p>Read <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>, <a href="/do-i-need-a-permit-for-a-shed">when a shed needs a permit</a>, or <a href="/shed-site-plan">how to draw a shed site plan</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a shed in Stirling?",
     "Not planning approval if it fits the City's small shed or large shed rules and isn't in a heritage area. A building permit is needed if it's over 10 m² or over 2.4 m high."),
    ("How big can a shed be in Stirling without planning approval?",
     "Up to 60 m² in total, or 10% of your lot, whichever is less, with walls up to 2.4 m and a ridge up to 4.2 m."),
    ("Can I put a shed on the boundary in Stirling?",
     "A single shed up to 10 m² and 2.7 m high can sit on up to two boundaries. Larger sheds need to be 1 m off, or 1.5 m for walls over 14 m long."),
    ("Do I need my neighbour's permission for a shed in Stirling?",
     "No. You don't need your neighbour's approval to lodge a planning application, though the City may ask them for comment."),
]


def page(S):
    return {"path": "city-of-stirling-shed-rules.html", "published": "2026-11-22", "type": "Council guide", "icon": "pin",
            "card": "City of Stirling shed rules: small vs large sheds, boundaries, heritage areas and when a permit is needed.",
            "title": "City of Stirling Shed Rules (2026)",
            "desc": "City of Stirling shed rules: the small and large shed options with no planning approval, setbacks, open space by R-Code, heritage areas and when you need a building permit.",
            "eyebrow": "Council guide", "h1": "City of Stirling shed rules", "crumb": "City of Stirling shed rules",
            "answer": "<p>In Stirling, a shed needs <strong>no planning approval</strong> if it's one shed up to <strong>10 m²</strong>, or sheds totalling up to <strong>60 m²</strong> (or 10% of the lot) with 2.4 m walls set 1 m off the boundary. Heritage areas always need approval. A <strong>building permit</strong> is needed over 10 m² or 2.4 m high.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Outbuildings information sheet, City of Stirling", "https://www.stirling.wa.gov.au/awcontent/Web/Documents/Outbuilding-Information-Sheet-July-2021.pdf"),
                        ("Where do I start?, City of Stirling", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/where-do-i-start"),
                        ("Residential Design Codes Volume 1, WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
