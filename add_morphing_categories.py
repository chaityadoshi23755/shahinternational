import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('</section>', content.find('Our Philosophy')) + 10

# New Product Categories section with morphing SVGs
category_section = """
    <!-- Premium Product Categories -->
    <section class="section" style="background-color: #111; padding: 6rem 0;">
      <div class="container">
        <div class="section-title text-center reveal">
          <h2 style="color: #fff; font-family: 'Playfair Display', serif;">Explore Collections</h2>
          <div style="width: 60px; height: 2px; background: var(--color-brand-red); margin: 1rem auto 3rem;"></div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem;">
          <!-- Category 1 -->
          <a href="woodgrains.html" class="category-card reveal reveal-delay-1" style="display: block; text-align: center; text-decoration: none; padding: 3rem 2rem; border: 1px solid rgba(255,255,255,0.1); transition: all 0.4s ease;">
            <svg class="category-icon" viewBox="0 0 100 100" width="80" height="80" stroke="var(--color-brand-red)" stroke-width="2" fill="none" style="margin-bottom: 2rem;">
              <!-- Initially a simple square, morphs on hover in CSS -->
              <path class="morph-shape" d="M 20 20 L 80 20 L 80 80 L 20 80 Z" style="transition: d 0.6s cubic-bezier(0.2, 1, 0.3, 1);" />
              <path class="morph-detail" d="M 20 40 L 80 40" opacity="0" style="transition: opacity 0.6s;" />
              <path class="morph-detail" d="M 20 60 L 80 60" opacity="0" style="transition: opacity 0.6s;" />
            </svg>
            <h3 style="color: #fff; font-family: 'Inter', sans-serif; letter-spacing: 2px; font-size: 1.2rem;">WOODGRAINS</h3>
          </a>
          
          <!-- Category 2 -->
          <a href="Synchron-range.html" class="category-card reveal reveal-delay-2" style="display: block; text-align: center; text-decoration: none; padding: 3rem 2rem; border: 1px solid rgba(255,255,255,0.1); transition: all 0.4s ease;">
            <svg class="category-icon" viewBox="0 0 100 100" width="80" height="80" stroke="var(--color-brand-red)" stroke-width="2" fill="none" style="margin-bottom: 2rem;">
              <path class="morph-shape" d="M 50 20 L 80 50 L 50 80 L 20 50 Z" style="transition: d 0.6s cubic-bezier(0.2, 1, 0.3, 1);" />
              <circle class="morph-detail" cx="50" cy="50" r="10" opacity="0" style="transition: opacity 0.6s;" />
            </svg>
            <h3 style="color: #fff; font-family: 'Inter', sans-serif; letter-spacing: 2px; font-size: 1.2rem;">SYNCHRON PORES</h3>
          </a>
          
          <!-- Category 3 -->
          <a href="Unique-colors.html" class="category-card reveal reveal-delay-3" style="display: block; text-align: center; text-decoration: none; padding: 3rem 2rem; border: 1px solid rgba(255,255,255,0.1); transition: all 0.4s ease;">
            <svg class="category-icon" viewBox="0 0 100 100" width="80" height="80" stroke="var(--color-brand-red)" stroke-width="2" fill="none" style="margin-bottom: 2rem;">
              <path class="morph-shape" d="M 30 30 C 50 10, 70 30, 70 70 C 50 90, 30 70, 30 30 Z" style="transition: d 0.6s cubic-bezier(0.2, 1, 0.3, 1);" />
            </svg>
            <h3 style="color: #fff; font-family: 'Inter', sans-serif; letter-spacing: 2px; font-size: 1.2rem;">UNIQUE SOLIDS</h3>
          </a>
        </div>
      </div>
      <style>
        .category-card:hover { background: rgba(255,255,255,0.03); transform: translateY(-5px); border-color: rgba(226,49,55,0.5) !important; }
        .category-card:hover .category-icon { transform: scale(1.1); transition: transform 0.4s ease; }
        .category-card:hover .morph-shape:nth-child(1) { d: path("M 30 10 C 60 10, 90 40, 70 90 C 40 90, 10 60, 30 10 Z"); }
        .category-card:nth-child(1):hover .morph-shape { d: path("M 20 20 Q 50 5, 80 20 T 80 80 Q 50 95, 20 80 T 20 20 Z") !important; }
        .category-card:nth-child(2):hover .morph-shape { d: path("M 20 20 L 80 20 L 80 80 L 20 80 Z") !important; }
        .category-card:nth-child(3):hover .morph-shape { d: path("M 50 10 C 80 10, 90 40, 50 90 C 10 40, 20 10, 50 10 Z") !important; }
        .category-card:hover .morph-detail { opacity: 1 !important; }
      </style>
    </section>
"""

new_content = content[:start_idx] + category_section + content[start_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added morphing categories section.")
