document.addEventListener("DOMContentLoaded", () => {
  const revealElements = document.querySelectorAll(".reveal");

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: "0px",
    threshold: 0.15 
  });

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // Rolling Numbers Counter Observer
  const counters = document.querySelectorAll('.counter');
  const speed = 100; // The lower the slower
  
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = +counter.getAttribute('data-target');
        
        const updateCount = () => {
          const current = +counter.innerText;
          const inc = target / speed;
          
          if (current < target) {
            counter.innerText = Math.ceil(current + inc);
            setTimeout(updateCount, 20);
          } else {
            counter.innerText = target;
          }
        };
        
        updateCount();
      } else {
        entry.target.innerText = '0';
      }
    });
  }, { threshold: 0.5 });
  
  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

});
