import glob
import re

woodgrain_svg = """
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Tree / Wood Rings -->
          <circle cx="50" cy="50" r="40" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="28" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="16" stroke="var(--color-brand-red)" />
          <!-- Abstract crack/grain line -->
          <path d="M 50 10 Q 60 30 50 50 T 45 90" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
        </svg>
"""

stone_svg = """
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Hexagon / Stone Geometry -->
          <polygon points="50,10 85,30 85,70 50,90 15,70 15,30" stroke="var(--color-brand-red)" />
          <polygon points="50,30 70,42 70,66 50,78 30,66 30,42" stroke="var(--color-brand-red)" />
          <path d="M 15 30 L 50 50 L 85 30" stroke="var(--color-brand-red)" />
          <path d="M 50 50 L 50 90" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
        </svg>
"""

colors_svg = """
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Interlocking Circles / Palette -->
          <circle cx="35" cy="40" r="25" stroke="var(--color-brand-red)" />
          <circle cx="65" cy="40" r="25" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="65" r="25" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="48" r="4" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
        </svg>
"""

generic_svg = """
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Diamond / Compass -->
          <polygon points="50,10 90,50 50,90 10,50" stroke="var(--color-brand-red)" />
          <polygon points="50,25 75,50 50,75 25,50" stroke="var(--color-brand-red)" />
          <path d="M 10 50 L 90 50" stroke="var(--color-brand-red)" />
          <path d="M 50 10 L 50 90" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
        </svg>
"""

def get_category(filename):
    wood_keywords = ['Oak', 'Maple', 'Beech', 'Walnut', 'Cherry', 'Pine', 'Ash', 'Sandal', 'Mahogany', 'Wenge', 'Elm', 'Acacia', 'Apple', 'Olive', 'Teak', 'woodgrains', 'Zebrano', 'Zebrawood', 'Mango', 'Chestnut']
    stone_keywords = ['Stone', 'Marble', 'statuario', 'blasutein', 'taj-mahal', 'roman_clay', 'Canyon-Monument']
    color_keywords = ['Unique-colors', 'pearl', 'Petrol', 'bluish', 'sea_blue', 'silk', 'true-blue', 'pine_nut', 'riva', 'triron', 'color', 'grey', 'blue']
    
    if any(k.lower() in filename.lower() for k in wood_keywords): return woodgrain_svg, "Premium Woodgrain Series"
    if any(k.lower() in filename.lower() for k in stone_keywords): return stone_svg, "Premium Stone & Marble Series"
    if any(k.lower() in filename.lower() for k in color_keywords): return colors_svg, "Premium Solid Colors Series"
    
    return generic_svg, "Explore Our Collection"

skip_files = [
    'e-catalogs.html', 'decor-applications.html', 'kingdecor-zhejiang-co-ltd-china.html', 
    'schattdecor-ag-germany.html', 'deurowood-gmbh-austria.html', 'mitsubishi-chemical-corporation.html',
    'hueck-rheinische-gmbh-germany.html', 'pyrus-panels-germany.html', 'index.html', 'about-us.html', 'Our-Clients.html'
]

html_files = glob.glob('*.html')

for filename in html_files:
    if filename in skip_files or 'old' in filename or 'india_paths' in filename or 'footer' in filename or 'header' in filename:
        continue
        
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Check if we already injected an intro section
    if 'class="editorial-heading"' in content and 'style="margin-bottom: 4rem;"' in content:
        continue

    # Find where to inject: after <section class="page-content">\n    <div class="container">
    # Try different whitespace combinations
    pattern = re.compile(r'<section class="page-content"[^>]*>\s*<div class="container"[^>]*>', re.IGNORECASE)
    match = pattern.search(content)
    
    if match:
        svg_code, subtitle = get_category(filename)
        
        # Extract title from the banner h1
        title_match = re.search(r'<div class="page-banner-content">\s*<h1>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "Premium Collection"
        
        intro_html = f"""
      <div class="text-center reveal" style="margin-bottom: 4rem; padding-top: 2rem;">
{svg_code}
        <h2 class="editorial-heading" style="font-size: 3rem; margin-bottom: 1rem; color: #111;">{title}</h2>
        <p style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: #555; max-width: 600px; margin: 0 auto;">{subtitle}</p>
      </div>
"""
        
        new_content = content[:match.end()] + intro_html + content[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected SVG intro to {filename}")
