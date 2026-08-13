// Page-wide constellation/network background -- gold nodes, thin connecting lines, gentle
// drift, plus a slow parallax shift tied to scroll position. Fixed to the viewport so it stays
// visible behind every section as the page scrolls. Always animates, regardless of the
// visitor's reduced-motion preference (an explicit design choice, not an oversight).
(function () {
  var canvas = document.querySelector('.page-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

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
    var margin = 80;
    var maxSpeed = 0.35;
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];

      // gentle random wander so direction changes feel organic, not mechanical
      n.vx += (Math.random() - 0.5) * 0.01;
      n.vy += (Math.random() - 0.5) * 0.01;

      // soft steering back inward near the edges instead of a hard velocity-flip bounce
      if (n.x < margin) n.vx += 0.006;
      if (n.x > W - margin) n.vx -= 0.006;
      if (n.y < margin) n.vy += 0.006;
      if (n.y > H - margin) n.vy -= 0.006;

      // clamp speed so the drift stays smooth and consistent, never jumpy
      var speed = Math.sqrt(n.vx * n.vx + n.vy * n.vy);
      if (speed > maxSpeed) {
        n.vx = (n.vx / speed) * maxSpeed;
        n.vy = (n.vy / speed) * maxSpeed;
      }

      n.x += n.vx;
      n.y += n.vy;
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
  requestAnimationFrame(loop);
  window.addEventListener('scroll', onScroll, { passive: true });

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
