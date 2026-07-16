import re

path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css'

with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the specific lines
css = css.replace('grid-template-columns: repeat(7, 1fr);', 'grid-template-columns: repeat(7, 1fr) !important;')
css = css.replace('grid-template-columns: repeat(6, 1fr);', 'grid-template-columns: repeat(6, 1fr) !important;')

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Added !important to grid columns")
