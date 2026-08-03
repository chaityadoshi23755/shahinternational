import glob

html_files = glob.glob('*.html')

old_str = '<div class="text-center reveal" style="margin-bottom: 4rem; padding-top: 2rem;">'
new_str = '<div class="text-center reveal" style="margin-top: -2rem; margin-bottom: 6rem;">'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed spacing on {filename}")
