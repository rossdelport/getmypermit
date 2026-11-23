BODY = """
<h2>What the City allows</h2>
<p>The City of Busselton can approve living temporarily in a caravan or <strong>tiny home on wheels</strong> on private land. The approval lasts up to <strong>24 months</strong>.</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Details</th></tr></thead><tbody>
<tr><td>How many</td><td>One caravan or tiny home on wheels per lot</td></tr>
<tr><td>Size</td><td>Up to 12.5 m long, 2.5 m wide and 4.3 m high, including wheels and drawbar</td></tr>
<tr><td>Floor area</td><td>Up to 50 m², including the van and any structures that go with it. It's treated like a granny flat</td></tr>
<tr><td>Built</td><td>Off site and towed in. Must be self-contained and liveable</td></tr>
<tr><td>Zoning</td><td>Land zoned to allow a house</td></tr>
<tr><td>Parking</td><td>At least one bay</td></tr>
</tbody></table></div>

<h2>Where it can go</h2>
<p>It should be set back far enough from neighbours to suit the City, and in residential areas it shouldn't be seen from the street. It must sit within any approved building envelope and follow any bushfire permit for the land. No clearing without a permit.</p>

<h2>What to send</h2>
<ul>
<li>The City's application form, signed by you and all landowners, with the fee.</li>
<li>Why you want to live there, start and end dates, and who will live there.</li>
<li>Details of drinking water, wastewater, rubbish and power.</li>
<li>A current Certificate of Title and anything registered on it, such as easements.</li>
<li>A site plan to scale (1:200 or better) showing boundaries, the van, services, other buildings, driveway and setbacks.</li>
<li>A floor plan with windows and floor area.</li>
<li>A check of the state's Aboriginal heritage system for your land.</li>
</ul>
<p>Sheds, carports, rigid annexes and tanks over 5,000 litres need their own planning and building approvals.</p>

<h2>After you apply</h2>
<p>If the City hasn't approved it within <strong>63 days</strong>, it's taken as refused. Approvals name the people living there, have conditions, and may require you to clear the site when they end.</p>
<p>See <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules</a>, <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your land</a> and <a href="/tiny-home-council-application">how to apply</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in Busselton?",
     "Yes, with City approval, for up to 24 months. One per lot, on land zoned for a house, up to 50 m² including any associated structures."),
    ("How big can a tiny home on wheels be in Busselton?",
     "Up to 12.5 m long, 2.5 m wide and 4.3 m high, including the wheels, drawbar and accessories."),
    ("How long does Busselton take to decide?",
     "If the City hasn't approved your application within 63 days, it's taken as refused."),
    ("Does a tiny home in Busselton need parking?",
     "Yes. At least one parking bay must be available."),
]


def page(S):
    return {"path": "city-of-busselton-tiny-homes.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Busselton tiny home rules: 24-month approvals, size limits, where it can go and what to send.",
            "title": "City of Busselton Tiny Home Rules (2026)",
            "desc": "City of Busselton tiny homes on wheels: 24-month approvals, one per lot, 12.5 m x 2.5 m x 4.3 m size limit, 50 m² floor area, parking, what to send and the 63-day rule.",
            "eyebrow": "Council guide", "h1": "City of Busselton tiny home rules", "crumb": "Busselton tiny homes",
            "answer": "<p>The City of Busselton can approve living in <strong>one</strong> caravan or <strong>tiny home on wheels</strong> per lot for up to <strong>24 months</strong>. It must be up to <strong>12.5 m x 2.5 m x 4.3 m</strong>, no more than <strong>50 m²</strong> with any structures, on land zoned for a house, with a parking bay.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your land"), ("/tiny-home-council-application", "Applying to your council")],
            "sources": [("Temporary camping application checklist (private property), City of Busselton", "https://www.busselton.wa.gov.au/documents/13597/temporary-residential-camping-checklist")]}
