BODY = """
<h2>When you don't need planning approval</h2>
<p>The City of Stirling says a granny flat doesn't need planning approval if it meets the R-Codes' standard rules, including:</p>
<ul>
<li>A floor area of no more than <strong>70 m²</strong> (not counting storerooms, verandahs, parking, courtyards and the like).</li>
<li>Enough open space and outdoor living area left for the main house (see the table).</li>
<li>Colours, roof pitch and materials that suit the existing house.</li>
<li>Setbacks and privacy that meet the R-Codes. The minimum side setback is <strong>1 m</strong>, more for longer or taller walls.</li>
</ul>
<p>The City's information sheet still lists a <strong>350 m²</strong> minimum lot size, but the state removed the minimum lot size in 2024. If your lot is smaller, ask the City which applies.</p>

<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Outdoor living area for the main house</th><th>Open space</th></tr></thead><tbody>
<tr><td>R10</td><td>No minimum</td><td>60%</td></tr>
<tr><td>R12.5</td><td>No minimum</td><td>55%</td></tr>
<tr><td>R20 / R25</td><td>30 m²</td><td>50%</td></tr>
<tr><td>R30</td><td>24 m²</td><td>45%</td></tr>
<tr><td>R40</td><td>20 m²</td><td>45%</td></tr>
<tr><td>R50 / R60</td><td>16 m²</td><td>40%</td></tr>
<tr><td>R80</td><td>16 m²</td><td>30%</td></tr>
</tbody></table></div>

<h2>Parking, boundaries and strata</h2>
<ul>
<li><strong>Parking:</strong> no extra bay within 800 m of a train station or 250 m of a high-frequency bus route. Otherwise, one extra bay on the lot.</li>
<li><strong>Boundary walls:</strong> allowed at R20 and above, on up to two side boundaries and up to 3.5 m high.</li>
<li><strong>Strata:</strong> only on green title or survey strata with no common property.</li>
</ul>

<h2>Heritage areas always need approval</h2>
<p>Every granny flat in the <strong>Mount Lawley, Menora and Inglewood</strong> heritage area, or on a heritage-listed property, needs planning approval.</p>

<h2>Timeframes and the old family-only rule</h2>
<p>If you need planning approval, the City has <strong>60 days</strong> to decide, and says granny flats are usually faster. You don't need your neighbour's approval to apply. Every granny flat needs a <strong>building permit</strong>.</p>
<p>Older Stirling approvals put a notice on the title saying only family could live there. That rule is gone, and you can ask the City for written planning advice to have the notice removed through Landgate. The City also offers a paid "deemed-to-comply check" to confirm whether you need planning approval.</p>
<p>Read about <a href="/granny-flat-parking">granny flat parking</a>, the <a href="/granny-flat-minimum-lot-size">minimum lot size</a>, or <a href="/rent-out-granny-flat-wa">renting out a granny flat</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a granny flat in Stirling?",
     "You always need a building permit. You usually don't need planning approval if it's up to 70 m² and meets the R-Codes, unless you're in the Mount Lawley, Menora or Inglewood heritage area."),
    ("Do I need a parking bay for a granny flat in Stirling?",
     "Not if you're within 800 m of a train station or 250 m of a high-frequency bus route. Otherwise, one extra bay."),
    ("Can I remove the family-only notice from my title?",
     "Yes. The rule has changed. Ask the City for written planning advice, then give it to Landgate to remove the notice."),
    ("How close to the boundary can a granny flat be in Stirling?",
     "At least 1 m, more for longer or taller walls. Boundary walls are allowed at R20 and above, up to 3.5 m high."),
]


def page(S):
    return {"path": "city-of-stirling-granny-flat-rules.html", "published": "2026-11-21", "type": "Council guide", "icon": "pin",
            "card": "City of Stirling granny flat rules: 70 m², open space, parking, heritage areas and title notices.",
            "title": "City of Stirling Granny Flat Rules (2026)",
            "desc": "City of Stirling granny flat rules: when you don't need planning approval, open space by R-Code, parking, boundary walls, heritage areas and removing old family-only title notices.",
            "eyebrow": "Council guide", "h1": "City of Stirling granny flat rules", "crumb": "City of Stirling granny flat rules",
            "answer": "<p>In Stirling, a granny flat up to <strong>70 m²</strong> that meets the R-Codes (open space, setbacks, matching materials) usually needs <strong>no planning approval</strong>, except in the Mount Lawley, Menora and Inglewood heritage area. It always needs a <strong>building permit</strong>. Near frequent trains or buses, no extra parking bay is needed.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-parking", "Granny flat parking"), ("/granny-flat-minimum-lot-size", "Granny flat minimum lot size"), ("/rent-out-granny-flat-wa", "Renting out a granny flat")],
            "sources": [("Ancillary dwelling (granny flat) information sheet, City of Stirling", "https://www.stirling.wa.gov.au/awcontent/Web/Documents/Ancillary-Dwellings-(Granny-Flat).pdf"),
                        ("Where do I start?, City of Stirling", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/where-do-i-start")]}
