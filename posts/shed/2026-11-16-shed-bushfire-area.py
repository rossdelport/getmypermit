BODY = """
<h2>Step 1: Check if you're in a bushfire-prone area</h2>
<p>Land is mapped as <strong>bushfire-prone</strong> on the state's Map of Bush Fire Prone Areas, run by DFES. Look up your address on the map before you order a shed, because it can change what your permit needs.</p>

<h2>Step 2: Check the 6 metre line</h2>
<p>For bushfire purposes, the distance between the shed and your <strong>house</strong> matters most. Under the Building Regulations, when a shed, garage or other Class 10a building (or a deck) is <strong>less than 6 m</strong> from the house, the certificate that goes with the permit must say:</p>
<ul>
<li>whether it's in a bushfire-prone area, and</li>
<li>if bushfire construction rules apply to it, the site's <strong>BAL</strong> (Bushfire Attack Level) or another approved assessment.</li>
</ul>
<p>A shed <strong>6 m or more</strong> from the house usually doesn't need to meet bushfire construction rules. Councils say the same thing in plain words: the Shire of Serpentine-Jarrahdale says a BAL may apply to a shed within 6 m of the house, and the City of Wanneroo says it applies if the house was built to bushfire rules and the shed is within 6 m.</p>

<h2>Step 3: Check how your house was built</h2>
<p>The regulations don't apply the bushfire rules to a shed or deck that goes with an older house that <strong>never had to meet</strong> bushfire construction rules. So the age and approval history of your house matters. Your building surveyor or council can confirm this from your property's records.</p>

<h2>Step 4: Get a BAL assessment if you need one</h2>
<p>If your shed is within 6 m of a house that was built to bushfire rules, you'll usually need a BAL assessment. The BAL tells your shed supplier which construction standard (AS 3959) the shed must meet, such as ember screens or sealed gaps.</p>

<h2>Step 5: Lodge the building permit</h2>
<p>The rest is the same as any shed: the BA1 or BA2 form, a site plan showing the distance to the house, elevations, a floor plan and engineering. Show the distance to the house clearly on the site plan.</p>

<div class="table-wrap"><table>
<thead><tr><th>Your situation</th><th>Bushfire rules for the shed?</th></tr></thead><tbody>
<tr><td>Not in a bushfire-prone area</td><td>No</td></tr>
<tr><td>Bushfire-prone, shed 6 m or more from the house</td><td>Usually no</td></tr>
<tr><td>Bushfire-prone, within 6 m, house built to bushfire rules</td><td>Usually yes: BAL needed</td></tr>
<tr><td>Bushfire-prone, within 6 m, older house not built to bushfire rules</td><td>Usually no, but the certificate must still say if it's in a bushfire-prone area</td></tr>
</tbody></table></div>
<p>Councils vary, so check with yours. Read <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>, see what goes on a <a href="/shed-site-plan">shed site plan</a>, or learn <a href="/what-is-a-class-10a-building">what a Class 10a building is</a>.</p>
"""

FAQS = [
    ("Does a shed need a BAL in WA?",
     "Usually only if it's in a bushfire-prone area and less than 6 m from a house that was built to bushfire rules. A shed 6 m or more away usually doesn't."),
    ("How far should a shed be from the house in a bushfire area?",
     "6 m is the key distance. Closer than that, the permit certificate must state whether it's bushfire-prone and, where the rules apply, the BAL."),
    ("How do I know if my property is bushfire-prone?",
     "Look up your address on the state's Map of Bush Fire Prone Areas."),
    ("Does a small exempt shed need to meet bushfire rules?",
     "A shed that's exempt from a building permit (freestanding, up to 10 m² and 2.4 m) doesn't go through the permit process, but it still has to meet the building standards that apply to it. Ask your council if you're close to the house."),
]


def page(S):
    return {"path": "shed-bushfire-area.html", "published": "2026-11-16", "type": "How-to guide", "icon": "flame",
            "card": "The 6 metre rule, when a shed needs a BAL and how to get it approved in a bushfire-prone area.",
            "title": "How to Get a Shed Approved in a Bushfire-Prone Area (WA)",
            "desc": "Building a shed in a WA bushfire-prone area: the 6 m rule, when you need a BAL assessment, how your house's age matters, and how to lodge the permit.",
            "eyebrow": "How-to guide", "h1": "How to get a shed approved in a bushfire-prone area", "crumb": "Sheds in bushfire areas",
            "answer": "<p>In a bushfire-prone area, the key is the <strong>6 m rule</strong>. A shed less than 6 m from your house usually needs a <strong>BAL assessment</strong> and bushfire construction if your house was built to bushfire rules. A shed 6 m or more away usually doesn't. It still needs a normal building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/shed-site-plan", "Shed site plan"), ("/what-is-a-class-10a-building", "What is a Class 10a building?")],
            "sources": [("Building Regulations 2012 (WA)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_46484.htm"),
                        ("Outbuildings information sheet, City of Wanneroo", "https://www.wanneroo.wa.gov.au/download/downloads/id/360/outbuildings_-_information_sheet.pdf"),
                        ("Sheds, garages and workshops, Shire of Serpentine-Jarrahdale", "https://www.sjshire.wa.gov.au/planning-building-and-roads/building/building-advice/sheds-garages-and-workshops.aspx"),
                        ("Bushfire prone areas, DFES", "https://www.dfes.wa.gov.au/hazard-information/bushfire/bushfire-prone-areas")]}
