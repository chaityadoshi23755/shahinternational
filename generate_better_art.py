import math

scale = 14
ox = 250 # Origin X
oy = 380 # Origin Y
svg_paths = []
bg_color = "#e23137" # matches var(--color-brand-red)

def pt(x, y, z):
    cx = ox + (x - y) * math.cos(math.pi/6) * scale
    cy = oy + (x + y) * math.sin(math.pi/6) * scale - z * scale
    return cx, cy

def add_path(pts, close=False, stroke_width=1, opacity=0.8, dash="", fill="none"):
    coords = []
    for i, p in enumerate(pts):
        if type(p) is str:
            coords.append(p) # raw SVG command
        else:
            cmd = "M" if i == 0 else "L"
            cx, cy = pt(*p)
            coords.append(f"{cmd} {cx:.1f} {cy:.1f}")
    if close:
        coords.append("Z")
    d = " ".join(coords)
    style = f'stroke-width="{stroke_width}" opacity="{opacity}" fill="{fill}"'
    if dash:
        style += f' stroke-dasharray="{dash}"'
    svg_paths.append(f'    <path d="{d}" {style} />')

# Base Grid (Laminate Flooring) - Back layer
for i in range(12):
    add_path([(i*2, 0, 0), (i*2, 22, 0)], stroke_width=0.4, opacity=0.2, dash="2 4")
    add_path([(0, i*2, 0), (22, i*2, 0)], stroke_width=0.4, opacity=0.2, dash="2 4")

# Stack of Laminate sheets (Occluding)
stack_x, stack_y = 12, 12
for i in range(5):
    z = i * 0.6
    # Top face
    add_path([
        (stack_x, stack_y, z), (stack_x+8, stack_y, z),
        (stack_x+8, stack_y+8, z), (stack_x, stack_y+8, z)
    ], close=True, stroke_width=1.2, fill=bg_color, opacity=0.9)
    # Front-left face
    add_path([
        (stack_x, stack_y+8, z), (stack_x+8, stack_y+8, z),
        (stack_x+8, stack_y+8, z-0.6), (stack_x, stack_y+8, z-0.6)
    ], close=True, stroke_width=1.2, fill=bg_color, opacity=0.9)
    # Front-right face
    add_path([
        (stack_x+8, stack_y, z), (stack_x+8, stack_y+8, z),
        (stack_x+8, stack_y+8, z-0.6), (stack_x+8, stack_y, z-0.6)
    ], close=True, stroke_width=1.2, fill=bg_color, opacity=0.9)

# A sleek Modern Desk (Furniture) made from Laminate!
desk_x, desk_y = 2, 2
dw, dd, dh = 10, 6, 8
# Desk Top
add_path([
    (desk_x, desk_y, dh), (desk_x+dw, desk_y, dh),
    (desk_x+dw, desk_y+dd, dh), (desk_x, desk_y+dd, dh)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)
# Desk Front Face
add_path([
    (desk_x, desk_y+dd, dh), (desk_x+dw, desk_y+dd, dh),
    (desk_x+dw, desk_y+dd, dh-0.5), (desk_x, desk_y+dd, dh-0.5)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)
# Desk Right Face
add_path([
    (desk_x+dw, desk_y, dh), (desk_x+dw, desk_y+dd, dh),
    (desk_x+dw, desk_y+dd, dh-0.5), (desk_x+dw, desk_y, dh-0.5)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)

# Desk Left Leg (Solid panel)
add_path([
    (desk_x, desk_y, 0), (desk_x, desk_y+dd, 0),
    (desk_x, desk_y+dd, dh), (desk_x, desk_y, dh)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)
# Left leg thickness
add_path([
    (desk_x+0.5, desk_y, 0), (desk_x+0.5, desk_y+dd, 0),
    (desk_x+0.5, desk_y+dd, dh-0.5), (desk_x+0.5, desk_y, dh-0.5)
], close=True, stroke_width=1.2, fill=bg_color, opacity=1.0)
add_path([
    (desk_x, desk_y+dd, 0), (desk_x+0.5, desk_y+dd, 0),
    (desk_x+0.5, desk_y+dd, dh-0.5), (desk_x, desk_y+dd, dh-0.5)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)

# Desk Right Leg (Solid panel)
add_path([
    (desk_x+dw-0.5, desk_y, 0), (desk_x+dw-0.5, desk_y+dd, 0),
    (desk_x+dw-0.5, desk_y+dd, dh-0.5), (desk_x+dw-0.5, desk_y, dh-0.5)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)
add_path([
    (desk_x+dw, desk_y, 0), (desk_x+dw, desk_y+dd, 0),
    (desk_x+dw, desk_y+dd, dh), (desk_x+dw, desk_y, dh)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)
add_path([
    (desk_x+dw-0.5, desk_y+dd, 0), (desk_x+dw, desk_y+dd, 0),
    (desk_x+dw, desk_y+dd, dh), (desk_x+dw-0.5, desk_y+dd, dh)
], close=True, stroke_width=1.5, fill=bg_color, opacity=1.0)

# Flowing Roll of Laminate bridging the stack to the desk
# We use a raw SVG path for the bezier curve to make it organic.
# Start at the top of the stack, swoop up, and land on the desk.
cx1, cy1 = pt(stack_x+4, stack_y, 5*0.6)
cx2, cy2 = pt(desk_x+5, desk_y+dd, dh)
c_mid1_x = cx1
c_mid1_y = cy1 - 100
c_mid2_x = cx2
c_mid2_y = cy2 - 100

d = f"M {cx1} {cy1} C {c_mid1_x} {c_mid1_y}, {c_mid2_x} {c_mid2_y}, {cx2} {cy2}"
svg_paths.append(f'    <path d="{d}" stroke-width="2" opacity="1.0" fill="none" stroke-dasharray="4 6" />')

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
print("Updated graphic to occluded isometric art!")
