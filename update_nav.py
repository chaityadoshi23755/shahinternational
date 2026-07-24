import os
import re

directory = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational_v2'
filepath = os.path.join(directory, 'header.html')

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Design and Trends with E-Catalogs and change the href
html = html.replace('href="Design-and-Trends.html">Design and Trends</a>', 'href="e-catalogs.html">E-Catalogs</a>')

# Replace About Us with Company Dropdown (Desktop)
old_about = '<li><a href="about-us.html">About Us</a></li>'
new_company_desktop = '''<li>
          <a href="#" class="dropdown-toggle">Company <span class="chevron"><i class="fa-solid fa-chevron-down"></i></span></a>
          <ul class="dropdown-menu">
            <li><a href="about-us.html">About Us</a></li>
            <li><a href="sustainability.html">Sustainability</a></li>
            <li><a href="csr.html">CSR</a></li>
            <li><a href="team.html">Our Team</a></li>
            <li><a href="distribution.html">Distribution Network</a></li>
          </ul>
        </li>'''
if old_about in html:
    html = html.replace(old_about, new_company_desktop, 1)

# Replace About Us with Company Dropdown (Mobile)
new_company_mobile = '''<li>
      <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">Company <i class="fa-solid fa-chevron-down" style="font-size:0.7em;"></i></button>
      <ul class="sub-menu">
        <li><a href="about-us.html">About Us</a></li>
        <li><a href="sustainability.html">Sustainability</a></li>
        <li><a href="csr.html">CSR</a></li>
        <li><a href="team.html">Our Team</a></li>
        <li><a href="distribution.html">Distribution Network</a></li>
      </ul>
    </li>'''
if old_about in html:
    html = html.replace(old_about, new_company_mobile, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Header navigation updated successfully.')
