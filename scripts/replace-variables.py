#!/usr/bin/env python3
"""
Portrait Studio — Static Site Variable Replacer
Easily update all REPLACE_BEFORE_PUBLISHING markers across the website files.
Usage:
    python3 scripts/replace-variables.py --operator "Acme LLC" --email "help@example.com" --jurisdiction "California"
"""

import os
import sys
import argparse

REPLACEMENTS = {
    "REPLACE_BEFORE_PUBLISHING_OPERATOR_LEGAL_NAME": None,
    "REPLACE_BEFORE_PUBLISHING_JURISDICTION": None,
    "REPLACE_BEFORE_PUBLISHING_SUPPORT_EMAIL": None,
    "REPLACE_BEFORE_PUBLISHING_PRIVACY_EMAIL": None,
    "REPLACE_BEFORE_PUBLISHING_MAILING_ADDRESS": None,
    "REPLACE_BEFORE_PUBLISHING_APP_STORE_URL": None
}

def main():
    parser = argparse.ArgumentParser(description="Replace placeholder variables in website files.")
    parser.add_argument("--operator", help="Legal operator name (e.g., 'Acme Studio LLC')")
    parser.add_argument("--jurisdiction", help="Legal jurisdiction (e.g., 'State of California, USA')")
    parser.add_argument("--email", help="Support and privacy email address")
    parser.add_argument("--privacy-email", help="Privacy email address (defaults to --email if omitted)")
    parser.add_argument("--address", help="Operator mailing address (optional)")
    parser.add_argument("--app-store-url", help="Live App Store URL")

    args = parser.parse_args()

    mapping = {}
    if args.operator:
        mapping["REPLACE_BEFORE_PUBLISHING_OPERATOR_LEGAL_NAME"] = args.operator
    if args.jurisdiction:
        mapping["REPLACE_BEFORE_PUBLISHING_JURISDICTION"] = args.jurisdiction
    if args.email:
        mapping["REPLACE_BEFORE_PUBLISHING_SUPPORT_EMAIL"] = args.email
        mapping["REPLACE_BEFORE_PUBLISHING_PRIVACY_EMAIL"] = args.privacy_email or args.email
    if args.privacy_email:
        mapping["REPLACE_BEFORE_PUBLISHING_PRIVACY_EMAIL"] = args.privacy_email
    if args.address:
        mapping["REPLACE_BEFORE_PUBLISHING_MAILING_ADDRESS"] = args.address
    if args.app_store_url:
        mapping["REPLACE_BEFORE_PUBLISHING_APP_STORE_URL"] = args.app_store_url

    if not mapping:
        print("No replacement flags provided. Run with -h for help.")
        sys.exit(1)

    site_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"Scanning site root: {site_root}")

    count = 0
    for root, _, files in os.walk(site_root):
        for f in files:
            if f.endswith((".html", ".json", ".js", ".xml", ".txt")):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                new_content = content
                for placeholder, val in mapping.items():
                    if val and placeholder in new_content:
                        new_content = new_content.replace(placeholder, val)
                
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"Updated: {os.path.relpath(path, site_root)}")
                    count += 1

    print(f"Completed. Updated {count} files.")

if __name__ == "__main__":
    main()
