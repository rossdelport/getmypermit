BODY = """
<h2>The permit rules are the same</h2>
<p>A council doesn't care whether your shed came in a kit or was designed from scratch. Both are Class 10a buildings, and both follow the same rules. The state has said there are <strong>no special exemptions</strong> for prefabricated or kit buildings, and warns that "permit-free" claims can be misleading.</p>
<p>A shed usually needs no building permit only if it's freestanding, <strong>10 m² or less</strong>, no more than <strong>2.4 m</strong> high, and not in wind region C or D. Anything bigger needs a permit, kit or not.</p>

<h2>Who does what</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Kit shed</th><th>Custom shed</th></tr></thead><tbody>
<tr><td>Structural engineering</td><td>May be supplied by the kit maker for your wind rating</td><td>Your builder or designer arranges it</td></tr>
<tr><td>Site plan</td><td>Usually yours to provide</td><td>Usually drawn by the builder or a drafter</td></tr>
<tr><td>Floor plan and elevations</td><td>May be included in the kit paperwork</td><td>Drawn to suit the design</td></tr>
<tr><td>Lodging the application</td><td>Usually you, unless the supplier offers it</td><td>Often the builder, but check your contract</td></tr>
<tr><td>Who builds it</td><td>You, or an installer</td><td>The builder</td></tr>
</tbody></table></div>
<p>Kit suppliers vary. Some say they handle the forms, drawings and engineering; others only send drawings. Ask in writing what's included before you buy.</p>

<h2>What councils ask for</h2>
<p>The Shire of Serpentine-Jarrahdale's list is typical:</p>
<ul>
<li>A BA1 or BA2 form, with all owners named</li>
<li>A site plan at 1:200 showing setbacks, shed size, soak wells or tanks, easements and any septic system</li>
<li>A floor plan and elevations at 1:100</li>
<li>Engineering signed by a structural engineer, covering footings, slab and tie-downs</li>
</ul>
<p>The Town of Mosman Park says every shed needing a permit must be certified by a structural engineer, whichever form you use. Serpentine-Jarrahdale also says a <strong>second-hand</strong> shed needs a recent engineer's sign-off for the new site, and a shed within 6 m of a house in a bushfire-prone area may need a BAL assessment.</p>

<h2>Do I need a registered builder?</h2>
<p>From 1 July 2026, a Class 10a building such as a shed or garage under <strong>$50,000</strong> doesn't need a registered builder, and an owner can build it without owner-builder approval. Over $50,000, the state says a prefab or kit building that needs a permit must be put up by a registered builder or an approved owner-builder.</p>
<p>Not sure what the site plan needs? See <a href="/shed-site-plan">how to draw a shed site plan</a>, check your size with the <a href="/shed-size-checker">shed size checker</a>, or read <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>.</p>
"""

FAQS = [
    ("Does a kit shed need council approval in WA?",
     "Yes, if it's over 10 m², over 2.4 m high, attached to another building or in wind region C or D. There are no special exemptions for kit or prefabricated buildings."),
    ("Does the kit shed company get the permit for me?",
     "Some say they do, others only supply drawings and engineering. Ask the supplier in writing what's included before you buy."),
    ("Do I need an engineer for a kit shed?",
     "Usually yes. Councils such as Mosman Park and Serpentine-Jarrahdale ask for engineering signed by a structural engineer. Some kit makers supply it for your wind rating."),
    ("Can I put up a second-hand kit shed?",
     "Yes, with a permit if it's over the size limits. Serpentine-Jarrahdale asks for a recent engineer's sign-off for the new site."),
    ("Do I need a registered builder for a kit shed?",
     "Not if it's under $50,000. From 1 July 2026 an owner can build a Class 10a shed under $50,000 without a registered builder or owner-builder approval."),
]


def page(S):
    return {"path": "kit-shed-vs-custom-shed.html", "published": "2026-11-10", "type": "Comparison", "icon": "shed",
            "card": "Same permit rules, different paperwork. Who supplies the engineering, plans and application.",
            "title": "Kit Shed vs Custom Shed: Who Handles the Permit? (WA)",
            "desc": "Kit shed or custom-built shed in WA: the permit rules are the same. Who supplies the engineering, site plan and application, and what councils ask for.",
            "eyebrow": "Comparison", "h1": "Kit shed vs custom shed: who handles the permit?", "crumb": "Kit vs custom shed",
            "answer": "<p>The permit rules are <strong>the same</strong> for kit and custom sheds: anything over 10 m² or 2.4 m high usually needs a building permit. The difference is paperwork. Kit makers may supply engineering and drawings, but you usually do the site plan and lodge it. With a custom shed, the builder often handles it, but check your contract.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-site-plan", "How to draw a shed site plan"), ("/shed-size-checker", "Shed size checker"), ("/how-to-get-a-shed-permit", "How to get a shed permit")],
            "sources": [("Consumers urged to do groundwork on DIY prefabricated pods and buildings (WA Government, July 2026)", "https://www.wa.gov.au/government/announcements/consumers-urged-do-groundwork-diy-prefabricated-pods-and-buildings"),
                        ("Sheds, garages and workshops (Shire of Serpentine-Jarrahdale)", "https://www.sjshire.wa.gov.au/planning-building-and-roads/building/building-advice/sheds-garages-and-workshops.aspx"),
                        ("Building a shed or outbuilding (Town of Mosman Park)", "https://www.mosmanpark.wa.gov.au/build/building-or-renovating/building-a-shed-or-outbuilding/"),
                        ("Building or renovating your home (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home")]}
