import urllib.request
import re

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
svg_data = response.read().decode('utf-8')

# Extract paths
paths = re.findall(r'<path[^>]*d="([^"]+)"', svg_data)

# Combine into a new SVG using Wikipedia map paths
new_svg = f'''<svg class="svg-draw" viewBox="0 0 2754 1398" fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" style="width: 100%; height: auto; filter: drop-shadow(0 10px 15px rgba(226,49,55,0.15));">'''

for p in paths:
    new_svg += f'\n<path d="{p}" opacity="0.8" />'

new_svg += '''
    <!-- Map Markers with Flags -->
    <!-- Positioned for 2754x1398 viewBox -->
    <g class="map-marker-group" transform="translate(1330, 240)">
        <image href="https://flagcdn.com/w40/de.png" x="-18" y="-30" width="36" height="24" preserveAspectRatio="xMidYMid slice" />
        <circle cx="0" cy="-18" r="6" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-18" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="3">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="24" y="-14" fill="var(--color-brand-red)" font-size="20" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Schattdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(1300, 270)">
        <image href="https://flagcdn.com/w40/ch.png" x="-18" y="-30" width="36" height="24" preserveAspectRatio="xMidYMid slice" />
        <circle cx="0" cy="-18" r="6" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-18" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="3">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="-24" y="-14" fill="var(--color-brand-red)" font-size="20" font-family="Inter, sans-serif" font-weight="700" text-anchor="end">Arcolor</text>
    </g>
    <g class="map-marker-group" transform="translate(2250, 480)">
        <image href="https://flagcdn.com/w40/cn.png" x="-18" y="-30" width="36" height="24" preserveAspectRatio="xMidYMid slice" />
        <circle cx="0" cy="-18" r="6" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-18" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="3">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="0" y="20" fill="var(--color-brand-red)" font-size="20" font-family="Inter, sans-serif" font-weight="700" text-anchor="middle">Kingdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(2390, 420)">
        <image href="https://flagcdn.com/w40/jp.png" x="-18" y="-30" width="36" height="24" preserveAspectRatio="xMidYMid slice" />
        <circle cx="0" cy="-18" r="6" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-18" r="16" fill="none" stroke="var(--color-brand-red)" stroke-width="3">
            <animate attributeName="r" values="16; 30; 16" dur="2s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
        </circle>
        <text x="0" y="20" fill="var(--color-brand-red)" font-size="20" font-family="Inter, sans-serif" font-weight="700" text-anchor="middle">Mitsubishi</text>
    </g>
</svg>
'''

html_content = open("index.html", "r", encoding="utf-8", errors="ignore").read()

start_marker = '<section id="who-we-are" class="section bg-light">'
end_marker = '</section>'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker, start_idx) + len(end_marker)

new_section = f'''<section id="who-we-are" class="section bg-light">

      <div class="container reveal">

        <h2 class="section-heading" style="text-align: center;">Who We Are</h2>

        <p class="section-subheading" style="text-align: center; margin-bottom: 4rem;">A Legacy of Excellence Since 1993</p>

        <div class="flex gap-lg who-we-are-container" style="align-items: center; margin-bottom: 3rem;">

          <!-- Map on the Left (Side-by-Side Format) -->
          <div class="who-we-are-img reveal reveal-delay-1" style="flex: 0 0 50%; display: flex; align-items: center; justify-content: center; padding: 1rem;">
            {new_svg}
          </div>
          
          <!-- Text on the Right (Side-by-Side Format) -->
          <div class="flex-1 reveal reveal-delay-2" style="display: flex; flex-direction: column; justify-content: center;">
            <p style="font-family: 'Inter', sans-serif; font-size: 1.15rem; line-height: 1.8; margin-bottom: 1.5rem; color: #444;">
              Founded by <strong style="color: var(--color-brand-red);">Mr. Kirti Shah</strong>, Shah International has built a legacy of <strong style="color: var(--color-brand-red);">over 30 years</strong> as a leading indenting house in the laminate and wood-based panel industry. Today, driven by the next generation of leadership, we proudly represent world-renowned global companies across the Indian subcontinent.
            </p>
            <p style="font-family: 'Inter', sans-serif; font-size: 1.15rem; line-height: 1.8; margin-bottom: 0; color: #444;">
              We are more than just suppliers; we are a reliable bridge connecting global manufacturing giants with India's booming interior infrastructure market. Our commitment to integrity, high-quality service, and long-term partnerships ensures that we continually deliver world-class innovation right to your doorstep.
            </p>
          </div>

        </div>
        
        <div style="text-align: center;" class="reveal reveal-delay-3">
          <a href="about-us.html" class="btn btn-outline" style="border-color: var(--color-brand-red); color: var(--color-brand-red);">READ OUR STORY</a>
        </div>

      </div>

    </section>'''

final_html = html_content[:start_idx] + new_section + html_content[end_idx:]

open("index.html", "w", encoding="utf-8").write(final_html)
print("Successfully laid out Wikipedia map and text side-by-side with no overlap!")
