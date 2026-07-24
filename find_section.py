content = open('index.html', 'r', encoding='utf-8').read()

# Find 'who-we-are' section boundaries
start = content.find('<section id="who-we-are"')
print(f'Section starts at char: {start}')

# Find the closing </section> after it
end = content.find('</section>', start)
print(f'Section ends at char: {end}')

# Count newlines to get line numbers  
start_line = content[:start].count('\n') + 1
end_line = content[:end+10].count('\n') + 1
print(f'Start line: {start_line}, End line: {end_line}')

# Print last 30 lines of the section
section = content[start:end+10]
lines = section.split('\n')
print(f'Total lines in section: {len(lines)}')
for i, line in enumerate(lines[-30:], len(lines)-29):
    print(f'L{start_line + i - 1}: {line[:150]}')
