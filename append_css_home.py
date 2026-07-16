css = """
/* ========== Our Clients Page Specific ========== */
.special-clients-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: var(--space-md);
  margin-bottom: var(--space-md);
}

.normal-clients-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--space-md);
}

@media (max-width: 768px) {
  .special-clients-grid {
    grid-template-columns: 1fr !important;
  }
  .normal-clients-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 0.5rem;
  }
  .normal-clients-grid .card-img-wrap {
    padding: 0.5rem !important;
  }
  .normal-clients-grid .card-img {
    height: 60px !important;
  }
}

/* ========== Home Page Mobile Fixes ========== */
@media (max-width: 768px) {
  .whom-we-sell-grid {
    grid-template-columns: 1fr !important;
  }
  .who-we-are-container {
    flex-direction: column-reverse !important;
  }
  .who-we-are-img {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    height: auto !important;
  }
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a', encoding='utf-8') as f:
    f.write(css)
print("Restored CSS!")
