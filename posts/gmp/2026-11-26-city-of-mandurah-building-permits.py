BODY = """
<h2>What needs a building permit in Mandurah</h2>
<p>The City of Mandurah's "Do I need approval?" page sets out the main home projects. Here's the short version:</p>
<div class="table-wrap"><table>
<thead><tr><th>Project</th><th>Building permit</th></tr></thead><tbody>
<tr><td>New house</td><td>Always</td></tr>
<tr><td>Additions and alterations</td><td>Yes, unless it's minor repair that doesn't affect the structure, use or safety</td></tr>
<tr><td>Garage</td><td>Always</td></tr>
<tr><td>Shed</td><td>Not if freestanding, 10 m² or less and 2.4 m or lower</td></tr>
<tr><td>Carport</td><td>Always</td></tr>
<tr><td>Patio</td><td>Not if freestanding, 10 m² or less and 2.4 m or lower</td></tr>
<tr><td>Pergola</td><td>Not if freestanding, 20 m² or less and 2.4 m or lower</td></tr>
<tr><td>Shade sail</td><td>Not if freestanding, 10 m² or less and 2.4 m or lower</td></tr>
<tr><td>Swimming pool or spa</td><td>Always</td></tr>
<tr><td>Granny flat</td><td>Always</td></tr>
<tr><td>Retaining wall</td><td>Not if it holds back 0.5 m or less, isn't part of other building work and doesn't affect the neighbours</td></tr>
<tr><td>Front or dividing fence</td><td>Not if built to the City's local law</td></tr>
<tr><td>Rooftop solar or solar hot water</td><td>No</td></tr>
</tbody></table></div>

<h2>Planning approval</h2>
<p>For most house projects, planning (development) approval <strong>may not be needed</strong> if you meet the R-Codes deemed-to-comply rules. It depends on your zoning, site cover, setbacks and any special conditions. The City offers a <strong>deemed-to-comply check</strong> (a fee applies) to confirm in writing before you start.</p>
<p>Some special cases:</p>
<ul>
<li><strong>Pergolas and shade sails:</strong> generally no planning approval, unless you're on the canals.</li>
<li><strong>Pools:</strong> generally no planning approval, unless you're in a heritage area. Pool fencing may still need it.</li>
<li><strong>Demolition:</strong> taking down a shed, patio or pergola of 40 m² or less doesn't need a demolition permit, as long as it's not heritage listed and there's no health or safety risk.</li>
</ul>

<h2>How to apply</h2>
<p>Use a BA1 (certified by a private building surveyor) or a BA2 (checked by the City). The City prefers online lodgement through "I want to" then "Building Lodgements" on its website. Building Services is on 9550 3777.</p>
<p>See <a href="/what-doesnt-need-a-building-permit">what doesn't need a building permit</a>, <a href="/which-ba-form">which BA form you need</a> and <a href="/retrospective-approval-cost">getting approval for work already built</a>.</p>
"""

FAQS = [
    ("Do I need a building permit for a carport in Mandurah?",
     "Yes. The City of Mandurah says a building permit is always required for a carport and a garage."),
    ("What can I build without a permit in Mandurah?",
     "Small freestanding sheds and patios up to 10 m² and 2.4 m high, pergolas up to 20 m², low retaining walls up to 0.5 m, compliant fences and rooftop solar, among others."),
    ("Does Mandurah have a deemed-to-comply check?",
     "Yes. For a fee, the City will confirm in writing whether your project meets the R-Codes and so doesn't need planning approval."),
    ("How do I lodge a building permit in Mandurah?",
     "Online through the Building Lodgements link on the City's website, or on paper if you can't lodge online."),
]


def page(S):
    return {"path": "city-of-mandurah-building-permits.html", "published": "2026-11-26", "type": "Council guide", "icon": "pin",
            "card": "City of Mandurah building permits: what needs one, what's exempt, planning approval and how to lodge.",
            "title": "City of Mandurah Building Permits (2026 Guide)",
            "desc": "City of Mandurah building permits: which home projects always need a permit, what's exempt (sheds, patios, pergolas, walls, fences), the deemed-to-comply check, canal lots and how to lodge.",
            "eyebrow": "Council guide", "h1": "City of Mandurah building permits", "crumb": "City of Mandurah",
            "answer": "<p>In the City of Mandurah, new houses, garages, <strong>carports</strong>, pools and granny flats always need a building permit. Small freestanding sheds and patios (up to <strong>10 m²</strong> and 2.4 m) and pergolas (up to <strong>20 m²</strong>) don't. Planning approval usually isn't needed if you meet the R-Codes.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/what-doesnt-need-a-building-permit", "What doesn't need a building permit?"), ("/which-ba-form", "Which BA form do I need?"), ("/retrospective-approval-cost", "Approval for work already built")],
            "sources": [("Do I need approval?, City of Mandurah", "https://www.mandurah.wa.gov.au/my-home-property-and-rates/building-and-improving-your-home/do-i-need-approval")]}
