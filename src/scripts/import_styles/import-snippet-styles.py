#!/usr/bin/env python3
"""
Import styles from snippet files into expanded Word document directories.
Maintains proper style ordering based on styles-order.yml.
Uses pure text/regex manipulation to preserve exact XML formatting.
"""

import sys
import re
from pathlib import Path
import yaml

def load_style_order(order_file):
    """Load and flatten the style order from YAML file."""
    with open(order_file, 'r') as f:
        data = yaml.safe_load(f)
    
    # Flatten all style groups into a single ordered list
    order = []
    for group_styles in data['style-groups'].values():
        if group_styles:  # Skip None/empty groups
            order.extend(group_styles)
    
    return order

def extract_style_id(style_text):
    """Extract styleId from a style XML string."""
    match = re.search(r'w:styleId="([^"]+)"', style_text)
    return match.group(1) if match else None

def compact_style(style_text):
    """Convert multi-line style to single-line format."""
    # Remove all newlines and collapse multiple spaces to single space
    compact = re.sub(r'\s+', ' ', style_text)
    # Clean up spaces around tags
    compact = re.sub(r'>\s+<', '><', compact)
    # Ensure space after self-closing tags
    compact = re.sub(r'/>\s*', ' />', compact)
    # Final cleanup - single spaces only
    return compact.strip()

def detect_formatting_style(content):
    """Detect if the file uses formatted (multi-line) or compact (single-line) style."""
    # Check first few style elements to see if they're formatted
    pattern = r'(<w:style\s[^>]*>.*?</w:style>)'
    styles = re.findall(pattern, content, re.DOTALL)
    
    if not styles:
        return 'compact'  # Default to compact if no styles found
    
    # Check if first style contains newlines
    first_style = styles[0]
    if '\n' in first_style:
        return 'formatted'
    else:
        return 'compact'

def load_snippet_styles(snippet_file, target_format='compact'):
    """Load style elements from snippet file as text, optionally converting format."""
    with open(snippet_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all w:style elements (NOT w:styles - the root element)
    # Use word boundary or space to ensure we match <w:style but not <w:styles
    pattern = r'(<w:style\s[^>]*>.*?</w:style>)'
    styles = re.findall(pattern, content, re.DOTALL)
    
    # Return dict of styleId -> style text (compact if target is compact)
    result = {}
    for style in styles:
        style_id = extract_style_id(style)
        if style_id:
            if target_format == 'compact':
                result[style_id] = compact_style(style)
            else:
                # Keep original formatting from snippet
                result[style_id] = style
    
    return result

def should_delete_companion_style(style_id, snippet_styles):
    """Check if a companion character style should be deleted."""
    # If snippet has Heading1 but not Heading1Char, we should delete Heading1Char
    companion_map = {
        'Heading1Char': 'Heading1',
        'Heading2Char': 'Heading2',
        'Heading3Char': 'Heading3',
        'Heading4Char': 'Heading4',
        'Heading5Char': 'Heading5',
        'Heading6Char': 'Heading6',
        'Heading7Char': 'Heading7',
        'Heading8Char': 'Heading8',
        'Heading9Char': 'Heading9',
    }
    
    if style_id in companion_map:
        base_style = companion_map[style_id]
        # Delete the Char style if base style is in snippet but Char style is not
        return base_style in snippet_styles and style_id not in snippet_styles
    
    return False

def extract_existing_styles(content):
    """Extract existing styles from styles.xml content."""
    pattern = r'(<w:style[^>]*>.*?</w:style>)'
    styles = re.findall(pattern, content, re.DOTALL)
    
    result = {}
    for style in styles:
        style_id = extract_style_id(style)
        if style_id:
            result[style_id] = style
    
    return result

def apply_styles_to_xml(styles_xml_path, snippet_styles, style_order):
    """Apply snippet styles to the styles.xml file maintaining proper order using text manipulation."""
    # Read the original file
    with open(styles_xml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Detect if file is formatted or compact
    format_style = detect_formatting_style(content)
    print(f"  Detected format: {format_style}")
    
    # Extract existing styles as text (NOT w:styles root element)
    # Require a space after w:style to avoid matching <w:styles>
    pattern = r'(<w:style\s[^>]*>.*?</w:style>)'
    existing_style_texts = re.findall(pattern, content, re.DOTALL)
    
    # Build dictionary of existing styles by styleId
    existing_styles = {}
    for style_text in existing_style_texts:
        style_id = extract_style_id(style_text)
        if style_id:
            existing_styles[style_id] = style_text
    
    # Track which snippet styles to add/replace
    snippet_style_ids = set(snippet_styles.keys())
    
    # Mark styles for deletion
    deleted_count = 0
    styles_to_delete = []
    
    for style_id in list(existing_styles.keys()):
        if style_id in snippet_style_ids:
            print(f"  Replacing: {style_id}")
            del existing_styles[style_id]
        elif should_delete_companion_style(style_id, snippet_styles):
            styles_to_delete.append(style_id)
            deleted_count += 1
            print(f"  Deleting: {style_id} (companion style not in snippet)")
    
    # Remove deleted styles
    for style_id in styles_to_delete:
        del existing_styles[style_id]
    
    # Build final ordered list of style texts
    final_style_texts = []
    added_ids = set()
    
    # First pass: add styles in the order defined in styles-order.yml
    for style_id in style_order:
        if style_id in snippet_styles:
            final_style_texts.append(snippet_styles[style_id])
            added_ids.add(style_id)
        elif style_id in existing_styles:
            final_style_texts.append(existing_styles[style_id])
            added_ids.add(style_id)
    
    # Second pass: add any existing styles not in the order list
    for style_id, style_text in existing_styles.items():
        if style_id not in added_ids:
            final_style_texts.append(style_text)
            added_ids.add(style_id)
    
    # Third pass: add any snippet styles not in the order list
    for style_id, style_text in snippet_styles.items():
        if style_id not in added_ids:
            final_style_texts.append(style_text)
            added_ids.add(style_id)
            print(f"  Adding (not in order): {style_id}")
    
    # Find the position where styles section ends in original content
    # We need to find </w:latentStyles> and replace everything from there to </w:styles>
    latent_end = content.find('</w:latentStyles>')
    if latent_end == -1:
        print("Error: Could not find </w:latentStyles> in styles.xml")
        return 0, 0
    
    styles_end = content.find('</w:styles>')
    if styles_end == -1:
        print("Error: Could not find </w:styles> in styles.xml")
        return 0, 0
    
    # Build new content
    before_styles = content[:latent_end + len('</w:latentStyles>')]
    after_styles = content[styles_end:]
    
    # Join styles with appropriate separator based on format
    if format_style == 'formatted':
        # For formatted files, add newline and proper indentation before each style
        separator = '\n    '  # newline + 4 spaces indentation
        styles_content = separator + separator.join(final_style_texts)
    else:
        # For compact files, just concatenate
        styles_content = ''.join(final_style_texts)
    
    # Assemble final content
    new_content = before_styles + styles_content + after_styles
    
    # Write back
    with open(styles_xml_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(snippet_style_ids), deleted_count

def main():
    if len(sys.argv) < 3:
        print("Usage: import-snippet-styles.py <target-dir> <snippet-file>")
        print("  target-dir   - Expanded Word document directory (e.g., in/, expanded/)")
        print("  snippet-file - XML file containing style snippets")
        sys.exit(1)
    
    target_dir = Path(sys.argv[1])
    snippet_file = Path(sys.argv[2])
    
    # Validate inputs
    if not target_dir.is_dir():
        print(f"Error: Target directory not found: {target_dir}")
        sys.exit(1)
    
    styles_xml = target_dir / "word" / "styles.xml"
    if not styles_xml.exists():
        print(f"Error: styles.xml not found at: {styles_xml}")
        sys.exit(1)
    
    if not snippet_file.exists():
        print(f"Error: Snippet file not found: {snippet_file}")
        sys.exit(1)
    
    # Find styles-order.yml
    script_dir = Path(__file__).parent
    order_file = script_dir / "styles-order.yml"
    if not order_file.exists():
        print(f"Error: styles-order.yml not found at: {order_file}")
        sys.exit(1)
    
    print(f"Loading style order from: {order_file.name}")
    style_order = load_style_order(order_file)
    
    # Detect target file format first
    with open(styles_xml, 'r', encoding='utf-8') as f:
        target_content = f.read()
    target_format = detect_formatting_style(target_content)
    
    print(f"Loading styles from: {snippet_file.name}")
    snippet_styles = load_snippet_styles(snippet_file, target_format)
    
    print(f"Applying {len(snippet_styles)} style(s) to: {styles_xml}")
    imported_count, deleted_count = apply_styles_to_xml(styles_xml, snippet_styles, style_order)
    
    print(f"✓ Successfully imported {imported_count} style(s)")
    if deleted_count > 0:
        print(f"  Deleted {deleted_count} companion style(s)")
    print(f"  Styles ordered according to: {order_file.name}")

if __name__ == "__main__":
    main()
