BODY = """
<h2>Building permit</h2>
<p>The City of Swan follows the state building rules. A freestanding shed of <strong>10 m² or less</strong> and no more than <strong>2.4 m</strong> high doesn't need a building permit. Anything bigger usually does. You can lodge online through the City's ePathway portal, and the City has <strong>25 business days</strong> to decide an uncertified (BA2) application, or 10 business days for a certified (BA1) one.</p>

<h2>Planning approval on a house block</h2>
<p>On residential lots, sheds usually don't need planning approval if they meet the R-Codes' standard ("deemed-to-comply") rules for outbuildings. These are the same across WA:</p>
<ul>
<li>Total outbuildings no more than <strong>60 m²</strong> or 10% of the lot, whichever is less</li>
<li>Walls no higher than <strong>2.4 m</strong> and the ridge no higher than <strong>4.2 m</strong></li>
<li>Usually at least <strong>1 m</strong> from side and rear boundaries</li>
<li>Not in the street setback, and not used to live in</li>
</ul>
<p>The City's own development application notices describe a 1 m setback and 2.4 m wall height as "permitted as of right". Bigger or taller sheds need planning approval. Heritage areas, heritage-listed places and lots near the Swan River usually need it too.</p>

<h2>Rural and Swan Valley lots</h2>
<p>The City of Swan's planning scheme (Local Planning Scheme No. 17, Schedule 5) exempts bigger rural sheds from planning approval if they meet all its conditions:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>General Rural, Swan Valley Rural</th><th>Special Rural, Rural Living, Rural Residential, Landscape, Resource</th></tr></thead><tbody>
<tr><td>Total area of sheds and outbuildings</td><td>Up to <strong>300 m²</strong></td><td>Up to <strong>200 m²</strong></td></tr>
<tr><td>Height</td><td>Up to 5 m</td><td>Up to 5 m</td></tr>
<tr><td>Cladding</td><td>Non-reflective</td><td>Non-reflective</td></tr>
<tr><td>Where</td><td>Meets the zone's boundary setbacks</td><td>Inside the approved building envelope, or meets the zone's setbacks</td></tr>
<tr><td>Not allowed for the exemption</td><td colspan="2">Flood-prone areas, heritage areas and heritage-listed lots</td></tr>
</tbody></table></div>
<p>Even when planning approval isn't needed, a shed this size still needs a building permit.</p>

<h2>Before you apply</h2>
<ul>
<li>Check your zoning and R-Code on the City's maps.</li>
<li>Check for sewer pipes and easements. See <a href="/shed-over-sewer-or-easement">building a shed near a sewer</a>.</li>
<li>The City also has a "Shed, Patio, Sea-Container and Water Tank Questionnaire" to help work out what approvals you need.</li>
</ul>
<p>Use the <a href="/shed-size-checker">shed size checker</a> for a quick answer, or read <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in the City of Swan?",
     "A freestanding shed of 10 m² or less and up to 2.4 m high doesn't need a building permit. Bigger sheds usually do. Planning approval is only needed if the shed doesn't meet the R-Codes or scheme rules."),
    ("How big can a shed be in the City of Swan without planning approval?",
     "On a house block, usually up to 60 m² of total outbuildings (or 10% of the lot), with 2.4 m walls and a 4.2 m ridge. On General Rural and Swan Valley Rural land, up to 300 m²; on Special Rural, Rural Living and similar zones, up to 200 m²."),
    ("How long does a City of Swan shed permit take?",
     "The City has 25 business days to decide an uncertified (BA2) application and 10 business days for a certified (BA1) one."),
    ("How close to the fence can a shed be in the City of Swan?",
     "Usually 1 m from side and rear boundaries to meet the standard R-Codes rules on a house block. Closer needs planning approval. Rural zones have their own setbacks."),
    ("Do rural sheds in the City of Swan need a building permit?",
     "Yes. The planning exemption for rural sheds doesn't remove the need for a building permit."),
]


def page(S):
    return {"path": "city-of-swan-shed-rules.html", "published": "2026-11-08", "type": "Council guide", "icon": "pin",
            "card": "House block and rural shed limits, setbacks and permit timeframes in the City of Swan.",
            "title": "City of Swan Shed Rules (2026): Sizes and Permits",
            "desc": "City of Swan shed rules: when you need a building permit, house block size limits, rural and Swan Valley shed exemptions up to 300 m², and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Swan shed rules", "crumb": "City of Swan shed rules",
            "answer": "<p>Sheds over <strong>10 m²</strong> or <strong>2.4 m</strong> high need a building permit. On a house block, planning approval usually isn't needed up to <strong>60 m²</strong> (or 10% of the lot) with 2.4 m walls and 1 m from the boundary. Rural lots get bigger exemptions: up to <strong>300 m²</strong> in General Rural and Swan Valley Rural, and <strong>200 m²</strong> in Rural Living and similar zones.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/shed-over-sewer-or-easement", "Building a shed near a sewer")],
            "sources": [("Local Planning Scheme No. 17, Schedule 5: Exempted development (City of Swan)", "https://www.swan.wa.gov.au/awcontent/Web/Documents/Planning-Building/local-planning-scheme-17_schedule_5_exempted_development.pdf"),
                        ("Building (City of Swan)", "https://www.swan.wa.gov.au/plan-and-build/building"),
                        ("Outbuilding (shed) (City of Joondalup, R-Codes summary)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)")]}
