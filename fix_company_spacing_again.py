import glob

files_to_fix = ['distribution.html', 'team.html', 'sustainability.html', 'csr.html']

old_str = '<div class="text-center reveal" style="margin-bottom: 6rem;">'
new_str = '<div class="text-center reveal" style="margin-bottom: 1.5rem;">'

for filename in files_to_fix:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        # Also fix the section padding to 4rem 0 to perfectly match page-content
        content = content.replace('style="padding: 6rem 0;"', 'style="padding: 4rem 0;"')
        content = content.replace('style="padding: 5rem 0;"', 'style="padding: 4rem 0;"')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed spacing on {filename}")

