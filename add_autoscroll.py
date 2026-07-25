js_code = """

// ==========================================
// V3 BANNER AUTO SCROLL
// ==========================================
document.addEventListener('DOMContentLoaded', function() {
  var banner = document.querySelector('.page-banner');
  // Check if we are at the top of the page (no hash in URL, and scrollY is 0)
  if (banner && !window.location.hash && window.scrollY === 0) {
    // Wait a brief moment so the user registers the banner before scrolling
    setTimeout(function() {
      // Calculate where to scroll to, leaving space for the sticky header
      var headerHeight = document.getElementById('shared-header') ? 80 : 0;
      var targetPosition = banner.offsetHeight - headerHeight;
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }, 1200); // 1.2 second delay
  }
});
"""

with open('includes.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print("Added banner auto-scroll script to includes.js")
