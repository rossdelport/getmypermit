TOOL = """
<div class="tool" id="fee-tool">
  <h3>Building permit fee calculator</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Uses the state's 2026 fees. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="fee-v">Value of the work, including GST ($) <span class="hint">materials, labour, services, fees and margin</span></label><input id="fee-v" type="number" inputmode="decimal" min="0" step="100" value="20000"></div>
    <div class="field"><label for="fee-t">Application type</label><select id="fee-t"><option value="ba2">BA2, uncertified (council checks the plans)</option><option value="ba1">BA1, certified (private surveyor checks first)</option></select></div>
    <div class="field"><label for="fee-c">Building type</label><select id="fee-c"><option value="1">House, granny flat, shed, garage, carport, patio, pool (Class 1 or 10)</option><option value="2">Other building (Class 2 to 9)</option></select></div>
  </div>
  <div class="result" id="fee-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function money(n) { return "$" + n.toLocaleString("en-AU", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function run() {
    var v = parseFloat(document.getElementById("fee-v").value); if (isNaN(v) || v < 0) v = 0;
    var t = document.getElementById("fee-t").value, c = document.getElementById("fee-c").value, html = "";
    if (t === "ba2" && c === "2") {
      html = "<h4>A BA2 can't be used for this building</h4><p>Class 2 to 9 buildings need a certified BA1 application.</p>";
      document.getElementById("fee-out").innerHTML = html; return;
    }
    var rate = t === "ba2" ? 0.0032 : (c === "1" ? 0.0019 : 0.0009);
    var fee = Math.round(Math.max(121, v * rate) * 100) / 100;
    var levy = Math.round((v <= 45000 ? 61.65 : v * 0.00137) * 100) / 100;
    var ctf = v > 100000 ? Math.round(v * 0.002 * 100) / 100 : 0;
    var total = Math.round((fee + levy + ctf) * 100) / 100;
    html = "<h4>" + money(total) + " in state fees</h4><p>Permit fee " + money(fee) + " + Building Services Levy " + money(levy) + (ctf ? " + Construction Training Fund levy " + money(ctf) : "") + ".</p>";
    if (t === "ba1") html += "<p>A BA1 also needs a private building surveyor, who charges their own fee.</p>";
    html += "<p>Not included: council extras like verge bonds, and planning approval if you need it.</p>";
    document.getElementById("fee-out").innerHTML = html;
  }
  document.querySelectorAll("#fee-tool input, #fee-tool select").forEach(function (el) { el.addEventListener("input", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>How the fees are worked out</h2>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Rate</th></tr></thead><tbody>
<tr><td>BA2 (uncertified)</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>BA1 (certified), Class 1 and 10</td><td>0.19% of the value, at least $121</td></tr>
<tr><td>BA1 (certified), Class 2 to 9</td><td>0.09% of the value, at least $121</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 up to $45,000; 0.137% of the value above that</td></tr>
<tr><td>Construction Training Fund levy</td><td>0.2%, only for work over $100,000 starting on or after 1 July 2026</td></tr>
</tbody></table></div>
<p>These are set by the state, so they're the same at every WA council.</p>

<h2>What counts as the value</h2>
<p>The Building Regulations say the value is the total of all goods, labour, services, fees, overheads and profit margin, including GST. Councils can question a value that looks too low.</p>

<h2>What the calculator leaves out</h2>
<ul>
<li>Council extras, like verge bonds (for example Wanneroo's $140 fee plus a $2,200 bond for work of $20,000 or more)</li>
<li>Planning approval, if your project needs it ($147 for work up to $50,000 at councils like Melville)</li>
<li>Surveyor, drafting and engineering fees</li>
</ul>
<p>See <a href="/building-permit-costs-perth-councils">building permit costs at Perth councils</a> for more.</p>
"""

FAQS = [
    ("How do I calculate my building permit fee in WA?",
     "For a BA2, multiply the value of the work by 0.32% (at least $121), then add the Building Services Levy: $61.65 for work up to $45,000, or 0.137% above that. Add 0.2% CTF levy if the work is over $100,000."),
    ("What is the minimum building permit fee in WA?",
     "$121, for both BA1 and BA2 applications."),
    ("Is the BA1 fee cheaper than BA2?",
     "Yes, 0.19% instead of 0.32% for houses and Class 10 structures, but you also pay a private building surveyor."),
    ("Does the fee include GST in the value?",
     "Yes. The value of the work must include GST, along with materials, labour, services, fees, overheads and profit."),
]


def page(S):
    return {"path": "building-permit-fee-calculator.html", "published": "2026-11-05", "type": "Free tool", "icon": "price",
            "card": "Enter the value of your work and see the exact state permit fee and levies.",
            "title": "WA Building Permit Fee Calculator (2026)",
            "desc": "Free WA building permit fee calculator using the 2026 state fees: BA1 and BA2 permit fees, the Building Services Levy and the Construction Training Fund levy.",
            "eyebrow": "Free tool", "h1": "WA building permit fee calculator", "crumb": "Permit fee calculator",
            "answer": "<p>A WA building permit costs <strong>0.32%</strong> of the value for a BA2 or <strong>0.19%</strong> for a BA1 (at least $121), plus the Building Services Levy (<strong>$61.65</strong> up to $45,000). Enter your value below to see the total.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/building-permit-costs-perth-councils", "Building permit costs at Perth councils"), ("/ba1-vs-ba2", "BA1 vs BA2"), ("/how-to-fill-in-a-ba2-form", "How to fill in a BA2 form")],
            "sources": [("Building approvals: fees and Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy")]}
