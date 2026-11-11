import build as b

Q = "/quote"

TREE = {
    "start": "s1", "depth": 3,
    "nodes": {
        "s1": {"q": "Does your project need planning approval (a development application) first?", "help": "Most projects that meet the R-Codes' deemed-to-comply rules don't. Heritage areas, setback variations and some council policies trigger one.", "opts": [
            {"t": "No, just a building permit", "go": "s2"},
            {"t": "Yes, it needs planning approval", "go": "s3"},
            {"t": "I'm not sure", "go": "r_unsure"}]},
        "s2": {"q": "Which building permit application will you lodge?", "opts": [
            {"t": "BA1, certified by a private surveyor", "go": "r_ba1"},
            {"t": "BA2, uncertified (the council checks it)", "go": "r_ba2"}]},
        "s3": {"q": "Will the council advertise it to neighbours (consultation)?", "help": "Councils usually advertise when a project asks to vary the rules in a way that affects neighbours.", "opts": [
            {"t": "No", "go": "r_da60"},
            {"t": "Yes, or probably", "go": "r_da90"}]},
        "r_ba1": {"result": True, "title": "About 10 business days, plus the surveyor",
            "body": "<p>The council must decide a complete <strong>BA1</strong> within <strong>10 business days</strong>. Before that, a private building surveyor checks your plans and issues a Certificate of Design Compliance, which adds their own turnaround time.</p><p>If the council asks for more information, you usually get <strong>21 days</strong> to supply it, and the clock pauses while you do.</p>",
            "cta": {"href": Q, "text": "Get a quote for your permit"}},
        "r_ba2": {"result": True, "title": "About 25 business days",
            "body": "<p>The council must decide a complete <strong>BA2</strong> within <strong>25 business days</strong>, which is about five weeks. BA2 can only be used for houses and Class 10 buildings like sheds, patios, carports and pools.</p><p>If the council asks for more information, you usually get <strong>21 days</strong> to supply it, and the clock pauses while you do.</p>",
            "cta": {"href": Q, "text": "Get a quote for your permit"}},
        "r_da60": {"result": True, "title": "About 60 days, then the building permit",
            "body": "<p>Planning approval usually takes up to <strong>60 days</strong> without consultation. Only after that can you lodge the building permit: add <strong>10 business days</strong> for a BA1 (plus the surveyor) or <strong>25 business days</strong> for a BA2.</p><p>All up, plan for roughly <strong>3 to 4 months</strong>.</p>",
            "cta": {"href": Q, "text": "Get help with both approvals"}},
        "r_da90": {"result": True, "title": "About 90 days, then the building permit",
            "body": "<p>When neighbours are consulted, planning approval can take up to <strong>90 days</strong>. Then add <strong>10 business days</strong> for a BA1 (plus the surveyor) or <strong>25 business days</strong> for a BA2.</p><p>All up, plan for roughly <strong>4 to 5 months</strong>.</p>",
            "cta": {"href": Q, "text": "Get help with both approvals"}},
        "r_unsure": {"result": True, "title": "Find out first, because it changes the timeline a lot",
            "body": "<p>A building permit on its own takes about <strong>10 to 25 business days</strong>. If you also need planning approval, add <strong>60 to 90 days</strong> before that. Ask your council, or send us your plans and we'll check.</p>",
            "cta": {"href": Q, "text": "Ask us to check"}},
    },
}

BODY = """
{CHECKER}
<h2>The time limits at a glance</h2>
<div class="table-wrap"><table>
<thead><tr><th>Approval</th><th>Time limit</th></tr></thead><tbody>
<tr><td>Building permit, BA1 (certified)</td><td>10 business days</td></tr>
<tr><td>Building permit, BA2 (uncertified)</td><td>25 business days</td></tr>
<tr><td>Supplying more information if asked</td><td>Usually 21 days</td></tr>
<tr><td>Planning approval, no consultation</td><td>60 days</td></tr>
<tr><td>Planning approval, with consultation</td><td>90 days</td></tr>
</tbody></table></div>
<p>These limits come from the state rules, so they're the same across WA. Councils such as Swan, Melville and Stirling publish them.</p>

<h2>When the clock starts</h2>
<p>The clock only starts once the council has a <strong>complete</strong> application. The City of Swan says it starts at midnight the day after a complete application is received. A missing form, plan or fee can add weeks before anything happens.</p>

<h2>What slows things down</h2>
<ul>
<li><strong>Missing documents.</strong> The council asks for more information, and the clock pauses.</li>
<li><strong>Not replying in time.</strong> If you miss the 21 days, the City of Swan says it may refuse the application, and fees are unlikely to be refunded.</li>
<li><strong>Planning approval.</strong> It must come first, and it's the longest step.</li>
<li><strong>Surveyor turnaround.</strong> For a BA1, the private surveyor's time comes before the 10 days.</li>
</ul>
<p>Not sure which form to use? Read <a href="/ba1-vs-ba2">BA1 vs BA2</a>, or <a href="/development-approval-vs-building-permit">planning approval vs building permit</a>.</p>
"""

FAQS = [
    ("How long does a building permit take in WA?",
     "A council must decide a complete BA1 within 10 business days and a complete BA2 within 25 business days."),
    ("How long does planning approval take in WA?",
     "Usually up to 60 days, or up to 90 days if the council advertises it to neighbours."),
    ("Does the clock stop if the council asks for more information?",
     "Yes. You usually get 21 days to supply it. Councils such as Swan may refuse the application if you don't."),
    ("Can I lodge the building permit and planning approval together?",
     "Councils such as Wanneroo say planning approval must come before the building permit."),
]


def page(S):
    title = "How long will my approval take?"
    return {"path": "approval-timeline-calculator.html", "published": "2026-11-12", "type": "Free tool", "icon": "clock",
            "card": "Answer up to three questions to see how long your WA building permit and planning approval will take.",
            "title": "Building Approval Timeline Calculator (WA)",
            "desc": "Free tool: how long does a building permit take in WA? BA1 10 business days, BA2 25 business days, planning approval 60 to 90 days, and what slows it down.",
            "eyebrow": "Free tool", "h1": "How long will my building approval take?", "crumb": "Timeline calculator",
            "answer": "<p>In WA a council must decide a complete <strong>BA1</strong> building permit within <strong>10 business days</strong> and a <strong>BA2</strong> within <strong>25 business days</strong>. If you also need planning approval, add <strong>60 days</strong>, or <strong>90 days</strong> if neighbours are consulted. Answer up to three questions below.</p>",
            "body": BODY.replace("{CHECKER}", b.checker(S, TREE, title, "Up to three quick questions.")), "faqs": FAQS,
            "related": [("/ba1-vs-ba2", "BA1 vs BA2"), ("/development-approval-vs-building-permit", "Planning approval vs building permit"), ("/city-of-swan-building-permits", "City of Swan building permits")],
            "sources": [("Building, City of Swan", "https://www.swan.wa.gov.au/plan-and-build/building"),
                        ("Building a shed or outbuilding, Town of Mosman Park", "https://www.mosmanpark.wa.gov.au/build/building-or-renovating/building-a-shed-or-outbuilding/"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
