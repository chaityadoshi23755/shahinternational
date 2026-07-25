import re
import glob

generic_svg = """
        <div class="text-center reveal" style="margin-bottom: 2rem;">
          <svg class="svg-draw" viewBox="0 0 100 100" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto; display: block;">
            <polygon points="50,10 90,50 50,90 10,50" stroke="var(--color-brand-red)" />
            <polygon points="50,25 75,50 50,75 25,50" stroke="var(--color-brand-red)" />
            <path d="M 10 50 L 90 50" stroke="var(--color-brand-red)" />
            <path d="M 50 10 L 50 90" stroke="var(--color-brand-red)" />
            <circle cx="50" cy="50" r="3" fill="var(--color-brand-red)" stroke="none" class="pulse-node" style="animation-duration: 3s;" />
          </svg>
        </div>
"""

# We'll use the generic_svg for all of these to keep them consistent, as requested.

files = [
    'distribution.html',
    'team.html',
    'sustainability.html',
    'csr.html',
    'kingdecor-zhejiang-co-ltd-china.html',
    'schattdecor-ag-germany.html',
    'deurowood-gmbh-austria.html',
    'mitsubishi-chemical-corporation.html',
    'hueck-rheinische-gmbh-germany.html',
    'pyrus-panels-germany.html'
]

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Some pages have <h2 class="section-heading">, some have <h2 class="editorial-heading">
        # Let's find the first occurrence of an h2 after the banner.
        # We can look for <h2 class="section-heading" or <h2 class="editorial-heading"
        
        match = re.search(r'(<h2[^>]*class="(?:section-heading|editorial-heading)"[^>]*>)', content)
        
        if match:
            # Check if we already injected SVG in this block
            if 'svg-draw' in content[max(0, match.start()-300):match.start()]:
                print(f"SVG already exists in {filename}")
                continue
                
            new_content = content[:match.start()] + generic_svg + content[match.start():]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected SVG to {filename}")
        else:
            print(f"Could not find heading injection point in {filename}")
    except FileNotFoundError:
        print(f"{filename} not found.")

