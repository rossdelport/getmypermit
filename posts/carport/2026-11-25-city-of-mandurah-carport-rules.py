BODY = """
<h2>Do you need a building permit?</h2>
<p>Yes. The City of Mandurah says a building permit is <strong>always required for a carport</strong>. It treats a carport as a structure with a waterproof roof, open on two or more sides, with at least a third of its outside edge open.</p>

<h2>Planning approval</h2>
<p>Usually not needed if the carport meets the R-Codes deemed-to-comply rules. Whether you're exempt depends on your lot's zoning, site cover, setbacks and any special conditions. The City offers a <strong>deemed-to-comply check</strong> (a fee applies) to confirm in writing before you start.</p>
<p>Setbacks come from:</p>
<ul>
<li>the City's town planning scheme,</li>
<li>the R-Codes,</li>
<li>local planning policies, and</li>
<li>any detailed area plan for your estate.</li>
</ul>
<p>You also need to keep the minimum open space and outdoor living area. If the carport breaks any of these, you need <strong>development approval first</strong>. The building permit can't be decided until that's approved. Check your zoning on the City's online map.</p>

<h2>What to send</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Details</th></tr></thead><tbody>
<tr><td>Form</td><td>BA1 (certified, with a Certificate of Design Compliance) or BA2 (uncertified)</td></tr>
<tr><td>Site plan</td><td>At least 1:200, with setbacks to boundaries and all buildings, pools and retaining walls, and ground levels</td></tr>
<tr><td>Drawings</td><td>Floor plan, section and elevations at least 1:100, with all sizes</td></tr>
<tr><td>Construction details</td><td>Materials, sizes, spans and spacing</td></tr>
<tr><td>Connections</td><td>How it fixes to the house and footing details</td></tr>
</tbody></table></div>
<p>The building surveyor may ask for more after checking your plans. Lodge online through "Building Lodgements" on the City's website, or on paper. Building Services is on 9550 3777.</p>
<p>See <a href="/carport-site-plan">carport site plans</a>, <a href="/carport-on-boundary">carports on the boundary</a> and <a href="/attached-vs-freestanding-carport">attached vs freestanding</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in Mandurah?",
     "Yes. The City of Mandurah says a building permit is always required for a carport."),
    ("Does a carport need planning approval in Mandurah?",
     "Usually not, if it meets the R-Codes deemed-to-comply rules. If it varies them, you need development approval first."),
    ("How close to the boundary can a carport be in Mandurah?",
     "It depends on your zoning, the R-Codes, local policies and any detailed area plan. The City's deemed-to-comply check can confirm it for your lot."),
    ("How do I lodge a carport application in Mandurah?",
     "Online, through the Building Lodgements link on the City's website. Paper applications are also accepted."),
]


def page(S):
    return {"path": "city-of-mandurah-carport-rules.html", "published": "2026-11-25", "type": "Council guide", "icon": "pin",
            "card": "City of Mandurah carport rules: permits, planning approval, the deemed-to-comply check and what to send.",
            "title": "City of Mandurah Carport Rules (2026)",
            "desc": "City of Mandurah carport rules: a building permit is always needed, when planning approval applies, where setbacks come from, the deemed-to-comply check and what to send.",
            "eyebrow": "Council guide", "h1": "City of Mandurah carport rules", "crumb": "Mandurah carport rules",
            "answer": "<p>In the City of Mandurah, every carport needs a <strong>building permit</strong>. Planning approval usually isn't needed if it meets the R-Codes deemed-to-comply rules. If it doesn't, you need <strong>development approval first</strong>. The City offers a paid deemed-to-comply check to confirm.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-site-plan", "Carport site plan"), ("/carport-on-boundary", "Carport on the boundary"), ("/attached-vs-freestanding-carport", "Attached vs freestanding carport")],
            "sources": [("Do I need approval?, City of Mandurah", "https://www.mandurah.wa.gov.au/my-home-property-and-rates/building-and-improving-your-home/do-i-need-approval"),
                        ("Patios and carports information sheet, City of Mandurah", "https://www.mandurah.wa.gov.au/getContentAsset/6bcb0b1b-fe5e-4f49-92fc-d295c942b2d7/8c05e2a8-714e-41ec-a13c-ec89cb576508/Patios%20and%20Carports%20Information%20Sheet.pdf?language=en")]}
