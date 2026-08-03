import re

with open('Our-Clients.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="clients-grid">')
if start_idx == -1:
    print("Could not find clients-grid, trying to find marquee instead.")
    start_idx = content.find('<div class="marquee-container')

end_idx = content.find('</div>', content.find('</div>', content.find('</div>', start_idx) + 1) + 1) + 6

logos = [
    ("sites/default/files/2019-06/greenlam_1.png", "Greenlam"),
    ("sites/default/files/2019-06/Merino Group_0.png", "Merino"),
    ("sites/default/files/2019-06/CenturyLaminates_MDMS_v1_1.png", "CenturyPly"),
    ("sites/default/files/2019-06/Action Tesa Logo WITH DOORS.png", "Action TESA"),
    ("sites/default/files/2019-06/AIROLAM logo_0.png", "AIROLAM"),
    ("sites/default/files/2019-06/godrej_0.png", "Godrej"),
    ("sites/default/files/2019-06/Stylam_0.png", "Stylam"),
    ("sites/default/files/2019-06/Virgo Laminate Logo_0.png", "Virgo"),
    ("sites/default/files/2019-06/Rushil Decor Ltd logo_0.png", "Rushil"),
    ("sites/default/files/2019-06/Spacewood Logo Side_0.png", "Spacewood"),
    ("sites/default/files/2019-06/Durian logo.png", "Durian")
]

grid_html = """
      <div class="principals-masonry" style="margin-bottom: 5rem;">
"""

for path, alt in logos:
    grid_html += f"""
        <div class="principal-tile reveal">
          <div class="principal-tile-hover-sweep"></div>
          <div class="principal-tile-pattern"></div>
          <div class="principal-tile-content">
            <img src="{path}" class="principal-tile-logo" alt="{alt}" style="max-height: 80px; width: auto; max-width: 200px;">
          </div>
          <div class="corner-mark top-left"></div>
          <div class="corner-mark bottom-right"></div>
        </div>"""

grid_html += "\n      </div>\n"

testimonials_start = content.find('<div class="testimonials-slider')

# If we found <style> before clients-grid, we need to remove it too
style_start = content.rfind('<style>', 0, start_idx)
if style_start != -1 and style_start > content.find('<section class="page-content">'):
    start_idx = style_start

new_content = content[:start_idx] + grid_html + content[testimonials_start:]

with open('Our-Clients.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Reverted Our-Clients.html to perfectly match homepage Global Giants grid.")
