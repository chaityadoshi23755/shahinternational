import glob
import re

html_files = glob.glob('*.html')
chevron_pattern = re.compile(r'<div class="banner-scroll-indicator"[^>]*>.*?</div>', re.DOTALL)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if chevron_pattern.search(content):
        new_content = chevron_pattern.sub('', content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed chevron from {filename}")
