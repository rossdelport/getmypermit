BODY = """
<h2>What counts as a granny flat</h2>
<p>The City of Cockburn calls it an ancillary dwelling: a self-contained home on the same lot as another home. It can be a separate studio out the back, a studio above a garage, a self-contained wing or upstairs area in the house, or a dual-key layout.</p>

<h2>Does it need planning approval?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Zone</th><th>Planning approval</th></tr></thead><tbody>
<tr><td>Residential</td><td>Not needed if it meets every rule below and the R-Codes</td></tr>
<tr><td>Resource, Rural Living and Rural</td><td>Always needed</td></tr>
</tbody></table></div>
<p>Lots over <strong>1,100 m²</strong> rated <strong>BAL-40 or Flame Zone</strong> also need planning approval, with a BAL assessment. After any planning approval, you still need a building permit.</p>

<h2>Rules in the Residential zone</h2>
<ul>
<li>One granny flat per lot.</li>
<li>Up to <strong>70 m²</strong> inside. The City will consider up to <strong>100 m²</strong> if it's built to the R-Codes standards for aged and dependent housing (fully accessible), as a condition of planning approval.</li>
<li>Behind the street setback line of the main house.</li>
<li>The main house must still have its minimum open space and outdoor living area.</li>
<li>Must meet the other R-Codes rules: sun and airflow, height, setbacks, overlooking, overshadowing and landscaping.</li>
<li><strong>One extra car bay</strong>, unless the lot is within 800 m of a train station on a frequent line or 250 m of a frequent bus route.</li>
</ul>

<h2>Rules in Resource, Rural Living and Rural zones</h2>
<ul>
<li>One per lot, generally up to <strong>100 m²</strong> of living area (not counting verandahs, patios, alfresco or carports).</li>
<li>Usually behind the main building line.</li>
<li>Design, materials and colours should match or suit the house. No reflective or second-hand materials.</li>
</ul>
<p>Call the City on 08 9411 3444. See <a href="/granny-flat-parking">granny flat parking</a>, <a href="/granny-flat-on-a-rural-lot">granny flats on rural lots</a> and <a href="/granny-flat-at-the-front">granny flats at the front</a>.</p>
"""

FAQS = [
    ("How big can a granny flat be in the City of Cockburn?",
     "Up to 70 m² in the Residential zone, or up to 100 m² if it's built to accessible aged and dependent standards. In rural-type zones the usual limit is 100 m²."),
    ("Do I need planning approval for a granny flat in Cockburn?",
     "Not in the Residential zone if it meets all the R-Codes and City rules. It's always needed in the Resource, Rural Living and Rural zones."),
    ("Does a granny flat need a parking bay in Cockburn?",
     "Yes, one extra bay, unless the lot is within 800 m of a frequent train station or 250 m of a frequent bus route."),
    ("Can a granny flat be in front of the house in Cockburn?",
     "Not without planning approval. It needs to sit behind the street setback line of the main house."),
]


def page(S):
    return {"path": "city-of-cockburn-granny-flat-rules.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Cockburn granny flat rules: the 70 m² and 100 m² limits, parking, rural zones and BAL-40.",
            "title": "City of Cockburn Granny Flat Rules (2026)",
            "desc": "City of Cockburn granny flat (ancillary dwelling) rules: when planning approval is needed, the 70 m² and 100 m² limits, the extra car bay and transit exemption, rural zone rules and bushfire areas.",
            "eyebrow": "Council guide", "h1": "City of Cockburn granny flat rules", "crumb": "Cockburn granny flat rules",
            "answer": "<p>In the City of Cockburn's Residential zone, a granny flat up to <strong>70 m²</strong> doesn't need planning approval if it meets the R-Codes, sits behind the house's street setback and has <strong>one extra car bay</strong> (unless near frequent transport). Rural-type zones allow up to <strong>100 m²</strong> but always need planning approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-parking", "Granny flat parking"), ("/granny-flat-on-a-rural-lot", "Granny flat on a rural lot"), ("/granny-flat-at-the-front", "Granny flat at the front")],
            "sources": [("Planning information sheet: ancillary dwellings, City of Cockburn", "https://www.cockburn.wa.gov.au/getattachment/9169ac33-95a9-404c-a244-7b2c3c85c942/ECM_5298052_v8_Information-Sheet-Ancillary-Dwellings-docx.aspx")]}
