import re

index_content = open('index.html', 'r', encoding='utf-8').read()
detailed_svg = open('detailed_world.svg', 'r', encoding='utf-8').read()

# Extract paths from detailed_world.svg
paths_match = re.findall(r'<path[^>]*d="([^"]+)"', detailed_svg)
paths_html = ""
for d in paths_match:
    paths_html += f'                <path class="svg-draw" d="{d}" opacity="0.8" fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>\n'

# Find the section boundaries in index.html
start_marker = '<section id="who-we-are" class="section bg-light">'
end_marker = '</section>'

start_idx = index_content.find(start_marker)
end_idx = index_content.find(end_marker, start_idx) + len(end_marker)

new_section = f'''<section id="who-we-are" class="section bg-light">

      <div class="container reveal">

        <h2 class="section-heading" style="text-align: center;">Who We Are</h2>

        <p class="section-subheading" style="text-align: center; margin-bottom: 4rem;">A Legacy of Excellence Since 1993</p>

        <div class="flex gap-lg who-we-are-container" style="align-items: center; margin-bottom: 3rem;">

          <!-- Text Content -->
          <div class="who-we-are-text reveal reveal-delay-1" style="flex: 1;">
            <p style="font-size: 1.05rem; line-height: 1.8; color: var(--color-text-base); margin-bottom: 1.5rem;">Founded by <strong style="color: var(--color-brand-red);">Mr. Kirti Shah</strong>, Shah International has built a legacy of <strong style="color: var(--color-brand-red);">over 30 years</strong> as a leading indenting house in the laminate and wood-based panel industry. Today, driven by the next generation of leadership, we proudly represent world-renowned global companies across the Indian subcontinent.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: var(--color-text-base);">We are more than just suppliers; we are a reliable bridge connecting global manufacturing giants with India&#8217;s booming interior infrastructure market. Our commitment to integrity, high-quality service, and long-term partnerships ensures that we continually deliver world-class innovation right to your doorstep.</p>
          </div>

        </div>

        <!-- World Map with Partner Markers -->
        <div class="reveal reveal-delay-2" style="position: relative; max-width: 900px; margin: 0 auto 3rem auto;">
            <!-- Detailed World Map SVG -->
            <svg viewBox="0 0 4378 2434" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto; filter: drop-shadow(0 10px 15px rgba(226,49,55,0.15));">
{paths_html}
            </svg>

            <!-- Map Markers with Flags -->
            <!-- Adjusted coordinates based on the 4378x2434 viewBox -->
            <div class="map-marker" style="left: 49%; top: 16%;" title="Schattdecor AG (Thansau, Germany)">
                <img src="https://flagcdn.com/w40/de.png" alt="Germany">
                <span>Schattdecor</span>
            </div>
            <div class="map-marker" style="left: 47%; top: 14%;" title="Hueck Rheinische (Viersen, Germany)">
                <img src="https://flagcdn.com/w40/de.png" alt="Germany">
                <span>Hueck</span>
            </div>
            <div class="map-marker" style="left: 48%; top: 21%;" title="Arcolor (Waldstatt, Switzerland)">
                <img src="https://flagcdn.com/w40/ch.png" alt="Switzerland">
                <span>Arcolor</span>
            </div>
            <div class="map-marker" style="left: 77%; top: 28%;" title="Kingdecor (Zhejiang, China)">
                <img src="https://flagcdn.com/w40/cn.png" alt="China">
                <span>Kingdecor</span>
            </div>
            <div class="map-marker" style="left: 83%; top: 20%;" title="Mitsubishi Chemical (Tokyo, Japan)">
                <img src="https://flagcdn.com/w40/jp.png" alt="Japan">
                <span>Mitsubishi</span>
            </div>
        </div>
        
        <div style="text-align: center;" class="reveal reveal-delay-3">

          <a href="about-us.html" class="btn btn-outline" style="border-color: var(--color-brand-red); color: var(--color-brand-red);">READ OUR STORY</a>

        </div>

      </div>

    </section>'''

final_html = index_content[:start_idx] + new_section + index_content[end_idx:]

open('index.html', 'w', encoding='utf-8').write(final_html)
print("Successfully replaced Who We Are section with realistic map!")
