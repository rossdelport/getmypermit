BODY = """
<h2>What always needs a building permit</h2>
<p>The City of Armadale says you always need a building permit for:</p>
<ul>
<li>a new house,</li>
<li>a new granny flat,</li>
<li>structural changes or additions to a house,</li>
<li>turning a shed, garage or carport into a room you live in, and</li>
<li>replacing a house roof.</li>
</ul>
<p>Patios, pergolas, shade sails, sheds, garages, carports, decks, retaining walls, earthworks and water tanks <strong>may</strong> need one, depending on size and height. The City has an info sheet and checklist for each. Rooftop solar on a house usually doesn't need a permit, unless the roof needs strengthening. A front fence that meets the City's Fencing Local Law 2011 doesn't need one either. Sheds can't go in the front yard.</p>

<h2>BA1 or BA2</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private registered building surveyor, who issues a Certificate of Design Compliance</td><td>The City's building surveyor</td></tr>
<tr><td>Which buildings</td><td>All types</td><td>Houses and Class 10 buildings (sheds, patios and the like) only</td></tr>
<tr><td>City decides within</td><td>10 business days</td><td>25 business days</td></tr>
</tbody></table></div>
<p>The form must be filled in fully and signed by the builder and the applicant. Work worth over <strong>$100,000</strong> also needs a Construction Training Fund levy receipt.</p>

<h2>If you don't meet the R-Codes</h2>
<p>You can apply to vary the R-Codes. If that's approved, you still need a building permit before you start. Some jobs also need planning or health approval first.</p>

<h2>After the permit</h2>
<ul>
<li>A permit lasts <strong>2 years</strong>. You can apply for more time.</li>
<li>The builder must send a <strong>BA7 notice of completion</strong> within 7 days of finishing.</li>
</ul>
<p>You can apply online, by email to info@armadale.wa.gov.au, by post or at 7 Orchard Avenue, Armadale. Building Services is on 9394 5000. See <a href="/which-ba-form">which BA form you need</a>, <a href="/ba7-notice-of-completion">the BA7 notice</a> and the <a href="/owner-builder-checker">owner-builder checker</a>.</p>
"""

FAQS = [
    ("What needs a building permit in the City of Armadale?",
     "Always: new houses, granny flats, structural additions, converting a shed or garage into a room, and a new house roof. Patios, sheds, carports and decks may need one depending on size."),
    ("How long does Armadale take to issue a building permit?",
     "Up to 10 business days for a certified (BA1) application and up to 25 business days for an uncertified (BA2) one."),
    ("How long is an Armadale building permit valid?",
     "Two years from the date it's granted. You can apply to extend it."),
    ("Do I need a permit to replace my roof in Armadale?",
     "Yes. The City says replacing a house roof always needs a building permit."),
]


def page(S):
    return {"path": "city-of-armadale-building-permits.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "City of Armadale building permits: what always needs one, BA1 vs BA2, timeframes and the 2-year rule.",
            "title": "City of Armadale Building Permits (2026 Guide)",
            "desc": "City of Armadale building permits: what always needs a permit (including re-roofing), BA1 vs BA2, 10 and 25 business-day timeframes, R-Code variations, the 2-year permit and the BA7.",
            "eyebrow": "Council guide", "h1": "City of Armadale building permits", "crumb": "City of Armadale",
            "answer": "<p>In the City of Armadale, new homes, granny flats, structural additions, room conversions and <strong>re-roofing a house</strong> always need a building permit. The City decides in <strong>10 business days</strong> (BA1) or <strong>25</strong> (BA2), and a permit lasts <strong>2 years</strong>. Sheds, patios and carports depend on size.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/ba7-notice-of-completion", "BA7 notice of completion"), ("/owner-builder-checker", "Owner-builder checker")],
            "sources": [("What can I build?, City of Armadale", "https://my.armadale.wa.gov.au/service/planning-and-building/building-services/what-can-i-build"),
                        ("Building information sheet: carport (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/3EU0cVeb0fudwwQOKbJCdI/ea1bbd43bb7a65ea28bdc751a4d39505/Building_Services_Information_Sheet_-_Carport_-_June_2026.PDF")]}
