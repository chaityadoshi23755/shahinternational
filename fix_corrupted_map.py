import urllib.request
import re

url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
svg_data = response.read().decode('utf-8')

# Extract paths
paths = re.findall(r'<path[^>]*d="([^"]+)"', svg_data)

new_svg = f'''<div class="reveal reveal-delay-2" style="position: relative; max-width: 1000px; margin: 0 auto 3rem auto; padding: 2rem 0;">
            <!-- Realistic Detailed World Map SVG -->
            <svg class="svg-draw" viewBox="0 0 2754 1398" fill="#f0f0f5" stroke="#d0d0d8" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" style="width: 100%; height: auto; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.08));">'''

for p in paths:
    new_svg += f'\n<path d="{p}" opacity="0.8" />'

# Define markers scaled to the 2754x1398 viewBox. 
# Previously:
# India HQ: (3000, 1100) -> 3000 / 4378 * 2754 = 1887. 1100 / 2434 * 1398 = 631
# DE: (2100, 420) -> 2100 / 4378 * 2754 = 1321. 420 / 2434 * 1398 = 241
# CH: (2050, 470) -> 2050 / 4378 * 2754 = 1289. 470 / 2434 * 1398 = 270
# CN: (3580, 840) -> 3580 / 4378 * 2754 = 2252. 840 / 2434 * 1398 = 482
# JP: (3800, 740) -> 3800 / 4378 * 2754 = 2390. 740 / 2434 * 1398 = 425

new_svg += '''
    <!-- Clip Paths for Circular Flags -->
    <defs>
        <clipPath id="circle-clip-de"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-ch"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-cn"><circle cx="0" cy="-35" r="18" /></clipPath>
        <clipPath id="circle-clip-jp"><circle cx="0" cy="-35" r="18" /></clipPath>
    </defs>

    <!-- Animated Trade Routes to India (1887, 631) -->
    <g class="trade-routes">
        <!-- Germany (1321, 241) to India -->
        <path d="M 1321 241 Q 1600 150 1887 631" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-dasharray="15 15" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- Switzerland (1289, 270) to India -->
        <path d="M 1289 270 Q 1550 200 1887 631" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-dasharray="15 15" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- China (2252, 482) to India -->
        <path d="M 2252 482 Q 2050 400 1887 631" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-dasharray="15 15" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite" />
        </path>
        <!-- Japan (2390, 425) to India -->
        <path d="M 2390 425 Q 2150 350 1887 631" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-dasharray="15 15" opacity="0.5">
            <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite" />
        </path>
    </g>

    <!-- India HQ Destination Marker -->
    <g class="map-marker-group" transform="translate(1887, 631)">
        <circle cx="0" cy="0" r="10" fill="var(--color-brand-red)" />
        <circle cx="0" cy="0" r="25" fill="none" stroke="var(--color-brand-red)" stroke-width="3">
            <animate attributeName="r" values="15; 45; 15" dur="2.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0.8; 0; 0.8" dur="2.5s" repeatCount="indefinite" />
        </circle>
        <circle cx="0" cy="0" r="50" fill="none" stroke="var(--color-brand-red)" stroke-width="1.5">
            <animate attributeName="r" values="45; 90; 45" dur="2.5s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0.4; 0; 0.4" dur="2.5s" repeatCount="indefinite" />
        </circle>
        <text x="0" y="45" fill="var(--color-brand-red)" font-size="28" font-family="Inter, sans-serif" font-weight="800" text-anchor="middle">India HQ</text>
    </g>

    <!-- Refined Partner Markers -->
    <g class="map-marker-group" transform="translate(1321, 241)">
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="7" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/de.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-de)" />
        <text x="35" y="-25" fill="#333333" font-size="24" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Schattdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(1289, 270)">
        <line x1="0" y1="0" x2="-45" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="7" fill="var(--color-brand-red)" />
        <circle cx="-45" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/ch.png" x="-65" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-ch)" />
        <text x="-75" y="-25" fill="#333333" font-size="24" font-family="Inter, sans-serif" font-weight="700" text-anchor="end">Arcolor</text>
    </g>
    <g class="map-marker-group" transform="translate(2252, 482)">
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="7" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/cn.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-cn)" />
        <text x="35" y="-25" fill="#333333" font-size="24" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Kingdecor</text>
    </g>
    <g class="map-marker-group" transform="translate(2390, 425)">
        <line x1="0" y1="0" x2="0" y2="-35" stroke="var(--color-brand-red)" stroke-width="2" />
        <circle cx="0" cy="0" r="7" fill="var(--color-brand-red)" />
        <circle cx="0" cy="-35" r="20" fill="#ffffff" filter="drop-shadow(0 5px 10px rgba(0,0,0,0.15))" />
        <image href="https://flagcdn.com/w40/jp.png" x="-20" y="-55" width="40" height="40" preserveAspectRatio="xMidYMid slice" clip-path="url(#circle-clip-jp)" />
        <text x="35" y="-25" fill="#333333" font-size="24" font-family="Inter, sans-serif" font-weight="700" text-anchor="start">Mitsubishi</text>
    </g>
</svg>
</div>'''

html_content = open("index.html", "r", encoding="utf-8", errors="ignore").read()

start_marker = '<!-- World Map with Partner Markers -->'
end_marker = '</svg>'

start_idx = html_content.find(start_marker)
# We need to find the </svg> that belongs to this map.
# But there is a broken map currently, let's find the </div> that closes it.
# It ends right before: <div style="text-align: center;" class="reveal reveal-delay-3">
end_marker2 = '<div style="text-align: center;" class="reveal reveal-delay-3">'
end_idx = html_content.find(end_marker2, start_idx)

final_html = html_content[:start_idx] + start_marker + "\n        " + new_svg + "\n        \n        " + html_content[end_idx:]

open("index.html", "w", encoding="utf-8").write(final_html)
print("Restored the Map successfully!")
