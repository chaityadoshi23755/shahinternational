css_overrides = """
/* ========== SMART HEADER ========== */
.header {
  transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.4s ease;
}
.header-hidden {
  transform: translateY(-100%);
}
.header-scrolled {
  background-color: rgba(255, 255, 255, 0.95) !important;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

/* ========== PDP 65/35 LOOKBOOK ========== */
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
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a') as f:
    f.write(css_overrides)
