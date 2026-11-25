BODY = """
<h2>Two ways to approve a tiny home on wheels</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>As a building</th><th>As a caravan (camping approval)</th></tr></thead><tbody>
<tr><td>When it fits</td><td>Built, placed and fixed to the lot to meet the building code</td><td>Doesn't meet every part of the building code, or you want flexibility</td></tr>
<tr><td>Approval</td><td>Building permit (and planning if needed)</td><td>Shire approval for up to 24 months in a row</td></tr>
<tr><td>If you move it</td><td>The permit stays with the land, so you need a new one at the new site</td><td>Approval stays valid if the same tiny home comes back. A different one needs a new application</td></tr>
</tbody></table></div>
<p>The Shire notes tiny homes on wheels often struggle with the building code, especially sleeping lofts (headroom and stairs), footings and tie-downs, and energy ratings.</p>

<h2>The Shire's camping approval rules</h2>
<ul>
<li><strong>One</strong> tiny home on wheels per property.</li>
<li><strong>Rural zone:</strong> on a vacant lot or where a house already exists. <strong>Other zones:</strong> only where a house already exists.</li>
<li>Not allowed on a lot that already has a granny flat or two houses.</li>
<li>Built from domestic-grade materials with the look of a home, and generally meeting the building code.</li>
<li>Power, which can be off-grid solar.</li>
<li>Preferably connected to sewer or an existing septic system.</li>
<li>No reticulated water? A tiny home under 70 m² needs at least <strong>38,000 litres</strong> of drinking water storage, on top of 92,000 litres for the main house.</li>
<li><strong>50 m</strong> from all boundaries in the Rural zone, normal setbacks elsewhere.</li>
<li>In a bushfire prone area, sited at BAL-29 or lower.</li>
<li><strong>No short-stay rental.</strong></li>
</ul>
<p>Converted buses, caravans, sea containers and park homes don't count as tiny homes on wheels under this policy.</p>
<p>Call the Shire on (08) 9848 0300. See <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules</a>, the <a href="/tiny-home-stay-calculator">stay calculator</a> and <a href="/tiny-home-services">connecting services</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in the Shire of Denmark?",
     "Yes. Under its policy, the Shire can approve one tiny home on wheels per property for up to 24 months in a row, if the policy's conditions are met."),
    ("Can I put a tiny home on a vacant block in Denmark?",
     "Only in the Rural zone. In all other zones, the lot must already have a house."),
    ("Can I rent out my tiny home in Denmark?",
     "Not as short-stay accommodation. The Shire's policy says an approved tiny home on wheels can't be used for short-term rental."),
    ("What setback does a tiny home need in Denmark's Rural zone?",
     "The policy says it should be 50 m from all lot boundaries in the Rural zone."),
]


def page(S):
    return {"path": "shire-of-denmark-tiny-homes.html", "published": "2026-11-26", "type": "Council guide", "icon": "pin",
            "card": "Shire of Denmark tiny home rules: the 24-month approval, one per lot, zones, water and setbacks.",
            "title": "Shire of Denmark Tiny Home Rules (2026)",
            "desc": "Shire of Denmark tiny home on wheels policy: building permit vs 24-month camping approval, one per lot, rural and residential zones, water tanks, 50 m rural setbacks and no short-stay rental.",
            "eyebrow": "Council guide", "h1": "Shire of Denmark tiny home rules", "crumb": "Denmark tiny homes",
            "answer": "<p>The Shire of Denmark can approve <strong>one tiny home on wheels</strong> per property for up to <strong>24 months</strong> at a time. Outside the Rural zone, the lot must already have a house. In the Rural zone it should be <strong>50 m</strong> from boundaries, and it can't be used for short-stay rental.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/tiny-home-stay-calculator", "Tiny home stay calculator"), ("/tiny-home-services", "Tiny home services")],
            "sources": [("Semi-permanent approvals for tiny homes on wheels policy (adopted 26 Nov 2024), Shire of Denmark", "https://www.denmark.wa.gov.au/documents/11408/policy-semi-permanent-approvals-for-tiny-homes-on-wheels")]}
