BODY = """
<h2>Do you need a building permit?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Patio or gazebo</td><td>Freestanding, up to 10 m² and up to 2.4 m high</td></tr>
<tr><td>Pergola or shade sail with a house</td><td>Up to 20 m² and up to 2.4 m high</td></tr>
<tr><td>Pergola or shade sail with any other building</td><td>Always needs a permit</td></tr>
</tbody></table></div>
<p>The City of Gosnells counts a <strong>pergola</strong> as an open structure with no roof, though it can have shade cloth. With a solid roof it fits the R-Codes' meaning of a patio (an open structure covered with a material water can't pass through), so the patio rules apply. The City suggests using engineer-certified designs for shade sails even when no permit is needed.</p>
<p>Most attached patios need a building permit. You can lodge a <strong>BA1</strong> with a Certificate of Design Compliance (BA3) from a private building surveyor, or an uncertified <strong>BA2</strong>.</p>

<h2>Do you need planning approval?</h2>
<p>Usually not for a patio at a house. You need development approval if your patio:</p>
<ul>
<li>Doesn't meet the R-Codes' standard ("deemed-to-comply") rules, such as setbacks.</li>
<li>Doesn't match a local development plan for your area.</li>
<li>Doesn't match one of the City's local planning policies.</li>
</ul>
<p>Under the R-Codes, a patio can usually go right up to a side or rear boundary (at the posts) if it's no more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, sits behind the front setback, and has its roof and gutters at least <strong>450 mm</strong> from the boundary.</p>
<p>Gosnells must decide a planning application within <strong>60 days</strong>, or <strong>90 days</strong> if neighbours are asked for comment. If the City asks for more information, you have <strong>21 days</strong> to provide it. You need planning approval before you apply for the building permit.</p>
<p>Use the <a href="/patio-approval-checker">patio approval checker</a>, read about a <a href="/patio-on-boundary-wa">patio on the boundary</a>, or see what happens if you <a href="/roof-on-pergola-approval">put a roof on a pergola</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Gosnells?",
     "Usually yes. Only freestanding patios up to 10 m² and 2.4 m high are exempt from a building permit."),
    ("Do I need a permit for a pergola in Gosnells?",
     "Not if it's with a house, has no solid roof, and is up to 20 m² and 2.4 m high."),
    ("Does a patio need planning approval in Gosnells?",
     "Usually not, unless it breaks the R-Codes' standard rules (such as setbacks), a local development plan or a local planning policy."),
    ("How long does Gosnells take to approve a patio?",
     "Planning approval, if needed, takes up to 60 days, or 90 if neighbours are consulted. The building permit follows."),
]


def page(S):
    return {"path": "city-of-gosnells-patio-rules.html", "published": "2026-11-19", "type": "Council guide", "icon": "pin",
            "card": "City of Gosnells patio and pergola rules: permit exemptions, planning approval and boundary setbacks.",
            "title": "City of Gosnells Patio and Pergola Rules (2026)",
            "desc": "City of Gosnells patio rules: when a patio or pergola needs a building permit (10 m² and 20 m² exemptions), when you need planning approval, and boundary setbacks.",
            "eyebrow": "Council guide", "h1": "City of Gosnells patio and pergola rules", "crumb": "City of Gosnells patio rules",
            "answer": "<p>In Gosnells, a patio needs a <strong>building permit</strong> unless it's freestanding, up to <strong>10 m²</strong> and <strong>2.4 m</strong> high. An open pergola with a house is exempt up to <strong>20 m²</strong>. You usually only need planning approval if the patio breaks the R-Codes' standard rules, such as setbacks.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/roof-on-pergola-approval", "Roof on a pergola")],
            "sources": [("Do I need a permit?, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Development approval, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Development-approval"),
                        ("Building Permits, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits"),
                        ("Residential Design Codes Volume 1 (April 2026), clause 5.1.3", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
