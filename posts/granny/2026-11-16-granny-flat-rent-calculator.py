FIELDS = [
    ("gr-rent", "Weekly rent ($)", "450"),
    ("gr-weeks", "Weeks rented per year", "50"),
    ("gr-costs", "Yearly costs: insurance, repairs, extra rates, bills you pay ($)", "3000"),
    ("gr-build", "Total build cost, including approvals ($)", "150000"),
]

ROWS = "".join(
    '<div class="field"><label for="%s">%s</label><input id="%s" type="number" inputmode="decimal" min="0" step="1" value="%s"></div>'
    % (i, l, i, v) for i, l, v in FIELDS)

TOOL = """
<div class="tool" id="gr-tool">
  <h3>Granny flat rental income calculator</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Put in your own numbers. Nothing is sent anywhere. This is before tax.</p>
  <div class="fields">""" + ROWS + """</div>
  <div class="result" id="gr-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function v(id) { var n = parseFloat(document.getElementById(id).value); return isNaN(n) || n < 0 ? 0 : n; }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-AU"); }
  function run() {
    var weeks = Math.min(v("gr-weeks"), 52);
    var gross = v("gr-rent") * weeks, net = gross - v("gr-costs"), build = v("gr-build"), html;
    html = "<h4>" + money(net) + " a year before tax</h4>";
    html += "<p>Rent in: <strong>" + money(gross) + "</strong>. Costs out: <strong>" + money(v("gr-costs")) + "</strong>.</p>";
    if (build > 0 && net > 0) {
      var yieldPct = Math.round(net / build * 1000) / 10, years = Math.round(build / net * 10) / 10;
      html += "<p>That's a return of about <strong>" + yieldPct + "%</strong> a year on the build cost, and it would take about <strong>" + years + " years</strong> of rent to cover the build.</p>";
    } else if (net <= 0) {
      html += "<p>Your costs are more than the rent, so the granny flat would lose money each year.</p>";
    }
    html += "<p>Rental income is taxable, and renting part of your home can affect your capital gains tax exemption. Talk to your accountant.</p>";
    document.getElementById("gr-out").innerHTML = html;
  }
  document.querySelectorAll("#gr-tool input").forEach(function (el) { el.addEventListener("input", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>Can you rent out a granny flat in WA?</h2>
<p>Yes. Since the R-Codes changed in 2024, a granny flat (ancillary dwelling) can be lived in by <strong>family, friends or tenants</strong>. It no longer has to be for a family member. Read the full rules in <a href="/rent-out-granny-flat-wa">can you rent out a granny flat in WA?</a></p>

<h2>How the calculator works</h2>
<ul>
<li><strong>Rent in</strong> = weekly rent × weeks rented. Allow a week or two a year for gaps between tenants.</li>
<li><strong>Net</strong> = rent in minus your yearly costs. Include insurance, repairs, any extra council or water charges, and bills you cover for the tenant.</li>
<li><strong>Return</strong> = net ÷ build cost. It's a simple way to compare the granny flat with other uses of the money.</li>
<li><strong>Years to cover the build</strong> = build cost ÷ net.</li>
</ul>
<p>The numbers in the boxes are only examples. We haven't found an official source for typical Perth granny flat rents, so check rents for similar places near you before you rely on the result.</p>

<h2>Tax</h2>
<p>The ATO says you must keep records of rental income and <strong>declare it</strong> in your tax return. Some expenses may be claimable. If the granny flat is on the same title as your home, renting it out means you're <strong>not entitled to the full main residence exemption</strong> from capital gains tax when you sell. Get advice from your accountant before you start.</p>

<h2>Approvals first</h2>
<p>A granny flat needs a <strong>building permit</strong>, and planning approval if it doesn't meet the standard R-Codes rules. See <a href="/granny-flat-approval-cost">granny flat approval cost</a> and <a href="/granny-flat-cost-perth">granny flat cost in Perth</a> for the build side of the sum.</p>
"""

FAQS = [
    ("Can I rent out my granny flat to anyone in WA?",
     "Yes. Since 2024, the R-Codes let a granny flat be lived in by family, friends or tenants."),
    ("Is granny flat rent taxable?",
     "Yes. The ATO says you must keep records of rental income and declare it in your tax return. Some expenses may be claimable."),
    ("Does renting a granny flat affect capital gains tax?",
     "The ATO says you're not entitled to the full main residence exemption if you rent out part of your home. Ask your accountant how it applies to you."),
    ("How do I work out if a granny flat is worth it?",
     "Take the yearly rent, subtract your yearly costs, and divide by the build cost to get a simple return. The calculator above does this for you."),
]


def page(S):
    return {"path": "granny-flat-rent-calculator.html", "published": "2026-11-16", "type": "Free tool", "icon": "price",
            "card": "Work out the yearly income, return and payback time from renting out a granny flat.",
            "title": "Granny Flat Rental Income Calculator (WA)",
            "desc": "Free granny flat rental income calculator: enter your rent, costs and build price to see yearly income, return and years to pay it off. Plus WA rental and tax rules.",
            "eyebrow": "Free tool", "h1": "Granny flat rental income calculator", "crumb": "Rent calculator",
            "answer": "<p>Yearly income = <strong>weekly rent × weeks rented</strong>, minus your yearly costs. Divide that by the build cost for a simple return. In WA you can rent a granny flat to <strong>anyone</strong>, but the rent is <strong>taxable</strong>. Use the calculator below with your own numbers.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/rent-out-granny-flat-wa", "Can you rent out a granny flat in WA?"), ("/granny-flat-approval-cost", "Granny flat approval cost"), ("/granny-flat-cost-perth", "Granny flat cost in Perth")],
            "sources": [("Ancillary dwelling information sheet, WA Planning", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("Renting out all or part of your home, ATO", "https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/sharing-economy-and-tax/renting-out-all-or-part-of-your-home"),
                        ("Using your home for rental or business, ATO", "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/using-your-home-for-rental-or-business")]}
