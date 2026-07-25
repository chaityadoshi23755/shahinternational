import re

with open('footer.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<footer class="site-footer"')
if start_idx == -1:
    print("Could not find footer element")
    exit(1)

container_idx = content.find('<div class="container"', start_idx)

bg_svg = """
  <!-- Premium Subtle Blueprint SVG Background -->
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; opacity: 0.05; pointer-events: none; overflow: hidden;">
    <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="blueprint-grid" width="40" height="40" patternUnits="userSpaceOnUse">
          <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-width="0.5"/>
        </pattern>
        <pattern id="blueprint-grid-large" width="200" height="200" patternUnits="userSpaceOnUse">
          <rect width="200" height="200" fill="url(#blueprint-grid)" />
          <path d="M 200 0 L 0 0 0 200" fill="none" stroke="#ffffff" stroke-width="1.5"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#blueprint-grid-large)" />
      
      <!-- Subtle architectural contour lines in the bottom right -->
      <path class="svg-draw" d="M 80% 60% C 85% 70%, 95% 65%, 100% 80%" fill="none" stroke="#ffffff" stroke-width="2" />
      <path class="svg-draw" d="M 78% 63% C 83% 73%, 93% 68%, 100% 83%" fill="none" stroke="#ffffff" stroke-width="1" />
      <path class="svg-draw" d="M 76% 66% C 81% 76%, 91% 71%, 100% 86%" fill="none" stroke="#ffffff" stroke-width="0.5" />
    </svg>
  </div>
"""

# Make footer relative
content = content[:start_idx] + content[start_idx:container_idx].replace('class="site-footer"', 'class="site-footer" style="position: relative;"') + content[container_idx:]

container_idx = content.find('<div class="container"', start_idx)
new_content = content[:container_idx] + bg_svg + content[container_idx:]

# Make the container relative and z-index 1 to stay above the bg
new_content = new_content.replace('<div class="container">', '<div class="container" style="position: relative; z-index: 1;">', 1)

with open('footer.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added SVG background pattern to footer.")
