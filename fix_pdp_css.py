import re

file_path = r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_css = """  /* ========== PDP 65/35 LOOKBOOK ========== */
  .product-detail-layout {
    grid-template-columns: 55% 45%; /* Slightly more balanced */
    align-items: start;
    gap: 3rem;
  }
  .product-image-container {
    order: -1;
  }
  .product-image-container .product-image img {
    max-height: 75vh;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  .product-info {
    position: sticky;
    top: 120px;
  }
  @media (max-width: 991px) {
    .product-detail-layout {
      grid-template-columns: 1fr;
      gap: 2rem;
    }
    .product-image-container {
      order: -1; /* Image appears ABOVE text on mobile */
    }
    .product-image-container .product-image img {
      max-height: 50vh; /* Shorter on mobile so it doesn't take the whole screen */
    }
    .product-info {
      position: static;
    }
  }
"""

old_chunk_match = re.search(r'/\* ========== PDP 65/35 LOOKBOOK ========== \*/.*?@media \(max-width: 991px\) \{.*?\}', content, re.DOTALL)
if old_chunk_match:
    # Need to match the closing brace of the media query manually
    # The regex above matches up to the first closing brace inside the media query
    # Let's just use a more robust regex or string replacement
    pass

# Simpler replacement
target = """  /* ========== PDP 65/35 LOOKBOOK ========== */
  .product-detail-layout {
    grid-template-columns: 65% 35%;
  }
  .product-image-container {
    order: -1; /* Move image to the left */
  }
  .product-info {
    position: sticky;
    top: 120px;
  }
  @media (max-width: 991px) {
    .product-detail-layout {
      grid-template-columns: 1fr;
    }
    .product-image-container {
      order: 0;
    }
    .product-info {
      position: static;
    }
  }"""

if target in content:
    new_content = content.replace(target, new_css.strip())
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success! Replaced PDP Lookbook CSS.")
else:
    print("Error: Target CSS not found.")
