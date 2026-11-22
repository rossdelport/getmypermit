BODY = """
<h2>The main rules</h2>
<ul>
<li><strong>Size:</strong> up to <strong>70 m²</strong>, not counting open verandahs or carports. A bigger one needs a planning application.</li>
<li><strong>How many:</strong> one granny flat per property.</li>
<li><strong>Renting:</strong> allowed, including to people who aren't family.</li>
<li><strong>Subdividing:</strong> building a granny flat doesn't let you split the lot, unless the planning scheme already allows it.</li>
<li><strong>Attached or detached:</strong> it can be attached to, built into, or separate from the house.</li>
</ul>

<h2>Planning approval</h2>
<p>For most homes you don't need planning approval if the granny flat meets every "deemed-to-comply" rule in the R-Codes. Some zones still need it. If you're unsure, the City offers a <strong>deemed-to-comply check</strong> before you lodge your building permit. To vary the rules, you apply for development approval with good reasons, and neighbours may be asked. Check your zone and density with Planning Services on (08) 9231 0606.</p>

<h2>Building permit: what to send</h2>
<p>A building permit is always needed before work starts.</p>
<div class="table-wrap"><table>
<thead><tr><th>BA2 (uncertified)</th><th>BA1 (certified)</th></tr></thead><tbody>
<tr><td>Site plan at 1:200 with setbacks, floor levels, north point and road reserves</td><td>Certificate of Design Compliance from a registered building surveyor</td></tr>
<tr><td>Floor plans, elevations and a cross-section at 1:100</td><td>The plans listed in the certificate</td></tr>
<tr><td>Contour survey, electrical plan with smoke alarms, stormwater details</td><td>Home indemnity insurance</td></tr>
<tr><td>Signed engineer's details, soil report, energy report, termite details, specifications</td><td>Any other approvals needed</td></tr>
<tr><td>Home indemnity insurance</td><td></td></tr>
<tr><td>City decides within <strong>25 working days</strong></td><td>City decides within <strong>10 working days</strong></td></tr>
</tbody></table></div>
<p>If the City asks for more information, you have 21 days to send it. Building it yourself over $20,000 needs owner-builder approval first. Check drainage easements with the City and Water Corporation before you design.</p>
<p>See <a href="/granny-flat-no-planning-approval">granny flats with no planning approval</a>, <a href="/granny-flat-building-permit">the building permit</a> and <a href="/granny-flat-setbacks-wa">granny flat setbacks</a>.</p>
"""

FAQS = [
    ("How big can a granny flat be in the City of Canning?",
     "Up to 70 m², not counting open verandahs or carports. Bigger ones need a planning application."),
    ("Can I rent out a granny flat in Canning?",
     "Yes. The City says granny flats can be rented to people who aren't family."),
    ("Do I need planning approval for a granny flat in Canning?",
     "Usually not, if it meets every R-Codes deemed-to-comply rule. Some zones still need it, and the City can check your plans first."),
    ("How long does Canning take to issue a granny flat permit?",
     "10 working days for a certified (BA1) application and 25 working days for an uncertified (BA2) one."),
]


def page(S):
    return {"path": "city-of-canning-granny-flat-rules.html", "published": "2026-11-23", "type": "Council guide", "icon": "pin",
            "card": "City of Canning granny flat rules: the 70 m² limit, renting, planning approval and what to send.",
            "title": "City of Canning Granny Flat Rules (2026)",
            "desc": "City of Canning granny flat (ancillary dwelling) rules: the 70 m² limit, one per lot, renting to non-family, planning approval, the deemed-to-comply check and what to send for a building permit.",
            "eyebrow": "Council guide", "h1": "City of Canning granny flat rules", "crumb": "Canning granny flat rules",
            "answer": "<p>In the City of Canning you can build <strong>one granny flat</strong> up to <strong>70 m²</strong> per property, and rent it to anyone. Planning approval usually isn't needed if it meets the R-Codes, but a <strong>building permit</strong> always is. The City decides in 10 working days (BA1) or 25 (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-no-planning-approval", "Granny flat with no planning approval"), ("/granny-flat-building-permit", "Granny flat building permit"), ("/granny-flat-setbacks-wa", "Granny flat setbacks")],
            "sources": [("Building information sheet: ancillary dwelling (BIS-25), City of Canning", "https://cdn.canning.wa.gov.au/media/4rsjaikg/bis-25-information-sheet-ancillary-dwelling.pdf"),
                        ("Building Services, City of Canning", "https://www.canning.wa.gov.au/plan-and-build/building-services/")]}
