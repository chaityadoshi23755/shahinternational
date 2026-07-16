import re

path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css'

with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace special grid columns to 1 per row
css = css.replace('grid-template-columns: repeat(7, 1fr) !important;', 'grid-template-columns: 1fr !important;')

# Add height fix
height_fix = """
.special-clients-grid .card-img,
.normal-clients-grid .card-img {
  height: auto !important;
  max-height: 120px !important;
}

.special-clients-grid .card-img-wrap,
.normal-clients-grid .card-img-wrap {
  padding: 1rem !important;
}
"""

css = css + height_fix

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated grid to 1 per row and fixed image height.")
