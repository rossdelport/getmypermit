BODY = """
<h2>What's the difference?</h2>
<ul>
<li><strong>Granny flat (ancillary dwelling):</strong> a small extra home that goes with the main house on the same lot. It can be detached, attached or built into the house.</li>
<li><strong>Grouped dwelling:</strong> two or more homes on the same lot, where none sits above another. Homes on a survey strata lot with common property also count as grouped dwellings.</li>
</ul>

<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Granny flat</th><th>Grouped dwelling</th></tr></thead><tbody>
<tr><td>Size</td><td>Usually up to 70 m² (not counting open verandahs and carports)</td><td>Set by the R-Codes for your zoning, not a fixed small cap</td></tr>
<tr><td>How many</td><td>Usually one per lot</td><td>Two or more on the lot</td></tr>
<tr><td>Planning approval</td><td>Often not needed if it meets the R-Codes deemed-to-comply rules</td><td>Always needed (City of Canning)</td></tr>
<tr><td>Building permit</td><td>Always</td><td>Always</td></tr>
</tbody></table></div>

<h2>Which one suits you?</h2>
<ul>
<li><strong>Granny flat</strong> if you want extra space for family or a tenant, and plan to keep the property as one lot. It's usually the faster path, because a compliant granny flat often skips planning approval. Try the <a href="/granny-flat-size-calculator">size calculator</a>.</li>
<li><strong>Grouped dwelling</strong> if you want a bigger second home, or plan to subdivide and sell. Your lot must have a zoning and size that allows a second dwelling. See <a href="/granny-flat-minimum-lot-size">minimum lot sizes</a> and <a href="/subdivide-granny-flat">subdividing a granny flat</a>.</li>
</ul>
<p>Councils vary, so check your zoning and local planning policies before you design. A planning officer can tell you which path your lot allows.</p>
"""

FAQS = [
    ("What is a grouped dwelling in WA?",
     "Two or more homes on the same lot where none sits above another. Homes on a survey strata lot with common property also count as grouped dwellings."),
    ("Does a grouped dwelling need planning approval?",
     "Yes. The City of Canning says planning approval is required in all cases where grouped dwellings are proposed."),
    ("Does a granny flat need planning approval?",
     "Often not, if it meets the R-Codes deemed-to-comply rules for ancillary dwellings, including the size limit, usually 70 m²."),
    ("Is a granny flat or a grouped dwelling quicker to approve?",
     "A compliant granny flat is usually quicker, because it often needs only a building permit, while a grouped dwelling always needs planning approval first."),
]


def page(S):
    return {"path": "granny-flat-vs-grouped-dwelling.html", "published": "2026-11-27", "type": "Comparison", "icon": "doc",
            "card": "Granny flat vs grouped dwelling: size, planning approval, permits and which suits your plans.",
            "title": "Granny Flat vs Grouped Dwelling: Approvals Compared (WA)",
            "desc": "Granny flat vs grouped dwelling in WA: what each one is, the 70 m² granny flat limit, why grouped dwellings always need planning approval, building permits, and which suits your plans.",
            "eyebrow": "Comparison", "h1": "Granny flat vs grouped dwelling", "crumb": "Granny flat vs grouped dwelling",
            "answer": "<p>A <strong>granny flat</strong> is a small extra home (usually up to <strong>70 m²</strong>) that goes with the main house and often needs no planning approval if it meets the R-Codes. A <strong>grouped dwelling</strong> is a second full home on the lot and <strong>always</strong> needs planning approval. Both need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-size-calculator", "Granny flat size calculator"), ("/granny-flat-minimum-lot-size", "Granny flat minimum lot size"), ("/subdivide-granny-flat", "Subdividing a granny flat")],
            "sources": [("Planning information sheet: is planning approval required, City of Canning", "https://www.canning.wa.gov.au/media/o2vphn2u/information-sheet-making-applications.pdf"),
                        ("Building information sheet: ancillary dwelling (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/40qQCMMHfyFz2fsz5rVvUq/618c3f6d9bd14b993fc41cc80e977718/Building_Services_Information_Sheet_-_Ancillary_Dwelling_-_June_2026.PDF"),
                        ("Do I need approval?, City of Mandurah", "https://www.mandurah.wa.gov.au/my-home-property-and-rates/building-and-improving-your-home/do-i-need-approval")]}
