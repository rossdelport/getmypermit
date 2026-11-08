BODY = """
<h2>Planning approval in Stirling</h2>
<p>The City of Stirling says patios may not need planning approval if they meet the R-Codes' deemed-to-comply rules. Pergolas and shade sails usually don't need planning approval at all, unless the property is in the City's <strong>Heritage Protection Area</strong> (Mount Lawley, Menora and Inglewood).</p>
<p>The main R-Codes rules for a patio on a single house (R40 and below) are:</p>
<ul>
<li>It meets the normal side and rear setbacks, <strong>or</strong> it can have its posts right on the boundary if it's no more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, sits behind the street setback, and keeps the eaves, gutters and roof at least <strong>450 mm</strong> from the boundary</li>
<li>It keeps enough open space and outdoor living area for your R-Code</li>
</ul>
<p>Higher-density lots (R50 and above for single houses) use a different part of the R-Codes, which allows patios up to the boundary if under 10 m long, with a 3 m equivalent wall height and 4.2 m ridge.</p>

<h2>Building permit in Stirling</h2>
<p>The state building rules apply:</p>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No building permit if...</th></tr></thead><tbody>
<tr><td>Patio (solid roof)</td><td>Freestanding, 10 m² or less, and 2.4 m high or less</td></tr>
<tr><td>Pergola or shade sail with a house</td><td>20 m² or less and 2.4 m high or less</td></tr>
<tr><td>Patio attached to the house</td><td>Always needs a permit</td></tr>
</tbody></table></div>
<p>Even when the planning rules allow posts on the boundary, the building code still applies, including fire separation. The R-Codes themselves note that separate building code requirements may apply.</p>

<h2>Timeframes and lodging</h2>
<ul>
<li>Lodge online through the City's eLodgement service.</li>
<li>The City has <strong>10 business days</strong> for a certified (BA1) application and <strong>25 business days</strong> for an uncertified (BA2) one.</li>
<li>Planning applications: up to <strong>60 days</strong>. You don't need your neighbours' approval to lodge one, but the City may advertise it to them.</li>
<li>The City can provide copies of existing plans for your property to the owner, which helps with drawings.</li>
</ul>

<h2>Heritage areas</h2>
<p>In the Heritage Protection Area, very few things are exempt from planning approval. Pergolas and shade sails need it too. Expect to show materials and roof colours.</p>

<h2>Rules are changing</h2>
<p>Stirling is preparing a new planning scheme (Local Planning Scheme No. 4), with a new policy on what's exempt from planning approval advertised in late 2025. It will only take effect once the new scheme is in place. Check the City's website for the current rules before you start.</p>
<p>Test your design with the <a href="/patio-approval-checker">patio approval checker</a>, or read <a href="/patio-on-boundary-wa">building a patio on the boundary</a> and <a href="/patio-building-permit">patio building permits</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a patio in the City of Stirling?",
     "Usually a building permit, unless it's freestanding, 10 m² or less and 2.4 m high or less. Planning approval isn't needed if it meets the R-Codes deemed-to-comply rules and isn't in the Heritage Protection Area."),
    ("Can I build a patio on the boundary in Stirling?",
     "Under the R-Codes, posts can go on the boundary for a patio up to 10 m long and 2.7 m high, behind the street setback, with the roof 450 mm back. Building code fire rules still apply."),
    ("Do pergolas need approval in the City of Stirling?",
     "Pergolas and shade sails usually don't need planning approval unless in the Heritage Protection Area. A building permit isn't needed if 20 m² or less and 2.4 m high or less."),
    ("Which Stirling suburbs are in the Heritage Protection Area?",
     "Mount Lawley, Menora and Inglewood. Patios, pergolas and shade sails there need planning approval."),
    ("How long does a patio permit take in Stirling?",
     "10 business days for a certified (BA1) application and 25 business days for an uncertified (BA2) one."),
]


def page(S):
    return {"path": "city-of-stirling-patio-rules.html", "published": "2026-11-09", "type": "Council guide", "icon": "pin",
            "card": "R-Code boundary rules, permit exemptions, heritage areas and timeframes in Stirling.",
            "title": "City of Stirling Patio Rules (2026)",
            "desc": "City of Stirling patio, pergola and shade sail rules: when planning approval is needed, boundary posts, building permit exemptions, heritage areas, timeframes.",
            "eyebrow": "Council guide", "h1": "City of Stirling patio rules", "crumb": "City of Stirling patio rules",
            "answer": "<p>In Stirling, a patio usually needs a <strong>building permit</strong> but no planning approval if it meets the R-Codes. Posts can go on the boundary for patios up to <strong>10 m long</strong> and <strong>2.7 m high</strong>, with the roof 450 mm back. Pergolas and shade sails usually skip planning approval, except in the <strong>Heritage Protection Area</strong> (Mount Lawley, Menora, Inglewood).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/patio-building-permit", "Patio building permits")],
            "sources": [("Where do I start? (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/where-do-i-start"),
                        ("Residential Design Codes Volume 1, April 2026 (WA Planning)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Lodging an application (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/lodging-an-application")]}
