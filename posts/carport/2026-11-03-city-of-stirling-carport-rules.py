BODY = """
<h2>When you don't need planning approval</h2>
<p>At the City of Stirling, a carport doesn't need development (planning) approval if it meets <strong>all</strong> of these:</p>
<ul>
<li>it's at least the minimum distance from the street boundary (table below)</li>
<li>the posts are at least <strong>1 m</strong> from the side boundary</li>
<li>enough open space is left on the lot (table below)</li>
<li>it's big enough to park in (minimum sizes below)</li>
<li>there's an unobstructed view between the house and the street</li>
<li>it's no wider than <strong>60%</strong> of the lot frontage</li>
</ul>
<p>Every carport needs a <strong>building permit</strong>, even when planning approval isn't needed.</p>

<h2>Street setback and open space by R-Code</h2>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Minimum street setback</th><th>Minimum open space</th></tr></thead><tbody>
<tr><td>R10</td><td>3.75 m</td><td>60%</td></tr>
<tr><td>R12.5</td><td>3.75 m</td><td>55%</td></tr>
<tr><td>R20, R25</td><td>3 m</td><td>50%</td></tr>
<tr><td>R30, R40</td><td>2 m</td><td>45%</td></tr>
<tr><td>R50, R60</td><td>1 m</td><td>40%</td></tr>
<tr><td>R80</td><td>0.5 m</td><td>30%</td></tr>
</tbody></table></div>
<p>Find your lot's R-Code with the Address and Application Assistant on the City's website.</p>

<h2>Minimum sizes</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Length</th><th>Width</th><th>Opening</th></tr></thead><tbody>
<tr><td>Single</td><td>5.4 m</td><td>2.4 m (3 m if a post or wall is next to the opening)</td><td>2.4 m</td></tr>
<tr><td>Double</td><td>5.4 m</td><td>4.8 m (5.4 m if a post or wall is next to the opening)</td><td>4.8 m</td></tr>
</tbody></table></div>

<h2>Doors, corners and laneways</h2>
<ul>
<li><strong>Doors.</strong> Any door must be visually permeable, such as a see-through tilt-up door.</li>
<li><strong>Corner lots.</strong> Face the secondary street where you can, and avoid access from busy roads like Walcott Street or Karrinyup Road. You can build as close as <strong>1.5 m</strong> to the secondary street.</li>
<li><strong>Laneways.</strong> Access from a laneway is encouraged (Local Planning Policy 6.5).</li>
</ul>

<h2>Heritage areas and strata</h2>
<p>All carports in the <strong>Heritage Protection Area</strong> (Mount Lawley, Menora and Inglewood) or on heritage-listed properties need planning approval, and must use the laneway if there is one. Strata lots may also need approval under the Strata Titles Act.</p>

<h2>If you do need planning approval</h2>
<p>The City has <strong>60 days</strong> to decide, though carports are usually quicker. You'll need the application form signed by every owner, a title search from the last six months, the fee, a site plan at 1:200, floor plan and elevations at 1:100, and a written justification for anything that doesn't meet the rules. Sloping sites need a feature survey. You don't need your neighbour's approval to apply.</p>
<p>City of Stirling: <strong>(08) 9205 8555</strong>.</p>
"""

FAQS = [
    ("Do I need council approval for a carport in Stirling?",
     "You always need a building permit. You only need planning approval as well if the carport doesn't meet the setback, side boundary, open space, size, view and 60% width rules, or if it's in the Heritage Protection Area."),
    ("How close to the street can a carport be in Stirling?",
     "It depends on your R-Code: 3 m on R20 and R25, 2 m on R30 and R40, 1 m on R50 and R60, and 0.5 m on R80."),
    ("Can I put a door on a carport in Stirling?",
     "Only a visually permeable one, such as a see-through tilt-up door."),
    ("How long does a carport planning application take in Stirling?",
     "The City has up to 60 days, but carports are normally faster."),
]


def page(S):
    return {"path": "city-of-stirling-carport-rules.html", "published": "2026-11-03", "type": "Council guide", "icon": "carport",
            "card": "Street setbacks by R-Code, the 60% rule, minimum sizes, doors and heritage areas in Stirling.",
            "title": "City of Stirling Carport Rules: Setbacks, Sizes and Approvals",
            "desc": "City of Stirling carport rules: street setbacks and open space by R-Code, the 60% frontage rule, 1 m side setback, minimum sizes, doors, corner lots and heritage areas.",
            "eyebrow": "Council guide", "h1": "City of Stirling carport rules", "crumb": "Stirling carport rules",
            "answer": "<p>In Stirling, a carport skips planning approval if it meets the street setback for your R-Code (<strong>3 m on R20</strong>, 2 m on R30), keeps posts <strong>1 m</strong> from the side boundary, is no wider than <strong>60%</strong> of the frontage and keeps the view to the street open. It always needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-corner-block", "Carports on corner blocks"), ("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
