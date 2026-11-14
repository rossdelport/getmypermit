BODY = """
<h2>The basics</h2>
<p>In the R-Codes, a granny flat is called an <strong>ancillary dwelling</strong>. The City of Rockingham sums up the key rules:</p>
<ul>
<li>Up to <strong>70 m²</strong> internal floor area.</li>
<li>Only <strong>one</strong> per lot.</li>
<li>Allowed on <strong>any lot size</strong>: there's no minimum.</li>
<li>Can be lived in by <strong>family, friends or tenants</strong>.</li>
<li>May need <strong>one extra parking bay</strong>, depending on location and zoning.</li>
<li>Must meet the National Construction Code.</li>
</ul>

<h2>Planning approval</h2>
<p>The City says single houses on residential land don't need development approval. A granny flat usually doesn't either, if it meets <strong>all the deemed-to-comply rules</strong> of the R-Codes (size, setbacks, site cover, height, privacy and parking).</p>
<p>You will need approval if:</p>
<ul>
<li>it doesn't meet one of the standard R-Codes rules, or</li>
<li>the lot is zoned <strong>Special Residential</strong> or <strong>Special Rural</strong>, where the City needs town planning consent for any development, or</li>
<li>the site is in a heritage-listed area.</li>
</ul>

<h2>Extra rules in the city centre</h2>
<p>Inside the <strong>Rockingham Strategic Centre</strong> (the city centre plan area), a granny flat must also:</p>
<ul>
<li>sit <strong>behind</strong> the main house or be an extension of it, and</li>
<li>use materials and colours that suit the main house.</li>
</ul>
<p>The plan restricts sheds, dongas and sea containers that haven't been properly converted.</p>

<h2>Building permit: always</h2>
<p>The City is clear: a building permit is needed in <strong>all cases</strong> before work starts. There are no exemptions for a granny flat.</p>

<h2>Council fees</h2>
<p>From the City's Building Services fee sheet (updated 7 July 2026):</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Fee</th></tr></thead><tbody>
<tr><td>Certified permit (BA1)</td><td>0.19% of the cost, minimum $121</td></tr>
<tr><td>Uncertified permit (BA2)</td><td>0.32% of the cost, minimum $121</td></tr>
<tr><td>Building services levy</td><td>0.137% of the cost, minimum $61.65</td></tr>
<tr><td>Kerb and footpath inspection, work over $100,000</td><td>$335</td></tr>
<tr><td>Certificate of design compliance from the City (BA3)</td><td>0.13% of the cost, minimum $150</td></tr>
<tr><td>R-Codes variation, $50,000 to $500,000</td><td>0.32% of the cost</td></tr>
</tbody></table></div>
<p>For a <strong>$150,000</strong> granny flat with a BA1, that's $285 + $205.50 levy + $335 kerb fee = <strong>$825.50</strong>, plus the certificate of design compliance. Rural, Special Rural and Special Residential lots don't pay the kerb fee.</p>
<p>See if yours can skip planning approval with <a href="/granny-flat-no-planning-approval">granny flats without planning approval</a>, or read <a href="/granny-flat-approval-cost">granny flat approval cost</a> and <a href="/granny-flat-building-permit">granny flat building permit</a>.</p>
"""

FAQS = [
    ("Can I build a granny flat in Rockingham?",
     "Yes, on any residential lot size. It can be up to 70 m², one per lot, and needs a building permit."),
    ("Do I need planning approval for a granny flat in Rockingham?",
     "Not usually, if it meets all the deemed-to-comply R-Codes rules. Special Residential and Special Rural lots, heritage areas and designs that don't comply need approval."),
    ("Can I rent out a granny flat in Rockingham?",
     "Yes. The City says a granny flat may be lived in by family, friends or tenants."),
    ("How much are council fees for a granny flat in Rockingham?",
     "For a $150,000 granny flat with a BA1: about $285 permit fee, $205.50 levy and a $335 kerb inspection fee, plus the certificate of design compliance."),
]


def page(S):
    return {"path": "city-of-rockingham-granny-flat-rules.html", "published": "2026-11-15", "type": "Council guide", "icon": "pin",
            "card": "Granny flat size, planning approval, city centre rules and council fees in Rockingham.",
            "title": "City of Rockingham Granny Flat Rules (2026)",
            "desc": "City of Rockingham granny flat rules: 70 m² on any lot size, when planning approval is needed, extra city centre rules, building permit and 2026 council fees.",
            "eyebrow": "Council guide", "h1": "City of Rockingham granny flat rules", "crumb": "Rockingham granny flat rules",
            "answer": "<p>In Rockingham, a granny flat can be up to <strong>70 m²</strong> on <strong>any lot size</strong>, one per lot, and can be rented out. It usually doesn't need <strong>planning approval</strong> if it meets the standard R-Codes rules, but it <strong>always needs a building permit</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-no-planning-approval", "Granny flats without planning approval"), ("/granny-flat-approval-cost", "Granny flat approval cost"), ("/granny-flat-building-permit", "Granny flat building permit")],
            "sources": [("Ancillary dwellings information sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/7a040ade-a3ae-4dac-9bb5-d684c8ee5a01/3ca954ad-3848-47c6-8f97-68cebe0b47a2/RSC-Information-Sheet-Ancillary-Dwelling.pdf?language=en"),
                        ("Rockingham Strategic Centre Precinct Structure Plan, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/localplanning/rockingham-strategic-centre-1/rockingham-strategic-centre-precinct-structure-plan"),
                        ("Development applications, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/development-applications"),
                        ("Building Services fee sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/d92d0adf-466c-4d62-bb92-fc64ccf62f7d/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Building-Services-Fee-Sheet.pdf?language=en")]}
