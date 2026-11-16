FIELDS = [
    ("tc-home", "Price of the tiny home ($)", "85000"),
    ("tc-move", "Delivery or transport ($)", "3000"),
    ("tc-site", "Site work: pad, footings, access ($)", "5000"),
    ("tc-serv", "Power, water and sewer or septic connections ($)", "8000"),
    ("tc-other", "Other: deck, steps, furniture, plans, council fees ($)", "2000"),
]

ROWS = "".join(
    '<div class="field"><label for="%s">%s</label><input id="%s" type="number" inputmode="decimal" min="0" step="1" value="%s"></div>'
    % (i, l, i, v) for i, l, v in FIELDS)

TOOL = """
<div class="tool" id="tc-tool">
  <h3>Tiny home cost calculator</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Put in your own quotes. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="tc-type">Type of tiny home</label><select id="tc-type"><option value="fixed">Fixed on footings (building permit)</option><option value="wheels">On wheels (no building permit)</option></select></div>
""" + ROWS + """</div>
  <div class="result" id="tc-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function v(id) { var n = parseFloat(document.getElementById(id).value); return isNaN(n) || n < 0 ? 0 : n; }
  function money(n) { return "$" + n.toLocaleString("en-AU", {maximumFractionDigits: 0}); }
  function cents(n) { return "$" + n.toLocaleString("en-AU", {minimumFractionDigits: 2, maximumFractionDigits: 2}); }
  function run() {
    var fixed = document.getElementById("tc-type").value === "fixed";
    var base = v("tc-home") + v("tc-move") + v("tc-site") + v("tc-serv") + v("tc-other");
    var html, fees = 0;
    if (fixed) {
      var work = v("tc-home") + v("tc-site") + v("tc-serv");
      var permit = Math.max(work * 0.0032, 121);
      var bsl = work > 45000 ? work * 0.00137 : 61.65;
      var ctf = work > 100000 ? work * 0.002 : 0;
      permit = Math.round(permit * 100) / 100; bsl = Math.round(bsl * 100) / 100; ctf = Math.round(ctf * 100) / 100;
      fees = permit + bsl + ctf;
      html = "<h4>About " + money(Math.round(base + fees)) + " all up</h4>";
      html += "<p>Your costs: <strong>" + money(base) + "</strong>. State building permit fees on " + money(work) + " of work (uncertified BA2): permit <strong>" + cents(permit) + "</strong>, Building Services Levy <strong>" + cents(bsl) + "</strong>" + (ctf ? ", Construction Training Fund levy <strong>" + cents(ctf) + "</strong>" : "") + ".</p>";
      html += "<p>Planning approval, a building surveyor (for a BA1), engineering, an energy report and a bushfire report can add more.</p>";
    } else {
      html = "<h4>About " + money(Math.round(base)) + " all up</h4>";
      html += "<p>A genuine tiny home on wheels is a caravan, so there's no building permit. To live in it for more than 5 nights in 28 days you need council approval, for up to 24 months at a time. Council fees vary.</p>";
    }
    document.getElementById("tc-out").innerHTML = html;
  }
  document.querySelectorAll("#tc-tool input, #tc-tool select").forEach(function (el) { el.addEventListener("input", run); el.addEventListener("change", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>What tiny homes cost to buy in Perth</h2>
<p>The home itself is the biggest cost. Sellers advertise starting prices from about <strong>$26,500</strong> (Everyday Tiny Homes) and <strong>$42,990</strong> (Perth Tiny House "Bek"), to <strong>$84,990</strong> (Treehab, 5 to 6 m) and <strong>$192,800</strong> (Summit Tiny Homes). See <a href="/tiny-home-prices-perth">tiny home prices in Perth</a> for what each includes.</p>

<h2>Costs people forget</h2>
<ul>
<li><strong>Delivery.</strong> Loads wider than 2.5 m or higher than 4.3 m need a Main Roads permit. Homes built interstate cost more to move.</li>
<li><strong>Site work.</strong> A level pad, and for a fixed home, engineered footings.</li>
<li><strong>Services.</strong> Licensed trades to connect power, water and sewer, or a septic system where there's no sewer.</li>
<li><strong>Approvals.</strong> A fixed tiny home needs a building permit and must meet the building code. One on wheels needs council approval to be lived in for more than 5 nights in 28 days.</li>
</ul>

<h2>How the fees are worked out</h2>
<p>For a fixed tiny home the calculator uses the state fees for an uncertified (BA2) permit: <strong>0.32%</strong> of the value of the work (at least $121), plus the Building Services Levy (<strong>$61.65</strong> up to $45,000, then 0.137%), plus the Construction Training Fund levy (<strong>0.2%</strong> on work over $100,000). The numbers in the boxes are only examples. Replace them with your own quotes.</p>
<p>Not sure which type you have? Try the <a href="/caravan-or-building-checker">caravan or building checker</a>, or compare <a href="/wheels-vs-fixed-tiny-home">wheels and fixed tiny homes</a>.</p>
"""

FAQS = [
    ("How much does a tiny home cost in Perth?",
     "Sellers advertise from about $26,500 to over $190,000 for the home itself. Delivery, site work, services and approvals add to that."),
    ("Do I need a building permit for a tiny home in WA?",
     "A fixed tiny home on footings does. A genuine towable tiny home on wheels is a caravan and doesn't, but it needs council approval to be lived in long term."),
    ("How much is the building permit for a fixed tiny home?",
     "For a BA2 it's 0.32% of the value of the work, plus the Building Services Levy and, over $100,000, the Construction Training Fund levy. The calculator works it out."),
    ("What costs do people forget with a tiny home?",
     "Delivery, a level pad or footings, connecting power, water and sewer, and approvals."),
]


def page(S):
    return {"path": "tiny-home-cost-calculator.html", "published": "2026-11-17", "type": "Free tool", "icon": "price",
            "card": "Add up the real cost of a tiny home: the home, delivery, site work, services and permit fees.",
            "title": "Tiny Home Cost Calculator (Perth)",
            "desc": "Free tiny home cost calculator for Perth: add the home, delivery, site work and connections, and see WA building permit fees for a fixed tiny home.",
            "eyebrow": "Free tool", "h1": "Tiny home cost calculator", "crumb": "Cost calculator",
            "answer": "<p>The total cost of a tiny home is the <strong>home</strong> plus <strong>delivery</strong>, <strong>site work</strong>, <strong>service connections</strong> and <strong>approvals</strong>. Perth sellers advertise homes from about $26,500 to over $190,000. A fixed tiny home also pays state building permit fees, which the calculator below works out.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-prices-perth", "Tiny home prices in Perth"), ("/caravan-or-building-checker", "Caravan or building checker"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home")],
            "sources": [("Building approvals: fees and levy, WA Government (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy"),
                        ("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Perth Tiny House (advertised prices)", "https://www.perthtinyhouse.com.au"),
                        ("Tiny houses in Perth, Treehab (advertised prices)", "https://www.treehab.com.au/perth"),
                        ("Tiny homes WA Perth, Everyday Tiny Homes (advertised prices)", "https://www.everydaytinyhomes.com.au/location/wa-perth/"),
                        ("Tiny home designs Perth, Summit Homes (advertised prices)", "https://www.summithomes.com.au/tiny-homes/tiny-home-designs/")]}
