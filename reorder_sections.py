import re

file_path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to extract the 4 sections.
# 1. Who We Represent
who_we_rep_match = re.search(r'<!-- Who We Represent -->(.*?)    <section id="whom-we-sell"', content, re.DOTALL)
who_we_rep_html = who_we_rep_match.group(1) if who_we_rep_match else ""

# 2. Whom We Sell To
whom_we_sell_match = re.search(r'(<section id="whom-we-sell".*?)</section>\s*<div class="marquee-bottom-bar"></div>', content, re.DOTALL)
whom_we_sell_html = whom_we_sell_match.group(0) if whom_we_sell_match else ""

# 3. Who We Are
who_we_are_match = re.search(r'<!-- Who We Are / About -->(.*?)    <!-- Our Philosophy', content, re.DOTALL)
who_we_are_html = who_we_are_match.group(1) if who_we_are_match else ""

# 4. Our Philosophy
philosophy_match = re.search(r'<!-- Our Philosophy \(Dramatic Dark Section\) -->(.*?)</main>', content, re.DOTALL)
philosophy_html = philosophy_match.group(1) if philosophy_match else ""

if who_we_rep_html and whom_we_sell_html and who_we_are_html and philosophy_html:
    # 1. "Who We Are" in White BG
    who_we_are_html = who_we_are_html.replace('class="section"', 'class="section bg-light"') # White/Light BG
    
    # 2. "Our Philosophy" in Red BG
    # Current style: style="background-color: #050505; color: #ffffff; padding: var(--space-xl) 0; border-top: 1px solid #1a1a1a;"
    philosophy_html = philosophy_html.replace('background-color: #050505;', 'background-color: var(--color-brand-red);')
    philosophy_html = philosophy_html.replace('border-top: 1px solid #1a1a1a;', '')
    # Change the red divider to white so it's visible on red bg
    philosophy_html = philosophy_html.replace('background-color: var(--color-brand-red); margin: 0 auto 3rem auto;', 'background-color: #fff; margin: 0 auto 3rem auto;')
    
    # 3. "Global Giants We Represent" in White BG
    who_we_rep_html = who_we_rep_html.replace('class="section bg-light"', 'class="section"') # Normal white bg
    
    # 4. "Whom We Sell To" in Red BG
    # Needs to be red bg. It's currently in .marquee-section (which is #f8f9fa). We can add an inline style to override it to red, and make text white.
    whom_we_sell_html = whom_we_sell_html.replace('<section id="whom-we-sell" class="marquee-section text-center">', '<section id="whom-we-sell" class="marquee-section text-center" style="background-color: var(--color-brand-red);">')
    whom_we_sell_html = whom_we_sell_html.replace('<h2 class="section-heading">', '<h2 class="section-heading" style="color: #fff;">')
    whom_we_sell_html = whom_we_sell_html.replace('color: var(--color-brand-red); text-decoration: underline;', 'color: #fff; text-decoration: underline;')
    whom_we_sell_html = whom_we_sell_html.replace('color: var(--color-text);', 'color: #fff;')
    whom_we_sell_html = whom_we_sell_html.replace('font-style: italic;">', 'font-style: italic; color: #fff;">')


    # Now reassemble
    new_body = f"""    <!-- Who We Are / About -->
{who_we_are_html}
    <!-- Our Philosophy (Dramatic Dark Section) -->
{philosophy_html}
    <!-- Who We Represent -->
{who_we_rep_html}
    {whom_we_sell_html}
  </main>"""

    # Replace the chunk in the file
    old_chunk_match = re.search(r'<!-- Who We Represent -->.*?</main>', content, re.DOTALL)
    if old_chunk_match:
        new_content = content[:old_chunk_match.start()] + new_body + content[old_chunk_match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success! Sections reordered and styled.")
    else:
        print("Error finding replacement block.")
else:
    print("Error matching sections.")
