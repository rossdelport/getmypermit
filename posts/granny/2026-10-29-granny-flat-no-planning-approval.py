BODY = """
<h2>Why it is worth designing for "no planning approval"</h2>
<p>Since 10 April 2024, a granny flat (the R-Codes call it an <strong>ancillary dwelling</strong>) that meets all the standard rules doesn't need planning approval on a residential lot of any size. That skips a step that can take up to 60 days and may involve your neighbours. You still need a building permit, but that is a shorter, more predictable process.</p>
<p>The trick is to design the granny flat around the rules from the start, instead of drawing it first and checking later.</p>

<h2>The design checklist</h2>
<ol>
<li><strong>Keep it to 70 m&sup2; or less inside.</strong> The limit is the internal floor area. Plan around 65 to 68 m&sup2; so small changes during design don't push you over. Ask your designer how your council measures it, as verandahs and alfresco areas are usually treated separately.</li>
<li><strong>Stay out of the street setback.</strong> Put the granny flat behind the front of the house or in the back yard.</li>
<li><strong>Meet the side and rear setbacks.</strong> Use the setbacks in the R-Codes and your council's local planning scheme for your lot's R-Code. Walls on the boundary have extra limits, so keep the granny flat off the boundary if you can.</li>
<li><strong>Keep enough open space.</strong> Every R-Code has a minimum share of the lot that must stay unroofed. The granny flat, house, patios and sheds all count. Small lots run out first.</li>
<li><strong>Stay single storey and low.</strong> Keep within the standard wall and roof heights. Floors, decks or windows more than 0.5 m above the ground that look over a neighbour bring in privacy setbacks, so a low, single-storey design avoids them.</li>
<li><strong>Give it its own access.</strong> A clear path from the street to the granny flat's front door is part of the standard rules.</li>
<li><strong>Check parking.</strong> In most cases no extra parking bay is needed. Some higher-density areas, and places far from public transport, are the exception.</li>
</ol>

<h2>When you will need planning approval anyway</h2>
<p>Even a perfect design needs planning approval in some places. Check these before you start:</p>
<ul>
<li><strong>Heritage-listed places and heritage areas.</strong></li>
<li><strong>Bushfire-prone areas</strong> with a high bushfire rating. The Shire of Mundaring, for example, says planning approval is likely needed in bushfire-prone areas.</li>
<li><strong>Rural and special rural zones</strong>, where the R-Codes may not apply in the same way. Many shires require planning approval there. <a href="/granny-flat-on-a-rural-lot">See granny flats on rural lots</a>.</li>
<li><strong>Estates with a local development plan</strong> or design guidelines that set different rules.</li>
<li><strong>Strata lots</strong>, which may also need the strata company's approval.</li>
</ul>

<h2>Watch out for old information</h2>
<p>The 350 m&sup2; minimum lot size was removed in 2024, and granny flats are now allowed on grouped dwelling and strata lots at all density codes. Some websites and even some council fact sheets still quote the old minimum. If you read "350 m&sup2;" or "450 m&sup2;", that information is out of date.</p>

<h2>What you still need: the building permit</h2>
<p>Skipping planning approval doesn't skip the building permit. Your granny flat must meet the National Construction Code like any house: fire safety, waterproofing, energy efficiency, ceiling heights and so on. Because a granny flat is a Class 1 building, you can lodge an uncertified application (BA2) with council, or a certified one (BA1) with a private surveyor's certificate for a faster decision.</p>

<h2>How to check your own lot in 15 minutes</h2>
<ol>
<li>Look up your lot on your council's online map to find the R-Code, zone and any heritage, bushfire or special control areas.</li>
<li>Check whether your estate has a local development plan.</li>
<li>Work out the lot area and how much is already roofed, to see how much open space is left.</li>
<li>Sketch where a 65 m&sup2; footprint fits behind the house with the setbacks around it.</li>
</ol>
<p>If it fits, you are probably looking at a building permit only. If it doesn't, we can design around the problem or prepare the planning application for you.</p>
"""

FAQS = [
    ("Do I need planning approval for a granny flat in WA?",
     "Not if it is 70 m&sup2; or less inside and meets all the standard R-Codes rules and your local scheme's setbacks, on a residential lot. Heritage, some bushfire areas, rural zones and estate rules can still require it."),
    ("Is there a minimum lot size for a granny flat in WA?",
     "Not any more for residential lots. The 350 m&sup2; minimum was removed when the 2024 R-Codes took effect in April 2024."),
    ("Can I rent out my granny flat?",
     "Yes. The state's info sheet says anyone can live in a granny flat, including a tenant you find yourself or through a real estate agent."),
    ("Does a granny flat need its own parking bay?",
     "In most cases, no. Some higher-density areas and places far from public transport are the exception."),
]


def page(S):
    return {"path": "granny-flat-no-planning-approval.html", "published": "2026-10-29", "type": "How-to guide", "icon": "plan",
            "card": "A seven-point design checklist for a granny flat that skips planning approval, and when you'll need it anyway.",
            "title": "How to Design a Granny Flat That Needs No Planning Approval (WA)",
            "desc": "A WA granny flat of 70 m² or less that meets the standard R-Codes rules needs no planning approval. A seven-point design checklist, the exceptions and how to check your lot.",
            "eyebrow": "How-to guide", "h1": "How to design a granny flat that needs no planning approval", "crumb": "Granny flat with no planning approval",
            "answer": "<p>Keep it to <strong>70 m&sup2; or less inside</strong>, out of the street setback, within the standard side and rear setbacks, low enough to avoid privacy setbacks, and leave enough open space on the lot. A granny flat that meets all the standard rules needs <strong>no planning approval</strong> on a residential lot of any size. It still needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-approval-process", "The approval process"), ("/granny-flat-on-a-rural-lot", "Granny flats on rural lots")],
            "sources": [("Revised R-Codes now in effect, 16 April 2024 (Department of Planning)", "https://www.planning.wa.gov.au/news-and-media-statements/revised-r-codes-now-in-effect"),
                        ("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Tiny homes and ancillary dwellings (Shire of Mundaring)", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx")]}
