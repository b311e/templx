with open(r'builds\osa\templates\osaReport\in\word\document.xml', 'rb') as f:
    data = f.read()
    
# Find the first rPr with noProof
idx = data.find(b'<w:rPr>')
if idx != -1:
    # Show 150 bytes around it to see the exact format
    start = max(0, idx - 20)
    end = min(len(data), idx + 150)
    sample = data[start:end]
    print("Bytes around first <w:rPr>:")
    print(repr(sample))
    print("\n\nAs string:")
    print(sample.decode('utf-8'))
