import re

# Read index.html
content = open('index.html', 'r', encoding='utf-8').read()

# Locate map SVG
map_start = content.find('<!-- Realistic Detailed World Map SVG -->')
svg_end = content.find('</svg>', map_start) + 6
map_content = content[map_start:svg_end]

# 1. Update Map Styling
# Currently: fill="rgba(226,49,55,0.05)" stroke="var(--color-brand-red)" stroke-width="2"
new_map_content = map_content.replace('fill="rgba(226,49,55,0.05)"', 'fill="#f0f0f5"')
new_map_content = new_map_content.replace('stroke="var(--color-brand-red)"', 'stroke="#d0d0d8"')
new_map_content = new_map_content.replace('stroke-width="2"', 'stroke-width="1.5"')
new_map_content = new_map_content.replace('rgba(226,49,55,0.15)', 'rgba(0,0,0,0.08)') # softer shadow

# 2. Rebuild Markers and Routes
# We will inject definitions and routes right after the long <path> element.
path_end = new_map_content.find('</path>') + 7

defs_and_routes = '''
    <!-- Clip Paths for Circular Flags -->
    <defs>
        <clipPath id="circle-clip-de"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-ch"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-cn"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-jp"><circle cx="0" cy="-35" r="18" /></clipPath>
    </defs>

    <!-- Animated Trade Routes to India (3000, 1100) -->
    <g class="trade-routes">
        <!-- Germany to India -->
        <path d="M 2100 420 Q 2600 300 3000 1100" fill="none" stroke="var(--color-brand-red)" stroke-width="6" stroke-dasharray="20 20" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="40" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- Switzerland to India -->
        <path d="M 2050 470 Q 2500 400 3000 1100" fill="none" stroke="var(--color-brand-red)" stroke-width="6" stroke-dasharray="20 20" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="40" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- China to India -->
        <path d="M 3580 840 Q 3300 700 3000 1100" fill="none" stroke="var(--color-brand-red)" stroke-width="6" stroke-dasharray="20 20" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="40" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- Japan to India -->
        <path d="M 3800 740 Q 3400 600 3000 1100" fill="none" stroke="var(--color-brand-red)" stroke-width="6" stroke-dasharray="20 20" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="40" to="0" dur="1s" repeatCount="indefinite" />
        </path>
    </g>

    <!-- India HQ Destination Marker -->
    <g class="map-marker-group" transform="translate(3000, 1100)">
        <circle cx="0" cy="0" r="15" fill="var(--color-brand-red)" />
        <circle cx="0" cy="0" r="40" fill="none" stroke="var(--color-brand-red)" stroke-width="4">
            <animate attributeName="r" values="20; 60; 20" dur="2.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0.8; 0; 0.8" dur="2.5s" repeatCount="indefinite" />
        </circle>
        <circle cx="0" cy="0" r="80" fill="none" stroke="var(--color-brand-red)" stroke-width="2">
            <animate attributeName="r" values="60; 120; 60" dur="2.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0.4; 0; 0.4" dur="2.5s" repeatCount="indefinite" />
        </circle>
        <text x="0" y="70" fill="var(--color-brand-red)" font-size="40" font-family="Inter, sans-serif" font-weight="800" text-anchor="middle">India HQ</text>
    </g>

    <!-- Refined Partner Markers -->
    <g class="map-marker-group" transform="translate(2100, 420)">
        <!-- Elegant connecting line -->
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="10" fill="var(--color-brand-red)" />
        <!-- Circular Flag Avatar -->
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/de.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-de)" />
        <text x="35" y="-25" fill="#333333" font-size="32" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Schattdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(2050, 470)">
        <line x1="0" y1="0" x2="-45" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="10" fill="var(--color-brand-red)" />
        <circle cx="-45" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/ch.png" x="-65" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-ch)" />
        <text x="-75" y="-25" fill="#333333" font-size="32" font-family="Inter, sans-serif" font-weight="700" text-anchor="end">Arcolor</text>
    </g>
    <g class="map-marker-group" transform="translate(3580, 840)">
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="10" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/cn.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-cn)" />
        <text x="35" y="-25" fill="#333333" font-size="32" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Kingdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(3800, 740)">
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="10" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/jp.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-jp)" />
        <text x="35" y="-25" fill="#333333" font-size="32" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Mitsubishi</text>
    </g>
'''

# Replace everything after the path with our new defs and markers
new_map_content = new_map_content[:path_end] + defs_and_routes + "\n</svg>"

final_content = content[:map_start] + new_map_content + content[svg_end:]

open('index.html', 'w', encoding='utf-8').write(final_content)
print("Updated World Map to premium visualization!")
