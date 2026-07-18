js_additions = """

/* ========== SMART HEADER ========== */
document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('shared-header');
  if (!header) return;
  
  let lastScroll = 0;
  
  window.addEventListener('scroll', () => {
    // The shared header injects a <header class="header"> inside it. We need to target that inner header.
    const innerHeader = header.querySelector('.header');
    if (!innerHeader) return;
    
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
      innerHeader.classList.remove('header-scrolled');
      return;
    }
    
    if (currentScroll > 50 && !innerHeader.classList.contains('header-scrolled')) {
      innerHeader.classList.add('header-scrolled');
    }
    
    if (currentScroll > lastScroll && currentScroll > 150) {
      // scroll down
      innerHeader.classList.add('header-hidden');
    } else if (currentScroll < lastScroll) {
      // scroll up
      innerHeader.classList.remove('header-hidden');
    }
    
    lastScroll = currentScroll;
  });
});
"""

with open(r'C:\Users\chait\OneDrive\Desktop\shahinternational\full_site\shahinternational.in\includes.js', 'a') as f:
    f.write(js_additions)
