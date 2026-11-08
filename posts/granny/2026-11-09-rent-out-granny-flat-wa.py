BODY = """
<h2>Yes, since 2024</h2>
<p>The state's granny flat changes to the R-Codes took effect in April 2024. The WA planning department's information sheet says <strong>anyone can live in a granny flat</strong>: "from a relative, friend or someone unknown to you who you or a real-estate agent enters into a rental agreement with."</p>
<p>The City of Joondalup says the same: a granny flat can be rented out separately from the main house, as long as it meets the R-Codes definition of a dwelling.</p>

<h2>What changed</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Old rules (some older council schemes)</th><th>Now (R-Codes 2024)</th></tr></thead><tbody>
<tr><td>Who can live there</td><td>Often family members of the people in the main house only</td><td>Anyone, including tenants</td></tr>
<tr><td>Minimum lot size</td><td>Often 350 m² or more</td><td>No minimum, if the deemed-to-comply rules are met</td></tr>
<tr><td>Strata and grouped lots</td><td>Usually not allowed</td><td>Allowed at all density codes in Volume 1</td></tr>
<tr><td>Size</td><td>Varied (some schemes 60 m²)</td><td>Up to 70 m² without planning approval</td></tr>
</tbody></table></div>
<p>Some council documents online still show the old rules. Check you're reading a current version.</p>

<h2>What doesn't change</h2>
<ul>
<li><strong>It stays on your title.</strong> A granny flat can't be subdivided or strata titled separately, so you can't sell it on its own. See <a href="/subdivide-granny-flat">subdividing a granny flat</a>.</li>
<li><strong>It must be a proper dwelling.</strong> It's a self-contained home, so a kitchen and bathroom are generally expected.</li>
<li><strong>It needs a building permit</strong> and must meet the National Construction Code.</li>
<li><strong>Planning rules still apply.</strong> Size, setbacks, open space and, in some councils, parking and matching the main house.</li>
</ul>

<h2>Before you rent it out</h2>
<ul>
<li><strong>Check it was approved.</strong> An unapproved granny flat, or a shed or garage converted without approval, isn't a legal dwelling. Fix that first with a building approval certificate.</li>
<li><strong>Normal renting rules apply.</strong> Once you sign a rental agreement, you're a landlord under WA tenancy law. Consumer Protection has guides for landlords.</li>
<li><strong>Talk to your insurer and accountant.</strong> Renting can change your insurance and tax.</li>
</ul>
<p>Planning one to rent? See the <a href="/granny-flat-approval-process">granny flat approval process</a> and <a href="/granny-flat-rules-wa">granny flat rules in WA</a>.</p>
"""

FAQS = [
    ("Can I rent out my granny flat in WA?",
     "Yes. Since the April 2024 R-Codes changes, anyone can live in a granny flat, including tenants under a rental agreement. It must meet the R-Codes definition of a dwelling."),
    ("Does a granny flat tenant have to be family in WA?",
     "No. The state's information sheet says anyone can live in a granny flat, from a relative or friend to a tenant you don't know."),
    ("Can I sell my granny flat separately?",
     "No. A granny flat can't be subdivided or strata titled separately from the main house."),
    ("Can I rent out a granny flat on a strata lot?",
     "The R-Codes now allow granny flats on grouped dwelling and strata lots at all density codes in Volume 1. You may also need strata approval."),
    ("Do I need approval to rent out an existing granny flat?",
     "Not to rent it, but it must have been approved as a dwelling. An unapproved granny flat needs to be made legal first, usually with a building approval certificate."),
]


def page(S):
    return {"path": "rent-out-granny-flat-wa.html", "published": "2026-11-09", "type": "Question answer", "icon": "granny",
            "card": "Yes since 2024. What changed, what didn't, and what to check before you rent.",
            "title": "Can You Rent Out a Granny Flat in WA? (2026)",
            "desc": "Renting out a granny flat in WA: anyone can live in one since the 2024 R-Codes changes. What changed, what still applies, and what to check before you rent.",
            "eyebrow": "Question answer", "h1": "Can you rent out a granny flat in WA?", "crumb": "Renting out a granny flat",
            "answer": "<p><strong>Yes.</strong> Since the April 2024 R-Codes changes, anyone can live in a WA granny flat, including tenants under a rental agreement. It must still be an approved dwelling, and it can't be sold separately from the main house.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/subdivide-granny-flat", "Can I subdivide my granny flat?"), ("/granny-flat-approval-process", "Granny flat approval process")],
            "sources": [("Granny flats info sheet (WA Planning)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Granny flat or ancillary dwelling (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/granny-flat-or-ancillary-dwelling"),
                        ("R-Codes Volume 1 Explanatory Guidelines 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-04/r-codes-vol-1-explanatory-guideline_2024-mar2024.pdf")]}
