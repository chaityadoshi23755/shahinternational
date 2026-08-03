import re

with open('Our-Clients.html', 'r', encoding='utf-8') as f:
    content = f.read()

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
      <style>
        .clients-grid {
          display: grid;
          grid-template-columns: repeat(5, 1fr);
          gap: 1.5rem;
          margin-top: 3rem;
          margin-bottom: 5rem;
        }
        @media (max-width: 1024px) { .clients-grid { grid-template-columns: repeat(3, 1fr); } }
        @media (max-width: 768px) { .clients-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (max-width: 480px) { .clients-grid { grid-template-columns: repeat(1, 1fr); } }

        .client-tile-container {
          position: relative;
          height: 180px;
          background-color: #ffffff;
          border: 1px solid rgba(0,0,0,0.05);
          border-radius: 16px;
          overflow: hidden;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.5s cubic-bezier(0.2, 1, 0.3, 1);
        }
        .client-tile-container:hover {
          transform: translateY(-5px);
          box-shadow: 0 15px 35px rgba(226,49,55,0.1);
          border-color: rgba(226,49,55,0.2);
        }
        .client-tile-logo {
          max-width: 130px;
          max-height: 60px;
          object-fit: contain;
          margin: 0 auto;
          filter: grayscale(100%) opacity(0.7);
          transition: all 0.5s cubic-bezier(0.2, 1, 0.3, 1);
          position: relative;
          z-index: 5;
        }
        .client-tile-container:hover .client-tile-logo {
          filter: grayscale(0%) opacity(1);
          transform: scale(1.05);
        }
      </style>
      
      <div class="clients-grid">
"""

for path, alt in logos:
    grid_html += f"""
        <div class="client-tile-container reveal">
          <div class="principal-tile-hover-sweep"></div>
          <div class="principal-tile-pattern"></div>
          <img src="{path}" class="client-tile-logo" alt="{alt}">
        </div>"""

grid_html += "\n      </div>\n"

# The end_idx might be tricky if there's multiple nested divs. Let's find the exact div
marquee_start = content.find('<div class="marquee-container')
testimonials_start = content.find('<div class="testimonials-slider')

new_content = content[:marquee_start] + grid_html + content[testimonials_start:]

with open('Our-Clients.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Our-Clients.html successfully.")
