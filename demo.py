"""
demo.py
-------
THEORY — Live Demo Script

Showcases all current capabilities in a single screen-recordable run.
Saves full output to output/theory_demo_output.txt for sharing.

Usage:
    python demo.py

What this demonstrates:
    1. CLI help and source listing
    2. Actor alias resolution ("Fancy Bear" → APT28)
    3. Full multi-source dossier (MITRE + Malpedia + OTX)
    4. Detection opportunities via Sigma rules (from cache)
    5. IOC table with ThreatFox enrichment (from cache)
    6. STIX 2.1 export summary
    7. All three output formats written to disk
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path("output/theory_demo_output.txt")
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# ANSI colors for the demo header (terminal only, stripped in file)
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"


def banner(text: str, width: int = 72) -> None:
    line = "─" * width
    print(f"\n{CYAN}{BOLD}{line}{RESET}")
    print(f"{CYAN}{BOLD}  {text}{RESET}")
    print(f"{CYAN}{BOLD}{line}{RESET}\n")


def step(n: int, text: str) -> None:
    print(f"{YELLOW}{BOLD}[{n}]{RESET} {BOLD}{text}{RESET}")
    print(f"{DIM}{'─' * 60}{RESET}")


def run_cmd(cmd: list[str], capture: bool = False) -> str:
    """Run a theory.py command, print output live, and optionally capture it."""
    print(f"{DIM}$ {' '.join(cmd)}{RESET}\n")
    time.sleep(0.5)   # brief pause so screen recording looks deliberate

    result = subprocess.run(
        cmd,
        capture_output=capture,
        text=True,
    )

    if capture:
        output = result.stdout + result.stderr
        print(output)
        return output
    return ""


def strip_ansi(text: str) -> str:
    """Remove ANSI escape codes for the plain-text output file."""
    import re
    return re.sub(r"\033\[[0-9;]*m", "", text)


def main() -> None:
    lines: list[str] = []   # accumulates everything for the output file

    def tee(text: str) -> None:
        """Print to terminal and accumulate for file."""
        print(text)
        lines.append(strip_ansi(text))

    def run_and_tee(cmd: list[str]) -> None:
        """Run command, print live, capture for file."""
        print(f"{DIM}$ {' '.join(cmd)}{RESET}\n")
        lines.append(f"$ {' '.join(cmd)}\n")
        time.sleep(0.4)

        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + (result.stderr if result.returncode != 0 else "")
        print(output)
        lines.append(output)

    # ──────────────────────────────────────────────────────────────────
    # Header
    # ──────────────────────────────────────────────────────────────────
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    banner("THEORY — Multi-Source Threat Actor Intelligence Framework")
    tee(f"  Demo run: {now}")
    tee(f"  Output file: {OUTPUT_FILE}\n")
    tee("  THEORY is an open-source alternative to enterprise TI platforms.")
    tee("  It generates analyst-grade dossiers from multiple free sources:")
    tee("  MITRE ATT&CK · Malpedia · AlienVault OTX · SigmaHQ · ThreatFox · CISA\n")

    time.sleep(1)

    # ──────────────────────────────────────────────────────────────────
    # Step 1: --help
    # ──────────────────────────────────────────────────────────────────
    banner("Step 1 of 7 — CLI Help")
    step(1, "Every flag and example, discoverable without reading docs.")
    run_and_tee([sys.executable, "theory.py", "--help"])
    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 2: --list-sources
    # ──────────────────────────────────────────────────────────────────
    banner("Step 2 of 7 — Available Sources")
    step(2, "Six intelligence sources — most require no API key.")
    run_and_tee([sys.executable, "theory.py", "--list-sources"])
    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 3: --list-actors
    # ──────────────────────────────────────────────────────────────────
    banner("Step 3 of 7 — Alias Resolution Table")
    step(3, "Any alias resolves to the same dossier.")
    tee('  "Fancy Bear", "Strontium", "Forest Blizzard", and "APT28" are all the same group.')
    tee("  THEORY knows them all.\n")
    run_and_tee([sys.executable, "theory.py", "--list-actors"])
    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 4: Alias resolution demo
    # ──────────────────────────────────────────────────────────────────
    banner("Step 4 of 7 — Alias Resolution in Action")
    step(4, 'Querying by alias "Fancy Bear" — resolves to APT28 automatically.')
    tee("  Analyst might know this group by any of 30+ names.")
    tee("  THEORY resolves to canonical name and pulls all data.\n")
    run_and_tee([
        sys.executable, "theory.py",
        "--actor", "Fancy Bear",
        "--sources", "mitre",
        "--no-save",
    ])
    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 5: Full multi-source dossier
    # ──────────────────────────────────────────────────────────────────
    banner("Step 5 of 7 — Full Multi-Source Dossier: APT28")
    step(5, "MITRE ATT&CK + Malpedia + OTX + Sigma + ThreatFox")
    tee("  This is the core capability — pulling from five sources simultaneously,")
    tee("  deduplicating, confidence-scoring, and rendering a unified dossier.\n")
    tee("  What you'll see:")
    tee("    · TTP table (87 techniques with names, tactics, confidence scores)")
    tee("    · Detection Opportunities (Sigma rules mapped to each technique)")
    tee("    · 47 malware families (MITRE + Malpedia enrichment)")
    tee("    · 66 IOCs (OTX + ThreatFox, with confidence + malware family tags)")
    tee("    · Targeted sectors, campaigns, aliases from 5 sources\n")
    time.sleep(1)

    run_and_tee([
        sys.executable, "theory.py",
        "--actor", "APT28",
        "--sources", "mitre,malpedia,otx,sigma,threatfox",
        "--output", "dossier",
    ])
    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 6: STIX export
    # ──────────────────────────────────────────────────────────────────
    banner("Step 6 of 7 — STIX 2.1 Export")
    step(6, "Machine-readable bundle for MISP, OpenCTI, Splunk ES, Microsoft Sentinel.")
    tee("  STIX 2.1 is the industry standard for threat intelligence sharing.")
    tee("  THEORY bundles include: intrusion-set, attack-pattern, malware,")
    tee("  indicator objects with STIX patterns, and all relationships.\n")

    run_and_tee([
        sys.executable, "theory.py",
        "--actor", "APT28",
        "--sources", "mitre,malpedia,otx",
        "--output", "stix",
        "--no-save",
    ])

    # Show bundle stats
    stix_path = Path("output/dossiers/apt28.stix.json")
    if stix_path.exists():
        import json
        bundle = json.loads(stix_path.read_text(encoding="utf-8"))
        objs   = bundle.get("objects", [])
        counts = {}
        for o in objs:
            t = o.get("type", "unknown")
            counts[t] = counts.get(t, 0) + 1
        tee("\n  STIX bundle contents:")
        for obj_type, count in sorted(counts.items()):
            tee(f"    {count:>4}  {obj_type}")
        tee(f"\n    {len(objs):>4}  TOTAL objects\n")

    time.sleep(0.5)

    # ──────────────────────────────────────────────────────────────────
    # Step 7: --output all
    # ──────────────────────────────────────────────────────────────────
    banner("Step 7 of 7 — All Formats at Once")
    step(7, "--output all writes markdown + JSON + STIX in a single command.")
    tee("  This is how THEORY fits into an existing workflow:")
    tee("  · apt28.md    → paste into a threat brief or wiki")
    tee("  · apt28.json  → feed into a script or dashboard")
    tee("  · apt28.stix.json → import into MISP or OpenCTI\n")

    run_and_tee([
        sys.executable, "theory.py",
        "--actor", "APT28",
        "--sources", "mitre,malpedia,otx",
        "--output", "all",
    ])

    # List the output files
    output_dir = Path("output/dossiers")
    if output_dir.exists():
        files = sorted(output_dir.glob("apt28*"))
        if files:
            tee("\n  Output files written:")
            for f in files:
                size_kb = f.stat().st_size / 1024
                tee(f"    {f.name:<35} {size_kb:>7.1f} KB")

    # ──────────────────────────────────────────────────────────────────
    # Closing
    # ──────────────────────────────────────────────────────────────────
    banner("Demo Complete")
    tee("  THEORY — open-source threat actor intelligence")
    tee("  github.com/threatcraft-co/theory\n")
    tee("  Current capabilities:")
    tee("    ✓ 6 intelligence sources (MITRE, Malpedia, OTX, Sigma, ThreatFox, CISA)")
    tee("    ✓ Cross-source alias resolution (30+ naming conventions per actor)")
    tee("    ✓ Confidence scoring (HIGH when 2+ sources agree on a TTP)")
    tee("    ✓ Detection Opportunities (Sigma rules mapped to actor TTPs)")
    tee("    ✓ IOC enrichment with malware family attribution")
    tee("    ✓ STIX 2.1 export (MISP / OpenCTI / Sentinel compatible)")
    tee("    ✓ 253 passing tests")
    tee("")
    tee("  Coming next:")
    tee("    → Vendor intelligence synthesis (LLM-powered: Mandiant, Unit42, Okta, etc.)")
    tee("    → 50+ actors in the alias table")
    tee("    → Full documentation + contributor guide")
    tee("")

    # ──────────────────────────────────────────────────────────────────
    # Write output file
    # ──────────────────────────────────────────────────────────────────
    full_output = "\n".join(lines)
    OUTPUT_FILE.write_text(full_output, encoding="utf-8")

    print(f"\n{GREEN}{BOLD}Full output saved → {OUTPUT_FILE}{RESET}")
    print(f"{DIM}Share this file with your mentor for the complete run output.{RESET}\n")


if __name__ == "__main__":
    main()
