#!/usr/bin/env python3
"""
Remove noProof elements from Word XML files.

The noProof element tells Word not to check spelling/grammar for specific text.
This is often added to form fields and template placeholders but isn't necessary
for clean template files.

Removes two patterns:
1. Standalone <w:noProof/> within run properties
2. Complete <w:rPr><w:noProof/></w:rPr> blocks (empty run properties containing only noProof)
"""

import sys
import re
from pathlib import Path

def clean_noproof(file_path):
    """Remove noProof elements from an XML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: Complete <w:rPr> blocks containing only <w:noProof/>
    # Matches any amount of whitespace before <w:rPr>, the tags, and preserves line structure
    # Example:
    #                <w:rPr>
    #                    <w:noProof/>
    #                </w:rPr>
    pattern1 = r'[ \t]*<w:rPr>\s*<w:noProof/>\s*</w:rPr>[\r\n]*'
    
    # Pattern 2: Standalone <w:noProof/> lines (within w:rPr that has other content)
    # Matches the line including leading whitespace and trailing newline
    # Example:
    #                    <w:noProof/>
    pattern2 = r'[ \t]*<w:noProof/>[\r\n]*'
    
    # Count occurrences
    rpr_blocks = len(re.findall(pattern1, content))
    standalone = len(re.findall(pattern2, content))
    
    # After removing full blocks, count remaining standalone (since pattern1 contains pattern2)
    temp_content = re.sub(pattern1, '', content)
    standalone_remaining = len(re.findall(pattern2, temp_content))
    
    total_count = rpr_blocks + standalone_remaining
    
    if total_count == 0:
        print(f"No noProof elements found in {file_path.name}")
        return 0
    
    # Remove all matches - order matters! Remove complete blocks first, then standalone
    cleaned_content = re.sub(pattern1, '', content)
    cleaned_content = re.sub(pattern2, '', cleaned_content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    return (rpr_blocks, standalone_remaining)

def main():
    if len(sys.argv) < 2:
        print("Usage: remove-noproof <xml-file-path>")
        print("  xml-file-path - Path to Word XML file (document.xml, styles.xml, etc.)")
        print("")
        print("Removes noProof elements from Word XML files.")
        print("The noProof element disables spell/grammar checking for specific text.")
        print("")
        print("Removes two patterns:")
        print("  1. Complete <w:rPr><w:noProof/></w:rPr> blocks")
        print("  2. Standalone <w:noProof/> elements within run properties")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    if not file_path.is_file():
        print(f"Error: Not a file: {file_path}")
        sys.exit(1)
    
    print(f"Cleaning noProof elements from: {file_path.name}")
    
    rpr_count, standalone_count = clean_noproof(file_path)
    total_count = rpr_count + standalone_count
    
    if total_count > 0:
        print(f"✓ Removed {total_count} noProof element(s):")
        if rpr_count > 0:
            print(f"  - {rpr_count} complete <w:rPr><w:noProof/></w:rPr> block(s)")
        if standalone_count > 0:
            print(f"  - {standalone_count} standalone <w:noProof/> element(s)")
    else:
        print("No noProof elements found")

if __name__ == "__main__":
    main()
