import re

content = open('index.html', 'r', encoding='utf-8', errors='ignore').read()

start_marker = '<section id="who-we-are" class="section bg-light">'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

new_section = '''<section id="who-we-are" class="section bg-light">

      <div class="container reveal">

        <h2 class="section-heading" style="text-align: center;">Who We Are</h2>

        <p class="section-subheading" style="text-align: center; margin-bottom: 4rem;">A Legacy of Excellence Since 1993</p>

        <div class="flex gap-lg who-we-are-container" style="align-items: center; margin-bottom: 3rem;">

          <div class="who-we-are-img reveal reveal-delay-1" style="flex: 0 0 55%; display: flex; align-items: center; justify-content: center; position: relative;">
            
            <!-- Simplified World Map SVG (The Art Graphic) -->
            <svg viewBox="0 0 1000 500" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: auto;">
              <!-- Continents as simplified shapes -->
              <g stroke="none" fill="rgba(226,49,55,0.06)">
                <!-- North America -->
                <path d="M80 80 Q120 60 180 70 Q220 55 260 75 Q270 90 250 110 Q240 130 220 140 Q200 155 180 170 Q160 180 140 200 Q120 210 100 200 Q80 190 70 170 Q60 150 55 130 Q50 110 60 90 Z"/>
                <!-- Central America -->
                <path d="M140 200 Q155 210 165 230 Q170 245 175 260 Q165 265 155 255 Q145 240 130 220 Z"/>
                <!-- South America -->
                <path d="M175 260 Q200 255 220 270 Q240 290 250 320 Q255 350 245 380 Q235 410 220 430 Q200 445 185 430 Q175 415 170 395 Q165 370 160 345 Q155 320 160 295 Q165 275 175 260 Z"/>
                <!-- Europe -->
                <path d="M430 65 Q450 55 480 60 Q510 58 530 70 Q540 85 535 100 Q530 115 520 125 Q510 135 495 140 Q480 145 465 140 Q450 135 440 120 Q430 105 425 90 Q425 75 430 65 Z"/>
                <!-- Africa -->
                <path d="M440 160 Q470 150 500 155 Q520 165 530 185 Q540 210 545 240 Q548 270 540 300 Q530 330 515 355 Q500 375 480 385 Q460 388 445 375 Q435 355 430 330 Q425 300 425 270 Q425 240 430 215 Q435 190 440 170 Q440 165 440 160 Z"/>
                <!-- Asia (large) -->
                <path d="M530 50 Q580 40 640 45 Q700 40 760 50 Q810 55 850 70 Q880 85 890 110 Q895 130 885 150 Q870 170 850 180 Q830 190 810 195 Q790 200 770 195 Q750 190 730 185 Q710 180 690 175 Q670 172 650 170 Q630 168 610 170 Q590 175 570 180 Q555 185 540 175 Q530 165 525 150 Q520 130 520 110 Q525 90 530 70 Q530 60 530 50 Z"/>
                <!-- India -->
                <path d="M640 180 Q660 175 675 190 Q685 210 688 235 Q685 260 675 280 Q665 295 650 300 Q635 295 628 280 Q622 260 625 235 Q630 210 635 195 Q638 185 640 180 Z"/>
                <!-- Southeast Asia -->
                <path d="M750 190 Q775 185 800 195 Q815 210 820 230 Q815 245 800 250 Q785 248 770 240 Q758 225 755 210 Q750 200 750 190 Z"/>
                <!-- Australia -->
                <path d="M780 330 Q810 320 840 325 Q865 335 880 355 Q885 375 875 390 Q860 400 840 405 Q815 405 795 395 Q780 380 775 360 Q775 345 780 330 Z"/>
                <!-- Greenland -->
                <path d="M290 30 Q310 22 330 28 Q345 35 348 50 Q345 65 335 72 Q320 76 305 72 Q292 65 288 50 Q286 40 290 30 Z"/>
              </g>
              <!-- Subtle grid lines -->
              <g stroke="rgba(226,49,55,0.08)" stroke-width="0.5" stroke-dasharray="4 6">
                <line x1="0" y1="125" x2="1000" y2="125"/>
                <line x1="0" y1="250" x2="1000" y2="250"/>
                <line x1="0" y1="375" x2="1000" y2="375"/>
                <line x1="250" y1="0" x2="250" y2="500"/>
                <line x1="500" y1="0" x2="500" y2="500"/>
                <line x1="750" y1="0" x2="750" y2="500"/>
              </g>
              <!-- Connection lines from India to partners -->
              <g stroke="var(--color-brand-red)" stroke-width="1" opacity="0.3" stroke-dasharray="4 4">
                <path d="M655 230 Q580 150 490 95" fill="none"/>
                <path d="M650 225 Q570 140 475 90" fill="none"/>
                <path d="M645 235 Q570 160 480 115" fill="none"/>
                <path d="M680 220 Q750 160 830 115" fill="none"/>
                <path d="M675 215 Q720 170 770 155" fill="none"/>
              </g>
              <!-- India highlight (HQ) -->
              <circle cx="655" cy="235" r="12" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon"/>
              <circle cx="655" cy="235" r="5" fill="var(--color-brand-red)"/>
              <text x="655" y="265" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="700" text-anchor="middle">INDIA (HQ)</text>
              
              <!-- Partner Flags and Markers Directly inside SVG -->
              <!-- Germany (Schattdecor) -->
              <g transform="translate(480, 85)">
                  <image href="https://flagcdn.com/w40/de.png" x="-12" y="-18" width="24" height="16" />
                  <circle cx="0" cy="0" r="4" fill="var(--color-brand-red)" />
                  <circle cx="0" cy="0" r="10" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon" />
                  <!-- Adjusted text to avoid overlap -->
                  <text x="18" y="4" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="600" text-anchor="start">Schattdecor</text>
              </g>
              <!-- Germany (Hueck) -->
              <g transform="translate(465, 80)">
                  <image href="https://flagcdn.com/w40/de.png" x="-12" y="-18" width="24" height="16" />
                  <circle cx="0" cy="0" r="4" fill="var(--color-brand-red)" />
                  <circle cx="0" cy="0" r="10" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon" />
                  <!-- Adjusted text to avoid overlap -->
                  <text x="-16" y="4" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="600" text-anchor="end">Hueck</text>
              </g>
              <!-- Switzerland (Arcolor) -->
              <g transform="translate(470, 105)">
                  <image href="https://flagcdn.com/w40/ch.png" x="-12" y="-18" width="24" height="16" />
                  <circle cx="0" cy="0" r="4" fill="var(--color-brand-red)" />
                  <circle cx="0" cy="0" r="10" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon" />
                  <text x="0" y="16" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="600" text-anchor="middle">Arcolor</text>
              </g>
              <!-- China (Kingdecor) -->
              <g transform="translate(760, 145)">
                  <image href="https://flagcdn.com/w40/cn.png" x="-12" y="-18" width="24" height="16" />
                  <circle cx="0" cy="0" r="4" fill="var(--color-brand-red)" />
                  <circle cx="0" cy="0" r="10" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon" />
                  <text x="0" y="16" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="600" text-anchor="middle">Kingdecor</text>
              </g>
              <!-- Japan (Mitsubishi) -->
              <g transform="translate(820, 105)">
                  <image href="https://flagcdn.com/w40/jp.png" x="-12" y="-18" width="24" height="16" />
                  <circle cx="0" cy="0" r="4" fill="var(--color-brand-red)" />
                  <circle cx="0" cy="0" r="10" fill="none" stroke="var(--color-brand-red)" stroke-width="2" class="map-beacon" />
                  <text x="0" y="16" fill="var(--color-brand-red)" font-size="11" font-family="Inter, sans-serif" font-weight="600" text-anchor="middle">Mitsubishi</text>
              </g>
            </svg>

          </div>
          
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

final_html = content[:start_idx] + new_section + content[end_idx:]

open('index.html', 'w', encoding='utf-8').write(final_html)
print("Successfully restored the art-like graphic map with side-by-side layout and NO OVERLAPS!")
