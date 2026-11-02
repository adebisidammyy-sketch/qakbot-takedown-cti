"""
Step 2: monthly Qakbot counts plus two controls, from the MalwareBazaar full dump.

For each month from 2022-01 to the latest month in the dump it writes:
  all_samples          every sample first seen that month (control 1)
  qakbot_samples       samples whose 'signature' matches Qakbot spellings
  qakbot_share_pct     qakbot_samples as a percentage of all_samples
  qakbot_reporters     distinct reporters of Qakbot samples (control 2)

Usage:
    python scripts/02_monthly_counts_and_controls.py path/to/full.csv.zip --out data

Limits (also stated in the report): counts measure what was submitted to one
platform, not attacker activity. The last month in a dump is usually partial.
"""
import argparse
import csv
import os
import re
import zipfile
from collections import Counter, defaultdict

PATTERN = re.compile(r"qakbot|qbot|quakbot|pinkslipbot", re.IGNORECASE)
START = "2022-01"


def rows(zip_path):
    with zipfile.ZipFile(zip_path) as z:
        name = z.namelist()[0]
        with z.open(name) as raw:
            lines = (l.decode("utf-8", errors="replace") for l in raw)
            data = (l for l in lines if not l.startswith("#") and l.strip())
            for row in csv.reader(data, skipinitialspace=True):
                if len(row) >= 9:  # 0=first_seen_utc, 4=reporter, 8=signature
                    yield row


def month_range(first, last):
    y, m = int(first[:4]), int(first[5:7])
    ly, lm = int(last[:4]), int(last[5:7])
    while (y, m) <= (ly, lm):
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("--out", default="data")
    args = ap.parse_args()

    total, qak = Counter(), Counter()
    reporters = defaultdict(set)
    latest = START
    for row in rows(args.zip_path):
        month = row[0][:7]
        if month < START:
            continue
        latest = max(latest, month)
        total[month] += 1
        if PATTERN.search(row[8]):
            qak[month] += 1
            reporters[month].add(row[4])

    os.makedirs(args.out, exist_ok=True)
    months = list(month_range(START, latest))
    with open(os.path.join(args.out, "malwarebazaar_controls_monthly.csv"), "w", newline="") as f1, \
         open(os.path.join(args.out, "malwarebazaar_qakbot_monthly.csv"), "w", newline="") as f2:
        w1, w2 = csv.writer(f1), csv.writer(f2)
        w1.writerow(["month", "all_samples", "qakbot_samples", "qakbot_share_pct", "qakbot_reporters"])
        w2.writerow(["month", "qakbot_count"])
        for mo in months:
            t, q = total.get(mo, 0), qak.get(mo, 0)
            share = round(100 * q / t, 2) if t else 0
            w1.writerow([mo, t, q, share, len(reporters.get(mo, ()))])
            w2.writerow([mo, q])
    print(f"Wrote {len(months)} months ({START} to {latest}) to {args.out}/")
    print(f"Note: {latest} may be a partial month.")


if __name__ == "__main__":
    main()
