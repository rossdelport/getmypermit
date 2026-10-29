BODY = """
<h2>Step 1: Sort the approval before it arrives</h2>
<p>Do this first, because it decides where the home can go and how long it can stay.</p>
<div class="table-wrap"><table>
<thead><tr><th>Your plan</th><th>Approval you need</th></tr></thead><tbody>
<tr><td>Stay in it on wheels for a few nights</td><td>Up to 5 nights: the landowner's permission only</td></tr>
<tr><td>Live in it on wheels longer (for example while building a house)</td><td>Council approval under the caravan rules, for up to 24 months at a time</td></tr>
<tr><td>Put it on footings as a home</td><td>A <strong>building permit</strong> before it is placed, and planning approval if it doesn't meet the standard rules</td></tr>
</tbody></table></div>
<p>Without approval or an exemption, living in a caravan or tiny home on wheels outside a licensed park is an offence, on private or public land.</p>

<h2>Step 2: Check it can legally travel</h2>
<p>A tiny home on wheels is a trailer when it is on the road. Main Roads WA says a vehicle or combination over any of these limits needs a permit or order:</p>
<div class="table-wrap"><table>
<thead><tr><th>Limit</th><th>Without a permit</th></tr></thead><tbody>
<tr><td>Width</td><td><strong>2.5 m</strong></td></tr>
<tr><td>Height</td><td><strong>4.3 m</strong></td></tr>
<tr><td>Length of a combination (tow vehicle plus tiny home)</td><td>19 m</td></tr>
</tbody></table></div>
<p>Most tiny homes are built to 2.5 m wide and under 4.3 m high so they can travel without a permit. Anything bigger is an oversize load, which needs a Main Roads permit and often escort vehicles. Western Power treats any load 4.3 m high or more as oversize, and it needs Western Power's authorisation too ($120 online in the Perth network) because of overhead power lines. The trailer generally needs to be licensed, and the tow vehicle must be rated for its weight. A specialist transport company will handle most of this.</p>

<h2>Step 3: Check the site access</h2>
<ul>
<li><strong>Width and turns.</strong> Walk the route from the street to the spot. Gates, side paths, trees and tight turns stop more deliveries than anything else.</li>
<li><strong>Overhead.</strong> Look for power lines, eaves and branches along the route.</li>
<li><strong>Ground.</strong> Soft sand or lawn may not hold a heavy trailer. Some deliveries need a crane instead, which needs a clear lift path and somewhere for the crane to stand.</li>
<li><strong>The verge.</strong> Heavy vehicles can damage the kerb and footpath. Some councils require a verge permit or bond for building work.</li>
</ul>

<h2>Step 4: Prepare the pad and services</h2>
<ul>
<li><strong>On wheels:</strong> a level, firm base, with the wheels kept on so the home stays movable. Council approval can require it to stay roadworthy and able to leave quickly, for example in a bushfire.</li>
<li><strong>On footings:</strong> footings designed by an engineer, built under the building permit.</li>
<li><strong>Services:</strong> power from the main switchboard by a licensed electrician, water by a licensed plumber, and sewer or an approved septic system. Council approval for a tiny home on wheels can require power, water, sewage and cooking facilities.</li>
</ul>

<h2>Step 5: After it lands</h2>
<p>For a home on footings, the builder lodges the notice of completion (BA7) within 7 days of finishing. For a home on wheels, keep a copy of your council approval and diary the expiry date so you can re-apply in time.</p>
"""

FAQS = [
    ("How wide can a tiny home be to tow without a permit in WA?",
     "2.5 m wide and 4.3 m high. Main Roads WA treats anything over those limits as a restricted access vehicle that needs a permit."),
    ("Do I need council approval before delivering a tiny home?",
     "If anyone will live in it for more than 5 nights, yes: council approval under the caravan rules for a home on wheels, or a building permit for a home on footings."),
    ("Can a crane lift a tiny home into my backyard?",
     "Often, yes. You'll need a clear lift path, space for the crane to set up, and sometimes a council permit to use the street or verge."),
    ("Can I take the wheels off later?",
     "Yes, but it then becomes a dwelling and needs a building permit, so it must meet the building code like any house or granny flat."),
]


def page(S):
    return {"path": "moving-a-tiny-home.html", "published": "2026-10-30", "type": "How-to guide", "icon": "pin",
            "card": "Approvals first, then road limits, site access, the pad and services: how to get a tiny home onto your land in WA.",
            "title": "How to Move a Tiny Home Onto Your Land in WA (Step by Step)",
            "desc": "Moving a tiny home onto your land in WA: the approvals you need first, the 2.5 m wide and 4.3 m high road limits, site access, cranes, the pad and connecting services.",
            "eyebrow": "How-to guide", "h1": "How to move a tiny home onto your land", "crumb": "Moving a tiny home",
            "answer": "<p>Get the <strong>approval first</strong> (council approval to live in it on wheels, or a building permit to put it on footings). Then check it is within the road limits of <strong>2.5 m wide and 4.3 m high</strong>, walk the access route, prepare a level pad and have licensed trades connect power, water and sewer.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels: WA rules"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/shire-of-mundaring-tiny-homes", "Shire of Mundaring tiny home rules")],
            "sources": [("Permits, orders and schemes: vehicle size limits (Main Roads WA)", "https://www.mainroads.wa.gov.au/heavy-vehicles/permit-order-scheme/"),
                        ("Oversize loads and powerline safety (Western Power)", "https://www.westernpower.com.au/issues-enquiries/requests-preferences/oversize-vehicles/"),
                        ("Temporary accommodation and camping outside of caravan parks (WA Government, updated June 2026)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks")]}
