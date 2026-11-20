TOOL = """
<div class="tool" id="os-tool">
  <h3>Will my patio keep enough open space?</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">For single houses coded R10 to R40. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="os-code">Your R-Code</label><select id="os-code"><option value="60">R10</option><option value="55">R12.5</option><option value="50">R15</option><option value="50">R17.5</option><option value="50" selected>R20</option><option value="50">R25</option><option value="45">R30</option><option value="45">R35</option><option value="45">R40</option></select></div>
    <div class="field"><label for="os-lot">Lot size (m²)</label><input id="os-lot" type="number" inputmode="decimal" min="0" value="500"></div>
    <div class="field"><label for="os-bld">Area already covered by buildings (m²)</label><input id="os-bld" type="number" inputmode="decimal" min="0" value="220"><small style="color:var(--muted)">House, garage, carport, sheds and other roofed areas</small></div>
    <div class="field"><label for="os-pat">New patio roof area (m²)</label><input id="os-pat" type="number" inputmode="decimal" min="0" value="30"></div>
    <div class="field"><label for="os-open">Is the patio open on at least 2 sides?</label><select id="os-open"><option value="yes">Yes</option><option value="no">No</option></select></div>
    <div class="field"><label for="os-high">Is the patio floor more than 0.5 m above the ground?</label><select id="os-high"><option value="no">No</option><option value="yes">Yes</option></select></div>
  </div>
  <div class="result" id="os-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function n(id) { var v = parseFloat(document.getElementById(id).value); return isNaN(v) || v < 0 ? 0 : v; }
  function r(x) { return Math.round(x * 10) / 10; }
  function run() {
    var lot = n("os-lot"), bld = n("os-bld"), pat = n("os-pat");
    var pct = parseFloat(document.getElementById("os-code").value);
    var ok = document.getElementById("os-open").value === "yes" && document.getElementById("os-high").value === "no";
    var cap = Math.min(lot * 0.1, 50);
    var credit = ok ? Math.min(pat, cap) : 0;
    var open = lot - bld - pat + credit;
    var need = lot * pct / 100;
    var html;
    if (lot <= 0) { html = "<h4>Enter your lot size</h4><p>You'll find it on your Certificate of Title or council rates notice.</p>"; }
    else {
      var share = r(open / lot * 100);
      var note = ok ? "<p>Up to <strong>" + r(cap) + " m²</strong> of your patio still counts as open space, because it's open on at least 2 sides and close to the ground.</p>"
                    : "<p>Your patio doesn't count as open space, because it isn't open on at least 2 sides or it's more than 0.5 m above the ground.</p>";
      if (open >= need) {
        html = "<h4>Likely OK on open space</h4><p>About <strong>" + share + "%</strong> of your lot stays open. Your R-Code needs <strong>" + pct + "%</strong> (" + r(need) + " m²).</p>" + note;
      } else {
        html = "<h4>You may be short on open space</h4><p>About <strong>" + share + "%</strong> of your lot stays open, but your R-Code needs <strong>" + pct + "%</strong>. You're about <strong>" + r(need - open) + " m²</strong> short, so you'd usually need planning approval, or a smaller or more open patio.</p>" + note;
      }
    }
    document.getElementById("os-out").innerHTML = html;
  }
  document.querySelectorAll("#os-tool input, #os-tool select").forEach(function (el) { el.addEventListener("input", run); el.addEventListener("change", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>How open space works</h2>
<p>The R-Codes say a set share of your lot must stay as <strong>open space</strong>, usually the area not covered by buildings. For single houses:</p>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Minimum open space</th></tr></thead><tbody>
<tr><td>R10</td><td>60%</td></tr>
<tr><td>R12.5</td><td>55%</td></tr>
<tr><td>R15 to R25</td><td>50%</td></tr>
<tr><td>R30 to R40</td><td>45%</td></tr>
</tbody></table></div>

<h2>The patio rule that helps</h2>
<p>A patio or verandah can still count as open space if it's:</p>
<ul>
<li>open (unenclosed) on at least <strong>2 sides</strong>,</li>
<li>no more than <strong>0.5 m</strong> above natural ground level, and</li>
<li>covering no more than <strong>10%</strong> of the lot or <strong>50 m²</strong>, whichever is less.</li>
</ul>
<p>Any patio area above that limit counts as covered. Pergolas without a roof always count as open space. Carports, garages and sheds never do.</p>

<h2>Don't forget the outdoor living area</h2>
<p>The R-Codes also want an outdoor living area next to your main living room (for example <strong>30 m²</strong> at R20), with at least <strong>two-thirds</strong> of it <strong>without a permanent roof</strong>. A big patio over your only backyard space can fail this even if open space is fine.</p>
<p>If your patio meets these rules it usually doesn't need planning approval, but it may still need a building permit. Councils vary.</p>
<p>Check boundary rules in <a href="/patio-on-boundary-wa">can a patio go on the boundary</a>, try the <a href="/patio-approval-checker">patio approval checker</a>, or read about <a href="/enclose-a-patio-approval">enclosing a patio</a>.</p>
"""

FAQS = [
    ("Does a patio count as open space in WA?",
     "It can. A patio open on at least 2 sides and no more than 0.5 m above ground counts as open space, up to 10% of the lot or 50 m², whichever is less."),
    ("How much open space do I need at R20?",
     "At least 50% of the lot for a single house, plus an outdoor living area of 30 m²."),
    ("Does a carport count as open space?",
     "No. Covered car parking spaces don't count as open space under the R-Codes."),
    ("What if my patio leaves too little open space?",
     "You'd usually need planning approval, or a design change such as a smaller patio, or one open on more sides."),
]


def page(S):
    return {"path": "patio-open-space-checker.html", "published": "2026-11-21", "type": "Free tool", "icon": "check",
            "card": "Check if your new patio leaves enough open space under the R-Codes.",
            "title": "Patio Open Space Checker for WA (2026)",
            "desc": "Free patio open space checker for WA: see if your patio keeps enough open space under the R-Codes (45% to 60% by R-Code), and when a patio still counts as open space.",
            "eyebrow": "Free tool", "h1": "Patio open space checker", "crumb": "Patio open space checker",
            "answer": "<p>Under the R-Codes, a single house must keep <strong>45% to 60%</strong> of the lot as open space, depending on the R-Code (50% at R20). A patio still counts as open space if it's open on <strong>2 sides</strong>, no more than <strong>0.5 m</strong> high, and up to <strong>10% of the lot or 50 m²</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-on-boundary-wa", "Can a patio go on the boundary?"), ("/patio-approval-checker", "Patio approval checker"), ("/enclose-a-patio-approval", "Enclosing a patio")],
            "sources": [("Residential Design Codes Volume 1 (Table B, definitions, 5.3.1), WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Ancillary dwelling information sheet (open space by R-Code), City of Stirling", "https://www.stirling.wa.gov.au/awcontent/Web/Documents/Ancillary-Dwellings-(Granny-Flat).pdf")]}
