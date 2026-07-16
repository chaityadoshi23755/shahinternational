import re

path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\Our-Clients.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the giant line
line22_match = re.search(r'<div class="card-grid grid-cols-4">(.*?)</div></div></div>', html)
if line22_match:
    inner_cards = line22_match.group(1)
    
    top_7 = '''      <!-- Special Clients -->
      <div class="card-grid special-clients-grid">
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/aica_0.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/AIROLAM logo_0.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/CenturyLaminates_MDMS_v1_1.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/godrej_0.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/greenlam_1.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/Merino Group_0.png" class="card-img" style="object-fit: contain;"></div></div>
        <div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/Royal Touch_0.png" class="card-img" style="object-fit: contain;"></div></div>
      </div>
      
      <h3 style="text-align: center; margin: 3rem 0; font-family: var(--font-heading); font-size: 2rem;">All Clients</h3>
      
      <div class="card-grid normal-clients-grid">''' + inner_cards + '</div>'

    html = html.replace(line22_match.group(0), top_7)
    
    # Also remove the 7 cards that were at the bottom
    html = re.sub(r'\s*<div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/(aica_0|AIROLAM logo_0|CenturyLaminates_MDMS_v1_1|godrej_0|greenlam_1|Merino Group_0|Royal Touch_0)\.png" class="card-img" style="object-fit: contain;"></div></div>', '', html)
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Success: Replaced HTML structure')
    except Exception as e:
        print('Write Error:', e)
else:
    print('Could not find line 22')
