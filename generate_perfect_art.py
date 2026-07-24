import math

vw, vh = 1100, 650
ox, oy = 550, 450

def iso(x, y, z):
    cos30 = math.cos(math.pi / 6)
    sin30 = math.sin(math.pi / 6)
    cx = ox + (x - y) * cos30
    cy = oy + (x + y) * sin30 - z
    return cx, cy

paths = []

def add_path(pts, close=False, sw=1.2, op=0.9, dash="", fill="none"):
    coords = []
    for i, p in enumerate(pts):
        if type(p) is str:
            coords.append(p)
        else:
            coords.append(f"{'M' if i==0 else 'L'} {p[0]:.2f} {p[1]:.2f}")
    if close:
        coords.append("Z")
    
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ''
    path_str = f'<path d="{" ".join(coords)}" fill="{fill}" stroke="#ffffff" stroke-width="{sw}" opacity="{op}" stroke-linecap="round" stroke-linejoin="round"{dash_attr} />'
    paths.append(path_str)

def add_circle(xc, yc, z, r, start_deg=0, end_deg=360, steps=60, sw=1.2, op=0.9, dash=""):
    pts = []
    for i in range(steps + 1):
        angle = math.radians(start_deg + (end_deg - start_deg) * i / steps)
        x = xc + r * math.cos(angle)
        y = yc + r * math.sin(angle)
        pts.append(iso(x, y, z))
    add_path(pts, sw=sw, op=op, dash=dash)

# 0. Grid (Fading into background)
# Use radial distance to fade opacity
for x in range(-400, 500, 50):
    pts = []
    for y in range(-300, 350, 50):
        dist = math.sqrt(x*x + y*y)
        op = max(0, 0.12 - (dist / 4000)) # Fades out further from origin
        pts.append((iso(x, y, 0), op))
    # Draw segment by segment to apply opacity? SVG paths can't change opacity mid-path.
    # Just draw the whole line with very low opacity
    add_path([iso(x, -300, 0), iso(x, 300, 0)], sw=0.5, op=0.08, dash="2 4")
    
for y in range(-300, 350, 50):
    add_path([iso(-400, y, 0), iso(500, y, 0)], sw=0.5, op=0.08, dash="2 4")

# Engineering Marks (Subtle corner/focus crosses)
marks = [(-300, -200), (400, -200), (-300, 200), (400, 200)]
for mx, my in marks:
    add_path([iso(mx-15, my, 0), iso(mx+15, my, 0)], sw=0.5, op=0.3)
    add_path([iso(mx, my-15, 0), iso(mx, my+15, 0)], sw=0.5, op=0.3)

# 1. Paper Roll (Hero Element - Increased by ~35%)
rx, ry = -320, 0
rr = 95
rh = 280

add_circle(rx, ry, rh, rr, sw=1.5, op=1.0)
add_circle(rx, ry, rh, rr-6, sw=0.6, op=0.4) # inner layer
add_circle(rx, ry, 0, rr, start_deg=45, end_deg=225, sw=1.5, op=1.0)
add_path([iso(rx + rr*math.cos(math.radians(45)), ry + rr*math.sin(math.radians(45)), 0),
          iso(rx + rr*math.cos(math.radians(45)), ry + rr*math.sin(math.radians(45)), rh)], sw=1.5, op=1.0)
add_path([iso(rx + rr*math.cos(math.radians(225)), ry + rr*math.sin(math.radians(225)), 0),
          iso(rx + rr*math.cos(math.radians(225)), ry + rr*math.sin(math.radians(225)), rh)], sw=1.5, op=1.0)

# Unrolling flap starts from the right side of the roll
flap_angle = 330
fx = rx + rr*math.cos(math.radians(flap_angle))
fy = ry + rr*math.sin(math.radians(flap_angle))
add_path([iso(fx, fy, 0), iso(fx, fy, rh)], sw=1.0, op=0.7)

# 2. Flowing Paper Sheet (Elegant & Continuous)
# The paper sheet is unrolling horizontally now and swooping down
flow_y_min = fy - 70 # Width of 140
flow_y_max = fy + 70
flow_x_start = fx
flow_x_end = -40

def get_flow_z(x):
    # Smooth cubic bezier transition for height from roll (rh) to panel (70)
    t = (x - flow_x_start) / (flow_x_end - flow_x_start)
    # Use ease-in-out curve
    t_smooth = t * t * (3 - 2 * t)
    return rh - t_smooth * (rh - 70)

# Generate sheet edges
left_edge = []
right_edge = []
for i in range(21):
    t = i / 20.0
    x = flow_x_start + t * (flow_x_end - flow_x_start)
    z = get_flow_z(x)
    
    # Add a graceful sideways curve (Y offset)
    y_offset = 30 * math.sin(t * math.pi)
    left_edge.append(iso(x, flow_y_min + y_offset, z))
    right_edge.append(iso(x, flow_y_max + y_offset, z))

add_path(left_edge, sw=1.5, op=1.0)
add_path(right_edge, sw=1.5, op=1.0)
add_path([left_edge[-1], right_edge[-1]], sw=1.5, op=1.0) # Leading edge

# Premium Shine / Decor Lines (Subtle solid parallel lines, no dashed tracks)
for i in range(1, 4): # Just 3 subtle lines
    y_interp = flow_y_min + i * (140 / 4)
    line_pts = []
    for j in range(21):
        t = j / 20.0
        x = flow_x_start + t * (flow_x_end - flow_x_start)
        z = get_flow_z(x)
        y_offset = 30 * math.sin(t * math.pi)
        line_pts.append(iso(x, y_interp + y_offset, z))
    add_path(line_pts, sw=0.4, op=0.3)


# 3. Exploded MDF Panel (X: -40 to 80, Y: -90 to 90)
px_min, px_max = -40, 80
py_min, py_max = -80, 80

# Core Layer (MDF) - Z: 20 to 30
add_path([iso(px_min, py_min, 30), iso(px_max, py_min, 30), iso(px_max, py_max, 30), iso(px_min, py_max, 30)], close=True, sw=1.2, op=0.8)
add_path([iso(px_min, py_min, 20), iso(px_min, py_max, 20), iso(px_min, py_max, 30), iso(px_min, py_min, 30)], close=True, sw=1.2, op=0.8)
add_path([iso(px_min, py_max, 20), iso(px_max, py_max, 20), iso(px_max, py_max, 30), iso(px_min, py_max, 30)], close=True, sw=1.2, op=0.8)

# Decor Paper Layer hovering above - Z: 70
# Show it actively wrapping onto the panel
add_path([iso(px_min, py_min, 70), iso(px_max, py_min, 70), iso(px_max, py_max, 70), iso(px_min, py_max, 70)], close=True, sw=1.5, op=1.0)
add_path([left_edge[-1], iso(px_min, py_min, 70)], sw=1.5, op=1.0)
add_path([right_edge[-1], iso(px_min, py_max, 70)], sw=1.5, op=1.0)

# Shine on the panel paper
add_path([iso(px_min+20, py_min, 70), iso(px_max, py_min+20, 70)], sw=0.5, op=0.3)
add_path([iso(px_min+40, py_min, 70), iso(px_max, py_min+40, 70)], sw=0.5, op=0.2)

# Explode connection lines
add_path([iso(px_min, py_min, 70), iso(px_min, py_min, 30)], sw=0.6, op=0.5, dash="2 3")
add_path([iso(px_max, py_min, 70), iso(px_max, py_min, 30)], sw=0.6, op=0.5, dash="2 3")
add_path([iso(px_max, py_max, 70), iso(px_max, py_max, 30)], sw=0.6, op=0.5, dash="2 3")
add_path([iso(px_min, py_max, 70), iso(px_min, py_max, 30)], sw=0.6, op=0.5, dash="2 3")


# 4. Premium Wardrobe (X: 180 to 360, Y: -100 to 100, Z: 0 to 280)
wx_min, wx_max = 200, 380
wy_min, wy_max = -90, 90
wz = 260

add_path([iso(wx_min, wy_min, wz), iso(wx_max, wy_min, wz), iso(wx_max, wy_max, wz), iso(wx_min, wy_max, wz)], close=True, sw=1.5, op=1.0)
add_path([iso(wx_min, wy_min, 0), iso(wx_min, wy_max, 0), iso(wx_min, wy_max, wz), iso(wx_min, wy_min, wz)], close=True, sw=1.5, op=1.0)
add_path([iso(wx_min, wy_max, 0), iso(wx_max, wy_max, 0), iso(wx_max, wy_max, wz), iso(wx_min, wy_max, wz)], close=True, sw=1.5, op=1.0)

# Cabinet Doors (Premium styling)
add_path([iso(wx_min, wy_max, 45), iso(wx_max, wy_max, 45)], sw=1.0, op=0.8) # Base drawer
add_path([iso(245, wy_max, 45), iso(245, wy_max, wz)], sw=1.0, op=0.8)
add_path([iso(290, wy_max, 45), iso(290, wy_max, wz)], sw=1.0, op=0.8)
add_path([iso(335, wy_max, 45), iso(335, wy_max, wz)], sw=1.0, op=0.8)
add_path([iso(290, wy_max, 0), iso(290, wy_max, 45)], sw=1.0, op=0.8) # Split drawer

# Premium Handles (Minimalist)
def draw_handle(hx, hz_start, hz_end):
    add_path([iso(hx, wy_max, hz_start), iso(hx, wy_max, hz_end)], sw=2.0, op=1.0)

draw_handle(235, 120, 170)
draw_handle(255, 120, 170)
draw_handle(325, 120, 170)
draw_handle(345, 120, 170)
add_path([iso(230, wy_max, 22.5), iso(260, wy_max, 22.5)], sw=2.0, op=1.0)
add_path([iso(320, wy_max, 22.5), iso(350, wy_max, 22.5)], sw=2.0, op=1.0)

# Premium Shine/Grain on Wardrobe (Matching the paper)
add_path([iso(210, wy_max, 45), iso(210, wy_max, wz)], sw=0.4, op=0.3)
add_path([iso(275, wy_max, 45), iso(275, wy_max, wz)], sw=0.4, op=0.3)


# 5. Elegant Transformation Guide
# Flow line from panel to wardrobe
add_path([iso(px_max+10, 0, 45), iso(wx_min-10, 0, 100)], sw=0.8, op=0.6, dash="4 4")
cx, cy = iso(wx_min-15, 0, 95)
add_path([f"M {cx-5} {cy-5} L {cx+5} {cy+5} L {cx-5} {cy+5}"], sw=0.8, op=0.6)


svg_content = f'''<svg class="philosophy-draw" viewBox="0 0 {vw} {vh}" fill="none" stroke="#ffffff" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 900px; display: block; margin: 0 auto; filter: drop-shadow(0 15px 35px rgba(0,0,0,0.15));">
{"\n".join(paths)}
</svg>'''

html = open("index.html", "r", encoding="utf-8").read()
start_marker = '<div class="philosophy-svg-container'
start_idx = html.find(start_marker)
svg_start_idx = html.find('<svg class="philosophy-draw"', start_idx)
svg_end_idx = html.find('</svg>', svg_start_idx) + 6

# Replace max-width 750px with 900px in the container if it exists
html = html[:start_idx] + html[start_idx:svg_start_idx].replace('max-width: 750px;', 'max-width: 900px;') + html[svg_start_idx:]

# Refind to be safe
start_idx = html.find(start_marker)
svg_start_idx = html.find('<svg class="philosophy-draw"', start_idx)
svg_end_idx = html.find('</svg>', svg_start_idx) + 6

final_content = html[:svg_start_idx] + svg_content + html[svg_end_idx:]

open("index.html", "w", encoding="utf-8").write(final_content)
print("Updated premium illustration!")
