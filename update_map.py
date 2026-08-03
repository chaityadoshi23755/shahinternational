import re

# Read the generated paths
paths = open('india_paths.html', encoding='utf-8').read()

# Read the HTML file
html = open('distribution.html', encoding='utf-8').read()

# The regex to replace the SVG content
# We want to replace the old viewBox and the old path.
# Old: viewBox="0 0 400 450"
# Old path: <!-- Detailed India Map Outline (Starting from Mumbai, looping clockwise) -->\n            <path d="M 80 240 ... Z" opacity="0.8" fill="rgba(226,49,55,0.05)" />

# We will just replace everything between <!-- Detailed India Map Outline... --> and <!-- Network lines inside map -->
pattern = re.compile(r'(<!-- Detailed India Map Outline.*?-->).*?(<!-- Network lines inside map -->)', re.DOTALL | re.IGNORECASE)

new_html = html.replace('viewBox="0 0 400 450"', 'viewBox="0 0 612 696"')
new_html = new_html.replace('stroke-width="2.5"', 'stroke-width="1.5"') # finer lines for detailed map

# Reposition the cities for the 612x696 viewBox!
# Old Mumbai: 80, 240. New Mumbai: ~130, 390
# Old Ahmedabad: 65, 205. New Ahmedabad: ~110, 310
# Old Delhi: 200, 120. New Delhi: ~180, 170
# Old Bangalore: 160, 330. New Bangalore: ~200, 520
# Old Kolkata: 270, 200. New Kolkata: ~420, 330

new_html = new_html.replace('d="M 80 240 L 200 120"', 'd="M 130 390 L 180 170"') # Mumbai to Delhi
new_html = new_html.replace('d="M 80 240 L 160 330"', 'd="M 130 390 L 200 520"') # Mumbai to Bangalore
new_html = new_html.replace('d="M 80 240 L 270 200"', 'd="M 130 390 L 420 330"') # Mumbai to Kolkata
new_html = new_html.replace('d="M 200 120 L 270 200"', 'd="M 180 170 L 420 330"') # Delhi to Kolkata
new_html = new_html.replace('d="M 160 330 L 270 200"', 'd="M 200 520 L 420 330"') # Bangalore to Kolkata

new_html = new_html.replace('cx="80" cy="240"', 'cx="130" cy="390"') # Mumbai
new_html = new_html.replace('x="10" y="245"', 'x="60" y="395"')
new_html = new_html.replace('cx="65" cy="205"', 'cx="110" cy="310"') # Ahmedabad
new_html = new_html.replace('x="5" y="195"', 'x="20" y="305"')
new_html = new_html.replace('cx="200" cy="120"', 'cx="180" cy="170"') # Delhi
new_html = new_html.replace('x="215" y="125"', 'x="195" y="175"')
new_html = new_html.replace('cx="160" cy="330"', 'cx="200" cy="520"') # Bangalore
new_html = new_html.replace('x="80" y="340"', 'x="120" y="530"')
new_html = new_html.replace('cx="270" cy="200"', 'cx="420" cy="330"') # Kolkata
new_html = new_html.replace('x="285" y="205"', 'x="435" y="335"')

replacement = f"\\1\n{paths}\n            \\2"
final_html = pattern.sub(replacement, new_html)

open('distribution.html', 'w', encoding='utf-8').write(final_html)
print("Updated distribution.html successfully.")
