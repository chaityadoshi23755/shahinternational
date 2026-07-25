import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<svg class="world-map-svg"')
if start_idx == -1:
    print("Could not find world-map-svg")
    exit(1)

# Find the end of this svg
end_idx = content.find('</svg>', start_idx)

# India is roughly at x=3100, y=1100
# Germany is roughly at x=2300, y=600
# China is roughly at x=3400, y=900
# Austria is roughly at x=2350, y=650

routes = """
  <!-- Export Journey Trade Routes -->
  <g class="svg-flow" stroke-dasharray="20 20" opacity="0.8">
    <defs>
      <linearGradient id="tradeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
        <stop offset="100%" stop-color="var(--color-brand-red)" stop-opacity="1" />
      </linearGradient>
    </defs>
    
    <!-- India to Germany -->
    <path d="M 3100 1100 Q 2700 700, 2300 600" fill="none" stroke="var(--color-brand-red)" stroke-width="6" />
    
    <!-- India to China -->
    <path d="M 3100 1100 Q 3200 800, 3400 900" fill="none" stroke="var(--color-brand-red)" stroke-width="6" />
    
    <!-- India to Austria -->
    <path d="M 3100 1100 Q 2800 600, 2350 650" fill="none" stroke="var(--color-brand-red)" stroke-width="6" />
    
    <!-- India to Turkey -->
    <path d="M 3100 1100 Q 2800 800, 2550 750" fill="none" stroke="var(--color-brand-red)" stroke-width="6" />
  </g>
"""

new_content = content[:end_idx] + routes + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added trade routes to world map.")
