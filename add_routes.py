import re

with open('distribution.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<svg class="svg-draw"')
if start_idx == -1:
    print("Could not find svg in distribution.html")
    exit(1)

end_idx = content.find('</svg>', start_idx)

routes = """
  <!-- Logistics Routes (Animated Flow) -->
  <g stroke="var(--color-brand-red)" stroke-width="2" fill="none" class="svg-flow" stroke-dasharray="10 10">
    <!-- Mumbai to Delhi -->
    <path d="M 155 365 Q 180 250, 210 180" opacity="0.6"/>
    <!-- Mumbai to Kolkata -->
    <path d="M 155 365 Q 300 350, 480 300" opacity="0.6"/>
    <!-- Mumbai to Bangalore -->
    <path d="M 155 365 Q 200 450, 210 500" opacity="0.6"/>
    <!-- Mumbai to Ahmedabad -->
    <path d="M 155 365 Q 150 300, 130 280" opacity="0.6"/>
    <!-- Mumbai to Chennai -->
    <path d="M 155 365 Q 250 450, 260 480" opacity="0.6"/>
  </g>
  <!-- City Nodes -->
  <g fill="var(--color-brand-red)">
    <!-- Mumbai (HQ) -->
    <circle cx="155" cy="365" r="8" class="pulse-node" style="transform-origin: 155px 365px;" />
    <circle cx="155" cy="365" r="4" />
    <text x="140" y="370" font-family="Inter, sans-serif" font-size="12" text-anchor="end" font-weight="bold">Mumbai</text>
    
    <!-- Delhi -->
    <circle cx="210" cy="180" r="3" />
    <!-- Kolkata -->
    <circle cx="480" cy="300" r="3" />
    <!-- Bangalore -->
    <circle cx="210" cy="500" r="3" />
    <!-- Ahmedabad -->
    <circle cx="130" cy="280" r="3" />
    <!-- Chennai -->
    <circle cx="260" cy="480" r="3" />
  </g>
"""

new_content = content[:end_idx] + routes + content[end_idx:]

with open('distribution.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added logistics routes successfully.")
