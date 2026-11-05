BODY = """
<h2>The approvals are the same</h2>
<p>A lot of transportable and "DIY" granny flats are sold as if they skip the paperwork. They don't. In July 2026 Building and Energy and Consumer Protection warned that "DIY" and "permit-free" claims for prefabricated buildings may be misleading. There are <strong>no special exemptions</strong> for prefabricated buildings.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Transportable (built in a factory)</th><th>Built on site</th></tr></thead><tbody>
<tr><td>Planning approval</td><td>Not needed if it meets the deemed-to-comply rules, including <strong>70 m²</strong> or less</td><td>Same</td></tr>
<tr><td>Building permit</td><td>Needed</td><td>Needed</td></tr>
<tr><td>Registered builder</td><td>Needed if the permit is required and it's worth over <strong>$20,000</strong> (unless you're an approved owner-builder)</td><td>Same</td></tr>
<tr><td>Power and plumbing</td><td>Licensed electrician and plumber</td><td>Same</td></tr>
<tr><td>Where the work happens</td><td>Mostly in a factory, then delivered and installed</td><td>On your block</td></tr>
<tr><td>Site access</td><td>Usually needs room for a truck and often a crane</td><td>Normal builder access</td></tr>
</tbody></table></div>

<h2>Where they really differ</h2>
<h3>Payments</h3>
<p>Consumer Protection's advice for modular homes: pay only a <strong>small deposit</strong>, then make progress payments tied to real stages, such as delivery of materials, manufacturing stages and installation. Ask for proof that each stage is done before you pay, for example a visit to the factory.</p>
<h3>Who's responsible</h3>
<p>The builder named on the building permit is responsible for making sure the finished building meets the standards. With a transportable, make sure you know who that is: the factory, the installer, or both.</p>
<h3>Getting it onto the block</h3>
<p>A transportable has to be trucked in and placed. Check the route, driveway width, overhead power lines and trees before you sign. A built-on-site flat avoids this, but takes longer on your property.</p>

<h2>Questions to ask either type of builder</h2>
<ul>
<li>Will you put in writing that the building and work meet all legal requirements?</li>
<li>Who applies for the building permit, and who is named as the builder?</li>
<li>What exactly is included: footings, connection to services, stormwater, steps, delivery and crane?</li>
<li>What does the home indemnity insurance cover?</li>
</ul>
<p>For more on picking a builder, read <a href="/choosing-a-granny-flat-builder">choosing a granny flat builder</a>. To check the size limit, use the <a href="/granny-flat-size-calculator">70 m² calculator</a>.</p>
"""

FAQS = [
    ("Do transportable granny flats need council approval in WA?",
     "Yes. They need a building permit like any granny flat. Planning approval isn't needed if the flat meets the deemed-to-comply rules, including being 70 m² or less."),
    ("Are DIY granny flat kits permit-free in WA?",
     "No. Building and Energy and Consumer Protection have warned that DIY and permit-free claims may be misleading. There are no special exemptions for prefabricated buildings."),
    ("Do I need a registered builder for a transportable granny flat?",
     "Yes, if it needs a building permit and is worth over $20,000, unless you're an approved owner-builder."),
    ("How should I pay for a transportable granny flat?",
     "Consumer Protection recommends a small deposit, then progress payments linked to stages like materials delivery, manufacturing and installation, with proof each stage is done."),
    ("Is a transportable or built-on-site granny flat easier to approve?",
     "Neither. The planning and building rules are the same. The differences are in how it's built, paid for and delivered."),
]


def page(S):
    return {"path": "transportable-vs-built-granny-flat.html", "published": "2026-11-06", "type": "Comparison", "icon": "granny",
            "card": "Same approvals either way. What really differs: payments, delivery and who's responsible.",
            "title": "Transportable vs Built-on-Site Granny Flat (WA)",
            "desc": "Transportable vs built-on-site granny flats in WA: the approvals are the same, plus the real differences in payments, delivery and builder responsibility.",
            "eyebrow": "Comparison", "h1": "Transportable vs built-on-site granny flat", "crumb": "Transportable vs built",
            "answer": "<p><strong>The approvals are the same.</strong> Both need a building permit, both skip planning approval if they meet the rules (including 70 m² or less), and both need a registered builder if over $20,000. The real differences are how you pay, how it gets onto your block, and who's responsible for the finished building.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/choosing-a-granny-flat-builder", "Choosing a granny flat builder"), ("/granny-flat-size-calculator", "Granny flat 70 m² calculator"), ("/granny-flat-approval-process", "Granny flat approval process")],
            "sources": [("Consumers urged to do groundwork on DIY prefabricated pods and buildings (Building and Energy, July 2026)", "https://www.wa.gov.au/government/announcements/consumers-urged-do-groundwork-diy-prefabricated-pods-and-buildings"),
                        ("Modular homes (Consumer Protection WA)", "https://www.consumerprotection.wa.gov.au/modular-homes"),
                        ("Ancillary dwelling information sheet (WA Planning)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
