BODY = """
<h2>First: wheels or no wheels?</h2>
<p>In WA, a tiny home on wheels that's built to be towed is a <strong>caravan</strong>. A tiny home without wheels is a <strong>building</strong>. The rules are completely different, so work out which yours is first with the <a href="/caravan-or-building-checker">caravan or building checker</a>.</p>

<h2>Tiny home on wheels in Rockingham</h2>
<p>The City of Rockingham handles approvals to camp in or occupy a caravan on land that isn't a caravan park. The state rules it applies are:</p>
<div class="table-wrap"><table>
<thead><tr><th>How long</th><th>What you need</th></tr></thead><tbody>
<tr><td>Up to 5 nights in any 28 days</td><td>The landowner's OK</td></tr>
<tr><td>Up to 24 months in a row</td><td>Council approval</td></tr>
<tr><td>Permanently</td><td>Not allowed outside a caravan park</td></tr>
</tbody></table></div>
<p>Other state rules to know:</p>
<ul>
<li>Council can set conditions, such as being safe and healthy and having access to power, water and sewage.</li>
<li>If council hasn't decided within <strong>63 days</strong>, the application is treated as refused. You can appeal to the Minister within 35 days.</li>
<li>Only <strong>one</strong> caravan can be used for camping on a lot at a time, unless approved.</li>
<li>It must keep its wheels and be able to be moved within 24 hours of disconnecting services.</li>
</ul>

<h2>Fixed tiny home in Rockingham</h2>
<p>Without wheels, a tiny home is a building. On a residential lot it's either the <strong>main house</strong> or a <strong>granny flat</strong> (ancillary dwelling):</p>
<ul>
<li><strong>As a granny flat:</strong> up to 70 m², one per lot, on any lot size. It usually needs no planning approval if it meets the standard R-Codes rules.</li>
<li><strong>As the main house:</strong> the City says single houses on residential land don't need development approval.</li>
<li><strong>Special Residential and Special Rural</strong> lots need town planning consent for any development.</li>
<li>A <strong>building permit</strong> is always needed, and it must meet the National Construction Code.</li>
</ul>
<p>In the <strong>Rockingham Strategic Centre</strong> (city centre plan area), a granny flat must sit behind the main house and suit its materials and colours. The plan restricts dongas and sea containers that haven't been properly converted.</p>

<h2>Council fees for a fixed tiny home</h2>
<p>From the City's fee sheet (updated 7 July 2026): a BA2 uncertified permit is <strong>0.32%</strong> of the cost (minimum $121), a BA1 certified permit <strong>0.19%</strong> (minimum $121), plus the building services levy of <strong>0.137%</strong> (minimum $61.65). For a $60,000 tiny home with a BA2, that's $192 + $82.20 = <strong>$274.20</strong>.</p>
<p>See <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a> and <a href="/tiny-home-approval-cost">tiny home approval cost</a> for more. Call the City on 9528 0333 to talk about your site.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in Rockingham?",
     "For up to 5 nights in any 28 days with the landowner's OK. For longer, up to 24 months at a time, you need approval from the City of Rockingham."),
    ("Can I put a fixed tiny home in my backyard in Rockingham?",
     "Yes, as a granny flat up to 70 m², one per lot. It needs a building permit and usually no planning approval if it meets the R-Codes."),
    ("Do I need a building permit for a tiny home in Rockingham?",
     "A fixed tiny home always needs one. A genuine towable tiny home on wheels is a caravan and doesn't need a building permit."),
    ("How long does Rockingham have to decide a caravan application?",
     "Under the state regulations, if council hasn't decided within 63 days, the application is treated as refused, and you can appeal to the Minister."),
]


def page(S):
    return {"path": "city-of-rockingham-tiny-homes.html", "published": "2026-11-15", "type": "Council guide", "icon": "pin",
            "card": "Rules for tiny homes on wheels and fixed tiny homes in the City of Rockingham, plus fees.",
            "title": "City of Rockingham Tiny Home Rules (2026)",
            "desc": "Tiny home rules in the City of Rockingham: how long you can live in a tiny home on wheels, fixed tiny homes as granny flats, building permits and council fees.",
            "eyebrow": "Council guide", "h1": "City of Rockingham tiny home rules", "crumb": "Rockingham tiny homes",
            "answer": "<p>In Rockingham, a towable tiny home on wheels is a <strong>caravan</strong>: you can stay <strong>5 nights in 28 days</strong> with the owner's OK, or up to <strong>24 months</strong> with council approval. A fixed tiny home is a building: usually a <strong>granny flat up to 70 m²</strong> that always needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land"), ("/tiny-home-approval-cost", "Tiny home approval cost")],
            "sources": [("Approval to camp or occupy a caravan, City of Rockingham (ABLIS)", "https://ablis.business.gov.au/service/wa/approval-to-camp-or-occupy-a-caravan-city-of-rockingham/31791"),
                        ("Temporary accommodation and camping outside of caravan parks, WA Government", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Ancillary dwellings information sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/7a040ade-a3ae-4dac-9bb5-d684c8ee5a01/3ca954ad-3848-47c6-8f97-68cebe0b47a2/RSC-Information-Sheet-Ancillary-Dwelling.pdf?language=en"),
                        ("Building Services fee sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/d92d0adf-466c-4d62-bb92-fc64ccf62f7d/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Building-Services-Fee-Sheet.pdf?language=en")]}
