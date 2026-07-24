import re

html_content = open("index.html", "r", encoding="utf-8").read()

# Replace svg-draw with philosophy-draw so JS ignores it
html_content = html_content.replace('class="svg-draw"', 'class="philosophy-draw"')

# Append the CSS directly to the head or style.css
css_patch = """
/* Philosophy SVG Pure CSS Animation */
.philosophy-svg-container.active .philosophy-draw path {
    stroke-dasharray: 1500;
    stroke-dashoffset: 1500;
    animation: draw-philosophy 3s ease-out forwards;
}

/* Stagger the drawing of the paths slightly for effect */
.philosophy-svg-container.active .philosophy-draw path:nth-child(1) { animation-delay: 0.2s; }
.philosophy-svg-container.active .philosophy-draw path:nth-child(2) { animation-delay: 0.4s; }
.philosophy-svg-container.active .philosophy-draw path:nth-child(3) { animation-delay: 0.6s; }
.philosophy-svg-container.active .philosophy-draw path:nth-child(4) { animation-delay: 0.8s; }
.philosophy-svg-container.active .philosophy-draw path:nth-child(5) { animation-delay: 1.0s; }
.philosophy-svg-container.active .philosophy-draw path:nth-child(6) { animation-delay: 1.2s; }

@keyframes draw-philosophy {
    to {
        stroke-dashoffset: 0;
    }
}
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_patch)

open("index.html", "w", encoding="utf-8").write(html_content)

print("Fixed SVG animation!")
