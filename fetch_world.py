import urllib.request
import re

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
svg_data = response.read().decode('utf-8')

# Extract paths
paths = re.findall(r'<path[^>]*d="([^"]+)"', svg_data)

# Combine into a new SVG
new_svg = f'''<svg class="svg-draw" viewBox="0 0 2754 1398" fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" style="width: 100%; max-width: 500px; filter: drop-shadow(0 10px 15px rgba(226,49,55,0.15));">'''

for p in paths:
    # Wikimedia SVG might have a lot of paths, we just take them all
    new_svg += f'\n<path d="{p}" opacity="0.8" />'

new_svg += "\n</svg>"

# Now replace the SVG in index.html
html_content = open("index.html", "r", encoding="utf-8").read()

# Find the start and end of the current SVG in Who We Are
start_idx = html_content.find('<div class="who-we-are-img')
if start_idx != -1:
    svg_start = html_content.find('<svg', start_idx)
    svg_end = html_content.find('</svg>', svg_start) + 6
    
    final_html = html_content[:svg_start] + new_svg + html_content[svg_end:]
    open("index.html", "w", encoding="utf-8").write(final_html)
    print("Successfully replaced SVG in index.html")
else:
    print("Could not find who-we-are-img div")
