import re

with open('about-us.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the style block
style_start = content.find('/* ========== S-CURVE CONTINUOUS PATH ========== */')
style_end = content.find('  </style>', style_start)

new_styles = """/* ========== VERTICAL SVG TIMELINE ========== */
    .timeline-container {
      position: relative;
      max-width: 1000px;
      margin: 4rem auto 8rem auto;
      padding: 2rem 0;
    }
    
    .timeline-svg-bg {
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 100px;
      height: 100%;
      z-index: -1;
    }
    
    .timeline-row {
      position: relative;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6rem;
      width: 100%;
    }
    .timeline-row:last-child {
      margin-bottom: 0;
    }
    
    .timeline-content-left, .timeline-content-right {
      width: 45%;
    }
    
    .timeline-content-left {
      text-align: right;
      padding-right: 3rem;
    }
    .timeline-content-right {
      text-align: left;
      padding-left: 3rem;
    }
    
    .timeline-node {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 24px;
      height: 24px;
      background-color: var(--color-brand-red);
      border: 4px solid #fff;
      border-radius: 50%;
      z-index: 10;
      box-shadow: 0 0 10px rgba(226,49,55,0.4);
    }
    
    .path-title {
      font-family: 'Inter', sans-serif; 
      font-weight: 600; 
      text-transform: uppercase; 
      letter-spacing: 2px; 
      color: var(--color-brand-red); 
      margin-bottom: 1rem;
    }
    
    @media (max-width: 768px) {
      .timeline-svg-bg {
        left: 20px;
        transform: none;
      }
      .timeline-row {
        flex-direction: column;
        align-items: flex-start;
      }
      .timeline-content-left, .timeline-content-right {
        width: 100%;
        text-align: left;
        padding-left: 60px;
        padding-right: 0;
      }
      .timeline-content-left {
        margin-bottom: 2rem;
      }
      .timeline-node {
        left: 20px;
        top: 20px;
        transform: translateX(-50%);
      }
    }"""

content = content[:style_start] + new_styles + "\n" + content[style_end:]

# Replace the HTML container
html_start = content.find('<!-- S-CURVE MASTER CONTAINER -->')
html_end = content.find('</div> <!-- End S-Curve Container -->') + 37

new_html = """<!-- VERTICAL SVG TIMELINE CONTAINER -->
  <div class="timeline-container" id="the-journey">
    
    <!-- Background SVG animated line -->
    <svg class="timeline-svg-bg svg-draw" preserveAspectRatio="none" viewBox="0 0 100 1000" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- A thick vertical line that draws itself from top to bottom -->
      <path d="M 50 0 L 50 1000" stroke="var(--color-brand-red)" stroke-width="4" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
    </svg>

    <!-- NODE 1 -->
    <div class="timeline-row reveal">
      <div class="timeline-node pulse-node"></div>
      <div class="timeline-content-left">
        <h2 class="editorial-heading" style="font-size: 3rem;">A Legacy of Excellence</h2>
        <p style="font-size: 1.1rem; line-height: 2; color: var(--color-text-light);">At Shah International, it has always been our endeavor to be a world-class service oriented company and provide an excellent service to our principals and customers.</p>
      </div>
      <div class="timeline-content-right">
        <div class="image-grid image-grid-2">
          <img src="themes/agatha/img/gallery/1.jpg" alt="Shah International office" class="story-img">
          <img src="themes/agatha/img/gallery/4.jpg" alt="Shah International team" class="story-img">
        </div>
      </div>
    </div>

    <!-- NODE 2 -->
    <div class="timeline-row reveal">
      <div class="timeline-node pulse-node"></div>
      <div class="timeline-content-left">
        <div style="background: var(--color-bg); padding: 2rem; border-right: 2px solid var(--color-brand-red); box-shadow: var(--shadow-sm); margin-bottom: 2rem;">
          <h4 class="path-title">Our Vision</h4>
          <p style="color: var(--color-text-light); line-height: 1.8;">To be a leading Indenting house providing high quality service to our valued customers and esteemed principals in the laminate and wood based panel industry.</p>
        </div>
        <div style="background: var(--color-bg); padding: 2rem; border-right: 2px solid var(--color-brand-red); box-shadow: var(--shadow-sm);">
          <h4 class="path-title">Our Mission</h4>
          <p style="color: var(--color-text-light); line-height: 1.8;">To maximize customer satisfaction and our principals value through best management practices and continually striving for excellence in the services we provide.</p>
        </div>
      </div>
      <div class="timeline-content-right">
        <h3 class="editorial-heading" style="font-size: 2.5rem;">Our Vision & Mission</h3>
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke="var(--color-brand-red)" stroke-width="3" style="width: 80px; margin-top: 2rem;">
          <circle cx="50" cy="50" r="40" />
          <circle cx="50" cy="50" r="25" />
          <circle cx="50" cy="50" r="10" />
          <path d="M 50 10 L 50 0 M 50 90 L 50 100 M 10 50 L 0 50 M 90 50 L 100 50" />
        </svg>
      </div>
    </div>

    <!-- NODE 3 -->
    <div class="timeline-row reveal">
      <div class="timeline-node pulse-node"></div>
      <div class="timeline-content-left">
        <h3 class="editorial-heading" style="font-size: 2.5rem;">Together we grow</h3>
        <p style="margin-bottom: 1.5rem; color: var(--color-text-light); line-height: 1.9;">We feel proud to share with you that we have completed more than 25 years in the industry. The company was founded by the grand vision of Mr. Kirti Shah in 1993.</p>
      </div>
      <div class="timeline-content-right">
        <img src="themes/agatha/img/gallery/8-1.jpg" alt="Shah International exhibition" class="story-img" style="max-height: 300px;">
      </div>
    </div>

    <!-- NODE 4 (Final summary) -->
    <div class="timeline-row reveal">
      <div class="timeline-node pulse-node"></div>
      <div class="timeline-content-left">
        <div style="display: flex; gap: 2rem; flex-wrap: wrap; justify-content: flex-end;">
          <div style="text-align: right;">
            <h4 class="path-title">1993</h4>
            <p style="color: var(--color-text-light);">Founded</p>
          </div>
          <div style="text-align: right;">
            <h4 class="path-title">2005</h4>
            <p style="color: var(--color-text-light);">Expansion</p>
          </div>
          <div style="text-align: right;">
            <h4 class="path-title">Today</h4>
            <p style="color: var(--color-text-light);">Next Gen</p>
          </div>
        </div>
      </div>
      <div class="timeline-content-right">
        <h3 class="editorial-heading" style="font-size: 2.5rem;">Values of Integration</h3>
        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--color-text-light);">At Shah International, we have fostered a culture of complete integration, honesty and teamwork. For us, these are not just words that form our vision statement. These are values and ways of life that we adhere to.</p>
      </div>
    </div>

  </div> <!-- End Timeline Container -->"""

new_content = content[:html_start] + new_html + content[html_end:]

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated about-us.html successfully.")
