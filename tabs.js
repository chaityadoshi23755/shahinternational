// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
  var tabBtns = document.querySelectorAll('.tab-btn');
  
  tabBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tabId = this.getAttribute('data-tab');
      
      // Deactivate all tabs
      document.querySelectorAll('.tab-btn').forEach(function(b) { b.classList.remove('active'); });
      document.querySelectorAll('.tab-panel').forEach(function(p) { p.classList.remove('active'); });
      
      // Activate clicked tab
      this.classList.add('active');
      document.getElementById('tab-' + tabId).classList.add('active');
    });
  });
});
