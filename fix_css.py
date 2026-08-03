lines = open("style.css", "r", encoding="utf-8").readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if line.strip() == ".principal-tile:hover {" and lines[i+1].strip() == "transform: translateY(-8px);" and lines[i+2].strip() == "box-shadow: 0 30px 60px rgba(0,0,0,0.3);" and "background-color: var(--color-brand-red);" in lines[i+3]:
        skip = True
    elif line.strip() == "/* ========== BULLETPROOF CONTRAST FIXES ========== */":
        # we will handle this manually to keep .philosophy-parallax-content p
        pass
    elif line.strip() == ".principal-tile {" and lines[i+1].strip() == "color: #fff !important;":
        skip = True
    elif line.strip() == ".principal-tile p {" and lines[i+1].strip() == "color: #fff !important;":
        skip = True
    elif line.strip() == ".principal-tile h3 {" and lines[i+1].strip() == "color: var(--color-brand-red) !important;":
        skip = True
    elif line.strip() == ".principal-tile:hover h3," and lines[i+4].strip() == "color: #fff !important;":
        skip = True
        
    if skip and line.strip() == "}":
        skip = False
        continue
        
    if not skip:
        new_lines.append(line)

open("style.css", "w", encoding="utf-8").writelines(new_lines)
print("Removed conflicting CSS!")
