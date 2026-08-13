// Mobile nav toggle.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('mobile-nav');
  if (!toggle || !menu) return;
  toggle.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  menu.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
})();

// Share widget: copy-link button, and close the <details> menu on outside click.
(function () {
  var widget = document.querySelector('.share-widget');
  var copyBtn = document.querySelector('.share-copy');
  if (!widget) return;

  document.addEventListener('click', function (e) {
    if (e.target.closest('.share-widget')) return;
    widget.open = false;
  });

  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var url = copyBtn.getAttribute('data-url');
      navigator.clipboard.writeText(url).then(function () {
        var label = copyBtn.querySelector('.share-copy-label');
        var original = label.textContent;
        label.textContent = 'Link Copied!';
        setTimeout(function () { label.textContent = original; }, 1800);
      });
    });
  }
})();
