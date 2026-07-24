import numpy as np
from scipy.interpolate import splprep, splev

# Original points from my crude map
pts = [(80, 240), (80, 220), (90, 210), (70, 210), (40, 200), (20, 190), (15, 170), (30, 160), (50, 160), (20, 140), (40, 120), (60, 130), (70, 110), (70, 90), (80, 70), (100, 60), (110, 40), (100, 20), (120, 5), (140, 10), (160, 5), (170, 20), (160, 40), (180, 60), (200, 70), (220, 80), (250, 85), (280, 95), (290, 90), (300, 70), (310, 90), (330, 95), (350, 80), (380, 70), (390, 100), (380, 120), (370, 140), (360, 170), (340, 190), (320, 180), (330, 160), (300, 150), (280, 170), (290, 190), (270, 200), (250, 230), (230, 260), (210, 300), (200, 330), (190, 350), (180, 380), (160, 400), (140, 380), (130, 360), (110, 330), (100, 300), (90, 270)]

# Close the loop
pts.append(pts[0])

x = [p[0] for p in pts]
y = [p[1] for p in pts]

# Fit spline
tck, u = splprep([x, y], s=0, per=True)

# Evaluate spline to get many smooth points
unew = np.linspace(0, 1, 200)
out = splev(unew, tck)

# Generate an SVG path with smooth cubic beziers using Catmull-Rom or just line segments
# If we have 200 points, even straight lines will look perfectly smooth
smooth_pts = list(zip(out[0], out[1]))

path = f"M {smooth_pts[0][0]:.1f} {smooth_pts[0][1]:.1f}"
for px, py in smooth_pts[1:]:
    path += f" L {px:.1f} {py:.1f}"
path += " Z"

with open("smooth_india.txt", "w") as f:
    f.write(path)
print("Saved smooth_india.txt")
