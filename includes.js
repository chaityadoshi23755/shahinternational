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
  });
})();
