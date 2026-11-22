BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes, for almost every carport. A <strong>freestanding</strong> carport only skips the permit if it's <strong>10 m² or less</strong> and <strong>2.4 m or lower</strong>, which is too small for a car. Any carport <strong>attached</strong> to the house or another structure needs a permit, whatever its size.</p>

<h2>Setbacks in residential zones</h2>
<div class="table-wrap"><table>
<thead><tr><th>Where</th><th>Usual setback</th></tr></thead><tbody>
<tr><td>Side or rear boundary, carport under 9 m long</td><td>1 m</td></tr>
<tr><td>Side or rear boundary, carport over 9 m long</td><td>1.5 m</td></tr>
<tr><td>Secondary street (corner lots)</td><td>1.5 m, any length</td></tr>
<tr><td>Front, carport at right angles to the street</td><td>3 m or 2 m, depending on zoning</td></tr>
</tbody></table></div>
<p>These are the City's general guide. Your lot's zoning and R-Code can change them, so check your density with Planning Services on (08) 9231 0606 or on the City's map.</p>

<h2>Planning approval</h2>
<p>Not needed for most homes if the carport meets every "deemed-to-comply" rule in the R-Codes. If you're not sure, the City offers a <strong>deemed-to-comply check</strong> before you lodge. To go closer than the rules allow, you apply for development approval with good reasons. Neighbours may be asked. Carports on non-residential land always need planning approval.</p>

<h2>What to send</h2>
<ul>
<li><strong>BA1 (certified):</strong> a Certificate of Design Compliance from a registered building surveyor and the plans it lists. The City decides within <strong>10 working days</strong>.</li>
<li><strong>BA2 (uncertified):</strong> a site plan at 1:200 showing boundaries, other buildings and floor level against the house, floor plans and elevations at 1:100, and structural details. The City decides within <strong>25 working days</strong>.</li>
</ul>
<p>The City says carport designs need a structural engineer's sign-off. Both the builder and all owners sign the form. If the City asks for more information, you get 21 days to send it. Check drainage easements with the City and Water Corporation first.</p>
<p>See <a href="/carport-in-front-setback">carports in the front setback</a>, <a href="/carport-corner-block">corner block carports</a> and <a href="/carport-site-plan">carport site plans</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in the City of Canning?",
     "Yes, unless it's freestanding, 10 m² or less and no more than 2.4 m high. Every attached carport needs a permit."),
    ("How close to the boundary can a carport be in Canning?",
     "Usually 1 m from a side or rear boundary if it's under 9 m long, and 1.5 m if it's longer or on a secondary street. Your zoning can change this."),
    ("Does a carport need planning approval in Canning?",
     "Not if it meets all the R-Codes deemed-to-comply rules. The City can check this for you before you lodge."),
    ("How long does Canning take to approve a carport?",
     "10 working days for a certified (BA1) application and 25 working days for an uncertified (BA2) one."),
]


def page(S):
    return {"path": "city-of-canning-carport-rules.html", "published": "2026-11-23", "type": "Council guide", "icon": "pin",
            "card": "City of Canning carport rules: permits, setbacks, the deemed-to-comply check and what to send.",
            "title": "City of Canning Carport Rules (2026)",
            "desc": "City of Canning carport rules: when you need a building permit, side, rear and front setbacks, planning approval and the deemed-to-comply check, plus what to send with a BA1 or BA2.",
            "eyebrow": "Council guide", "h1": "City of Canning carport rules", "crumb": "Canning carport rules",
            "answer": "<p>In the City of Canning almost every carport needs a <strong>building permit</strong>. Only tiny freestanding ones (10 m² or less, 2.4 m or lower) are exempt. In residential zones carports usually sit <strong>1 m</strong> from side and rear boundaries (1.5 m if over 9 m long). Planning approval isn't needed if it meets the R-Codes.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-in-front-setback", "Carport in the front setback"), ("/carport-corner-block", "Carport on a corner block"), ("/carport-site-plan", "Carport site plan")],
            "sources": [("Building information sheet: carport (BIS-24), City of Canning", "https://cdn.canning.wa.gov.au/media/fzegvbl5/bis-24-information-sheet-carport-update.pdf"),
                        ("Building Services, City of Canning", "https://www.canning.wa.gov.au/plan-and-build/building-services/")]}
