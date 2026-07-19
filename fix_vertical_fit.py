import os
import glob

directory = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational_v2'
style_path = os.path.join(directory, 'style.css')

with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Align the grid and info blocks to the TOP so no space is wasted at the top of the scroll
css = css.replace('.pdp-grid-55-45 {\n  display: grid;\n  grid-template-columns: 55% 45%;\n  gap: 4rem;\n  align-items: center;',
                  '.pdp-grid-55-45 {\n  display: grid;\n  grid-template-columns: 55% 45%;\n  gap: 4rem;\n  align-items: flex-start;')

css = css.replace('.pdp-info {\n  display: flex;\n  flex-direction: column;\n  justify-content: center;\n}',
                  '.pdp-info {\n  display: flex;\n  flex-direction: column;\n  justify-content: flex-start;\n}')

# 2. Reduce the image max-height slightly to ensure it strictly fits on all laptop screens without overflow
if 'max-height: 75vh;' in css:
    css = css.replace('max-height: 75vh;', 'max-height: 65vh;')

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update all HTML files to bust the cache (style.css?v=4 -> style.css?v=5)
count = 0
for file_path in glob.glob(os.path.join(directory, '*.html')):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if 'href="style.css?v=4"' in html:
        html = html.replace('href="style.css?v=4"', 'href="style.css?v=5"')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Fixed vertical fit logic and busted cache on {count} HTML files.")
