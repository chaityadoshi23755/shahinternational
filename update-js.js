const fs = require('fs');
const jsPath = 'C:/Users/chait/OneDrive/Desktop/shahinternational/full_site/shahinternational.in/includes.js';
let js = fs.readFileSync(jsPath, 'utf8');

const scrollRevealLogic = 
  // Scroll Reveal Logic (Premium Aesthetic)
  function initScrollReveal() {
    // Inject .reveal classes to major elements if they don't have it yet
    const elementsToReveal = document.querySelectorAll('h1, h2, .card, .product-thumbnails img, .text-center p, .principal-logo');
    elementsToReveal.forEach((el, index) => {
      if (!el.classList.contains('reveal')) {
        el.classList.add('reveal');
        // Add staggered delays for grids
        if (el.classList.contains('card') || el.parentElement.classList.contains('grid')) {
          const delayClass = 'reveal-delay-' + ((index % 3) + 1);
          el.classList.add(delayClass);
        }
      }
    });

    const observer = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    });

    document.querySelectorAll('.reveal').forEach(function(el) {
      observer.observe(el);
    });
  }
  
  // Call it on load and also after include loads to ensure elements exist
  document.addEventListener('DOMContentLoaded', initScrollReveal);
  setTimeout(initScrollReveal, 500); // safety fallback for included content
;

js = js.replace('})();', scrollRevealLogic + '\n})();');
fs.writeFileSync(jsPath, js, 'utf8');
console.log('includes.js updated successfully');
