import re

with open('Our-Clients.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous style and also remove the principal-tile-logo class which enforces height: 50px
content = content.replace('class="principal-tile-logo"', 'class="client-grid-logo"')

# Now add .client-grid-logo styles into the file if not already present
if '<style>' not in content[:content.find('<div class="principals-masonry"')]:
    style_block = """
      <style>
        .client-grid-logo {
          height: 180px !important;
          width: 100%;
          max-width: 250px;
          object-fit: contain;
          margin: 0 auto;
          filter: grayscale(100%);
          opacity: 0.7;
          transition: all 0.5s ease;
          position: relative;
          z-index: 5;
        }
        .principal-tile:hover .client-grid-logo {
          filter: grayscale(0%);
          opacity: 1;
          transform: scale(1.05);
        }
      </style>
"""
    # Insert it before the masonry grid
    idx = content.find('<div class="principals-masonry"')
    content = content[:idx] + style_block + content[idx:]

with open('Our-Clients.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed logo sizes.")
