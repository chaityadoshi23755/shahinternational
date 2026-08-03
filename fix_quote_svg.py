import re

with open('Our-Clients.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the unconstrained SVG quote tag with one that has inline style
target = '<svg class="svg-draw svg-quote" viewBox="0 0 100 100" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
replacement = '<svg class="svg-draw svg-quote" viewBox="0 0 100 100" fill="none" stroke="var(--color-brand-red)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="width: 80px; height: 80px; margin: 0 auto 1.5rem auto; display: block;">'

content = content.replace(target, replacement)

with open('Our-Clients.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed SVG quote in Our-Clients.html")
