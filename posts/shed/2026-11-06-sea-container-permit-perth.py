BODY = """
<h2>Why containers are different</h2>
<p>Perth councils often have a separate planning policy just for sea containers (also called shipping containers). They don't treat a container like a normal garden shed, so the shed size rules you may have read about don't simply apply. The City of Wanneroo, for example, says containers are not assessed as "outbuildings" under the R-Codes.</p>

<h2>Two councils, two very different answers</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>City of Cockburn</th><th>City of Wanneroo</th></tr></thead><tbody>
<tr><td>Container kept on a normal home block</td><td>Not allowed, except while you build (see below)</td><td>Needs planning approval unless it meets the scheme and R-Codes standard rules</td></tr>
<tr><td>Storage while you build</td><td>Up to 18 months, with planning approval, one container at a time</td><td>Allowed without planning approval once a building permit is issued; remove within 14 days of finishing</td></tr>
<tr><td>Moving house</td><td>Not covered by the policy</td><td>Up to 7 days without planning approval</td></tr>
<tr><td>Rural or rural living lots</td><td>One container up to 6 m, with planning approval</td><td>Needs planning approval</td></tr>
<tr><td>On the verge</td><td>Up to 14 days, 6 m maximum, by request to the City</td><td>Covered by local laws, not this policy</td></tr>
</tbody></table></div>

<h2>Conditions councils usually set</h2>
<ul>
<li>Behind the house and screened from the street and neighbours</li>
<li>Painted to match the house or the landscape, and kept in good repair</li>
<li>Used for storage only (Cockburn rules out living, business or industrial use)</li>
<li>Not in car parking bays or blocking access</li>
<li>No refrigerated containers on home or rural lots (Cockburn)</li>
</ul>

<h2>Does it need a building permit too?</h2>
<p>Often, yes, if it's set up and used as a building. Building and Energy says there are <strong>no special exemptions</strong> for prefabricated buildings, and councils can take action if one goes up without the right approvals. A container fitted out as a workshop, studio or room is the clearest case. Any power or plumbing must be done by licensed trades.</p>
<p>If you want to live or work in it, the rules get much stricter. Wanneroo says a container used for habitable purposes must meet all relevant laws, like any other home.</p>

<h2>What to do</h2>
<ol>
<li>Check your council's sea container policy (search "[your council] sea container policy").</li>
<li>If it needs planning approval, apply for that first.</li>
<li>Then check whether a building permit is needed for how you'll use it.</li>
</ol>
<p>Not sure if a normal shed would be simpler? Try our <a href="/shed-size-checker">shed size checker</a> or read <a href="/do-i-need-a-permit-for-a-shed">do I need a permit for a shed?</a></p>
"""

FAQS = [
    ("Do I need council approval for a sea container in Perth?",
     "Usually, yes, unless it's short-term. Many councils have a sea container policy. Cockburn doesn't allow them on residential lots except during building works, and Wanneroo needs planning approval unless the container meets its standard rules."),
    ("Can I keep a shipping container in my backyard?",
     "It depends on your council. Some allow it with planning approval and conditions like screening and painting. Others, like Cockburn, don't allow them on residential lots except while you build."),
    ("How long can a sea container stay on my property?",
     "In Wanneroo, up to 7 days for moving house, or during building works until 14 days after they finish. In Cockburn, up to 18 months during building works, with planning approval."),
    ("Does a shipping container need a building permit?",
     "Often, if it's used as a building. Building and Energy says there are no special exemptions for prefabricated buildings. Check with your council."),
    ("Can I live in a shipping container in WA?",
     "Only if it meets all the rules for a home. Wanneroo says containers used for habitable purposes must comply with all relevant laws, and Cockburn's policy limits them to storage."),
]


def page(S):
    return {"path": "sea-container-permit-perth.html", "published": "2026-11-06", "type": "Question answer", "icon": "shed",
            "card": "Why councils treat containers differently, with Cockburn and Wanneroo compared.",
            "title": "Do You Need a Permit for a Sea Container in Perth?",
            "desc": "Sea container approval in Perth: council container policies, Cockburn vs Wanneroo rules, time limits, conditions, and when a building permit is needed.",
            "eyebrow": "Question answer", "h1": "Do you need a permit for a sea container in Perth?", "crumb": "Sea container permits",
            "answer": "<p><strong>Usually yes, unless it's short-term.</strong> Many Perth councils have their own sea container policy, and it's often stricter than the shed rules. Cockburn doesn't allow containers on home lots except during building works. Wanneroo needs planning approval unless the container meets its standard rules. A container used as a building may need a building permit too.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/city-of-wanneroo-shed-rules", "City of Wanneroo shed rules")],
            "sources": [("Sea Containers, LPP 5.8 (City of Cockburn)", "https://www.cockburn.wa.gov.au/getattachment/5b69177d-38a1-470f-a7bf-bfac2bb76990/ECM_4516539_v9_Sea-Containers-LPP5-docx.aspx"),
                        ("Sea Containers, LPP 2.10 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/3780/sea_containers_-_lpp_210.pdf"),
                        ("Consumers urged to do groundwork on DIY prefabricated pods and buildings (Building and Energy, July 2026)", "https://www.wa.gov.au/government/announcements/consumers-urged-do-groundwork-diy-prefabricated-pods-and-buildings")]}
