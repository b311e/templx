import re

# Read the file in binary to check line endings
with open(r"C:\code\coga-template-manager\builds\osa\templates\osaReport\in\word\document.xml", 'rb') as f:
    binary_content = f.read()

print(f"File size: {len(binary_content)} bytes")
print(f"CRLF (\\r\\n) count: {binary_content.count(b'\\r\\n')}")
print(f"LF only (\\n) count: {binary_content.count(b'\\n') - binary_content.count(b'\\r\\n')}")

# Read as text
with open(r"C:\code\coga-template-manager\builds\osa\templates\osaReport\in\word\document.xml", 'r', encoding='utf-8') as f:
    content = f.read()

# Find first noProof occurrence
noproof_idx = content.find('<w:noProof/>')
if noproof_idx != -1:
    # Show 200 chars before and after
    start = max(0, noproof_idx - 200)
    end = min(len(content), noproof_idx + 200)
    sample = content[start:end]
    print(f"\nFirst noProof context (showing repr):")
    print(repr(sample))
    
    # Test patterns on this section
    pattern1 = r'[ \t]*<w:pPr>[\r\n]+[ \t]*<w:rPr>[\r\n]+[ \t]*<w:noProof/>[\r\n]+[ \t]*</w:rPr>[\r\n]+[ \t]*</w:pPr>[\r\n]*'
    pattern2 = r'[ \t]*<w:rPr>[\r\n]+[ \t]*<w:noProof/>[\r\n]+[ \t]*</w:rPr>[\r\n]*'
    pattern3 = r'[ \t]*<w:noProof/>[\r\n]+'
    
    if re.search(pattern1, sample):
        print("\n✓ Pattern 1 matches this section")
    if re.search(pattern2, sample):
        print("✓ Pattern 2 matches this section")  
    if re.search(pattern3, sample):
        print("✓ Pattern 3 matches this section")
else:
    print("No noProof found in file!")
