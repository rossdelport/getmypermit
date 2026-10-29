BODY = """
<h2>The standard distances</h2>
<p>Most Perth house lots follow the R-Codes, the state's housing rules. For sheds and other outbuildings, the standard (deemed-to-comply) distances to a side or rear fence are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Your shed</th><th>Distance to a side or rear fence</th></tr></thead><tbody>
<tr><td>Wall up to 9 m long and up to 2.4 m high</td><td>1 m</td></tr>
<tr><td>Wall longer than 9 m</td><td>1.5 m</td></tr>
<tr><td>Wall higher than 3.5 m</td><td>More, and it already needs planning approval because of the height</td></tr>
<tr><td>Facing the side street on a corner lot (R20)</td><td>1.5 m</td></tr>
<tr><td>In the front yard (street setback)</td><td>Not allowed without planning approval</td></tr>
</tbody></table></div>
<p>The distance is measured from the wall at right angles to the boundary. The same rules cap the shed's wall height at 2.4 m and the roof ridge at 4.2 m, measured from natural ground level.</p>

<h2>Can a shed go right against the fence?</h2>
<p>Often, yes, but not automatically. A shed wall built on or very close to the boundary is treated as a <strong>boundary wall</strong>. Joondalup, for example, treats any wall closer than 600 mm to the boundary as a boundary wall. Boundary walls have their own limits on height and length, and many councils have local policies that are more relaxed for small garden sheds.</p>
<p>If your shed doesn't fit the standard rules or your council's policy, you need <strong>planning approval</strong> before the building permit. Council may ask your neighbours for comments. That's normal, and plenty of these are approved.</p>

<h2>Small sheds are not exempt from setbacks</h2>
<p>A freestanding shed of 10 m&sup2; or less and no taller than 2.4 m usually doesn't need a <strong>building permit</strong>. It can still need <strong>planning approval</strong> if it sits closer to the fence than the rules allow. As the City of Joondalup puts it, small outbuildings "do not require a building permit but may still require planning approval".</p>

<h2>Fire safety close to the boundary</h2>
<p>The building code has its own rules for buildings near a boundary or near your house. A shed very close to the fence may need fire-resistant walls or other measures, depending on its size and what it is built from. Your shed supplier's engineering and the permit plans show how this is met.</p>

<h2>Other things that move your shed</h2>
<ul>
<li><strong>Sewer lines and easements.</strong> You generally can't build over them without permission from the Water Corporation or whoever holds the easement.</li>
<li><strong>Your house.</strong> Keep space for access, windows and drainage. Building code fire rules can apply between a shed and the house too.</li>
<li><strong>Estate rules.</strong> Newer estates often have a local development plan with different setbacks. Check yours before you order the shed.</li>
<li><strong>Retaining walls.</strong> If the shed sits on a retaining wall at the boundary, the wall height counts as part of the shed's wall height.</li>
</ul>

<h2>How to check your own lot</h2>
<ol>
<li>Find your R-Code and any local policies on your council's online map or planning page.</li>
<li>Measure the shed's wall length and height, and the distance from each wall to the fence.</li>
<li>Compare with the table above and your council's outbuilding policy.</li>
<li>If anything is closer, longer or higher, plan for planning approval first.</li>
</ol>
"""

FAQS = [
    ("Can I put a shed 500 mm from the fence?",
     "Sometimes. Under the standard rules the distance is 1 m, so 500 mm needs your council's local policy to allow it, or planning approval. Many councils approve this for small sheds."),
    ("Do I need my neighbour's permission to build a shed near the fence?",
     "Not usually. If planning approval is needed, council may ask your neighbour for comments, but the decision is council's. If footings or the roof will cross onto their land, you need their written consent on a BA20 form."),
    ("How far from the house should a shed be?",
     "There is no single planning distance, but building code fire rules can apply when a shed is close to the house. Leave room for access, windows and drainage, and check the engineering."),
    ("Is the distance measured to the fence or the boundary?",
     "To the boundary. Fences are not always on the exact boundary, so if it is tight, check the survey pegs or your site plan."),
]


def page(S):
    return {"path": "how-close-can-a-shed-be-to-the-fence.html", "published": "2026-10-29", "type": "Question answer", "icon": "pin",
            "card": "The standard distances from a side or rear fence, when a shed can go on the boundary, and what needs approval.",
            "title": "How Close Can a Shed Be to the Fence in WA? (2026 Rules)",
            "desc": "Under WA's standard rules a shed wall up to 9 m long sits 1 m from a side or rear fence. When it can go closer or on the boundary, and what needs planning approval.",
            "eyebrow": "Question answer", "h1": "How close can a shed be to the fence in WA?", "crumb": "How close can a shed be to the fence?",
            "answer": "<p>Under the standard WA rules, a shed wall up to 9 m long and 2.4 m high should be <strong>1 m from a side or rear fence</strong>, or 1.5 m if the wall is longer. Closer, or right on the boundary, is often possible, but it needs your council's local policy to allow it or <strong>planning approval</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/garage-building-permit", "Garage building permits"), ("/retrospective-shed-approval", "Retrospective shed approval")],
            "sources": [("Outbuildings information sheet (City of Joondalup)", "https://api.joondalup.wa.gov.au/files/Outbuildings.pdf"),
                        ("Residential Design Codes (WA Government)", "https://www.wa.gov.au/government/document-collections/residential-design-codes")]}
