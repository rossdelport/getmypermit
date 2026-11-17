BODY = """
<h2>Building permit</h2>
<p>Every granny flat in the City of Swan needs a <strong>building permit</strong>. You can lodge a <strong>BA1</strong> (certified by a private building surveyor), which the City has <strong>10 business days</strong> to decide, or a <strong>BA2</strong> (uncertified), which it has <strong>25 business days</strong> to decide. Applications are lodged online through the City's ePathway portal.</p>

<h2>Do you need planning approval?</h2>
<p>The City has a granny flat questionnaire to work this out. It flags that you'll need a planning application (development approval) if:</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Planning application needed if</th></tr></thead><tbody>
<tr><td>Is there a house on the same lot?</td><td>No (a granny flat must go with a single house)</td></tr>
<tr><td>Lot size</td><td>Less than 450 m²</td></tr>
<tr><td>Granny flat size (plot ratio)</td><td>More than 70 m²</td></tr>
<tr><td>Parking</td><td>No extra bay, unless you're within 800 m of a high-frequency train station or 250 m of a high-frequency bus route</td></tr>
</tbody></table></div>
<p>The questionnaire also asks how wastewater will be handled, which matters on lots without sewer. The state R-Codes allow a granny flat on any size lot if it meets the standard rules, so ask the City which applies to your lot. Councils vary.</p>

<h2>Rural lots (Policy POL-C-066)</h2>
<p>On rural-zoned land, the City's Ancillary Accommodation policy says a granny flat should:</p>
<ul>
<li>Be no bigger than <strong>70 m²</strong>, not counting verandahs, patios, carports, garages and pergolas.</li>
<li>Have <strong>one extra car bay</strong>.</li>
<li>Be within <strong>10 m</strong> of the main house.</li>
</ul>
<p>The City may add a condition that only dependent family members live there, and a granny flat can't be used as a reason to subdivide.</p>
<p>Read about a <a href="/granny-flat-on-a-rural-lot">granny flat on a rural lot</a>, <a href="/granny-flat-parking">granny flat parking rules</a>, or the <a href="/granny-flat-building-permit">granny flat building permit</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a granny flat in the City of Swan?",
     "You always need a building permit. You may also need planning approval, for example if the granny flat is over 70 m² or you can't provide an extra parking bay."),
    ("How big can a granny flat be in the City of Swan?",
     "Up to 70 m² without a planning application. On rural land, the 70 m² doesn't include verandahs, patios, carports, garages and pergolas."),
    ("How far from the house can a granny flat be on a rural lot in Swan?",
     "Within 10 m of the main house, under the City's Ancillary Accommodation policy POL-C-066."),
    ("How long does the City of Swan take to approve a granny flat?",
     "10 business days for a certified BA1 building permit, or 25 business days for an uncertified BA2. Planning approval, if needed, comes first."),
]


def page(S):
    return {"path": "city-of-swan-granny-flat-rules.html", "published": "2026-11-18", "type": "Council guide", "icon": "pin",
            "card": "City of Swan granny flat rules: building permits, when you need planning approval, and rural lot limits.",
            "title": "City of Swan Granny Flat Rules (2026)",
            "desc": "City of Swan granny flat rules: building permit times, when you need planning approval (70 m², parking, lot size), and rural lot rules under POL-C-066.",
            "eyebrow": "Council guide", "h1": "City of Swan granny flat rules", "crumb": "City of Swan granny flat rules",
            "answer": "<p>In the City of Swan, every granny flat needs a <strong>building permit</strong>. You'll also need planning approval if it's over <strong>70 m²</strong>, you can't add an extra parking bay (unless you're near high-frequency transport), or, per the City's questionnaire, the lot is under <strong>450 m²</strong>. On rural land it must be within <strong>10 m</strong> of the house.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-on-a-rural-lot", "Granny flat on a rural lot"), ("/granny-flat-parking", "Granny flat parking"), ("/granny-flat-building-permit", "Granny flat building permit")],
            "sources": [("Granny flat (ancillary dwelling) questionnaire, City of Swan", "https://www.swan.wa.gov.au/awcontent/Web/Documents/PlanBuildSubdivisionSpecifications/Granny-Flat-Ancillary-Dwelling-Development-Application-Questionniare-DSI-7676064.pdf"),
                        ("POL-C-066 Ancillary Accommodation Dwellings in Rural Areas, City of Swan", "https://www.swan.wa.gov.au/awcontent/Web/Documents/Policies/POL-C-066-Ancillary-Accommodation-Dwellings-in-Rural-Areas.pdf"),
                        ("Building, City of Swan", "https://www.swan.wa.gov.au/plan-and-build/building"),
                        ("Useful documents and links, City of Swan", "https://www.swan.wa.gov.au/plan-and-build/useful-documents-and-links"),
                        ("Residential Design Codes Volume 1 (April 2026)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
