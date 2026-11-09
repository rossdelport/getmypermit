BODY = """
<h2>The rule in the R-Codes</h2>
<p>For a granny flat to skip planning approval, it must meet the R-Codes "deemed-to-comply" rules, and parking is one of them. The rule depends on two things: your lot's density code, and how close you are to good public transport.</p>
<div class="table-wrap"><table>
<thead><tr><th>Your lot</th><th>Near a station or frequent stop (Location A)</th><th>Everywhere else (Location B)</th></tr></thead><tbody>
<tr><td>Most house lots (single house R40 or lower, grouped dwelling R25 or lower)</td><td><strong>No</strong> extra bay</td><td><strong>One</strong> extra bay</td></tr>
<tr><td>Higher-density lots (R-Codes Part C)</td><td>No minimum</td><td>No minimum</td></tr>
</tbody></table></div>

<h2>Am I in Location A?</h2>
<p>You're in Location A if your lot is within:</p>
<ul>
<li>An <strong>800 m walk</strong> of a train station on a high-frequency rail route, or</li>
<li>A <strong>250 m walk</strong> of a bus or transit stop on a high-frequency route, or a stop where several routes combined stop every 15 minutes in weekday peaks (7 to 9 am and 5 to 7 pm)</li>
</ul>
<p>On higher-density lots, land inside an activity centre also counts. Everywhere else is Location B. Distances are walking distances, not straight lines.</p>

<h2>What counts as a bay</h2>
<p>The rule asks for an <strong>on-site</strong> car parking space. It doesn't say the space must be covered, so it doesn't have to be a new carport. It does have to be on your lot, on top of the bays the main house needs. Councils check this on your site plan, and they can differ on whether a space behind another car on the driveway counts, so ask yours.</p>

<h2>If you can't fit the bay</h2>
<p>Missing the parking rule doesn't mean no granny flat. It means it isn't "deemed-to-comply", so you'd apply for planning approval and show why the design still works. Your council decides. The granny flat must also sit behind the street setback line and leave the house enough open space and outdoor living area.</p>
<p>Some councils explain the rule on their own sites. The City of Joondalup lists the same one-bay rule and exemptions on its granny flat page.</p>
<p>See what else skips planning approval in <a href="/granny-flat-no-planning-approval">granny flats without planning approval</a>, read the full <a href="/granny-flat-rules-wa">granny flat rules in WA</a>, or see <a href="/granny-flat-at-the-front">can a granny flat go at the front?</a></p>
"""

FAQS = [
    ("Does a granny flat need a parking bay in WA?",
     "On most house lots, yes: one extra bay, unless the lot is within an 800 m walk of a high-frequency train station or 250 m of a high-frequency bus stop. Higher-density lots under R-Codes Part C have no minimum."),
    ("What is Location A in the R-Codes?",
     "Land within an 800 m walk of a train station on a high-frequency rail route, or 250 m of a stop on a high-frequency transit route. A high-frequency route runs at least every 15 minutes in weekday peaks."),
    ("Does the granny flat parking bay need to be covered?",
     "The R-Codes ask for an on-site space and don't say it must be covered. Ask your council whether an existing driveway space counts."),
    ("What if I can't fit a parking bay for my granny flat?",
     "You can still apply, but you'll need planning approval because it isn't deemed-to-comply. The council decides whether the design is acceptable."),
]


def page(S):
    return {"path": "granny-flat-parking.html", "published": "2026-11-10", "type": "Question answer", "icon": "car",
            "card": "One extra bay on most house lots, none near good transport. How to tell which applies.",
            "title": "Does a Granny Flat Need a Parking Bay in WA? (2026)",
            "desc": "Granny flat parking in WA: one extra bay on most house lots, none within 800 m of a train station or 250 m of a frequent bus stop. How the R-Codes rule works.",
            "eyebrow": "Question answer", "h1": "Does a granny flat need its own parking bay?", "crumb": "Granny flat parking",
            "answer": "<p>On most house lots, <strong>yes: one extra bay</strong>. You don't need one if your lot is within an <strong>800 m walk</strong> of a high-frequency train station or <strong>250 m</strong> of a high-frequency bus stop. Higher-density lots have no minimum. Miss the rule and you'll need planning approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-no-planning-approval", "Granny flats without planning approval"), ("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-at-the-front", "Can a granny flat go at the front?")],
            "sources": [("State Planning Policy 7.3 R-Codes Volume 1, April 2026 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Granny flat or ancillary dwelling (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/granny-flat-or-ancillary-dwelling")]}
