with open(r'builds\osa\templates\osaReport\in\word\document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'File size: {len(content)} chars')
print(f'Contains noProof: {"noProof" in content}')
print(f'Count of noProof: {content.count("noProof")}')
print(f'Has line breaks: {"\\n" in content or "\\r" in content}')

# Check patterns
pattern_mini_block = '<w:rPr><w:noProof/></w:rPr>'
pattern_mini_standalone = '<w:noProof/>'

print(f'\nMinified block pattern matches: {content.count(pattern_mini_block)}')
print(f'Minified standalone pattern matches: {content.count(pattern_mini_standalone)}')
