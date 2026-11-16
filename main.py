#!/usr/bin/env python3
"""Pseudonymize selected CSV columns using HMAC-SHA256."""
import argparse
import csv
import hashlib
import hmac
import os
from pathlib import Path

def pseudonym(value: str, salt: str) -> str:
    digest = hmac.new(salt.encode("utf-8"), value.encode("utf-8"), hashlib.sha256).hexdigest()
    return "anon_" + digest[:20]

def anonymize_file(source: Path, destination: Path, columns: set[str], salt: str) -> int:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("r", encoding="utf-8-sig", newline="") as inp:
        reader = csv.DictReader(inp)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row.")
        missing = columns - set(reader.fieldnames)
        if missing:
            raise ValueError("Unknown column(s): " + ", ".join(sorted(missing)))
        with destination.open("w", encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
            writer.writeheader()
            count = 0
            for row in reader:
                for column in columns:
                    if row.get(column):
                        row[column] = pseudonym(row[column], salt)
                writer.writerow(row)
                count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description="Pseudonymize chosen CSV columns without printing source values.")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--columns", required=True, help="Comma-separated column names")
    parser.add_argument("--salt-env", default="CSV_ANON_SALT", help="Environment variable holding the secret salt")
    args = parser.parse_args()
    salt = os.environ.get(args.salt_env)
    if not salt:
        parser.error(f"Set the {args.salt_env} environment variable first.")
    columns = {item.strip() for item in args.columns.split(",") if item.strip()}
    if not columns:
        parser.error("Select at least one column.")
    try:
        count = anonymize_file(args.source, args.destination, columns, salt)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Processed {count} rows. Selected values were not printed.")
if __name__ == "__main__":
    main()
