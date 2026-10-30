BODY = """
<h2>The three rules that matter</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>What it means for you</th></tr></thead><tbody>
<tr><td>A shed is not lived in</td><td>WA councils define an outbuilding as a freestanding enclosed structure that is <strong>not lived in</strong>. A toilet or shower is fine; sleeping or living in it is not.</td></tr>
<tr><td>A licensed plumber does the plumbing</td><td>Apart from a few small jobs like changing a shower head, all water supply, sanitary and drainage plumbing in WA must be done by a licensed plumber.</td></tr>
<tr><td>Waste has to go somewhere approved</td><td>Connect to the sewer, or on a septic lot, get council approval for the septic system.</td></tr>
</tbody></table></div>

<h2>When it stops being a shed</h2>
<p>A toilet, basin or shower on its own is common in workshops, man caves and pool sheds. The trouble starts when a shed has a toilet, a shower <em>and</em> a kitchen and bed. At that point it looks like somewhere to live, and councils assess it as a <strong>dwelling</strong>, such as a granny flat. That means a different building standard (insulation, ceiling heights, energy efficiency, fire separation) and possibly planning approval.</p>
<p>The planning exemptions for sheds also depend on this. The City of Melville, for example, says a shed in a residential zone usually skips planning approval only if, among other things, it is <strong>non-habitable</strong>. If you want somewhere to live, <a href="https://grannyflatpermit.com.au/granny-flat-rules-wa">build it as a granny flat</a> from the start.</p>

<h2>The approvals for a shed with a bathroom</h2>
<ul>
<li><strong>Building permit.</strong> Most sheds need one anyway once they are over 10 m&sup2; or 2.4 m high. Show the toilet, shower and any wall linings on the plans.</li>
<li><strong>Plumbing.</strong> Your plumber handles the plumbing paperwork. For new fixtures, they must give you a <strong>certificate of compliance</strong> within five working days of finishing. Keep it, as buyers and insurers may ask for it.</li>
<li><strong>Septic.</strong> If your lot isn't on sewer, adding a toilet means a septic or treatment system, which needs council's health approval before it is installed.</li>
<li><strong>Electrical.</strong> Hot water, lighting and an exhaust fan need a licensed electrician.</li>
</ul>

<h2>Practical tips</h2>
<ul>
<li>Order a <strong>drainage plumbing diagram</strong> for your property before you pick the shed's spot. It shows where your sewer runs, so you can place the shed where connecting is cheapest.</li>
<li>Don't build over existing sewer or drainage pipes.</li>
<li>Remember the shed setbacks: usually 1 m from side and rear boundaries to skip planning approval. <a href="/how-close-can-a-shed-be-to-the-fence">How close can a shed be to the fence?</a></li>
</ul>
"""

FAQS = [
    ("Do I need a permit to put a toilet in my shed in WA?",
     "The plumbing must be done by a licensed plumber, who gives you a certificate of compliance. The shed itself needs a building permit if it is over 10 m&sup2; or 2.4 m high, and the toilet should be shown on the plans."),
    ("Can I put a shower in my shed?",
     "Yes, as long as a licensed plumber installs it and the shed is not used as somewhere to live. A shed with a bathroom, kitchen and bed is treated as a dwelling."),
    ("Can I live in my shed if it has a bathroom?",
     "No. A shed is an outbuilding that is not lived in. To live in it, it must be approved as a dwelling, such as a granny flat, which has stricter building rules."),
    ("Can I do the plumbing in my shed myself?",
     "No. WA homeowners can only do a few basic tasks, like replacing a shower head or a cistern washer. All other water supply, sanitary and drainage plumbing must be done by a licensed plumber."),
]


def page(S):
    return {"path": "toilet-or-shower-in-a-shed.html", "published": "2026-10-31", "type": "Question answer", "icon": "shed",
            "card": "Yes, usually, with a licensed plumber, as long as nobody lives in it. The rules, the approvals and where it goes wrong.",
            "title": "Can I Put a Toilet or Shower in My Shed in WA?",
            "desc": "You can usually add a toilet or shower to a shed in WA if a licensed plumber does it and nobody lives in it. Permits, septic, and when a shed becomes a dwelling.",
            "eyebrow": "Question answer", "h1": "Can I put a toilet or shower in my shed?", "crumb": "Toilet or shower in a shed",
            "answer": "<p><strong>Usually yes.</strong> A licensed plumber must do the work and give you a certificate of compliance, and the waste must go to the sewer or an approved septic system. The shed must stay a shed: if it has a bathroom, kitchen and bed, council treats it as a <strong>dwelling</strong>, which needs different approvals.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-size-checker", "Shed size checker")],
            "sources": [("Plumbing work in your home (Building and Energy, WA Government, updated July 2026)", "https://www.wa.gov.au/organisation/building-and-energy/plumbing-work-your-home"),
                        ("Building a shed or outbuilding (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Outbuilding (shed) (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)"),
                        ("Building documents: apparatus for the treatment of sewage application (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/building-advice/building-documents")]}
