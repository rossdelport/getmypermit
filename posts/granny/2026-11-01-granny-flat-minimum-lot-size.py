BODY = """
<h2>What changed in 2024</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Before (R-Codes 2021)</th><th>Now (R-Codes Volume 1, 2024)</th></tr></thead><tbody>
<tr><td>Minimum lot size</td><td>350 m&sup2;</td><td><strong>None</strong></td></tr>
<tr><td>Maximum size</td><td>70 m&sup2; internal floor area</td><td>70 m&sup2; internal floor area</td></tr>
<tr><td>Grouped dwellings and strata lots</td><td>Not allowed under the exemption</td><td>Allowed, at all density codes in Volume 1</td></tr>
<tr><td>Who can live there</td><td colspan="2">Anyone: family, friends or tenants</td></tr>
</tbody></table></div>
<p>The changes took effect in mid-April 2024. Some websites still quote 350 m&sup2; or 450 m&sup2; minimums. Those are out of date.</p>

<h2>So can any lot have a granny flat?</h2>
<p>Any size lot can, <strong>if the granny flat fits the standard rules</strong> (the "deemed-to-comply" rules). Those include:</p>
<ul>
<li><strong>Setbacks</strong> from the boundaries, including your scheme's setbacks.</li>
<li><strong>Site cover</strong>: the lot must keep its required open space with the granny flat added.</li>
<li><strong>Height.</strong></li>
<li><strong>Visual privacy</strong> towards the neighbours.</li>
<li><strong>Access</strong> to the granny flat.</li>
</ul>
<p>On a small lot, open space and setbacks are usually what stop a granny flat, not a minimum lot size. If yours can't meet one of the rules, it isn't refused automatically; it just needs <strong>planning approval</strong>, where council assesses it on its merits.</p>

<h2>Parking</h2>
<p>In most cases a granny flat doesn't need its own parking bay. The exception is some densities and locations far from public transport, where a car is more likely to be needed.</p>

<h2>A building permit is always needed</h2>
<p>Skipping planning approval doesn't mean skipping the building permit. Every granny flat needs one and must meet the National Construction Code.</p>
"""

FAQS = [
    ("What is the minimum lot size for a granny flat in WA?",
     "There isn't one any more. The 350 m&sup2; minimum was removed in the R-Codes Volume 1 (2024), effective mid-April 2024. A granny flat of up to 70 m&sup2; can go on any size lot if it meets the deemed-to-comply rules."),
    ("Can I build a granny flat on a 300 m² block in Perth?",
     "Possibly. There's no minimum lot size, but it must meet the setbacks, open space, height, privacy and access rules. On small lots, open space is often the limit. If it can't meet them, it needs planning approval."),
    ("Can I build a granny flat on a strata lot?",
     "Since 2024 the R-Codes allow granny flats on grouped dwelling and strata lots at all density codes in Volume 1, subject to the same deemed-to-comply rules."),
    ("Does a granny flat need its own parking bay in WA?",
     "Usually not. A parking bay is only required at some densities and in locations far from public transport."),
]


def page(S):
    return {"path": "granny-flat-minimum-lot-size.html", "published": "2026-11-01", "type": "Question answer", "icon": "granny",
            "card": "The 350 m² minimum was removed in 2024. What limits a granny flat on a small lot now.",
            "title": "Is There a Minimum Lot Size for a Granny Flat in WA? (2026)",
            "desc": "No. WA removed the 350 m² minimum lot size for granny flats in April 2024. What now decides if a granny flat fits: setbacks, open space, height, privacy and access.",
            "eyebrow": "Question answer", "h1": "Is there a minimum lot size for a granny flat?", "crumb": "Minimum lot size",
            "answer": "<p><strong>No.</strong> The old 350 m&sup2; minimum was removed in the <strong>R-Codes Volume 1 (2024)</strong>, from mid-April 2024. A granny flat of up to 70 m&sup2; can go on any size lot, including strata lots, as long as it meets the standard rules for setbacks, open space, height, privacy and access.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-no-planning-approval", "Granny flat with no planning approval"), ("/granny-flat-cost-perth", "Granny flat cost in Perth")],
            "sources": [("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
