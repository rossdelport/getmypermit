BODY = """
<h2>What a site plan is</h2>
<p>A site plan is a bird's-eye drawing of your whole block. It shows where the shed will go in relation to the boundaries and everything else on the lot. Councils use it to check setbacks and fire separation, and that the shed avoids pipes and easements. It's needed for most shed building permits, especially uncertified (BA2) applications.</p>

<h2>What councils ask to see</h2>
<p>Requirements vary a little, but these Perth councils' checklists overlap a lot:</p>
<ul>
<li><strong>All lot boundaries with their dimensions</strong> (City of Swan)</li>
<li><strong>The new shed, with its distance to every boundary</strong> (Swan, Wanneroo, Belmont)</li>
<li><strong>All existing buildings and structures</strong>, with distances to the shed (Swan says all existing structures must be shown)</li>
<li><strong>Ground levels</strong>: contour survey or spot levels, and the proposed finished floor level (Wanneroo, Belmont)</li>
<li><strong>Easements</strong> (Belmont)</li>
<li><strong>Septic systems</strong>, if you have one (Wanneroo)</li>
<li><strong>A north point</strong> (Wanneroo)</li>
</ul>

<h2>Scale</h2>
<p>Draw it to scale, usually <strong>1:200</strong> for a house block. The City of Swan suggests 1:200 for residential site plans and 1:100 for floor plans and elevations. Belmont and Wanneroo say a minimum of 1:200.</p>

<h2>Step by step</h2>
<ol>
<li><strong>Get your lot shape.</strong> Your certificate of title or a Landgate plan shows the boundary lengths.</li>
<li><strong>Get your existing house plans.</strong> Councils such as Stirling will supply copies of plans on record to the owner, which saves measuring.</li>
<li><strong>Find pipes and easements.</strong> Get free plans from Before You Dig Australia (or call 1100) and check your title. See <a href="/shed-over-sewer-or-easement">building a shed near a sewer</a>.</li>
<li><strong>Measure and mark the shed.</strong> Show its size and the distance from each wall to the nearest boundary and building.</li>
<li><strong>Add levels if the block slopes.</strong> On sloping blocks, councils may ask for a feature survey by a licensed surveyor.</li>
<li><strong>Label everything.</strong> Address, lot number, north point, scale and your name. Number all pages (Swan asks for "1 of 4" style numbering).</li>
</ol>

<h2>What else goes with it</h2>
<p>The site plan is one part of the package. Swan's checklist for Class 10 structures like sheds also lists working drawings (floor plan, elevations, cross section), structural engineer's certification, a termite management plan and, if the shed doesn't meet the R-Codes, a variation request with neighbours' comments.</p>
<p>Check the setbacks your shed needs with <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>, and see the full <a href="/how-to-get-a-shed-permit">shed permit process</a>.</p>
"""

FAQS = [
    ("What should a shed site plan show?",
     "All lot boundaries with dimensions, the shed and its distance to each boundary, all existing buildings, ground levels, easements, any septic system and a north point. Councils vary a little."),
    ("What scale should a shed site plan be?",
     "Usually 1:200 for a house block. Councils such as Swan, Belmont and Wanneroo ask for 1:200 site plans and 1:100 for elevations."),
    ("Can I draw my own shed site plan?",
     "Usually, yes. The council checklists ask for an accurate plan to scale showing the right details, not a particular drafter. Structural engineering must still come from an engineer."),
    ("Do I need to show sewer pipes on my site plan?",
     "Show easements and any nearby sewer or water pipes. Councils check these, and Water Corporation sets minimum distances from its pipes."),
    ("What else do I need with a shed site plan?",
     "Usually floor plans, elevations, structural engineering, the BA2 form and fees. Swan also lists a termite management plan."),
]


def page(S):
    return {"path": "shed-site-plan.html", "published": "2026-11-09", "type": "How-to guide", "icon": "plan",
            "card": "What to show, what scale to use, and a step-by-step way to draw it yourself.",
            "title": "How to Draw a Shed Site Plan for Council (WA)",
            "desc": "How to draw a shed site plan for a WA council: what to show (boundaries, setbacks, levels, easements), the right scale, and a step-by-step guide.",
            "eyebrow": "How-to guide", "h1": "How to draw a shed site plan for council", "crumb": "Shed site plan",
            "answer": "<p>Draw your block from above, usually at <strong>1:200</strong>. Show all boundaries with dimensions, the new shed and its distance to each boundary, all existing buildings, ground levels, easements, any septic system and a north point. You can usually draw it yourself if it's accurate and to scale.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-over-sewer-or-easement", "Building a shed near a sewer")],
            "sources": [("General checklist for uncertified Class 10 applications (City of Swan)", "https://www.swan.wa.gov.au/awcontent/Web/Documents/PlanBuildSubdivisionSpecifications/GENERAL_CHECKLIST_FOR_AN_UNCERTIFIED_Class_10s.pdf"),
                        ("Patios information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Patio, pergola or shade sail (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/i-want-to-build/patio,-pergola-or-shade-sail")]}
