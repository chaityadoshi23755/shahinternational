import re

# 1. Update index.html
html = open("index.html", "r", encoding="utf-8", errors="ignore").read()

start_marker = '<!-- 2. Interactive Who We Represent -->'
end_marker = '<!-- 4. Marquee Hover Bloom -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

new_html = '''<!-- 2. Interactive Who We Represent -->
    <section id="who-we-represent" class="section bg-light" style="background-color: #f8f9fa;">
      <div class="container">
        <div class="text-center reveal">
          <h2 class="section-heading">Global Giants We Represent</h2>
          <p class="section-subheading">Bringing world-class quality and innovation to the Indian market.</p>
        </div>
        
        <div class="principals-masonry">
          
          <a href="schattdecor-ag-germany.html" class="principal-tile reveal">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <img src="themes/agatha/img/logos/schattdecor.jpg" class="principal-tile-logo" alt="Schattdecor">
              <h3 class="country-name">Germany</h3>
              <p class="desc">World market leader in printed décor paper, integrating creativity, technology, and science since 1985.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
          <a href="kingdecor-zhejiang-co-ltd-china.html" class="principal-tile reveal reveal-delay-1">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <img src="themes/agatha/img/logos/kingdecor.jpg" class="principal-tile-logo" alt="Kingdecor">
              <h3 class="country-name">China</h3>
              <p class="desc">Asia's largest producer of base paper, manufacturing eco-friendly solid base and print base paper.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
          <a href="deurowood-gmbh-austria.html" class="principal-tile reveal reveal-delay-2">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <img src="themes/agatha/img/logos/log2.jpg" class="principal-tile-logo" alt="Deurowood">
              <h3 class="country-name">Austria</h3>
              <p class="desc">Global leaders in ecological chemical additives and hardeners for perfect surface finishing.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
          <a href="hueck-rheinische-gmbh-germany.html" class="principal-tile reveal">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <img src="themes/agatha/img/logos/log1.jpg" class="principal-tile-logo" alt="Hueck Rheinische">
              <h3 class="country-name">Germany</h3>
              <p class="desc">Pioneers of high-quality press pads that ensure optimal heat transfer and pressure distribution.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
          <a href="arcolor.html" class="principal-tile reveal reveal-delay-1">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <div class="principal-text-logo">Arcolor</div>
              <h3 class="country-name">Switzerland</h3>
              <p class="desc">Leading suppliers of innovative, sustainable, water-based, and VOC-free printing inks.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
          <a href="mitsubishi-chemical-corporation.html" class="principal-tile reveal reveal-delay-2">
            <div class="principal-tile-hover-sweep"></div>
            <div class="principal-tile-pattern"></div>
            <div class="principal-tile-content">
              <div class="principal-text-logo">Mitsubishi</div>
              <h3 class="country-name">Japan</h3>
              <p class="desc">Providing innovative solutions in chemistry, specializing in acrylic films for exterior UV protection.</p>
            </div>
            <div class="corner-mark top-left"></div>
            <div class="corner-mark bottom-right"></div>
          </a>
          
        </div>
      </div>
    </section>

    '''

final_html = html[:start_idx] + new_html + html[end_idx:]
open("index.html", "w", encoding="utf-8").write(final_html)
print("Updated index.html")

# 2. Update style.css
css = open("style.css", "r", encoding="utf-8").read()

start_css = css.find('.principals-masonry {')
end_css = css.find('.philosophy-parallax {')

new_css = '''
/* Global Giants Redesign */
.principals-masonry {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 4rem;
}

@media (max-width: 991px) {
  .principals-masonry {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .principals-masonry {
    grid-template-columns: 1fr;
  }
}

.principal-tile {
  position: relative;
  height: 360px;
  background-color: #ffffff;
  border: 1px solid rgba(0,0,0,0.05);
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
  transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
  padding: 2.5rem;
  box-sizing: border-box;
}

.principal-tile:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}

/* Hover Sweep Interaction */
.principal-tile-hover-sweep {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(135deg, rgba(226,49,55,0.0) 0%, rgba(226,49,55,0.03) 100%);
  opacity: 0;
  transition: opacity 0.5s ease;
  z-index: 0;
  pointer-events: none;
}

.principal-tile:hover .principal-tile-hover-sweep {
  opacity: 1;
}

/* SVG Blueprint Pattern */
.principal-tile-pattern {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: linear-gradient(rgba(226,49,55,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(226,49,55,0.1) 1px, transparent 1px);
  background-size: 20px 20px;
  opacity: 0;
  transition: opacity 0.5s ease, transform 0.8s ease;
  transform: scale(1.1);
  z-index: 1;
  pointer-events: none;
}

.principal-tile:hover .principal-tile-pattern {
  opacity: 0.3;
  transform: scale(1);
}

.principal-tile-content {
  position: relative;
  z-index: 2;
  text-align: center;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Logos */
.principal-tile-logo {
  height: 50px;
  margin-bottom: 2rem;
  object-fit: contain;
  transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
  filter: grayscale(20%);
}

.principal-text-logo {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 2rem;
  height: 50px;
  display: flex;
  align-items: center;
  transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.principal-tile:hover .principal-tile-logo,
.principal-tile:hover .principal-text-logo {
  transform: scale(1.03);
  filter: grayscale(0%);
}

/* Country Name */
.principal-tile .country-name {
  font-size: 1.1rem;
  text-transform: uppercase;
  letter-spacing: 3px;
  font-weight: 600;
  color: #222;
  margin-bottom: 1.5rem;
  position: relative;
  display: inline-block;
  transition: color 0.3s ease;
}

/* Animated Red Underline */
.principal-tile .country-name::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background-color: var(--color-brand-red);
  transition: width 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.principal-tile:hover .country-name::after {
  width: 40px;
}
.principal-tile:hover .country-name {
  color: var(--color-brand-red);
}

/* Description */
.principal-tile .desc {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #666;
  max-width: 90%;
  margin: 0 auto;
  transition: color 0.4s ease;
}

/* Corner Marks */
.corner-mark {
  position: absolute;
  width: 15px;
  height: 15px;
  border: 1.5px solid rgba(226,49,55, 0.3);
  opacity: 0;
  transition: opacity 0.4s ease, transform 0.4s ease;
  z-index: 3;
}
.corner-mark.top-left {
  top: 15px;
  left: 15px;
  border-right: none;
  border-bottom: none;
  transform: translate(-5px, -5px);
}
.corner-mark.bottom-right {
  bottom: 15px;
  right: 15px;
  border-left: none;
  border-top: none;
  transform: translate(5px, 5px);
}

.principal-tile:hover .corner-mark {
  opacity: 1;
  transform: translate(0, 0);
}
'''

final_css = css[:start_css] + new_css + css[end_css:]
open("style.css", "w", encoding="utf-8").write(final_css)
print("Updated style.css")
