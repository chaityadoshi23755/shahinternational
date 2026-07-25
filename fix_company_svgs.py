import glob

generic_svg = """
        <div class="text-center reveal" style="margin-bottom: 6rem;">
          <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
            <polygon points="50,10 90,50 50,90 10,50" stroke="var(--color-brand-red)" />
            <polygon points="50,25 75,50 50,75 25,50" stroke="var(--color-brand-red)" />
            <path d="M 10 50 L 90 50" stroke="var(--color-brand-red)" />
            <path d="M 50 10 L 50 90" stroke="var(--color-brand-red)" />
            <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
          </svg>
        </div>
"""

# Fix spacing on the ones already injected
files_to_fix = ['distribution.html', 'team.html', 'sustainability.html', 'csr.html']
old_str = '<div class="text-center reveal" style="margin-bottom: 2rem;">'
new_str = '<div class="text-center reveal" style="margin-bottom: 6rem;">'

for filename in files_to_fix:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed spacing on {filename}")

# Inject into Principal pages
principal_pages = {
    'kingdecor-zhejiang-co-ltd-china.html': ('Kingdecor (Zhejiang) Co. Ltd', 'Explore our global partnership in China.'),
    'schattdecor-ag-germany.html': ('Schattdecor AG, Germany', 'Explore our global partnership in Germany.'),
    'deurowood-gmbh-austria.html': ('Deurowood GmbH, Austria', 'Explore our global partnership in Austria.'),
    'mitsubishi-chemical-corporation.html': ('Mitsubishi Chemical Corporation', 'Explore our global partnership in Japan.'),
    'hueck-rheinische-gmbh-germany.html': ('Hueck Rheinische GmbH', 'Explore our global partnership in Germany.'),
    'pyrus-panels-germany.html': ('Pyrus Panels, Germany', 'Explore our global partnership in Germany.')
}

import re
for filename, (title, subtitle) in principal_pages.items():
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    match = re.search(r'<section class="page-content"[^>]*>\s*<div class="container"[^>]*>', content, re.IGNORECASE)
    if match:
        if 'svg-draw' in content[match.end():match.end()+300]:
            print(f"SVG already exists in {filename}")
            continue

        intro_html = f"""
      <div class="text-center reveal" style="margin-bottom: 6rem;">
        <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">
          <!-- Diamond / Compass -->
          <polygon points="50,10 90,50 50,90 10,50" stroke="var(--color-brand-red)" />
          <polygon points="50,25 75,50 50,75 25,50" stroke="var(--color-brand-red)" />
          <path d="M 10 50 L 90 50" stroke="var(--color-brand-red)" />
          <path d="M 50 10 L 50 90" stroke="var(--color-brand-red)" />
          <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
        </svg>
        <h2 class="editorial-heading" style="font-size: 3rem; margin-bottom: 1rem; color: #111;">{title}</h2>
        <p style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: #555; max-width: 600px; margin: 0 auto;">{subtitle}</p>
      </div>
"""
        new_content = content[:match.end()] + intro_html + content[match.end():]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected SVG intro to {filename}")
    else:
        print(f"Could not find injection point in {filename}")
