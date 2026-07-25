import re

with open('about-us.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a Factory SVG to Node 4 (Values of Integration) replacing the 1993/2005/Today text block
start_idx = content.find('<!-- NODE 4 (Final summary) -->')
end_idx = content.find('</div>', content.find('<div style="display: flex; gap: 2rem; flex-wrap: wrap; justify-content: flex-end;">', start_idx)) + 6

factory_svg = """<!-- Factory & Growth SVG -->
        <div style="text-align: right; margin-top: -2rem;">
          <svg class="svg-draw" viewBox="0 0 400 200" fill="none" stroke="var(--color-brand-red)" stroke-width="2" style="width: 100%; max-width: 300px;">
            <!-- Factory Base -->
            <path d="M 50 180 L 350 180" />
            <!-- Buildings -->
            <path d="M 80 180 L 80 100 L 140 60 L 140 180" stroke-linejoin="round" />
            <path d="M 140 120 L 200 80 L 200 180" stroke-linejoin="round" />
            <path d="M 200 140 L 280 90 L 280 180" stroke-linejoin="round" />
            <path d="M 280 110 L 320 110 L 320 180" stroke-linejoin="round" />
            <!-- Smoke stacks -->
            <path d="M 100 85 L 100 40" stroke-width="4" stroke-linecap="round"/>
            <path d="M 120 70 L 120 30" stroke-width="4" stroke-linecap="round"/>
            <path d="M 220 120 L 220 50" stroke-width="4" stroke-linecap="round"/>
            <!-- Smoke circles animating -->
            <circle cx="100" cy="20" r="5" class="pulse-node" style="transform-origin: 100px 20px;" fill="var(--color-brand-red)" stroke="none" />
            <circle cx="220" cy="30" r="8" class="pulse-node" style="transform-origin: 220px 30px;" fill="var(--color-brand-red)" stroke="none" />
            
            <!-- Growth Chart overlaid -->
            <path d="M 60 160 L 120 120 L 180 130 L 250 80 L 330 40" stroke="#111" stroke-width="3" stroke-dasharray="5 5" class="svg-flow" />
            <circle cx="330" cy="40" r="4" fill="#111" stroke="none" />
          </svg>
          <div style="display: flex; justify-content: flex-end; gap: 2rem; margin-top: 1rem;">
            <div style="text-align: right;"><h4 class="path-title">1993</h4><p style="color: var(--color-text-light);">Founded</p></div>
            <div style="text-align: right;"><h4 class="path-title">2005</h4><p style="color: var(--color-text-light);">Expansion</p></div>
            <div style="text-align: right;"><h4 class="path-title">Today</h4><p style="color: var(--color-text-light);">Next Gen</p></div>
          </div>
        </div>"""

new_content = content[:content.find('<div style="display: flex; gap: 2rem; flex-wrap: wrap; justify-content: flex-end;">', start_idx)] + factory_svg + content[end_idx:]

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Factory SVG to about-us.html")
