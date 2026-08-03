import urllib.request
import re

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
svg_data = response.read().decode('utf-8')

# Extract paths
paths = re.findall(r'<path[^>]*d="([^"]+)"', svg_data)

# Combine into a new SVG
new_svg = f'''<svg class="svg-draw" viewBox="0 0 2754 1398" fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" style="width: 100%; height: auto; filter: drop-shadow(0 10px 15px rgba(226,49,55,0.15));">'''

for p in paths:
    new_svg += f'\n<path d="{p}" opacity="0.8" />'

new_svg += '''
    <!-- Map Markers with Flags -->
    <!-- Positioned for 2754x1398 viewBox -->
    <g class="map-marker-group" transform="translate(1330, 240)">
        <!-- Germany (Schattdecor/Hueck) -->
        <image href="https://flagcdn.com/w40/de.png" x="0" y="0" width="24" height="16" preserveAspectRatio="xMidYMid slice" />
        <circle cx="12" cy="8" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="2">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
    </g>
    <g class="map-marker-group" transform="translate(1300, 270)">
        <!-- Switzerland (Arcolor) -->
        <image href="https://flagcdn.com/w40/ch.png" x="0" y="0" width="24" height="16" preserveAspectRatio="xMidYMid slice" />
        <circle cx="12" cy="8" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="2">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
    </g>
    <g class="map-marker-group" transform="translate(2250, 480)">
        <!-- China (Kingdecor) -->
        <image href="https://flagcdn.com/w40/cn.png" x="0" y="0" width="24" height="16" preserveAspectRatio="xMidYMid slice" />
        <circle cx="12" cy="8" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="2">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
    </g>
    <g class="map-marker-group" transform="translate(2390, 420)">
        <!-- Japan (Mitsubishi) -->
        <image href="https://flagcdn.com/w40/jp.png" x="0" y="0" width="24" height="16" preserveAspectRatio="xMidYMid slice" />
        <circle cx="12" cy="8" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="2">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
    </g>
</svg>
'''

html_content = open("index.html", "r", encoding="utf-8").read()

start_marker = '<section id="who-we-are" class="section bg-light">'
end_marker = '</section>'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker, start_idx) + len(end_marker)

new_section = f'''<section id="who-we-are" class="section bg-light">

      <div class="container reveal">

        <h2 class="section-heading" style="text-align: center;">Who We Are</h2>

        <p class="section-subheading" style="text-align: center; margin-bottom: 4rem;">A Legacy of Excellence Since 1993</p>

        <div class="who-we-are-container" style="display: flex; flex-direction: column; align-items: center; margin-bottom: 3rem;">

          <!-- Text Content on top to avoid overlap -->
          <div class="who-we-are-text reveal reveal-delay-1" style="max-width: 900px; text-align: center; margin-bottom: 2rem;">
            <p style="font-size: 1.15rem; line-height: 1.8; color: var(--color-text-base); margin-bottom: 1.5rem;">Founded by <strong style="color: var(--color-brand-red);">Mr. Kirti Shah</strong>, Shah International has built a legacy of <strong style="color: var(--color-brand-red);">over 30 years</strong> as a leading indenting house in the laminate and wood-based panel industry. Today, driven by the next generation of leadership, we proudly represent world-renowned global companies across the Indian subcontinent.</p>
            <p style="font-size: 1.15rem; line-height: 1.8; color: var(--color-text-base);">We are more than just suppliers; we are a reliable bridge connecting global manufacturing giants with India&#8217;s booming interior infrastructure market. Our commitment to integrity, high-quality service, and long-term partnerships ensures that we continually deliver world-class innovation right to your doorstep.</p>
          </div>

          <!-- Smaller Map Below -->
          <div class="who-we-are-img reveal reveal-delay-2" style="width: 100%; max-width: 700px; position: relative; display: flex; justify-content: center; align-items: center;">
            {new_svg}
          </div>

        </div>
        
        <div style="text-align: center;" class="reveal reveal-delay-3">
          <a href="about-us.html" class="btn btn-outline" style="border-color: var(--color-brand-red); color: var(--color-brand-red);">READ OUR STORY</a>
        </div>

      </div>

    </section>'''

final_html = html_content[:start_idx] + new_section + html_content[end_idx:]

open("index.html", "w", encoding="utf-8").write(final_html)
print("Successfully restored 800KB map with correct layout and flags")
