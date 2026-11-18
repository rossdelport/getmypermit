BODY = """
<h2>When you need planning approval</h2>
<p>A granny flat that meets all the R-Codes' standard ("deemed-to-comply") rules usually doesn't need planning approval. You need it when your design breaks one of them, for example:</p>
<ul>
<li>It's bigger than <strong>70 m²</strong>.</li>
<li>It's too close to a boundary or sits in the street setback.</li>
<li>There's no extra parking bay, and you're not near high-frequency transport.</li>
<li>It overlooks neighbours from an upper floor or deck.</li>
<li>It's on land with a local plan, heritage listing or rural zoning that adds rules.</li>
</ul>
<p>Breaking a standard rule doesn't mean a "no". The council checks your design against the R-Codes' <strong>design principles</strong> instead, which are more flexible.</p>

<h2>Step by step</h2>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What to do</th></tr></thead><tbody>
<tr><td>1. Find the problem</td><td>List each rule your design breaks. Some councils offer a paid check to tell you.</td></tr>
<tr><td>2. Explain why it works</td><td>For each one, write how your design still meets the design principle, such as no overshadowing or privacy screening.</td></tr>
<tr><td>3. Lodge the application</td><td>Lodge online with the form, plans and fee. A planning fee for work under $50,000 is $147 in 2025/26. Bigger jobs cost more.</td></tr>
<tr><td>4. Neighbour comment</td><td>If the change affects neighbours, the council may ask them for comment.</td></tr>
<tr><td>5. Decision</td><td>Councils have <strong>60 days</strong>, or <strong>90 days</strong> with neighbour comment. Approval may come with conditions.</td></tr>
<tr><td>6. Building permit</td><td>Only then apply for the building permit, meeting any conditions.</td></tr>
</tbody></table></div>
<p>If the council asks for more information, reply quickly. The City of Gosnells, for example, gives you 21 days or it may refuse. Applying after you've already built costs more: the City of Joondalup adds a penalty of twice the fee.</p>

<h2>If it's bigger than 70 m²</h2>
<p>Over 70 m² is outside the granny flat rules, so the council may assess it as a second house instead. That brings in lot size and density rules, so ask your council early. Councils vary.</p>
<p>Check if you can <a href="/granny-flat-no-planning-approval">skip planning approval</a>, use the <a href="/granny-flat-size-calculator">granny flat size calculator</a>, or read the full <a href="/granny-flat-approval-process">granny flat approval process</a>.</p>
"""

FAQS = [
    ("Can I build a granny flat that breaks the rules in WA?",
     "Often yes, with planning approval. The council checks your design against the R-Codes' design principles, which are more flexible than the standard rules."),
    ("How long does planning approval for a granny flat take?",
     "Councils have 60 days, or 90 days if neighbours are asked for comment."),
    ("How much does planning approval for a granny flat cost?",
     "Council planning fees are set by the state. For work under $50,000 it's $147 in 2025/26. Bigger jobs cost more, and plans and reports add to that."),
    ("What if my granny flat is bigger than 70 m²?",
     "It's outside the granny flat rules, so the council may assess it as a second house, with lot size and density rules."),
]


def page(S):
    return {"path": "granny-flat-planning-approval.html", "published": "2026-11-19", "type": "How-to guide", "icon": "plan",
            "card": "How to get planning approval when your granny flat breaks the standard rules.",
            "title": "Granny Flat Planning Approval in WA: Step by Step (2026)",
            "desc": "How to get planning approval for a granny flat that breaks the R-Codes rules (over 70 m², setbacks, parking): the steps, fees, 60 or 90 day timeline and tips.",
            "eyebrow": "How-to guide", "h1": "How to get approval when your granny flat breaks the rules", "crumb": "Granny flat planning approval",
            "answer": "<p>If your granny flat breaks a standard R-Codes rule (such as size, setbacks or parking), apply for <strong>planning approval</strong>. Show how the design still meets the R-Codes' <strong>design principles</strong>. Councils have <strong>60 days</strong> to decide, or <strong>90</strong> with neighbour comment. Then apply for the building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-no-planning-approval", "Granny flat without planning approval"), ("/granny-flat-size-calculator", "Granny flat size calculator"), ("/granny-flat-approval-process", "Granny flat approval process")],
            "sources": [("Development approval, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Development-approval"),
                        ("Planning services fees and charges 2025/26, City of Joondalup", "https://www.joondalup.wa.gov.au/awcontent/Web/Documents/Budget,%20Fees%20and%20Financial%20Reports/Planning-Services-fees-and-charges-2025_26.pdf"),
                        ("Residential Design Codes Volume 1 (April 2026)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
