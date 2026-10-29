BODY = """
<p>The Shire of Mundaring is one of the few WA councils with a page just for tiny homes. Its rules are a good guide to how most Perth hills and rural councils think. Here they are in plain English, with what they mean for you.</p>

<h2>Tiny homes on wheels</h2>
<p>If your tiny home is on a trailer or wheels, the Shire treats it as a <strong>caravan</strong>, however nicely it is built. That leads to three rules:</p>
<div class="table-wrap"><table>
<thead><tr><th>What you want to do</th><th>The Shire of Mundaring rule</th></tr></thead><tbody>
<tr><td>Stay on private land for a short time</td><td>Up to <strong>5 nights in any 28 days</strong> with the landowner's consent, no approval needed</td></tr>
<tr><td>Live in it while you build your house</td><td>Up to <strong>2 years</strong> with an Application for Temporary Accommodation (see below)</td></tr>
<tr><td>Live in it permanently</td><td>Only in an <strong>approved caravan park</strong></td></tr>
<tr><td>Rent it out (for example on Airbnb)</td><td>Only in an <strong>approved caravan park</strong></td></tr>
</tbody></table></div>

<h3>Living in it while you build</h3>
<p>You can apply for Temporary Accommodation if you have a <strong>building permit for your house</strong> and the land is zoned Rural Residential, Rural Smallholdings or General Agriculture, or the lot is over 2,000 m&sup2;. The tiny home must:</p>
<ul>
<li>stay roadworthy and able to be moved off the site at any time, so you can leave in a bushfire;</li>
<li>be kept in a shed; and</li>
<li>be connected to permanent power, water and effluent disposal.</li>
</ul>

<h2>Tiny homes without wheels</h2>
<p>A tiny home on permanent footings has a clear path to approval. The Shire treats it as a <strong>Single House</strong>, or as an <strong>Ancillary Dwelling</strong> (granny flat) if there is already a house on the lot. There is no minimum size for a Single House, so tiny is fine, but it has to work as a real home:</p>
<ul>
<li>a proper kitchen (with a stove or oven and a sink), bathroom (basin, shower or bath, waterproofing, ventilation) and enclosed laundry (trough, waterproof floor);</li>
<li>minimum ceiling heights;</li>
<li>power, running water, and sewer or septic;</li>
<li>structural engineering certification;</li>
<li>energy efficiency compliance; and</li>
<li>a BAL (bushfire) report if the lot is bushfire-prone, which much of the Shire is.</li>
</ul>

<h2>The approvals, in order</h2>
<ol>
<li><strong>Environmental check.</strong> If the block is mapped as a Local Natural Area or has native vegetation or a watercourse, the Shire suggests an Environmental Asset Inspection. Book it for the same time as the BAL assessment.</li>
<li><strong>Health approval.</strong> On septic, Environmental Health approves the system for the extra kitchen and bathroom.</li>
<li><strong>Planning (development) approval.</strong> Likely needed if you are in a bushfire-prone area, on a heritage property, or if the design doesn't meet the standard R-Codes rules (setbacks, size and so on). For a <strong>$73</strong> fee, Shire planners will do a preliminary check of your site plan, elevations and floor plan first.</li>
<li><strong>Building permit.</strong> Always needed for the tiny home itself.</li>
</ol>

<h2>Tiny homes as tourist stays</h2>
<p>A tiny home on wheels can't be approved as tourism accommodation unless it is part of an approved caravan park. A tiny home without wheels can be considered on its merits as a tourism development.</p>

<h2>What this means for you</h2>
<ul>
<li><strong>Want to live in it long term?</strong> Put it on footings and approve it as a house or granny flat.</li>
<li><strong>Building a house first?</strong> A tiny home on wheels can be your home on site for up to two years, if your lot and zoning qualify.</li>
<li><strong>Bushfire-prone lot?</strong> Expect a BAL report and probably planning approval. Get the BAL done early, as it shapes the design.</li>
</ul>
<p>Contact numbers from the Shire: Planning Services (08) 9290 6740, Building Services (08) 9290 6666.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in the Shire of Mundaring?",
     "Permanently, only in an approved caravan park. On private land you can stay up to 5 nights in any 28 days, or up to 2 years with Temporary Accommodation approval while your house is being built."),
    ("Is there a minimum house size in Mundaring?",
     "The Shire says there is no minimum size for a Single House, so a tiny home on footings can be approved if it has a proper kitchen, bathroom and laundry and meets the building code."),
    ("Can I Airbnb a tiny home in the hills?",
     "Not a tiny home on wheels, unless it is in an approved caravan park. A tiny home without wheels can be considered on its merits as a tourism development."),
    ("How much does the Shire's preliminary planning check cost?",
     "The Shire lists a $73 fee for a preliminary assessment, with a site plan, elevations and floor plan."),
]


def page(S):
    return {"path": "shire-of-mundaring-tiny-homes.html", "published": "2026-10-29", "type": "Council guide", "icon": "pin",
            "card": "The Shire of Mundaring's rules for tiny homes on wheels and on footings, explained in plain English.",
            "title": "Shire of Mundaring Tiny Home Rules (2026) | On Wheels and Fixed",
            "desc": "Shire of Mundaring tiny home rules in plain English: 5 nights in 28 days on wheels, up to 2 years while you build, and approving a fixed tiny home as a house or granny flat.",
            "eyebrow": "Council guide", "h1": "Shire of Mundaring tiny home rules", "crumb": "Shire of Mundaring tiny homes",
            "answer": "<p>On wheels, a tiny home is a <strong>caravan</strong>: you can stay <strong>5 nights in any 28 days</strong> on private land, or up to <strong>2 years</strong> with approval while you build a house on rural or large lots. Permanent living is only allowed in caravan parks. On footings, it can be approved as a <strong>house or granny flat</strong> with a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels: WA rules"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/tiny-home-council-application", "Applying to your council")],
            "sources": [("Tiny homes (Shire of Mundaring)", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx")]}
