import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The container starts with <div class="philosophy-svg-container
start_idx = content.find('<div class="philosophy-svg-container')
if start_idx == -1:
    print("Could not find philosophy container")
    exit(1)

svg_end = content.find('</svg>', start_idx)
end_idx = content.find('</div>', svg_end) + 6

new_svg = """<div class="philosophy-svg-container reveal reveal-delay-1" style="flex: 1; min-width: 300px; display: flex; justify-content: center; position: relative;">
  <svg class="svg-draw philosophy-network" viewBox="0 0 800 600" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 700px; display: block; margin: 0 auto; filter: drop-shadow(0 15px 35px rgba(0,0,0,0.2));">
    <defs>
      <linearGradient id="bridgeGrad1" x1="100" y1="150" x2="600" y2="300" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
      </linearGradient>
      <linearGradient id="bridgeGrad2" x1="100" y1="300" x2="600" y2="300" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
      </linearGradient>
      <linearGradient id="bridgeGrad3" x1="100" y1="450" x2="600" y2="300" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.2" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
      </linearGradient>
      <radialGradient id="nodeGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
        <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
      </radialGradient>
    </defs>
    
    <path class="svg-draw" d="M 150 150 C 350 150, 400 300, 600 300" stroke="url(#bridgeGrad1)" stroke-width="4" stroke-linecap="round"/>
    <path class="svg-draw" d="M 150 300 C 350 300, 400 300, 600 300" stroke="url(#bridgeGrad2)" stroke-width="4" stroke-linecap="round"/>
    <path class="svg-draw" d="M 150 450 C 350 450, 400 300, 600 300" stroke="url(#bridgeGrad3)" stroke-width="4" stroke-linecap="round"/>

    <path d="M 150 150 C 350 200, 400 450, 150 450" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1" stroke-dasharray="4 4" />
    <path d="M 150 150 L 150 300 L 150 450" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1" stroke-dasharray="4 4" />
    
    <circle cx="150" cy="150" r="15" fill="none" stroke="#ffffff" stroke-opacity="0.5" stroke-width="2"/>
    <circle cx="150" cy="150" r="4" fill="#ffffff" />
    <text x="120" y="155" fill="#ffffff" fill-opacity="0.6" font-family="Inter, sans-serif" font-size="12" text-anchor="end" letter-spacing="2">GERMANY</text>
    
    <circle cx="150" cy="300" r="20" fill="none" stroke="#ffffff" stroke-opacity="0.5" stroke-width="2"/>
    <circle cx="150" cy="300" r="6" fill="#ffffff" />
    <text x="110" y="305" fill="#ffffff" fill-opacity="0.6" font-family="Inter, sans-serif" font-size="12" text-anchor="end" letter-spacing="2">CHINA</text>
    
    <circle cx="150" cy="450" r="15" fill="none" stroke="#ffffff" stroke-opacity="0.5" stroke-width="2"/>
    <circle cx="150" cy="450" r="4" fill="#ffffff" />
    <text x="120" y="455" fill="#ffffff" fill-opacity="0.6" font-family="Inter, sans-serif" font-size="12" text-anchor="end" letter-spacing="2">AUSTRIA</text>

    <circle cx="600" cy="300" r="60" fill="none" stroke="#ffffff" stroke-opacity="0.1" stroke-width="1" class="pulse-node" style="transform-origin: 600px 300px;"/>
    <circle cx="600" cy="300" r="45" fill="none" stroke="#ffffff" stroke-opacity="0.3" stroke-width="2"/>
    <circle cx="600" cy="300" r="30" fill="url(#nodeGlow)"/>
    <circle cx="600" cy="300" r="10" fill="#ffffff" />
    <text x="600" y="390" fill="#ffffff" font-family="'Playfair Display', serif" font-size="20" text-anchor="middle" font-weight="600" letter-spacing="1">SHAH INTERNATIONAL</text>
  </svg>
</div>"""

new_content = content[:start_idx] + new_svg + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced Philosophy SVG successfully.")
