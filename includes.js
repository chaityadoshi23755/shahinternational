// Loads the shared header and footer into every page from header.html / footer.html.
// To update the navigation or footer site-wide, edit those two files only.
(function () {
  function highlightActiveNav() {
    var path = window.location.pathname;
    var current = path.substring(path.lastIndexOf('/') + 1);
    if (current === '') {
      current = 'index.html';
    }
    var links = document.querySelectorAll('#header a[href], #cd-lateral-nav a[href]');
    links.forEach(function (link) {
      var href = link.getAttribute('href');
      if (href === current) {
        link.classList.add('is-active');
      }
    });
  }

  function loadInclude(placeholderId, url, callback) {
    var el = document.getElementById(placeholderId);
    if (!el) return;
    fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load ' + url);
        return res.text();
      })
      .then(function (html) {
        el.outerHTML = html;
        if (callback) callback();
      })
      .catch(function (err) {
        console.error(err);
      });
  }

  document.addEventListener('DOMContentLoaded', function () {
    loadInclude('shared-header', 'header.html', highlightActiveNav);
    loadInclude('shared-footer', 'footer.html');

    // Image Magnifier logic for Product Detail Pages
    var mainImg = document.getElementById('main-product-image');
    if (mainImg) {
      var container = mainImg.parentElement;
      container.style.position = 'relative';

      var glass = document.createElement('DIV');
      glass.setAttribute('class', 'img-magnifier-glass');
      container.insertBefore(glass, mainImg);

      var zoom = 2; // Zoom level

      function showGlass(e) {
        glass.style.display = 'block';
        container.style.cursor = 'none';
        if (e) moveGlass(e);
      }

      function hideGlass() {
        glass.style.display = 'none';
        container.style.cursor = '';
      }

      function moveGlass(e) {
        if (e.cancelable) e.preventDefault(); // Prevent scrolling on touch
        
        var bgUrl = 'url("' + mainImg.src + '")';
        if (glass.style.backgroundImage !== bgUrl) {
          glass.style.backgroundImage = bgUrl;
          glass.style.backgroundRepeat = 'no-repeat';
          glass.style.backgroundSize = (mainImg.width * zoom) + 'px ' + (mainImg.height * zoom) + 'px';
        }

        var rect = mainImg.getBoundingClientRect();
        
        var clientX = e.clientX;
        var clientY = e.clientY;
        
        if (e.touches && e.touches.length > 0) {
           clientX = e.touches[0].clientX;
           clientY = e.touches[0].clientY;
        }

        var x = clientX - rect.left;
        var y = clientY - rect.top;
        
        var w = glass.offsetWidth / 2;
        var h = glass.offsetHeight / 2;

        var bgX = x;
        var bgY = y;
        
        if (bgX > mainImg.width - (w / zoom)) { bgX = mainImg.width - (w / zoom); }
        if (bgX < w / zoom) { bgX = w / zoom; }
        if (bgY > mainImg.height - (h / zoom)) { bgY = mainImg.height - (h / zoom); }
        if (bgY < h / zoom) { bgY = h / zoom; }

        glass.style.left = (x - w) + 'px';
        glass.style.top = (y - h) + 'px';
        glass.style.backgroundPosition = '-' + ((bgX * zoom) - w) + 'px -' + ((bgY * zoom) - h) + 'px';
      }

      container.addEventListener('mouseenter', showGlass);
      container.addEventListener('touchstart', showGlass, {passive: false});
      
      container.addEventListener('mouseleave', hideGlass);
      container.addEventListener('touchend', hideGlass);
      container.addEventListener('touchcancel', hideGlass);
      
      container.addEventListener('mousemove', moveGlass);
      container.addEventListener('touchmove', moveGlass, {passive: false});
    }
  });

  // Auto lazy-scroll to main content for Product and Category pages
  window.addEventListener('load', function() {
    var mainImage = document.getElementById('main-product-image');
    var cardGrid = document.querySelector('.card-grid');
    var pageContent = document.querySelector('.page-content');
    
    // If it's a PDP, Category page, or About Us, and we have a content section
    var isAboutUs = window.location.pathname.toLowerCase().indexOf('about-us') !== -1;
    if ((mainImage || cardGrid || isAboutUs) && pageContent) {
      setTimeout(function() {
        // Only auto-scroll if the user hasn't already scrolled down manually
        if (window.scrollY < 50) {
          var headerEl = document.getElementById('header');
          var headerOffset = headerEl ? headerEl.offsetHeight : 80;
          var elementPosition = pageContent.getBoundingClientRect().top;
          var offsetPosition = elementPosition + window.scrollY - headerOffset;
          
          window.scrollTo({
             top: offsetPosition,
             behavior: 'smooth'
          });
        }
      }, 800); // 800ms delay lets them appreciate the banner first
    }
  });

  // Handle color thumbnail clicks on category cards
  var cardThumbnails = document.querySelectorAll('.card-thumbnail');
  cardThumbnails.forEach(function(thumb) {
    thumb.addEventListener('click', function(e) {
      e.preventDefault(); // Prevent navigating to PDP immediately
      e.stopPropagation(); // Prevent the parent <a> from firing
      
      // Remove active class from siblings
      var siblings = this.parentElement.querySelectorAll('.card-thumbnail');
      siblings.forEach(function(el) { el.classList.remove('active'); });
      this.classList.add('active');
      
      // Change the main card image
      var card = this.closest('.card');
      var cardImg = card.querySelector('.card-img');
      if (cardImg) {
        cardImg.src = this.dataset.full;
      }
      
      // Update the card link with the color parameter
      var originalHref = card.getAttribute('href').split('?')[0];
      card.setAttribute('href', originalHref + '?color=' + this.dataset.index);
    });
  });

  // Pre-select color on PDP load if ?color= is present in URL
  window.addEventListener('load', function() {
    if (window.location.search.indexOf('color=') !== -1) {
      var urlParams = new URLSearchParams(window.location.search);
      var colorParam = urlParams.get('color');
      if (colorParam !== null) {
        var pdpThumbs = document.querySelectorAll('.gallery-thumb');
        var index = parseInt(colorParam, 10);
        if (!isNaN(index) && index >= 0 && index < pdpThumbs.length) {
          // Trigger click on the correct thumbnail to pre-select it
          pdpThumbs[index].click();
        }
      }
    }
  });
})();

// Mobile menu functions (must be global because they are called from inline onclick handlers)
window.openMobileMenu = function() {
  document.getElementById('mobileNav').classList.add('is-open');
  document.getElementById('mobileOverlay').classList.add('is-open');
  document.body.style.overflow = 'hidden';
};
window.closeMobileMenu = function() {
  document.getElementById('mobileNav').classList.remove('is-open');
  document.getElementById('mobileOverlay').classList.remove('is-open');
  document.body.style.overflow = '';
};
window.toggleMobileDropdown = function(btn) {
  var sub = btn.nextElementSibling;
  sub.classList.toggle('is-open');
  var icon = btn.querySelector('i');
  icon.style.transform = sub.classList.contains('is-open') ? 'rotate(180deg)' : '';
};
