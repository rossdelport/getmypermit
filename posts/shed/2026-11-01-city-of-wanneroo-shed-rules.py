BODY = """
<h2>Do you need a building permit?</h2>
<p>Wanneroo follows the state rule: no building permit for a shed that is <strong>10 m&sup2; or less and 2.4 m high or less</strong>. Anything bigger or taller needs one. Planning approval is only exempt in a <strong>residential zone</strong>; on rural and other zones, check with the City first.</p>

<h2>Wanneroo's planning rules for sheds</h2>
<p>A shed skips planning approval if it meets either the small or the large outbuilding standard:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Small outbuilding</th><th>Large or multiple outbuildings</th></tr></thead><tbody>
<tr><td>Size</td><td>10 m&sup2; or less, and only one per lot</td><td>All outbuildings together no more than 60 m&sup2; or 10% of the lot, whichever is less</td></tr>
<tr><td>Height</td><td>Wall and ridge up to 2.7 m</td><td>Wall up to 2.4 m, ridge up to 4.2 m</td></tr>
<tr><td>Boundaries</td><td>No more than two walls on the boundary</td><td>1 m from side boundaries for walls up to 14 m long; 1.5 m if longer</td></tr>
<tr><td>Front yard</td><td colspan="2">Not in the primary or secondary street setback</td></tr>
<tr><td>Open space</td><td colspan="2">Must not reduce your lot's required open space or outdoor living area</td></tr>
</tbody></table></div>
<p>Two small sheds count as multiple outbuildings, so they're assessed under the large standard. These rules suit most R20 and R30 lots; estates with a Local Development Plan or Structure Plan can differ.</p>

<h2>Fire separation and bushfire</h2>
<ul>
<li>Every shed, permit or not, needs <strong>900 mm of separation</strong> for fire safety: either 900 mm from the boundary, or 900 mm from the house.</li>
<li>If your house was built to bushfire requirements and the shed is <strong>within 6 m</strong> of it, the shed needs a new bushfire (BAL) report and must meet it.</li>
</ul>

<h2>What to lodge</h2>
<p>For an uncertified application (BA2), Wanneroo asks for:</p>
<ul>
<li>A site plan at 1:200 or larger, showing the distance to each boundary and other structures</li>
<li>Floor plan and elevations at 1:100 or larger, with all dimensions</li>
<li>Construction details: materials, sizes, spacing, spans and footings</li>
<li>Structural engineer's details</li>
<li>A bushfire (BAL) report, if needed</li>
<li>A <strong>Street and Verge Bond Permit</strong> application, required with every building permit</li>
<li>Planning approval, if needed. A BA2 can be lodged while planning is pending, but it waits until planning is approved</li>
</ul>
<p>You can lodge online through the City's website. The building permit fee is set by the state: 0.32% of the value for a BA2, at least $121, plus the $61.65 Building Services Levy.</p>

<h2>Contact</h2>
<p>City of Wanneroo Building Services: 9405 5000.</p>
"""

FAQS = [
    ("What size shed can I build without approval in Wanneroo?",
     "A shed of 10 m&sup2; or less and 2.4 m high or less needs no building permit. To also skip planning approval it must meet the City's small outbuilding standard, including staying out of the front setback."),
    ("How close to the fence can a shed be in Wanneroo?",
     "1 m from the side boundary for walls up to 14 m long, or 1.5 m for longer walls, under the large outbuilding standard. A small shed of 10 m&sup2; or less can have up to two walls on the boundary."),
    ("Do I need a verge bond for a shed in Wanneroo?",
     "Yes. The City requires a Street and Verge Bond Permit application with every building permit. It includes a non-refundable admin fee, plus a bond depending on the value of the work."),
    ("How big can my shed be in Wanneroo?",
     "All outbuildings together can be up to 60 m&sup2; or 10% of your lot, whichever is less, with walls up to 2.4 m and a ridge up to 4.2 m. Bigger needs planning approval."),
]


def page(S):
    return {"path": "city-of-wanneroo-shed-rules.html", "published": "2026-11-01", "type": "Council guide", "icon": "pin",
            "card": "Wanneroo's shed rules: permit size limits, the small and large outbuilding standards, setbacks, verge bond and what to lodge.",
            "title": "City of Wanneroo Shed Rules: Sizes, Setbacks and Permits",
            "desc": "City of Wanneroo shed rules: no permit up to 10 m² and 2.4 m, the small and large outbuilding standards, 1 m setbacks, fire separation, verge bonds and what to lodge.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo shed rules", "crumb": "City of Wanneroo",
            "answer": "<p>In Wanneroo, a shed of <strong>10 m&sup2; or less and 2.4 m high or less</strong> needs no building permit. Bigger sheds need one. To skip planning approval, all your outbuildings together must stay within <strong>60 m&sup2; or 10% of the lot</strong>, with walls up to 2.4 m, a ridge up to 4.2 m, <strong>1 m from side boundaries</strong> and out of the front yard.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?")],
            "sources": [("Outbuildings information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/360/outbuildings_-_information_sheet.pdf"),
                        ("What approvals do I need? Shed (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/directory_record/107/shed_also_referred_to_as_an_outbuilding"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
