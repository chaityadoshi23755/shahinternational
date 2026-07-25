import glob

scroll_html = """
    <div class="banner-scroll-indicator" onclick="window.scrollTo({top: window.innerHeight - 80, behavior: 'smooth'})">
      <i class="fa-solid fa-chevron-down"></i>
    </div>
"""

company_pages = [
    "kingdecor-zhejiang-co-ltd-china.html",
    "schattdecor-ag-germany.html",
    "deurowood-gmbh-austria.html",
    "mitsubishi-chemical-corporation.html",
    "hueck-rheinische-gmbh-germany.html",
    "pyrus-panels-germany.html"
]

for filename in company_pages:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<section class="page-banner">' in content and 'banner-scroll-indicator' not in content:
        # Insert before the closing </section> of page-banner
        # Since there might be nested divs, the safest way is to find the end of page-banner-content
        # and insert it after, or find the closing </section> for page-banner.
        # Let's find '<section class="page-banner">' and then the first '</section>' after it.
        start_idx = content.find('<section class="page-banner">')
        if start_idx != -1:
            end_idx = content.find('</section>', start_idx)
            if end_idx != -1:
                content = content[:end_idx] + scroll_html + content[end_idx:]
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")
