BODY = """
<h2>Work that doesn't need a building permit</h2>
<p>The City of Canning follows the state's list of exempt work. The main ones for homes:</p>
<div class="table-wrap"><table>
<thead><tr><th>Work</th><th>No permit if</th></tr></thead><tbody>
<tr><td>Freestanding shed, garage or carport</td><td>10 m² or less and 2.4 m high or less</td></tr>
<tr><td>Pergola (open roof)</td><td>20 m² or less and 2.4 m high or less</td></tr>
<tr><td>Fence or screen</td><td>Built to the City's local laws, or masonry up to 0.75 m, other materials up to 1.8 m. Pool fences always need a permit</td></tr>
<tr><td>Retaining wall</td><td>Holds back 0.5 m of soil or less, isn't part of other building work and doesn't affect next door</td></tr>
<tr><td>Water tank</td><td>5,000 litres or less</td></tr>
<tr><td>Solar panels or solar hot water</td><td>On the roof of a house or a shed that goes with it</td></tr>
<tr><td>Repairs and renovations</td><td>Not structural, similar materials, no change to size or height, not heritage listed</td></tr>
</tbody></table></div>
<p>Exempt work must still meet the building rules and any planning rules.</p>

<h2>Planning approval</h2>
<p>For a house on its own lot, planning approval is usually only needed if it:</p>
<ul>
<li>doesn't meet the R-Codes deemed-to-comply rules,</li>
<li>is in the aircraft noise special control area, or</li>
<li>is in a bushfire prone area.</li>
</ul>
<p>Compliant patios, sheds, carports and garages on non-heritage lots don't need planning approval. Two or more homes on a lot (grouped dwellings), apartments, and work on commercial or industrial land always need it. The City offers a <strong>deemed-to-comply check</strong> if you're not sure.</p>

<h2>Applying for the permit</h2>
<ul>
<li><strong>BA1 (certified):</strong> needs a Certificate of Design Compliance from a private building surveyor. The City decides within <strong>10 working days</strong>.</li>
<li><strong>BA2 (uncertified):</strong> the City checks the plans itself, for houses and Class 10 buildings only. It decides within <strong>25 working days</strong>.</li>
</ul>
<p>If the City asks for more information, you have 21 days to send it. You can lodge online. Building Services is on 1300 422 664, weekdays 8.15am to 5pm, and also has info sheets on patios, sheds, carports, granny flats, pools and retrospective approval.</p>
<p>See <a href="/what-doesnt-need-a-building-permit">what doesn't need a permit</a>, <a href="/which-ba-form">which BA form to use</a> and <a href="/retrospective-approval">retrospective approval</a>.</p>
"""

FAQS = [
    ("What doesn't need a building permit in the City of Canning?",
     "Small freestanding sheds and carports (10 m² or less, 2.4 m or lower), pergolas up to 20 m², water tanks up to 5,000 litres, rooftop solar on a house, low retaining walls and many repairs."),
    ("Do I need planning approval for a house in Canning?",
     "Usually not, unless it breaks the R-Codes deemed-to-comply rules or is in the aircraft noise or bushfire prone areas."),
    ("How long does the City of Canning take to issue a building permit?",
     "10 working days for a certified (BA1) application and 25 working days for an uncertified (BA2) one."),
    ("How do I contact City of Canning Building Services?",
     "Call 1300 422 664 between 8.15am and 5pm on weekdays, or send an online enquiry."),
]


def page(S):
    return {"path": "city-of-canning-building-permits.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Canning building permits: exempt work, when you need planning approval and how long it takes.",
            "title": "City of Canning Building Permits (2026 Guide)",
            "desc": "City of Canning building permits: what work is exempt, when a house needs planning approval, the deemed-to-comply check, BA1 vs BA2 and processing times.",
            "eyebrow": "Council guide", "h1": "City of Canning building permits", "crumb": "City of Canning",
            "answer": "<p>In the City of Canning, most building work needs a <strong>building permit</strong>. Small freestanding sheds (10 m² or less, 2.4 m or lower), pergolas up to 20 m² and some repairs are exempt. The City decides in <strong>10 working days</strong> (BA1) or <strong>25</strong> (BA2). Planning approval is usually only needed if you don't meet the R-Codes.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/what-doesnt-need-a-building-permit", "What doesn't need a building permit"), ("/which-ba-form", "Which BA form do I need?"), ("/retrospective-approval", "Retrospective approval")],
            "sources": [("Building information sheet: work where a building permit is not required (BIS-03), City of Canning", "https://cdn.canning.wa.gov.au/media/2ghei4nv/bis-03-information-sheet-work-where-a-building-permit-is-not-required.pdf"),
                        ("Planning information sheet: is planning approval required, City of Canning", "https://www.canning.wa.gov.au/media/o2vphn2u/information-sheet-making-applications.pdf"),
                        ("Building Services, City of Canning", "https://www.canning.wa.gov.au/plan-and-build/building-services/")]}
