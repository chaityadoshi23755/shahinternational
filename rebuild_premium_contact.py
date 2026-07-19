import re

file_path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\contact-us.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content_block = """  <section class="page-content" style="background-color: #f8f9fa;">
    <div class="container reveal">
      <div style="text-align: center; margin-bottom: 4rem;">
        <h2 class="section-heading" style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #111; margin-bottom: 1rem;">Contact Us</h2>
        <div style="width: 40px; height: 2px; background-color: var(--color-brand-red); margin: 0 auto;"></div>
      </div>
      
      <!-- Row 1: Office and Warehouse -->
      <div class="grid grid-cols-2 gap-lg" style="margin-bottom: 2rem; align-items: stretch;">
        <div class="premium-contact-card">
          <h3 class="premium-contact-heading"><i class="fa-solid fa-building"></i> Our Office</h3>
          <p class="premium-contact-text"><strong>Shah International</strong><br>308-313, Goldcrest Business Park,<br>Behind Kailash Esplanade, Opp. Shreyas Cinema,<br>L.B.S. Marg, Ghatkopar West,<br>Mumbai - 400086, India</p>
          <div style="margin-top: 2rem;">
            <p class="premium-contact-text" style="margin-bottom: 0.5rem;"><i class="fa-solid fa-phone" style="color: var(--color-brand-red); margin-right: 12px;"></i> (+91) 22 4099 0000</p>
            <p class="premium-contact-text" style="margin-bottom: 0.5rem;"><i class="fa-solid fa-envelope" style="color: var(--color-brand-red); margin-right: 12px;"></i> <a href="mailto:info@shahinternational.in" class="premium-contact-link">info@shahinternational.in</a></p>
            <p class="premium-contact-text"><i class="fa-brands fa-instagram" style="color: var(--color-brand-red); margin-right: 12px;"></i> <a href="https://www.instagram.com/shahinternational_india" target="_blank" class="premium-contact-link">@shahinternational_india</a></p>
          </div>
        </div>
        
        <div class="premium-contact-card">
          <h3 class="premium-contact-heading"><i class="fa-solid fa-warehouse"></i> Our Warehouse</h3>
          <p class="premium-contact-text">Shree Ganesh Comm. & Indl. Complex,<br>Bldg No.1, Gala No. 4/5, Behind Gupta Complex,<br>Dapode, Bhiwandi - 421302,<br>Dist - Thane, India</p>
        </div>
      </div>

      <!-- Row 2: Form and Map -->
      <div class="grid grid-cols-2 gap-lg" style="align-items: stretch;">
        <div class="premium-contact-card">
          <h3 class="premium-contact-heading" style="margin-bottom: 2.5rem;">Send a Message</h3>
          <form action="#" method="POST" class="contact-form">
            <div class="minimalist-input-group">
              <input type="text" id="name" name="name" class="minimalist-input" placeholder="Full Name *" required>
            </div>
            <div class="minimalist-input-group">
              <input type="email" id="email" name="email" class="minimalist-input" placeholder="Email Address *" required>
            </div>
            <div class="minimalist-input-group">
              <input type="tel" id="phone" name="phone" class="minimalist-input" placeholder="Phone Number">
            </div>
            <div class="minimalist-input-group">
              <textarea id="message" name="message" rows="3" class="minimalist-input" placeholder="Your Message *" required style="resize: vertical;"></textarea>
            </div>
            <button type="submit" class="premium-btn" style="margin-top: 1rem;">Send Message</button>
          </form>
        </div>
        
        <div class="premium-map-container">
          <iframe allowfullscreen frameborder="0" height="100%" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15080.780391163471!2d72.9061212!3d19.0990952!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c7bd0b29d5b3%3A0x66f14ce9cfa31b3a!2sSHAH%20INTERNATIONAL!5e0!3m2!1sen!2sin!4v1652921627579!5m2!1sen!2sin" style="border:0; width: 100%; min-height: 100%;"></iframe>
        </div>
      </div>
    </div>
  </section>"""

# Replace everything from <section class="page-content"> to </section> before the footer
old_chunk_match = re.search(r'<section class="page-content".*?>.*?</section>', content, re.DOTALL)
if old_chunk_match:
    new_content = content[:old_chunk_match.start()] + new_content_block + content[old_chunk_match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success! Replaced the contact section with premium UI.")
else:
    print("Error finding replacement block.")
