import math

# ViewBox dimensions
vw, vh = 1000, 600
ox, oy = 500, 400  # Origin for isometric projection (center-bottom)

def iso(x, y, z):
    # 30 degree isometric
    cos30 = math.cos(math.pi / 6)
    sin30 = math.sin(math.pi / 6)
    cx = ox + (x - y) * cos30
    cy = oy + (x + y) * sin30 - z
    return cx, cy

paths = []

def add_path(pts, close=False, sw=1.5, op=0.9, dash="", fill="none"):
    coords = []
    for i, p in enumerate(pts):
        if type(p) is str:
            coords.append(p)
        else:
            cx, cy = iso(*p)
            coords.append(f"{'M' if i==0 else 'L'} {cx:.2f} {cy:.2f}")
    if close: coords.append("Z")
    style = f'fill="{fill}" stroke="#ffffff" stroke-width="{sw}" opacity="{op}" stroke-linecap="round" stroke-linejoin="round"'
    if dash: style += f' stroke-dasharray="{dash}"'
    paths.append(f'    <path d="{" ".join(coords)}" {style} />')

def add_raw_path(d_str, sw=1.5, op=0.9, dash="", fill="none"):
    style = f'fill="{fill}" stroke="#ffffff" stroke-width="{sw}" opacity="{op}" stroke-linecap="round" stroke-linejoin="round"'
    if dash: style += f' stroke-dasharray="{dash}"'
    paths.append(f'    <path d="{d_str}" {style} />')

def draw_box(x, y, z, dx, dy, dz, sw=1.5, op=0.9, dash="", fill="none"):
    # Bottom
    add_path([(x,y,z), (x+dx,y,z), (x+dx,y+dy,z), (x,y+dy,z)], True, sw, op, dash, fill)
    # Top
    add_path([(x,y,z+dz), (x+dx,y,z+dz), (x+dx,y+dy,z+dz), (x,y+dy,z+dz)], True, sw, op, dash, fill)
    # Pillars
    for px, py in [(x,y), (x+dx,y), (x+dx,y+dy), (x,y+dy)]:
        add_path([(px,py,z), (px,py,z+dz)], False, sw, op, dash, fill)

def draw_cylinder(x, y, z, r, h, sw=1.5, op=0.9):
    pts_bottom = []
    pts_top = []
    segments = 32
    for i in range(segments + 1):
        a = math.pi * 2 * i / segments
        px = x + r * math.cos(a)
        py = y + r * math.sin(a)
        pts_bottom.append((px, py, z))
        pts_top.append((px, py, z + h))
    add_path(pts_bottom, False, sw, op)
    add_path(pts_top, False, sw, op)
    # Tangent lines for isometric cylinder
    t1 = -math.pi/4
    t2 = 3*math.pi/4
    add_path([(x+r*math.cos(t1), y+r*math.sin(t1), z), (x+r*math.cos(t1), y+r*math.sin(t1), z+h)], False, sw, op)
    add_path([(x+r*math.cos(t2), y+r*math.sin(t2), z), (x+r*math.cos(t2), y+r*math.sin(t2), z+h)], False, sw, op)

# --- 1. Construction Grid & Markers ---
for i in range(-5, 6):
    add_path([(i*50, -250, 0), (i*50, 250, 0)], sw=0.5, op=0.2, dash="2 4")
    add_path([(-250, i*50, 0), (250, i*50, 0)], sw=0.5, op=0.2, dash="2 4")

# Cross markers
for mx, my in [(-250, -250), (250, 250), (-250, 250), (250, -250), (0,0)]:
    cx, cy = iso(mx, my, 0)
    add_raw_path(f"M {cx-5} {cy} L {cx+5} {cy} M {cx} {cy-5} L {cx} {cy+5}", sw=1, op=0.5)

# --- 2. Left Side: Paper Rolls (x < y region, e.g. x=-100, y=100) ---
# We want them far left. Let's use x = -150, y = 150.
# cx = ox + (-300)*cos30 = 500 - 260 = 240. Good.
draw_cylinder(-100, 180, 0, 15, 120, op=0.8)
draw_cylinder(-140, 150, 0, 18, 140, op=0.8)
draw_cylinder(-180, 120, 0, 12, 100, op=0.8)

# Flowing Paper (Bezier curves from rolls to center)
# We will use 2D screen coordinates for beautiful flowing ribbons.
# Center panels will be around ox=500, oy=400-z
def bezier_ribbon(start_pt, end_pt, c1, c2, w, lines, dash=""):
    for i in range(lines):
        offset = (i / (lines - 1)) * w - w/2
        s = (start_pt[0], start_pt[1] + offset)
        e = (end_pt[0], end_pt[1] + offset)
        ctrl1 = (c1[0], c1[1] + offset)
        ctrl2 = (c2[0], c2[1] + offset)
        add_raw_path(f"M {s[0]} {s[1]} C {ctrl1[0]} {ctrl1[1]}, {ctrl2[0]} {ctrl2[1]}, {e[0]} {e[1]}", sw=0.8 if dash else 1.2, op=0.7, dash=dash)

r1_base = iso(-140, 150, 20)
center_dest = iso(0, 0, 80)
# Ribbon 1 (Wood grain - parallel lines)
bezier_ribbon(r1_base, center_dest, (r1_base[0]+100, r1_base[1]-150), (center_dest[0]-150, center_dest[1]+50), 30, 6)

r2_base = iso(-100, 180, 40)
center_dest2 = iso(20, 20, 90)
# Ribbon 2 (Marble/Linen texture - dashed lines)
bezier_ribbon(r2_base, center_dest2, (r2_base[0]+120, r2_base[1]-100), (center_dest2[0]-100, center_dest2[1]-20), 20, 4, dash="3 3")


# --- 3. Center: Exploded Panels (x=0, y=0) ---
pw, pd = 60, 40
# Layer 1: Backing
draw_box(-pw/2, -pd/2, 20, pw, pd, 2, op=0.7)
# Layer 2: MDF Core
draw_box(-pw/2, -pd/2, 40, pw, pd, 8, op=0.9)
# Layer 3: Resin
draw_box(-pw/2, -pd/2, 65, pw, pd, 1, op=0.5, dash="1 2")
# Layer 4: Decorative Paper
draw_box(-pw/2, -pd/2, 80, pw, pd, 1, op=0.9)

# Explosion guide lines (vertical)
for px, py in [(-pw/2, -pd/2), (pw/2, -pd/2), (pw/2, pd/2), (-pw/2, pd/2)]:
    add_path([(px, py, 20), (px, py, 80)], sw=0.5, op=0.4, dash="2 2")


# --- 4. Right Side: Premium Furniture (x > 0, y < 0) ---
# Wardrobe
draw_box(100, -200, 0, 60, 40, 150)
# Wardrobe doors (vertical lines)
add_path([(130, -200, 0), (130, -200, 150)], sw=1)
add_path([(100, -180, 0), (100, -180, 150)], sw=1) # Side panel line

# Kitchen Island
draw_box(100, -100, 0, 80, 50, 60)
# Overhang (Countertop)
draw_box(95, -105, 60, 90, 60, 4, op=1.0) # slightly thicker top
# Island details
add_path([(100, -75, 0), (100, -75, 60)], sw=0.8) # cabinet split

# Floating Cabinet / Shelving Unit
draw_box(200, -150, 80, 40, 80, 40)
# Shelves inside
add_path([(200, -150, 95), (200, -70, 95)], sw=0.8)
add_path([(200, -150, 105), (200, -70, 105)], sw=0.8)

# Transformational Lines (From center decorative panel to furniture)
dec_pt = iso(pw/2, -pd/2, 80)
wardrobe_pt = iso(100, -200, 100)
island_pt = iso(100, -100, 60)

add_raw_path(f"M {dec_pt[0]} {dec_pt[1]} Q {dec_pt[0]+100} {dec_pt[1]-50} {wardrobe_pt[0]} {wardrobe_pt[1]}", sw=0.8, op=0.6, dash="4 4")
add_raw_path(f"M {dec_pt[0]} {dec_pt[1]} Q {dec_pt[0]+80} {dec_pt[1]+20} {island_pt[0]} {island_pt[1]}", sw=0.8, op=0.6, dash="4 4")

# Output SVG
svg_content = f'''<svg class="philosophy-draw" viewBox="0 0 {vw} {vh}" fill="none" stroke="#ffffff" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 650px; display: block; margin: 0 auto; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.15));">
{"\n".join(paths)}
</svg>'''

html = open("index.html", "r", encoding="utf-8").read()
start_marker = '<div class="philosophy-svg-container'
start_idx = html.find(start_marker)

# Update container max-width to allow the wider illustration
html = html[:start_idx] + html[start_idx:].replace('max-width: 450px;', 'max-width: 650px;', 1)

# Now find the SVG
start_idx = html.find(start_marker) # re-find in case offsets changed
svg_start_idx = html.find('<svg class="philosophy-draw"', start_idx)
svg_end_idx = html.find('</svg>', svg_start_idx) + 6

final_content = html[:svg_start_idx] + svg_content + html[svg_end_idx:]

open("index.html", "w", encoding="utf-8").write(final_content)
print("Updated graphic to premium minimalist hero illustration!")
