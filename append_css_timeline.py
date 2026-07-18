css_timeline = """
/* ========== COMPANY JOURNEY TIMELINE ========== */
.timeline {
  position: relative;
  max-width: 800px;
  margin: 4rem auto;
  padding-left: 2rem;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 2px;
  background-color: #e0e0e0;
}

.timeline-item {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 2rem;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -29px; /* 2px width line + padding adjustment to center the dot */
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: #fff;
  border: 4px solid var(--color-brand-red);
  box-shadow: 0 0 0 4px rgba(209, 42, 42, 0.1);
  transition: all 0.3s ease;
}

.timeline-item:hover::before {
  background-color: var(--color-brand-red);
  box-shadow: 0 0 0 6px rgba(209, 42, 42, 0.2);
}

.timeline-year {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-brand-red);
  font-family: 'Playfair Display', serif;
  margin-bottom: 0.5rem;
}

.timeline-content {
  background: #fff;
  padding: 1.5rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}

.timeline-content h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.timeline-content p {
  color: var(--color-text-muted);
  font-size: 1rem;
  margin: 0;
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a') as f:
    f.write(css_timeline)
