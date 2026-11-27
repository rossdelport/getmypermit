BODY = """
<h2>Do you need a building permit?</h2>
<p>Usually yes. The City of Armadale says a shed or garage doesn't need a permit only if it is <strong>all</strong> of these:</p>
<ul>
<li>less than <strong>10 m²</strong> in floor area,</li>
<li><strong>freestanding</strong>, and</li>
<li>no higher than <strong>2.4 m</strong>.</li>
</ul>
<p>Even a permit-free shed must meet the building code, including fire separation from boundaries and other buildings (for example, at least <strong>900 mm</strong>). Check yours with the <a href="/shed-size-checker">shed size checker</a>.</p>

<h2>Where it can go</h2>
<p>Sheds aren't allowed in the <strong>front setback area</strong>, which is the front yard forward of the house line. Other setbacks follow the City's local planning policies and the R-Codes. Planning approval may be needed before a building permit can be issued. See <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>

<h2>Who can build it</h2>
<p>The City's June 2026 sheet says a registered builder or owner-builder approval is needed if the build cost is <strong>$50,000 or more</strong>.</p>

<h2>How long it takes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Application</th><th>Who checks it</th><th>City's time limit</th></tr></thead><tbody>
<tr><td>Certified (BA1)</td><td>A private building surveyor signs a certificate first</td><td>Up to 10 business days</td></tr>
<tr><td>Uncertified (BA2)</td><td>The City's building surveyor</td><td>Up to 25 business days</td></tr>
</tbody></table></div>
<p>The permit lasts <strong>2 years</strong>. When the shed is finished, the builder lodges a BA7 notice of completion within 7 days.</p>

<h2>What to send</h2>
<ul>
<li>A BA1 or BA2 form, signed by the builder and the applicant, and the fees.</li>
<li>A site plan at 1:200 showing the shed, existing buildings, boundary setbacks, fire separation and any septic tanks or leach drains.</li>
<li>A floor plan, elevations and cross-section at 1:100.</li>
<li>A structural engineer's certificate.</li>
<li>A bushfire (BAL) assessment and planning approval, if needed.</li>
<li>A Construction Training Fund levy receipt if the work is over $100,000.</li>
</ul>
<p>See <a href="/shed-site-plan">shed site plans</a>. Call the City on 9394 5000.</p>
"""

FAQS = [
    ("What size shed can I build without a permit in Armadale?",
     "One that is less than 10 m², freestanding and no higher than 2.4 m. It must still meet the building code, including fire separation."),
    ("Can I put a shed in my front yard in Armadale?",
     "No. The City says outbuildings aren't permitted in the front setback area, forward of the house line."),
    ("How long does a shed permit take in Armadale?",
     "Up to 10 business days for a certified (BA1) application, or up to 25 business days for an uncertified (BA2) one, unless more information is needed."),
    ("Do I need a registered builder for a shed in Armadale?",
     "Only if the build cost is $50,000 or more. Below that, you can build it yourself with a permit."),
]


def page(S):
    return {"path": "city-of-armadale-shed-rules.html", "published": "2026-11-28", "type": "Council guide", "icon": "pin",
            "card": "City of Armadale shed rules: the 10 m² permit exemption, no sheds in the front yard, timeframes and what to send.",
            "title": "City of Armadale Shed Rules (2026)",
            "desc": "City of Armadale shed and garage rules: when you need a building permit, the 10 m² and 2.4 m exemption, front setback ban, the $50,000 builder rule, BA1 and BA2 timeframes and what to send.",
            "eyebrow": "Council guide", "h1": "City of Armadale shed rules", "crumb": "Armadale shed rules",
            "answer": "<p>In the City of Armadale, a shed needs a <strong>building permit</strong> unless it's under <strong>10 m²</strong>, freestanding and no higher than <strong>2.4 m</strong>. Sheds can't go in the front setback area. The City decides certified applications in up to <strong>10 business days</strong> and uncertified ones in up to <strong>25</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/shed-site-plan", "Shed site plan")],
            "sources": [("Building information sheet: shed or garage (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/2Vf3c5sy6fAI5u3NuEkHeT/dc7652d7db061e2fa60791d5d7b156d3/Building_Services_Information_Sheet_-_Shed_or_Garage_-_June_2026.PDF"),
                        ("What can I build?, City of Armadale", "https://my.armadale.wa.gov.au/service/planning-and-building/building-services/what-can-i-build")]}
