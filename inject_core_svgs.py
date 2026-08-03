import re

generic_svg = """
      <div class="text-center reveal" style="margin-bottom: 4rem; padding-top: 2rem;">
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

pages = {
    'about-us.html': ('About Shah International', 'Discover our legacy and commitment to excellence.'),
    'contact-us.html': ('Get in Touch', 'We are here to assist you. Reach out to our team.'),
    'Our-Clients.html': ('Our Global Partners', 'Trusted by the world\'s leading brands and manufacturers.')
}

for filename, (title, subtitle) in pages.items():
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # The content could start with <section class="page-content"> or we might just inject it below the banner.
    # In about-us.html, we have:
    # <div class="timeline-container" id="the-journey"> or <div class="container text-center reveal" style="margin-top: 4rem; margin-bottom: 2rem;">
    # Wait, Our-Clients.html has:
    # <section class="page-content">
    #   <div class="container">
    #     <div class="principals-masonry">
    # Let's use a simpler injection approach for these 3 files.

    if filename == 'Our-Clients.html':
        match = re.search(r'<section class="page-content"[^>]*>\s*<div class="container"[^>]*>', content, re.IGNORECASE)
        if match:
            intro_html = generic_svg.format(title=title, subtitle=subtitle)
            new_content = content[:match.end()] + intro_html + content[match.end():]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected SVG intro to {filename}")

    elif filename == 'contact-us.html':
        match = re.search(r'<section class="page-content"[^>]*>\s*<div class="container"[^>]*>', content, re.IGNORECASE)
        if match:
            intro_html = generic_svg.format(title=title, subtitle=subtitle)
            new_content = content[:match.end()] + intro_html + content[match.end():]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected SVG intro to {filename}")

    elif filename == 'about-us.html':
        # about-us doesn't have page-content section directly after banner. It has <div class="container text-center reveal" style="margin-top: 4rem; margin-bottom: 2rem;">
        match = re.search(r'<!-- Quick Links -->', content, re.IGNORECASE)
        if match:
            intro_html = generic_svg.format(title=title, subtitle=subtitle)
            new_content = content[:match.start()] + intro_html + content[match.start():]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected SVG intro to {filename}")

