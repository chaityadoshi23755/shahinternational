import re

# Read the SVG path data from detailed_world.svg
svg_content = open('detailed_world.svg', 'r', encoding='utf-8').read()
path_match = re.search(r'<path[^>]*d="([^"]+)"', svg_content)
if not path_match:
    print("Could not find path in detailed_world.svg")
    exit(1)
path_d = path_match.group(1)

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

          <!-- Text Content -->
          <div class="who-we-are-text reveal reveal-delay-1" style="flex: 1;">
            <p style="font-size: 1.05rem; line-height: 1.8; color: var(--color-text-base); margin-bottom: 1.5rem;">Founded by <strong style="color: var(--color-brand-red);">Mr. Kirti Shah</strong>, Shah International has built a legacy of <strong style="color: var(--color-brand-red);">over 30 years</strong> as a leading indenting house in the laminate and wood-based panel industry. Today, driven by the next generation of leadership, we proudly represent world-renowned global companies across the Indian subcontinent.</p>
            <p style="font-size: 1.05rem; line-height: 1.8; color: var(--color-text-base);">We are more than just suppliers; we are a reliable bridge connecting global manufacturing giants with India&#8217;s booming interior infrastructure market. Our commitment to integrity, high-quality service, and long-term partnerships ensures that we continually deliver world-class innovation right to your doorstep.</p>
          </div>

        </div>

        <!-- World Map with Partner Markers -->
        <div class="reveal reveal-delay-2" style="position: relative; max-width: 1000px; margin: 0 auto 3rem auto; padding: 2rem 0;">
            <!-- Realistic Detailed World Map SVG -->
            <svg class="svg-draw" viewBox="0 0 4378 2434" fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" style="width: 100%; height: auto; filter: drop-shadow(0 10px 15px rgba(226,49,55,0.15));" xmlns="http://www.w3.org/2000/svg">
                <path d="{path_d}" opacity="0.8" />
                
                <!-- Map Markers with Flags -->
                <g class="map-marker-group" transform="translate(2100, 420)">
                    <image href="https://flagcdn.com/w40/de.png" x="-25" y="-45" width="50" height="34" preserveAspectRatio="xMidYMid slice" />
                    <circle cx="0" cy="-28" r="8" fill="var(--color-brand-red)" />
                    <circle cx="0" cy="-28" r="22" fill="none" stroke="var(--color-brand-red)" stroke-width="4">
                        <animate attributeName="r" values="22; 45; 22" dur="2s" repeatCount="indefinite" />
                        <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
                    </circle>
                    <text x="35" y="-22" fill="var(--color-brand-red)" font-size="28" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Schattdecor</text>
                </g>
                <g class="map-marker-group" transform="translate(2050, 470)">
                    <image href="https://flagcdn.com/w40/ch.png" x="-25" y="-45" width="50" height="34" preserveAspectRatio="xMidYMid slice" />
                    <circle cx="0" cy="-28" r="8" fill="var(--color-brand-red)" />
                    <circle cx="0" cy="-28" r="22" fill="none" stroke="var(--color-brand-red)" stroke-width="4">
                        <animate attributeName="r" values="22; 45; 22" dur="2s" repeatCount="indefinite" />
                        <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
                    </circle>
                    <text x="-35" y="-22" fill="var(--color-brand-red)" font-size="28" font-family="Inter, sans-serif" font-weight="700" text-anchor="end">Arcolor</text>
                </g>
                <g class="map-marker-group" transform="translate(3580, 840)">
                    <image href="https://flagcdn.com/w40/cn.png" x="-25" y="-45" width="50" height="34" preserveAspectRatio="xMidYMid slice" />
                    <circle cx="0" cy="-28" r="8" fill="var(--color-brand-red)" />
                    <circle cx="0" cy="-28" r="22" fill="none" stroke="var(--color-brand-red)" stroke-width="4">
                        <animate attributeName="r" values="22; 45; 22" dur="2s" repeatCount="indefinite" />
                        <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
                    </circle>
                    <text x="0" y="30" fill="var(--color-brand-red)" font-size="28" font-family="Inter, sans-serif" font-weight="700" text-anchor="middle">Kingdecor</text>
                </g>
                <g class="map-marker-group" transform="translate(3800, 740)">
                    <image href="https://flagcdn.com/w40/jp.png" x="-25" y="-45" width="50" height="34" preserveAspectRatio="xMidYMid slice" />
                    <circle cx="0" cy="-28" r="8" fill="var(--color-brand-red)" />
                    <circle cx="0" cy="-28" r="22" fill="none" stroke="var(--color-brand-red)" stroke-width="4">
                        <animate attributeName="r" values="22; 45; 22" dur="2s" repeatCount="indefinite" />
                        <animate attributeName="opacity" values="1; 0; 1" dur="2s" repeatCount="indefinite" />
                    </circle>
                    <text x="0" y="30" fill="var(--color-brand-red)" font-size="28" font-family="Inter, sans-serif" font-weight="700" text-anchor="middle">Mitsubishi</text>
                </g>
            </svg>
        </div>

        <div style="text-align: center;" class="reveal reveal-delay-3">
          <a href="about-us.html" class="btn btn-outline" style="border-color: var(--color-brand-red); color: var(--color-brand-red);">READ OUR STORY</a>
        </div>

      </div>

    </section>'''

final_html = html_content[:start_idx] + new_section + html_content[end_idx:]

open("index.html", "w", encoding="utf-8").write(final_html)
print("Successfully restored the exact code layout for the Who We Are section!")
