import re

file_path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\contact-us.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content_block = """  <section class="page-content" style="background-color: #f8f9fa;">
    <div class="container reveal">
      <h2 class="section-heading text-center" style="margin-bottom: 3rem; font-family: 'Playfair Display', serif;">Contact Details</h2>
      
      <!-- Row 1: Office and Warehouse -->
      <div class="grid grid-cols-2 gap-lg" style="margin-bottom: 2rem; align-items: stretch;">
        <div class="card p-lg" style="background: #fff; height: 100%;">
          <h3 style="margin-bottom: 1rem; color: var(--color-brand-red); font-size: 1.5rem;">Our Office</h3>
          <p style="color: #444; line-height: 1.8;"><strong>Shah International</strong><br>308-313, Goldcrest Business Park,<br>Behind Kailash Esplanade, Opp. Shreyas Cinema,<br>L.B.S. Marg, Ghatkopar West,<br>Mumbai - 400086, India</p>
          <div style="margin-top: 1.5rem;">
            <p style="margin-bottom: 0.5rem;"><i class="fa-solid fa-phone" style="color: var(--color-brand-red); margin-right: 8px;"></i> (+91) 22 4099 0000</p>
            <p style="margin-bottom: 0.5rem;"><i class="fa-solid fa-envelope" style="color: var(--color-brand-red); margin-right: 8px;"></i> <a href="mailto:info@shahinternational.in" style="color: inherit;">info@shahinternational.in</a></p>
            <p><i class="fa-brands fa-instagram" style="color: var(--color-brand-red); margin-right: 8px;"></i> <a href="https://www.instagram.com/shahinternational_india" target="_blank" style="color: inherit;">@shahinternational_india</a></p>
          </div>
        </div>
        
        <div class="card p-lg" style="background: #fff; height: 100%;">
          <h3 style="margin-bottom: 1rem; color: var(--color-brand-red); font-size: 1.5rem;">Our Warehouse</h3>
          <p style="color: #444; line-height: 1.8;">Shree Ganesh Comm. & Indl. Complex,<br>Bldg No.1, Gala No. 4/5, Behind Gupta Complex,<br>Dapode, Bhiwandi - 421302,<br>Dist - Thane, India</p>
        </div>
      </div>

      <!-- Row 2: Form and Map -->
      <div class="grid grid-cols-2 gap-lg" style="align-items: stretch;">
        <div class="card p-lg" style="background: #fff; height: 100%;">
          <h3 style="margin-bottom: 1.5rem; font-size: 1.5rem;">Send us a Message</h3>
          <form action="#" method="POST" class="contact-form">
            <div style="margin-bottom: 1.25rem;">
              <input type="text" id="name" name="name" placeholder="Full Name *" required style="width: 100%; padding: 1rem; border: 1px solid #eee; border-radius: 4px; background: #f9f9f9; font-family: inherit;">
            </div>
            <div style="margin-bottom: 1.25rem;">
              <input type="email" id="email" name="email" placeholder="Email Address *" required style="width: 100%; padding: 1rem; border: 1px solid #eee; border-radius: 4px; background: #f9f9f9; font-family: inherit;">
            </div>
            <div style="margin-bottom: 1.25rem;">
              <input type="tel" id="phone" name="phone" placeholder="Phone Number" style="width: 100%; padding: 1rem; border: 1px solid #eee; border-radius: 4px; background: #f9f9f9; font-family: inherit;">
            </div>
            <div style="margin-bottom: 1.25rem;">
              <textarea id="message" name="message" rows="4" placeholder="Your Message *" required style="width: 100%; padding: 1rem; border: 1px solid #eee; border-radius: 4px; background: #f9f9f9; resize: vertical; font-family: inherit;"></textarea>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center; padding: 1rem; font-size: 1.1rem;">Send Message</button>
          </form>
        </div>
        
        <div class="card" style="padding: 0; overflow: hidden; border-radius: var(--radius-md); box-shadow: var(--shadow-md); height: 100%; min-height: 400px;">
          <iframe allowfullscreen frameborder="0" height="100%" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15080.780391163471!2d72.9061212!3d19.0990952!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c7bd0b29d5b3%3A0x66f14ce9cfa31b3a!2sSHAH%20INTERNATIONAL!5e0!3m2!1sen!2sin!4v1652921627579!5m2!1sen!2sin" style="border:0; width: 100%; min-height: 100%;"></iframe>
        </div>
      </div>
    </div>
  </section>"""

# Replace everything from <section class="page-content"> to </section> before the footer
old_chunk_match = re.search(r'<section class="page-content">.*?</section>', content, re.DOTALL)
if old_chunk_match:
    new_content = content[:old_chunk_match.start()] + new_content_block + content[old_chunk_match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success! Replaced the contact section.")
else:
    print("Error finding replacement block.")
