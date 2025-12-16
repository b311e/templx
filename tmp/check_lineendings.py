with open(r'builds\osa\templates\osaReport\tmp-backup\document.xml', 'rb') as f:
    data = f.read()
    
print(f"File size: {len(data)}")
print(f"Has CRLF (\\r\\n): {b'\\r\\n' in data}")
print(f"Has LF (\\n): {b'\\n' in data}")

# Find noProof
idx = data.find(b'noProof')
if idx != -1:
    print(f"\nFound noProof at byte {idx}")
    start = max(0, idx - 100)
    end = min(len(data), idx + 100)
    print(f"Sample around it:")
    print(repr(data[start:end]))
