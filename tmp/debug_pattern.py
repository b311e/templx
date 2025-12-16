import re

with open(r'builds\osa\templates\osaReport\in\word\document.xml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show lines 108-116 with repr to see exact spacing
print("Lines 108-116:")
for i in range(107, 116):
    if i < len(lines):
        print(f"Line {i+1}: {repr(lines[i])}")

# Try to match the pattern
content = ''.join(lines[107:116])
print("\nCombined content:")
print(repr(content))

pattern = re.compile(r'^[ \t]*<w:rPr>\n[ \t]*<w:noProof/>\n[ \t]*</w:rPr>\n', re.MULTILINE)
matches = pattern.findall(content)
print(f"\nMatches found: {len(matches)}")
if matches:
    print("Match:")
    print(repr(matches[0]))
