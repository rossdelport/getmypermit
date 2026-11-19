BODY = """
<h2>Why councils want engineering</h2>
<p>A patio roof has to stand up to wind and its own weight. The engineering shows the posts, beams, footings and fixings are strong enough for your site. Without it, the council or building surveyor can't confirm the patio meets the building rules.</p>
<ul>
<li>The <strong>City of Belmont</strong> asks for an engineer-certified structure with every BA2 patio application, plus a 1:200 site plan and 1:100 elevations.</li>
<li>For a <strong>BA1</strong>, the building surveyor's certificate (BA3) has to list the plans and technical documents that show the patio complies.</li>
<li>Perth patio kit sellers say engineering detail is required for a building permit application.</li>
</ul>

<h2>When you don't need it</h2>
<p>If the patio is exempt from a building permit, you don't need to lodge engineering. In many Perth councils a <strong>freestanding</strong> patio up to <strong>10 m²</strong> and <strong>2.4 m</strong> high is exempt. Attached patios usually need a permit. Councils vary, so check yours. It still has to be built safely.</p>

<h2>What it costs</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Advertised price (Nov 2026)</th></tr></thead><tbody>
<tr><td>Engineering with a patio kit (Patio &amp; Shed Kits WA)</td><td>$350</td></tr>
<tr><td>Standard patio steel engineering (Perth Drafting)</td><td>About $450 + GST</td></tr>
<tr><td>Footing or slab design, custom (The Quote Yard WA guide)</td><td>$900 to $3,500</td></tr>
</tbody></table></div>
<p>Most patio kits and builders include engineering in their package. If you're building from scratch, a local engineer or drafter can do it.</p>
<p>See what goes in <a href="/patio-plans-for-council">patio plans for council</a>, <a href="/patio-approval-cost-perth">what patio approval costs</a>, or <a href="/patio-building-permit">when a patio needs a permit</a>.</p>
"""

FAQS = [
    ("Does a patio need engineering in WA?",
     "Usually yes, if it needs a building permit. Councils ask for engineering that shows the posts, beams, footings and fixings are strong enough."),
    ("How much does patio engineering cost in Perth?",
     "Advertised prices are about $350 to $450 for a standard patio. Custom footing designs can cost $900 to $3,500."),
    ("Do patio kits come with engineering?",
     "Most Perth patio kit sellers offer engineering with the kit, often as an add-on."),
    ("Does an exempt patio need engineering?",
     "You don't need to lodge it with council, but the patio must still be built safely."),
]


def page(S):
    return {"path": "patio-engineering-wa.html", "published": "2026-11-20", "type": "Question answer", "icon": "pergola",
            "card": "Does a patio need engineering in WA? Why councils ask for it and what it costs.",
            "title": "Does a Patio Need Engineering in WA? (2026)",
            "desc": "Does a patio need engineering in WA? Usually yes if it needs a building permit. Why councils ask for it, when you don't need it, and what it costs in Perth.",
            "eyebrow": "Question answer", "h1": "Does a patio need engineering in WA?", "crumb": "Patio engineering",
            "answer": "<p>Usually <strong>yes</strong>. If your patio needs a building permit, councils ask for engineering that shows the posts, beams, footings and fixings are strong enough. Standard patio engineering is advertised at about <strong>$350 to $450</strong> in Perth, and most kits include it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-plans-for-council", "Patio plans for council"), ("/patio-approval-cost-perth", "Patio approval cost in Perth"), ("/patio-building-permit", "Patio building permit")],
            "sources": [("WA permits, Patio & Shed Kits WA", "https://patiokitswa.com.au/wa-permits/"),
                        ("Patios, City of Belmont", "https://www.belmont.wa.gov.au/Build/Demolishing-and-Building/Approval-for-buildings-and-structures/I-want-to-build/Patio,-pergola-or-shade-sail"),
                        ("Building Permits, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits")]}
