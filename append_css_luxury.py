css_overrides = """
/* ========== LUXURY UI OVERRIDES (Whitespace, Typography, Hover) ========== */

:root {
  /* Increase breathing room (Negative Space) */
  --space-md: 3rem;
  --space-lg: 5rem;
  --space-xl: 8rem;
}

/* Typography Enhancements */
h1, .hero h1 {
  font-size: clamp(3rem, 6vw, 4.5rem);
  letter-spacing: -0.03em;
  font-weight: 700;
}

h2, .section-heading {
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  letter-spacing: -0.02em;
}

h3 {
  font-size: clamp(1.75rem, 3vw, 2.25rem);
}

p {
  line-height: 1.8;
  font-size: 1.125rem;
  color: #333; /* Stark contrast */
}

/* Enhancing the App-like Hover Effects */
.btn {
  transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.3s ease;
}

.btn:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.card {
  transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
}

.card-img-wrap {
  overflow: hidden;
}

.card:hover .card-img {
  transform: scale(1.05);
  transition: transform 0.7s cubic-bezier(0.165, 0.84, 0.44, 1);
}

/* Base state for scroll animations */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
  will-change: opacity, transform;
}

.reveal.active {
  opacity: 1;
  transform: translateY(0);
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a') as f:
    f.write(css_overrides)
