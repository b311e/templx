#!/usr/bin/env python3
"""
Remove RSID (Revision Save ID) elements from Word XML files.
RSIDs are used by Word for tracking document changes but are not needed for templates.
"""

import sys
import re
from pathlib import Path

def clean_rsids(file_path):
    """Remove all w:rsid elements from an XML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern matches: optional whitespace, <w:rsid w:val="HEXVALUE" />, optional newlines
    # Using re.MULTILINE to match ^ at start of lines
    pattern = r'^\s*<w:rsid w:val="[0-9A-F]+" />[\r\n]*'
    
    original_count = len(re.findall(pattern, content, re.MULTILINE))
    
    if original_count == 0:
        print(f"No RSID elements found in {file_path.name}")
        return 0
    
    # Remove all matches
    cleaned_content = re.sub(pattern, '', content, flags=re.MULTILINE)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    return original_count

def main():
    if len(sys.argv) < 2:
        print("Usage: remove-styles-rsid <styles.xml-path>")
        print("  styles.xml-path - Path to styles.xml file")
        print("")
        print("Removes RSID (Revision Save ID) elements from Word styles.xml file.")
        print("RSIDs are used by Word for change tracking but aren't needed in templates.")
        sys.exit(1)
    
    styles_path = Path(sys.argv[1])
    
    if not styles_path.exists():
        print(f"Error: File not found: {styles_path}")
        sys.exit(1)
    
    if not styles_path.is_file():
        print(f"Error: Not a file: {styles_path}")
        sys.exit(1)
    
    print(f"Cleaning RSIDs from: {styles_path.name}")
    
    count = clean_rsids(styles_path)
    
    if count > 0:
        print(f"✓ Removed {count} RSID element(s)")
    else:
        print("No RSID elements found")

if __name__ == "__main__":
    main()
