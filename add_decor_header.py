import re

with open('decor-applications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert the new header just inside the container of the editorial-container section
insertion_point = content.find('<div class="container">', content.find('<section class="editorial-container">')) + len('<div class="container">')

header_html = """
      <div class="text-center reveal" style="margin-bottom: 5rem; padding-top: 2rem;">
        
        <!-- Animated Decor Grid SVG -->
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Frame -->
          <rect x="15" y="15" width="70" height="70" rx="8" stroke="var(--color-brand-red)" />
          <!-- Inner Divisions to represent panels/applications -->
          <path d="M 50 15 L 50 85" stroke="var(--color-brand-red)" />
          <path d="M 50 50 L 85 50" stroke="var(--color-brand-red)" />
          <!-- Small animated accent circle in one of the panels -->
          <circle cx="67.5" cy="32.5" r="4" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="transform-origin: 67.5px 32.5px; animation-duration: 3s;" />
        </svg>

        <h2 style="font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 400; margin-bottom: 1rem; color: #111;">Inspiring Applications</h2>
        <p style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: #555; max-width: 600px; margin: 0 auto;">Discover how our premium decor papers transform surfaces and elevate interior spaces across a variety of applications.</p>
      </div>
"""

new_content = content[:insertion_point] + header_html + content[insertion_point:]

with open('decor-applications.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added animated header to Decor Applications.")
