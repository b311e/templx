#!/usr/bin/env python3
"""
Import styles from snippet files into expanded Word document directories.
Maintains proper style ordering based on styles-order.yml.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import yaml

# Word namespace
WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace('w', WORD_NS)

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

def get_style_id(style_element):
    """Extract styleId from a style element."""
    style_id = style_element.get(f'{{{WORD_NS}}}styleId')
    return style_id

def load_snippet_styles(snippet_file):
    """Load style elements from snippet file."""
    tree = ET.parse(snippet_file)
    root = tree.getroot()
    
    # Get all w:style elements from the snippet
    styles = root.findall(f'.//{{{WORD_NS}}}style')
    
    # Return dict of styleId -> style element
    return {get_style_id(s): s for s in styles if get_style_id(s)}

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

def apply_styles_to_xml(styles_xml_path, snippet_styles, style_order):
    """Apply snippet styles to the styles.xml file maintaining proper order."""
    tree = ET.parse(styles_xml_path)
    root = tree.getroot()
    
    # Get existing styles
    existing_styles = {get_style_id(s): s for s in root.findall(f'.//{{{WORD_NS}}}style') if get_style_id(s)}
    
    # Track which snippet styles to add/replace
    snippet_style_ids = set(snippet_styles.keys())
    
    # Remove existing styles that will be replaced or deleted
    deleted_count = 0
    for style_elem in list(root.findall(f'.//{{{WORD_NS}}}style')):
        style_id = get_style_id(style_elem)
        if style_id in snippet_style_ids:
            root.remove(style_elem)
            print(f"  Replacing: {style_id}")
        elif should_delete_companion_style(style_id, snippet_styles):
            root.remove(style_elem)
            del existing_styles[style_id]
            deleted_count += 1
            print(f"  Deleting: {style_id} (companion style not in snippet)")
    
    # Build final ordered list of styles
    final_styles = []
    added_ids = set()
    
    # First pass: add styles in the order defined in styles-order.yml
    for style_id in style_order:
        if style_id in snippet_styles:
            final_styles.append(snippet_styles[style_id])
            added_ids.add(style_id)
        elif style_id in existing_styles:
            final_styles.append(existing_styles[style_id])
            added_ids.add(style_id)
    
    # Second pass: add any existing styles not in the order list
    for style_id, style_elem in existing_styles.items():
        if style_id not in added_ids and style_id not in snippet_style_ids:
            final_styles.append(style_elem)
            added_ids.add(style_id)
    
    # Third pass: add any snippet styles not in the order list
    for style_id, style_elem in snippet_styles.items():
        if style_id not in added_ids:
            final_styles.append(style_elem)
            added_ids.add(style_id)
            print(f"  Adding (not in order): {style_id}")
    
    # Clear all existing styles and add in correct order
    for style_elem in list(root.findall(f'.//{{{WORD_NS}}}style')):
        root.remove(style_elem)
    
    for style_elem in final_styles:
        root.append(style_elem)
    
    # Write back with proper formatting
    tree.write(styles_xml_path, encoding='utf-8', xml_declaration=True)
    
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
    
    print(f"Loading styles from: {snippet_file.name}")
    snippet_styles = load_snippet_styles(snippet_file)
    
    print(f"Applying {len(snippet_styles)} style(s) to: {styles_xml}")
    imported_count, deleted_count = apply_styles_to_xml(styles_xml, snippet_styles, style_order)
    
    print(f"✓ Successfully imported {imported_count} style(s)")
    if deleted_count > 0:
        print(f"  Deleted {deleted_count} companion style(s)")
    print(f"  Styles ordered according to: {order_file.name}")

if __name__ == "__main__":
    main()
