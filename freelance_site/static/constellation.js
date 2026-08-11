// Page-wide constellation/network background -- gold nodes, thin connecting lines, gentle
// drift, plus a slow parallax shift tied to scroll position. Fixed to the viewport so it stays
// visible behind every section as the page scrolls. Respects prefers-reduced-motion (static
// frame, no drift animation, no parallax).
(function () {
  var canvas = document.querySelector('.page-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var W, H, DPR;
  var nodes = [];
  var NODE_COUNT = 60;
  var LINK_DIST = 150;
  var GOLD = '201, 161, 90';
  var BASE_ALPHA = 0.4;

  function resize() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * DPR;
    canvas.height = H * DPR;
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  function seed() {
    nodes = [];
    for (var i = 0; i < NODE_COUNT; i++) {
      nodes.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.12,
        vy: (Math.random() - 0.5) * 0.12,
        r: Math.random() * 1.4 + 0.8
      });
    }
  }

  function step() {
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      n.x += n.vx;
      n.y += n.vy;
      if (n.x < 0 || n.x > W) n.vx *= -1;
      if (n.y < 0 || n.y > H) n.vy *= -1;
    }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    for (var i = 0; i < nodes.length; i++) {
      for (var j = i + 1; j < nodes.length; j++) {
        var a = nodes[i], b = nodes[j];
        var dx = a.x - b.x, dy = a.y - b.y;
        var dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < LINK_DIST) {
          ctx.strokeStyle = 'rgba(' + GOLD + ', ' + (1 - dist / LINK_DIST) * BASE_ALPHA + ')';
          ctx.lineWidth = 0.6;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }
    for (var k = 0; k < nodes.length; k++) {
      var n2 = nodes[k];
      ctx.fillStyle = 'rgba(' + GOLD + ', 0.8)';
      ctx.beginPath();
      ctx.arc(n2.x, n2.y, n2.r, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function loop() {
    step();
    draw();
    requestAnimationFrame(loop);
  }

  // Slow parallax: the whole canvas drifts a little as you scroll, so the background feels
  // alive while you move through the page, not just while sitting still on the hero.
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var shift = window.scrollY * 0.06;
      canvas.style.transform = 'translateY(' + shift + 'px)';
      ticking = false;
    });
  }

  resize();
  seed();
  draw();
  if (!reduced) {
    requestAnimationFrame(loop);
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      resize();
      seed();
      draw();
    }, 200);
  });
})();
