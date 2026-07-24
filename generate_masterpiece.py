import math

scale = 13
ox = 250 # Origin X
oy = 380 # Origin Y
svg_paths = []

def pt(x, y, z):
    cx = ox + (x - y) * math.cos(math.pi/6) * scale
    cy = oy + (x + y) * math.sin(math.pi/6) * scale - z * scale
    return cx, cy

def add_path(pts, close=False, stroke_width=1, opacity=0.8, dash=""):
    coords = []
    for i, p in enumerate(pts):
        cmd = "M" if i == 0 else "L"
        cx, cy = pt(*p)
        coords.append(f"{cmd} {cx:.1f} {cy:.1f}")
    if close:
        coords.append("Z")
    d = " ".join(coords)
    style = f'stroke-width="{stroke_width}" opacity="{opacity}"'
    if dash:
        style += f' stroke-dasharray="{dash}"'
    svg_paths.append(f'    <path d="{d}" {style} />')

# Base Grid (Laminate Flooring)
for i in range(13):
    add_path([(i*2, 0, 0), (i*2, 24, 0)], stroke_width=0.4, opacity=0.3, dash="2 4")
    add_path([(0, i*2, 0), (24, i*2, 0)], stroke_width=0.4, opacity=0.3, dash="2 4")

# Left Wall Panels (Vertical wood slats)
for i in range(12):
    add_path([(0, i*2, 0), (0, i*2, 16)], stroke_width=0.6, opacity=0.4)
add_path([(0,0,16), (0,24,16), (0,24,0)], stroke_width=1.5, opacity=0.9)

# Right Wall
add_path([(0,0,16), (24,0,16), (24,0,0)], stroke_width=1.5, opacity=0.9)

# Right wall abstract shapes (Shelves/Art)
add_path([(6, 0, 8), (14, 0, 8), (14, 0, 9), (6, 0, 9)], close=True, stroke_width=1)
add_path([(8, 0, 11), (16, 0, 11), (16, 0, 12), (8, 0, 12)], close=True, stroke_width=1)

# Stack of Laminate sheets on the floor
stack_x, stack_y = 16, 16
for i in range(6):
    z = i * 0.5
    add_path([
        (stack_x, stack_y, z), (stack_x+6, stack_y, z),
        (stack_x+6, stack_y+6, z), (stack_x, stack_y+6, z)
    ], close=True, stroke_width=0.8, opacity=0.8)
    if i < 5:
        add_path([(stack_x, stack_y+6, z), (stack_x, stack_y+6, z+0.5)], stroke_width=0.5)
        add_path([(stack_x+6, stack_y+6, z), (stack_x+6, stack_y+6, z+0.5)], stroke_width=0.5)

# Modern Sofa
sofa_x, sofa_y = 4, 4
sw, sd, sh = 10, 5, 3  # width, depth, seat height
bh = 7 # backrest height
# Base
add_path([
    (sofa_x, sofa_y, 0), (sofa_x+sw, sofa_y, 0),
    (sofa_x+sw, sofa_y+sd, 0), (sofa_x, sofa_y+sd, 0)
], close=True, stroke_width=1)
# Seat cushion
add_path([
    (sofa_x, sofa_y, sh), (sofa_x+sw, sofa_y, sh),
    (sofa_x+sw, sofa_y+sd, sh), (sofa_x, sofa_y+sd, sh)
], close=True, stroke_width=1.2)
# Front vertical lines
add_path([(sofa_x, sofa_y+sd, 0), (sofa_x, sofa_y+sd, sh)])
add_path([(sofa_x+sw, sofa_y+sd, 0), (sofa_x+sw, sofa_y+sd, sh)])
# Backrest
add_path([
    (sofa_x, sofa_y, sh), (sofa_x+sw, sofa_y, sh),
    (sofa_x+sw, sofa_y+1, sh), (sofa_x, sofa_y+1, sh)
], close=True, stroke_width=1)
add_path([
    (sofa_x, sofa_y, bh), (sofa_x+sw, sofa_y, bh),
    (sofa_x+sw, sofa_y+1, bh), (sofa_x, sofa_y+1, bh)
], close=True, stroke_width=1.2)
add_path([(sofa_x, sofa_y+1, sh), (sofa_x, sofa_y+1, bh)])
add_path([(sofa_x+sw, sofa_y+1, sh), (sofa_x+sw, sofa_y+1, bh)])
add_path([(sofa_x, sofa_y, sh), (sofa_x, sofa_y, bh)])
add_path([(sofa_x+sw, sofa_y, sh), (sofa_x+sw, sofa_y, bh)])

# Armrests
add_path([
    (sofa_x, sofa_y+1, sh), (sofa_x+1, sofa_y+1, sh),
    (sofa_x+1, sofa_y+sd, sh), (sofa_x, sofa_y+sd, sh)
], close=True, stroke_width=1)
add_path([
    (sofa_x, sofa_y+1, bh-1), (sofa_x+1, sofa_y+1, bh-1),
    (sofa_x+1, sofa_y+sd, bh-1), (sofa_x, sofa_y+sd, bh-1)
], close=True, stroke_width=1.2)
add_path([(sofa_x+1, sofa_y+sd, sh), (sofa_x+1, sofa_y+sd, bh-1)])
add_path([(sofa_x, sofa_y+sd, sh), (sofa_x, sofa_y+sd, bh-1)])
add_path([(sofa_x, sofa_y+1, sh), (sofa_x, sofa_y+1, bh-1)])

add_path([
    (sofa_x+sw-1, sofa_y+1, sh), (sofa_x+sw, sofa_y+1, sh),
    (sofa_x+sw, sofa_y+sd, sh), (sofa_x+sw-1, sofa_y+sd, sh)
], close=True, stroke_width=1)
add_path([
    (sofa_x+sw-1, sofa_y+1, bh-1), (sofa_x+sw, sofa_y+1, bh-1),
    (sofa_x+sw, sofa_y+sd, bh-1), (sofa_x+sw-1, sofa_y+sd, bh-1)
], close=True, stroke_width=1.2)
add_path([(sofa_x+sw-1, sofa_y+sd, sh), (sofa_x+sw-1, sofa_y+sd, bh-1)])
add_path([(sofa_x+sw, sofa_y+sd, sh), (sofa_x+sw, sofa_y+sd, bh-1)])
add_path([(sofa_x+sw, sofa_y+1, sh), (sofa_x+sw, sofa_y+1, bh-1)])

# Coffee Table
tx, ty = 7, 12
add_path([
    (tx, ty, 0), (tx+5, ty, 0), (tx+5, ty+3, 0), (tx, ty+3, 0)
], close=True, stroke_width=0.5, opacity=0.3, dash="2 2")
add_path([
    (tx, ty, 2), (tx+5, ty, 2), (tx+5, ty+3, 2), (tx, ty+3, 2)
], close=True, stroke_width=1.2)
add_path([(tx, ty+3, 0), (tx, ty+3, 2)])
add_path([(tx+5, ty+3, 0), (tx+5, ty+3, 2)])
add_path([(tx+5, ty, 0), (tx+5, ty, 2)])

# Floating Laminate Panels (Artistic representation of architecture)
for i in range(3):
    z = 5 + i * 2.5
    add_path([
        (tx-2+i, ty-2, z), (tx+4+i, ty-2, z),
        (tx+4+i, ty+3, z), (tx-2+i, ty+3, z)
    ], close=True, stroke_width=1.5, opacity=0.9)
    # Dotted connection lines
    if i > 0:
        add_path([(tx-2+i, ty-2, z), (tx-2+i-1, ty-2, z-2.5)], stroke_width=0.5, dash="2 4", opacity=0.6)
        add_path([(tx+4+i, ty+3, z), (tx+4+i-1, ty+3, z-2.5)], stroke_width=0.5, dash="2 4", opacity=0.6)

# Construct final SVG
new_svg = f'''<svg class="philosophy-draw" viewBox="0 0 500 500" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 450px; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2)); margin: 0 auto;">
{"\n".join(svg_paths)}
</svg>'''

content = open("index.html", "r", encoding="utf-8").read()
start_marker = '<div class="philosophy-svg-container'
start_idx = content.find(start_marker)
svg_start_idx = content.find('<svg class="philosophy-draw"', start_idx)
svg_end_idx = content.find('</svg>', svg_start_idx) + 6

final_content = content[:svg_start_idx] + new_svg + content[svg_end_idx:]

open("index.html", "w", encoding="utf-8").write(final_content)
print("Updated graphic to incredible isometric art!")
