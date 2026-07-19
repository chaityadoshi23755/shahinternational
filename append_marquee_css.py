css_marquee = """
/* ========== MARQUEE SECTION ========== */
.marquee-section {
  background-color: var(--color-brand-red);
  padding: 4rem 0;
  color: #fff;
  overflow: hidden;
  position: relative;
}
.marquee-section h2 {
  color: #fff;
  margin-bottom: 3rem;
  font-family: 'Playfair Display', serif;
}
.marquee-container {
  display: flex;
  width: 200%; /* Enough width for the duplicated items */
  animation: marqueeScroll 20s linear infinite;
}
.marquee-container:hover {
  animation-play-state: paused;
}
.marquee-item {
  flex: 0 0 auto;
  width: 250px;
  margin: 0 1rem;
  background-color: #fff;
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 120px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.marquee-item img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); } /* Scrolls exactly half the width (one full set) */
}

/* Optional green bar at the bottom like the image */
.marquee-bottom-bar {
  height: 20px;
  background-color: #4CAF50; /* Adjust to match the green in the image */
  width: 100%;
}
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\style.css', 'a') as f:
    f.write(css_marquee)
