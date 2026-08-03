import glob
import re

html_files = glob.glob('*.html')

for filename in html_files:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    pattern = r'<section class="tech-directory-header[^>]*>.*?<h1[^>]*>(.*?)</h1>.*?<ol class="breadcrumb"[^>]*>(.*?)</ol>.*?</section>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        title = match.group(1).strip()
        breadcrumb_inner = match.group(2).strip()
        
        # Build the new banner
        new_banner = f"""<section class="page-banner">
    <img src="sites/default/files/2018-12/about.jpg" alt="{title}" class="page-banner-bg">
    <div class="page-banner-overlay"></div>
    <div class="page-banner-content">
      <h1>{title}</h1>
      <ol class="breadcrumb">{breadcrumb_inner}</ol>
    </div>
    <div class="banner-scroll-indicator" onclick="window.scrollTo({{top: window.innerHeight - 80, behavior: 'smooth'}})">
      <i class="fa-solid fa-chevron-down"></i>
    </div>
  </section>"""
        
        content = content[:match.start()] + new_banner + content[match.end():]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {filename}")
