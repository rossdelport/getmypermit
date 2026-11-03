BODY = """
<h2>When you don't need planning approval</h2>
<p>The City of Joondalup says a granny flat is generally exempt from planning (development) approval if it meets the standard R-Codes rules, including:</p>
<ul>
<li><strong>Floor area</strong> no more than <strong>70 m²</strong></li>
<li><strong>Parking</strong> (see below)</li>
<li><strong>All other R-Codes rules</strong>, such as height and setbacks</li>
<li><strong>Design that matches the house</strong>: the same colour, roof pitch and materials</li>
<li>Any extra rules if your lot is in a <strong>structure plan area</strong></li>
</ul>
<p>Check your lot's R-Code and whether it's in a structure plan area with the City's online mapping system.</p>

<h2>Parking: Joondalup can ask for an extra bay</h2>
<div class="table-wrap"><table>
<thead><tr><th>Main home</th><th>Extra car bay for the granny flat?</th></tr></thead><tbody>
<tr><td>Single house, R40 or lower</td><td><strong>Yes, one bay</strong>, unless within 800 m walk of a train station or 250 m of a high-frequency bus route</td></tr>
<tr><td>Grouped dwelling, R25 or lower</td><td><strong>Yes, one bay</strong>, with the same exemptions</td></tr>
<tr><td>Single house R50 or higher, or grouped dwelling R30 or higher</td><td>No</td></tr>
</tbody></table></div>
<p>Check your R-Code first, and leave room for the extra bay if you need one.</p>

<h2>If you don't meet the rules</h2>
<p>You'll need development approval: an application form, building plans and a cover letter, plus the application fee.</p>

<h2>Building permit</h2>
<p>Every granny flat in Joondalup needs a <strong>building permit</strong>. You can lodge:</p>
<ul>
<li>a <strong>BA1</strong> (certified), with a Certificate of Design Compliance (BA3) from a registered building surveyor, or</li>
<li>a <strong>BA2</strong> (uncertified), with the City's checklist for dwellings and habitable additions.</li>
</ul>

<h2>Renting it out</h2>
<p>The City confirms a granny flat can be rented out separately from the main house.</p>

<h2>Contact</h2>
<p>City of Joondalup, <strong>9400 4000</strong>, info@joondalup.wa.gov.au, 90 Boas Avenue, Joondalup.</p>
"""

FAQS = [
    ("Do I need planning approval for a granny flat in Joondalup?",
     "Not usually. It's generally exempt if it's 70 m² or less, meets parking and all other R-Codes rules, and matches the house's colour, roof pitch and materials."),
    ("Does a granny flat in Joondalup need its own parking bay?",
     "Yes, one extra bay if the main home is a single house on R40 or lower, or a grouped dwelling on R25 or lower, unless you're within 800 m of a train station or 250 m of a high-frequency bus route."),
    ("Do I need a building permit for a granny flat in Joondalup?",
     "Yes, always. Lodge a BA1 with a Certificate of Design Compliance, or a BA2 with the City's checklist."),
    ("Can I rent out a granny flat in Joondalup?",
     "Yes. The City says a granny flat can be rented out separately from the main house."),
]


def page(S):
    return {"path": "city-of-joondalup-granny-flat-rules.html", "published": "2026-11-04", "type": "Council guide", "icon": "granny",
            "card": "The 70 m² limit, Joondalup's extra parking bay rule, matching design and the building permit.",
            "title": "City of Joondalup Granny Flat Rules (2026)",
            "desc": "City of Joondalup granny flat rules: when you skip planning approval, the 70 m² limit, the extra car bay rule, matching design, structure plan areas and building permits.",
            "eyebrow": "Council guide", "h1": "City of Joondalup granny flat rules", "crumb": "Joondalup granny flat rules",
            "answer": "<p>In Joondalup, a granny flat usually skips planning approval if it's <strong>70 m² or less</strong>, meets the R-Codes, <strong>matches the house</strong> in colour, roof pitch and materials, and has <strong>one extra car bay</strong> on most lower-density lots. It always needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-size-calculator", "Granny flat 70 m² calculator"), ("/granny-flat-no-planning-approval", "Granny flats with no planning approval")],
            "sources": [("Granny flat or ancillary dwelling (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/granny-flat-or-ancillary-dwelling")]}
