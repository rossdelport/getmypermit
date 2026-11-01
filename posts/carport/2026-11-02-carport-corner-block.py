BODY = """
<h2>Why corner blocks are different</h2>
<p>A corner block has two street boundaries: the <strong>primary street</strong> (usually the one the house faces) and the <strong>secondary street</strong> (the side street). Each has its own setback, so there's less room to play with than on a normal lot.</p>

<h2>The secondary street is often the best spot</h2>
<p>The City of Stirling's carport and garage guide says that on corner lots, carports and garages <strong>should face the secondary street</strong> and avoid access from busy roads. They can come as close as <strong>1.5 m</strong> to the secondary street boundary. The City of Wanneroo also uses a 1.5 m secondary street setback for carports.</p>
<p>That often means a carport down the side of the house, opening onto the quieter street, is easier to get approved than one in front of the house.</p>

<h2>If the carport goes in front of the house</h2>
<p>The normal front (primary street) rules apply. A carport can come forward into the street setback if it's:</p>
<ul>
<li>no wider than <strong>60% of the frontage</strong></li>
<li>open, with an unobstructed view between the house and the street (no solid door)</li>
<li>in materials that suit the house</li>
</ul>
<p>Try our <a href="/front-setback-carport-calculator">front setback carport calculator</a> with your numbers.</p>

<h2>Minimum street setbacks at Stirling</h2>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Carport street setback</th></tr></thead><tbody>
<tr><td>R10, R12.5</td><td>3.75 m</td></tr>
<tr><td>R20, R25</td><td>3 m</td></tr>
<tr><td>R30, R40</td><td>2 m</td></tr>
<tr><td>R50, R60</td><td>1 m</td></tr>
<tr><td>R80</td><td>0.5 m</td></tr>
</tbody></table></div>
<p>Posts also need to be at least 1 m from the side boundary to skip planning approval at Stirling.</p>

<h2>Other things to check</h2>
<ul>
<li><strong>A new or wider crossover</strong> needs its own approval from council.</li>
<li><strong>Laneway.</strong> If your lot backs onto a laneway, councils like Stirling encourage using it instead of the street.</li>
<li><strong>Heritage areas</strong> always need planning approval.</li>
<li><strong>A building permit</strong> is needed for every carport, even when planning approval isn't.</li>
</ul>
"""

FAQS = [
    ("Can I build a carport on a corner block in WA?",
     "Yes. On a corner block, councils such as Stirling prefer the carport to face the secondary (side) street, where it can be as close as 1.5 m to the boundary."),
    ("What is the secondary street setback for a carport?",
     "Both the City of Stirling and the City of Wanneroo use 1.5 m from the secondary street boundary."),
    ("Does a corner block carport need council approval?",
     "Every carport needs a building permit. It only needs planning approval as well if it doesn't meet the setback, width, view and materials rules, or if it's in a heritage area."),
]


def page(S):
    return {"path": "carport-corner-block.html", "published": "2026-11-02", "type": "Question answer", "icon": "carport",
            "card": "Corner blocks have two street setbacks. Why the side street is often the easiest spot.",
            "title": "Can I Build a Carport on a Corner Block? (WA Rules)",
            "desc": "Carports on corner blocks in WA: the 1.5 m secondary street setback, why councils prefer the side street, the 60% frontage rule and the R-Code street setbacks.",
            "eyebrow": "Question answer", "h1": "Can I build a carport on a corner block?", "crumb": "Carport on a corner block",
            "answer": "<p><strong>Yes.</strong> On a corner block, councils like Stirling prefer the carport to <strong>face the secondary (side) street</strong>, where it can come as close as <strong>1.5 m</strong> to the boundary. In front of the house, the usual 60% frontage and open-view rules apply. Every carport still needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-in-front-setback", "Carports in the front setback"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf")]}
