v2 = open('../shahinternational_v2/index.html', encoding='utf-8').read()
v3 = open('index.html', encoding='utf-8').read()

start_marker = '<section id="who-we-are"'
end_marker = '</section>'

v2_start = v2.find(start_marker)
v2_end = v2.find(end_marker, v2_start) + len(end_marker)
v2_section = v2[v2_start:v2_end]

v3_start = v3.find(start_marker)
v3_end = v3.find(end_marker, v3_start) + len(end_marker)

print(f"v2 section size: {len(v2_section)}")

# Replace v3 section with v2 section
new_v3 = v3[:v3_start] + v2_section + v3[v3_end:]
open('index.html', 'w', encoding='utf-8').write(new_v3)
print("Restored Who We Are section from v2.")
