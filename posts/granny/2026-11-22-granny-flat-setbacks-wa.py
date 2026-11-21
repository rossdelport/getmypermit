BODY = """
<h2>From the street</h2>
<p>A granny flat must sit <strong>behind the street setback line</strong> to avoid planning approval. The usual street setbacks are:</p>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Usual front street setback</th></tr></thead><tbody>
<tr><td>R10 / R12.5</td><td>7.5 m</td></tr>
<tr><td>R20 / R25</td><td>6 m</td></tr>
<tr><td>R30 / R40</td><td>4 m</td></tr>
<tr><td>R50 / R60</td><td>2 m</td></tr>
</tbody></table></div>
<p>The R-Codes allow some reductions, for example by averaging with the neighbours' houses. Councils vary, and local policies or estate rules can ask for more.</p>

<h2>From side and rear boundaries</h2>
<p>The setback depends on the wall's <strong>height</strong> and <strong>length</strong>, and whether it has <strong>major openings</strong> (big windows or glass doors from a bedroom or living area). For a single-storey wall up to <strong>3.5 m</strong> high:</p>
<div class="table-wrap"><table>
<thead><tr><th>Wall length</th><th>No major openings</th><th>With major openings</th></tr></thead><tbody>
<tr><td>Up to 14 m</td><td>1 m</td><td>1.5 m</td></tr>
<tr><td>15 m or longer</td><td>1.5 m</td><td>1.5 m</td></tr>
</tbody></table></div>
<p>Taller walls need more. For example, a 4 m high wall with major openings needs <strong>1.8 m</strong> if it is up to 9 m long, rising to <strong>2.7 m</strong> at 14 m. Eaves and gutters can usually project up to 0.75 m into the setback.</p>

<h2>Building on the boundary</h2>
<p>A wall can usually go right on the boundary, behind the street setback, if:</p>
<ul>
<li>it's against a neighbour's boundary wall of the same size or bigger; or</li>
<li>at <strong>R20 and R25</strong>, it's no more than <strong>3.5 m</strong> high and up to 9 m long (or a third of the boundary behind the front setback, if more), on up to two boundaries; or</li>
<li>at <strong>R30 to R40</strong>, it's no more than 3.5 m high, for up to two-thirds of the boundary behind the front setback, on up to two boundaries.</li>
</ul>

<h2>What happens if you don't meet them</h2>
<p>You'll usually need <strong>planning approval</strong>. The council then judges the design against the R-Codes' design principles: building bulk, sunlight, ventilation and privacy for the neighbours. Upper floors and decks 0.5 m or more above the ground also have privacy setbacks. Every granny flat still needs a <strong>building permit</strong>.</p>
<p>Read <a href="/granny-flat-no-planning-approval">how to skip planning approval</a>, <a href="/granny-flat-at-the-front">putting a granny flat at the front</a>, or the <a href="/city-of-stirling-granny-flat-rules">City of Stirling granny flat rules</a>.</p>
"""

FAQS = [
    ("How close to the boundary can a granny flat be in WA?",
     "Usually 1 m from a side or rear boundary for a single-storey wall up to 14 m long with no big windows, or 1.5 m with them. It can sometimes go right on the boundary."),
    ("Can a granny flat be built on the boundary in WA?",
     "Often yes, at R20 and above, behind the street setback. At R20/R25 the wall can be up to 3.5 m high and 9 m long on up to two boundaries."),
    ("Can a granny flat go in front of the house?",
     "Not without planning approval. To skip it, the granny flat has to be behind the street setback line."),
    ("What if my granny flat doesn't meet the setbacks?",
     "You usually need planning approval, where the council looks at bulk, sunlight and privacy for the neighbours."),
]


def page(S):
    return {"path": "granny-flat-setbacks-wa.html", "published": "2026-11-22", "type": "Question answer", "icon": "granny",
            "card": "Granny flat setbacks in WA: street, side and rear boundaries, boundary walls and windows.",
            "title": "Granny Flat Setback Rules in WA (2026)",
            "desc": "Granny flat setback rules in WA: street setbacks by R-Code, the 1 m and 1.5 m side setbacks, when windows push it further, and when you can build on the boundary.",
            "eyebrow": "Question answer", "h1": "What are the setback rules for a granny flat in WA?", "crumb": "Granny flat setbacks",
            "answer": "<p>A granny flat must sit <strong>behind the street setback</strong> (usually 6 m at R20). For a single-storey wall, the side or rear setback is usually <strong>1 m</strong>, or <strong>1.5 m</strong> if the wall is longer than 14 m or has big windows. At R20 and above it can often go <strong>on the boundary</strong>, up to 3.5 m high.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-no-planning-approval", "Granny flat with no planning approval"), ("/granny-flat-at-the-front", "Granny flat at the front"), ("/city-of-stirling-granny-flat-rules", "City of Stirling granny flat rules")],
            "sources": [("Residential Design Codes Volume 1, WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Ancillary dwelling (granny flat) information sheet, City of Stirling", "https://www.stirling.wa.gov.au/awcontent/Web/Documents/Ancillary-Dwellings-(Granny-Flat).pdf")]}
