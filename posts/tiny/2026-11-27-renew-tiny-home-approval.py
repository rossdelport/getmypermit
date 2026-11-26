BODY = """
<h2>How the 24-month approval works</h2>
<p>Under WA's Caravan Parks and Camping Grounds Regulations, living in a caravan or tiny home on wheels on private land works like this:</p>
<div class="table-wrap"><table>
<thead><tr><th>How long</th><th>Who needs to approve</th></tr></thead><tbody>
<tr><td>Up to 5 nights</td><td>The property owner</td></tr>
<tr><td>Up to 24 months</td><td>The property owner and the local council</td></tr>
<tr><td>After 24 months (re-applying)</td><td>The property owner and the local council again</td></tr>
</tbody></table></div>
<p>So there's no automatic extension. When your approval is close to ending, you <strong>re-apply</strong>. Work out your dates with the <a href="/tiny-home-stay-calculator">stay calculator</a>.</p>

<h2>Steps to re-apply</h2>
<ol>
<li><strong>Check your end date</strong> on your current approval, and start early so there's no gap.</li>
<li><strong>Get the owner's written OK</strong> again, if you're not the owner.</li>
<li><strong>Lodge a new application</strong> with your council on its "approval to camp" form.</li>
<li><strong>Show the conditions are still met.</strong> Councils can attach health and safety conditions, such as enough power, water, sewage and cooking facilities.</li>
<li><strong>Tell the council about changes.</strong> In the Shire of Denmark, for example, a <strong>different</strong> tiny home needs a new application, while the same one leaving and coming back keeps its approval.</li>
</ol>

<h2>If the council says no</h2>
<p>The Minister for Local Government can consider a camping approval if a council refuses or revokes one. An approval given by the Minister can't be revoked by the council.</p>

<h2>Want to stay for good?</h2>
<p>Living permanently is a different path. A tiny home built and fixed to the ground to meet the building code can get a <strong>building permit</strong>, like any small home. See <a href="/fixed-tiny-home-permit">fixed tiny home permits</a> and <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules</a>.</p>
<p>Councils vary, so check your own council's form and conditions.</p>
"""

FAQS = [
    ("What happens when my 24-month tiny home approval ends in WA?",
     "You re-apply. The State's fact sheet says re-applying after 24 months needs approval from the property owner and the local government again."),
    ("Is a tiny home approval renewed automatically?",
     "No. You need to lodge a new application with your council before the current approval ends."),
    ("What if my council refuses my tiny home application?",
     "The Minister for Local Government can consider a camping approval if a council refuses or revokes one, and the council can't revoke the Minister's approval."),
    ("Do I need a new approval if I swap tiny homes?",
     "Often yes. In the Shire of Denmark, a different tiny home needs a new application, while the same one coming back keeps its approval."),
]


def page(S):
    return {"path": "renew-tiny-home-approval.html", "published": "2026-11-27", "type": "How-to guide", "icon": "doc",
            "card": "How to renew your tiny home approval after 24 months: who approves, the steps and what if it's refused.",
            "title": "How to Renew Your Tiny Home Approval After 24 Months (WA)",
            "desc": "How to renew a tiny home on wheels approval in WA after 24 months: re-applying to your council and the owner, conditions councils set, swapping tiny homes, and the Minister's role if refused.",
            "eyebrow": "How-to guide", "h1": "How to renew your tiny home approval after 24 months", "crumb": "Renew tiny home approval",
            "answer": "<p>In WA, a council can approve a tiny home on wheels on private land for up to <strong>24 months</strong>. It doesn't renew itself. Before it ends, <strong>re-apply</strong> to your council with the owner's OK again. If the council refuses, the <strong>Minister for Local Government</strong> can consider it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-stay-calculator", "Tiny home stay calculator"), ("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/fixed-tiny-home-permit", "Fixed tiny home permit")],
            "sources": [("Temporary accommodation and camping outside of caravan parks (updated 18 June 2026), Government of WA", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Semi-permanent approvals for tiny homes on wheels policy, Shire of Denmark", "https://www.denmark.wa.gov.au/documents/11408/policy-semi-permanent-approvals-for-tiny-homes-on-wheels")]}
