import re

content = open("index.html", "r", encoding="utf-8").read()

new_svg = """<svg class="philosophy-draw" viewBox="0 0 100 100" fill="none" stroke="#ffffff" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 350px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.15)); margin: 0 auto;">
    
    <!-- Decorative connecting elements (Blueprint style) -->
    <line x1="50" y1="25" x2="80" y2="25" stroke-dasharray="2 2" stroke-width="0.4" opacity="0.6" />
    <circle cx="80" cy="25" r="1" fill="#ffffff" stroke="none">
        <animate attributeName="opacity" values="0.2; 1; 0.2" dur="3s" repeatCount="indefinite" />
    </circle>
    
    <line x1="20" y1="75" x2="45" y2="75" stroke-dasharray="2 2" stroke-width="0.4" opacity="0.6" />
    <circle cx="20" cy="75" r="1" fill="#ffffff" stroke="none">
        <animate attributeName="opacity" values="0.2; 1; 0.2" dur="3s" repeatCount="indefinite" />
    </circle>
    
    <!-- Laminates (Layers) -->
    <g transform="translate(10, 15) scale(1.5)">
        <polygon points="12 2 2 7 12 12 22 7 12 2" />
        <polyline points="2 12 12 17 22 12" />
        <polyline points="2 17 12 22 22 17" />
    </g>
    
    <!-- Furniture (Sofa) -->
    <g transform="translate(45, 45) scale(1.5)">
        <path d="M20 9V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v3" />
        <path d="M2 11v5a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-5a2 2 0 0 0-4 0v2H6v-2a2 2 0 0 0-4 0Z" />
        <path d="M4 18v2" />
        <path d="M20 18v2" />
        <path d="M12 4v9" />
    </g>
</svg>"""

start_marker = '<div class="philosophy-svg-container'
start_idx = content.find(start_marker)
svg_start_idx = content.find('<svg class="philosophy-draw"', start_idx)
svg_end_idx = content.find('</svg>', svg_start_idx) + 6

final_content = content[:svg_start_idx] + new_svg + content[svg_end_idx:]

open("index.html", "w", encoding="utf-8").write(final_content)
print("Successfully replaced the graphic in Our Philosophy section!")
