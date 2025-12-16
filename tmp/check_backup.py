with open(r'builds\osa\templates\osaReport\tmp-backup\document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File has {len(content)} characters")
print(f"Has newlines: {chr(10) in content}")
print(f"Contains 'noProof': {'noProof' in content}")
print(f"Count of 'noProof': {content.count('noProof')}")

# Find first occurrence
idx = content.find('<w:noProof/>')
if idx != -1:
    # Show 100 chars before and after
    start = max(0, idx - 100)
    end = min(len(content), idx + 100)
    print(f"\nFirst occurrence at position {idx}:")
    print(repr(content[start:end]))
