css_premium = """
/* ========== PREMIUM CONTACT UI ========== */
.premium-contact-card {
  background: #fff;
  border: 1px solid #eaeaea;
  border-radius: var(--radius-md);
  padding: 3rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
}

.premium-contact-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.06);
}

.premium-contact-heading {
  font-family: 'Playfair Display', serif;
  font-size: 1.75rem;
  color: #111;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.premium-contact-heading i {
  color: var(--color-brand-red);
  font-size: 1.2rem;
}

.premium-contact-text {
  color: #555;
  line-height: 1.9;
  font-size: 1.05rem;
  font-weight: 300;
}

.premium-contact-text strong {
  color: #111;
  font-weight: 600;
}

.premium-contact-link {
  color: #555;
  text-decoration: none;
  transition: color 0.3s ease;
}

.premium-contact-link:hover {
  color: var(--color-brand-red);
}

/* Minimalist Form Inputs */
.minimalist-input-group {
  margin-bottom: 2rem;
  position: relative;
}

.minimalist-input {
  width: 100%;
  padding: 10px 0;
  font-size: 1rem;
  color: #111;
  border: none;
  border-bottom: 1px solid #ccc;
  outline: none;
  background: transparent;
  transition: border-color 0.3s ease;
  font-family: var(--font-body);
}

.minimalist-input::placeholder {
  color: #999;
  font-weight: 300;
}

.minimalist-input:focus {
  border-bottom: 2px solid var(--color-brand-red);
}

.premium-btn {
  background-color: #111;
  color: #fff;
  border: none;
  padding: 1rem 2.5rem;
  font-size: 0.95rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  font-weight: 600;
  transition: background-color 0.3s ease;
  cursor: pointer;
  width: 100%;
  border-radius: 4px;
}

.premium-btn:hover {
  background-color: var(--color-brand-red);
}

.premium-map-container {
  border-radius: var(--radius-md);
  overflow: hidden;
  height: 100%;
  min-height: 400px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.06);
  border: 1px solid #eaeaea;
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a') as f:
    f.write(css_premium)
