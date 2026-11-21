BODY = """
<h2>When you don't need planning approval</h2>
<p>For a house or grouped dwelling, the City of Joondalup says you generally don't need planning approval if the carport:</p>
<ul>
<li>keeps a clear view between the house and the street;</li>
<li>matches the house in materials, roof design, roof pitch and colour;</li>
<li>is no wider than <strong>60%</strong> of the lot frontage;</li>
<li>meets the street setback, side setback and open space for your R-Code; and</li>
<li>leaves at least half the front setback area landscaped if you add a driveway.</li>
</ul>
<p>Carports for apartments, multiple dwellings or commercial sites always need planning approval.</p>

<h2>Setbacks on an R20 lot</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Carport</th></tr></thead><tbody>
<tr><td>Front street setback</td><td>3 m, with all buildings averaging 6 m</td></tr>
<tr><td>Side street (corner lot)</td><td>1.5 m</td></tr>
<tr><td>Side or rear boundary, 10 to 14 m long</td><td>1 m</td></tr>
<tr><td>Side or rear boundary, over 14 m long</td><td>1.5 m</td></tr>
<tr><td>Open space kept</td><td>50% of the lot</td></tr>
<tr><td>Driveway width at the street</td><td>6 m for one, 9 m total for two (at least 0.5 m apart)</td></tr>
</tbody></table></div>
<p>The length counts the carport plus anything attached to it. Under the R-Codes, posts can usually go on the side boundary if the carport is no more than 10 m long and 2.7 m high, behind the street setback, with the roof and gutters at least 450 mm off the boundary.</p>
<p>Dual-coded lots developed at the higher code (R20/25 up to R20/60) use a <strong>5.5 m</strong> front setback for parking and 1 to 1.5 m to a side street. Check your R-Code on the City's online map.</p>

<h2>Building permit</h2>
<p>A building permit is <strong>always</strong> needed for a carport in Joondalup. You can lodge a BA1 with a building surveyor's certificate (BA3), or a BA2 with the City's outbuilding checklist.</p>

<h2>Turning it into a room later?</h2>
<p>Enclosing a carport into a room needs a building permit, 2.4 m ceilings, hardwired smoke alarms, moisture and termite protection, and the meter box moved outside. It needs planning approval if it doesn't match the house, has a window within 1.5 m of the boundary, or leaves fewer than the required parking bays (usually two).</p>
<p>Read the <a href="/carport-in-front-setback">front setback rules</a>, <a href="/carport-on-boundary">carports on the boundary</a>, or <a href="/enclose-a-carport">enclosing a carport</a>. Call the City on 9400 4000.</p>
"""

FAQS = [
    ("Do I need council approval for a carport in Joondalup?",
     "You always need a building permit. You usually don't need planning approval if it meets the setbacks, matches the house and is no wider than 60% of the frontage."),
    ("How close to the street can a carport be in Joondalup?",
     "On an R20 lot, 3 m from the front boundary, as long as all buildings average 6 m. On a corner, 1.5 m from the side street."),
    ("Can I build a carport on the boundary in Joondalup?",
     "Usually the posts can go on the side boundary if it's no more than 10 m long and 2.7 m high, behind the street setback, with the roof 450 mm off."),
    ("Do carports on strata lots need planning approval in Joondalup?",
     "Carports for multiple dwellings and commercial sites always do. For grouped dwellings, the normal R-Code rules apply."),
]


def page(S):
    return {"path": "city-of-joondalup-carport-rules.html", "published": "2026-11-22", "type": "Council guide", "icon": "pin",
            "card": "City of Joondalup carport rules: setbacks, the 60% rule, boundaries and converting a carport.",
            "title": "City of Joondalup Carport Rules (2026)",
            "desc": "City of Joondalup carport rules: when you don't need planning approval, R20 setbacks, the 60% frontage rule, driveways, dual-coded lots and converting a carport to a room.",
            "eyebrow": "Council guide", "h1": "City of Joondalup carport rules", "crumb": "City of Joondalup carport rules",
            "answer": "<p>In Joondalup, every carport needs a <strong>building permit</strong>. You usually don't need <strong>planning approval</strong> if it matches the house, is no wider than <strong>60%</strong> of the frontage and meets the setbacks: on an R20 lot, <strong>3 m</strong> from the street (averaging 6 m) and 1 m from the side for 10 to 14 m long.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-in-front-setback", "Carport in the front setback"), ("/carport-on-boundary", "Carport on the boundary"), ("/enclose-a-carport", "Enclosing a carport")],
            "sources": [("Carport or garage and converting a garage to a habitable room, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/carport-or-garage-and-converting-a-garage-to-a-habitable-room"),
                        ("Residential Design Codes Volume 1, WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
