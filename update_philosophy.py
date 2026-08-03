content = open('index.html', 'r', encoding='utf-8').read()

start_marker = '<!-- 3. Parallax Philosophy Section -->'
start_idx = content.find(start_marker)
end_idx = content.find('</section>', start_idx) + 10

new_section = '''<!-- 3. Redesigned Philosophy Section -->
    <section class="section" style="background-color: var(--color-brand-red); padding: 8rem 0; position: relative; overflow: hidden;">
      <!-- Subtle background pattern -->
      <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03; background-image: radial-gradient(#ffffff 1px, transparent 1px); background-size: 20px 20px;"></div>
      
      <div class="container relative z-10">
        <div class="flex gap-xl" style="align-items: center; flex-wrap: wrap;">
          
          <!-- Left side: The self-revealing artistic laminate SVG -->
          <div class="philosophy-svg-container reveal reveal-delay-1" style="flex: 1; min-width: 300px; display: flex; justify-content: center; position: relative;">
            <svg class="svg-draw" viewBox="0 0 500 500" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 450px; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));">
                <!-- Stack of wood panels (Isometric) -->
                <!-- Bottom Panel -->
                <path d="M 100 350 L 250 420 L 400 350 L 250 280 Z" />
                <path d="M 100 350 L 100 370 L 250 440 L 400 370 L 400 350" />
                
                <!-- Middle Panel -->
                <path d="M 100 310 L 250 380 L 400 310 L 250 240 Z" />
                <path d="M 100 310 L 100 330 L 250 400 L 400 330 L 400 310" />
                
                <!-- Laminate Paper Unrolling -->
                <!-- Paper resting on top -->
                <path d="M 100 270 L 250 340 L 350 293" />
                <!-- The swooping unroll -->
                <path d="M 350 293 C 400 270 420 200 370 150 C 320 100 250 50 200 100 C 150 150 200 220 250 270 C 300 320 380 320 400 250" />
                <!-- The swirl inside the roll -->
                <path d="M 230 130 C 200 160 230 200 260 170" />
                
                <!-- Lines indicating wood grain / texture on panels -->
                <path d="M 120 340 L 200 378" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>
                <path d="M 150 330 L 240 372" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>
                <path d="M 120 300 L 200 338" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>
                <path d="M 150 290 L 240 332" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>
                
                <!-- Dotted abstract accent lines -->
                <circle cx="100" cy="150" r="4" fill="#ffffff" stroke="none">
                    <animate attributeName="opacity" values="0.4; 1; 0.4" dur="3s" repeatCount="indefinite" />
                </circle>
                <path d="M 100 150 L 150 100" stroke-width="1.5" stroke-dasharray="2 4" opacity="0.5" />
                
                <circle cx="400" cy="100" r="5" fill="none" stroke-width="1.5" opacity="0.8">
                    <animate attributeName="r" values="3; 8; 3" dur="2.5s" repeatCount="indefinite" />
                </circle>
                <path d="M 400 100 L 350 150" stroke-width="1.5" stroke-dasharray="2 4" opacity="0.5" />
                
                <path d="M 50 220 C 60 200 80 180 100 170" stroke-width="1.5" opacity="0.4" />
                <path d="M 450 300 C 440 320 420 340 400 350" stroke-width="1.5" opacity="0.4" />
            </svg>
          </div>

          <!-- Right side: The Philosophy Text -->
          <div class="philosophy-text-container reveal reveal-delay-2" style="flex: 1; min-width: 300px; padding: 2rem;">
            <h2 style="color: #ffffff; font-size: 3.5rem; margin-bottom: 1.5rem; font-family: 'Playfair Display', serif;">Our Philosophy</h2>
            <div style="width: 80px; height: 3px; background-color: #ffffff; margin-bottom: 2.5rem;"></div>
            <p style="color: rgba(255,255,255,0.95); font-size: 1.65rem; line-height: 1.8; font-style: italic; font-family: 'Playfair Display', serif; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">
              "Beyond Business. We build ties that bridge global innovation with Indian excellence. Our commitment is not just to supply materials, but to elevate the very foundation of interior architecture."
            </p>
            <div style="margin-top: 3rem;">
              <a href="about-us.html" class="btn btn-outline" style="border-color: #ffffff; color: #ffffff;">DISCOVER MORE</a>
            </div>
          </div>

        </div>
      </div>
    </section>'''

final_content = content[:start_idx] + new_section + content[end_idx:]

open('index.html', 'w', encoding='utf-8').write(final_content)
print("Successfully replaced Philosophy section with the red background and line-art SVG!")
