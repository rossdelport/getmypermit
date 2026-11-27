BODY = """
<h2>It's an offence under the Building Act</h2>
<p>Section 9 of the WA <em>Building Act 2011</em> says you must not do building work unless a building permit is in place, or the work is exempt. This covers small jobs too, such as patios, sheds, fences, retaining walls, pools and spas. See <a href="/what-doesnt-need-a-building-permit">what doesn't need a building permit</a>.</p>

<h2>The fines</h2>
<div class="table-wrap"><table>
<thead><tr><th>Offence</th><th>Penalty under section 9</th></tr></thead><tbody>
<tr><td>First offence</td><td>Fine of $50,000</td></tr>
<tr><td>Second offence</td><td>Fine of $75,000</td></tr>
<tr><td>Third or later offence</td><td>Fine of $100,000 and 12 months' jail</td></tr>
</tbody></table></div>
<p>These are the maximum penalties in the Act. Councils usually look at how serious the case is. The City of Gosnells, for example, says it may act where someone has "flagrantly disregarded" the need for a permit. You can also be prosecuted under the <em>Planning and Development Act 2005</em> if planning approval was needed too.</p>

<h2>What else can happen</h2>
<ul>
<li><strong>You may have to fix it.</strong> If the work doesn't meet the building standards, the council can ask for changes.</li>
<li><strong>It may have to come down.</strong> If the work is badly non-compliant, or the fixes aren't done, the council can refuse approval and act to have it removed.</li>
<li><strong>Selling gets harder.</strong> If the council has no approval on record, the structure counts as unauthorised. Buyers are often told to get a plan search to check this before they buy. See <a href="/check-if-building-is-approved">how to check if a building is approved</a>.</li>
</ul>

<h2>How to fix it</h2>
<p>You can apply for approval after the fact. For houses, sheds, patios and other Class 1 and 10 buildings, this is a <strong>BA13</strong> (building approval certificate) application, with a <strong>BA18</strong> certificate of building compliance from a registered building surveyor. The BA18 must refer to as-built plans showing the work complies. Approval isn't guaranteed. See <a href="/retrospective-approval">retrospective approval</a>.</p>
<p>Councils vary, so check with your own council's building team.</p>
"""

FAQS = [
    ("What is the fine for building without a permit in WA?",
     "Under section 9 of the Building Act 2011, up to $50,000 for a first offence, $75,000 for a second, and $100,000 plus 12 months' jail for a third or later offence."),
    ("Can the council make me pull down unapproved work?",
     "Yes. If the work doesn't comply and isn't fixed, the council can refuse approval and take action to have it removed."),
    ("Can I get approval after I've built?",
     "Often yes. For Class 1 and 10 buildings you apply with a BA13 and a BA18 certificate of building compliance from a registered building surveyor."),
    ("How do I know if a building on my property is approved?",
     "Ask your council for a plan search. If the council has no approval on record, the building is treated as unauthorised."),
]


def page(S):
    return {"path": "building-without-a-permit-wa.html", "published": "2026-11-28", "type": "Question answer", "icon": "doc",
            "card": "What happens if you build without a permit in WA: the fines, removal orders and how to fix it.",
            "title": "What Happens If You Build Without a Permit in WA? (2026)",
            "desc": "Building without a permit in WA: the Building Act fines ($50,000 first offence, up to $100,000 and jail), removal orders, problems when selling, and how to get approval after the fact.",
            "eyebrow": "Question answer", "h1": "What happens if you build without a permit in WA?", "crumb": "Building without a permit",
            "answer": "<p>Building without a needed permit is an offence under the WA <em>Building Act 2011</em>. The maximum fine is <strong>$50,000</strong> for a first offence, rising to <strong>$100,000 and 12 months' jail</strong> for repeat offences. The council can also make you fix the work or remove it. You can often apply for approval after the fact.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/retrospective-approval", "Retrospective approval"), ("/check-if-building-is-approved", "Check if a building is approved"), ("/certificate-of-building-compliance", "Certificate of building compliance")],
            "sources": [("Building Act 2011 (WA), section 9, AustLII", "https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/wa/num_act/ba201124o2011137/s9.html"),
                        ("Unauthorised work, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work")]}
