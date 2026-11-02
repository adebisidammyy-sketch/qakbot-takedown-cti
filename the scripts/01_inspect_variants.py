"""
Step 1: inspect the MalwareBazaar full dump before counting anything.

Prints the number of rows, the date range, and every spelling of Qakbot found
in the 'signature' column (so the counting script catches all of them).

Usage:
    python scripts/01_inspect_variants.py path/to/full.csv.zip

Needs only the Python standard library. The dump is NOT included in this
repository: download it yourself from https://bazaar.abuse.ch/export/ with a
free abuse.ch Auth-Key. Never commit the key or the dump.
"""
import csv
import re
import sys
import zipfile
from collections import Counter

PATTERN = re.compile(r"qakbot|qbot|quakbot|pinkslipbot", re.IGNORECASE)


def rows(zip_path):
    """Yield data rows from the dump, skipping '#' comment lines."""
    with zipfile.ZipFile(zip_path) as z:
        name = z.namelist()[0]
        with z.open(name) as raw:
            lines = (l.decode("utf-8", errors="replace") for l in raw)
            data = (l for l in lines if not l.startswith("#") and l.strip())
            for row in csv.reader(data, skipinitialspace=True):
                if len(row) >= 9:  # columns: 0=first_seen_utc, 4=reporter, 8=signature
                    yield row


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/01_inspect_variants.py path/to/full.csv.zip")
    total, variants = 0, Counter()
    earliest = latest = None
    for row in rows(sys.argv[1]):
        total += 1
        date = row[0][:10]
        earliest = date if earliest is None or date < earliest else earliest
        latest = date if latest is None or date > latest else latest
        if PATTERN.search(row[8]):
            variants[row[8]] += 1
    print("Total rows (all malware):", total)
    print("Date range:", earliest, "to", latest)
    print("Names matching Qakbot and their counts:")
    for name, n in variants.most_common():
        print(" ", repr(name), n)


if __name__ == "__main__":
    main()
