(function(){
  "use strict";
  var $ = function(s){ return document.querySelector(s); };
  var $$ = function(s){ return Array.prototype.slice.call(document.querySelectorAll(s)); };
  var fine = window.matchMedia('(pointer:fine)').matches;

  /* ---------- preloader ---------- */
  var pre = $('#preloader'), pc = $('#preCount');
  if (pre){
    var p = 0;
    var pt = setInterval(function(){
      p = Math.min(100, p + Math.ceil(Math.random()*16));
      pc.textContent = String(p).padStart(3,'0');
      if (p >= 100){
        clearInterval(pt);
        setTimeout(function(){
          pre.classList.add('done');
          document.body.classList.add('loaded');
          setTimeout(function(){ pre.remove(); }, 900);
        }, 180);
      }
    }, 55);
  } else {
    document.body.classList.add('loaded');
  }

  /* ---------- reveal on scroll ---------- */
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: .12 });
  $$('[data-reveal]').forEach(function(el){ io.observe(el); });

  /* ---------- counters ---------- */
  function animCount(el){
    var target = parseFloat(el.getAttribute('data-count'));
    var dec = parseInt(el.getAttribute('data-dec') || '0', 10);
    var dur = 1600, st = null;
    function f(n){
      if (st === null) st = n;
      var k = Math.min(1, (n - st) / dur);
      var e = 1 - Math.pow(1 - k, 3);
      el.textContent = (target * e).toLocaleString('en-NG', { minimumFractionDigits: dec, maximumFractionDigits: dec });
      if (k < 1) requestAnimationFrame(f);
    }
    requestAnimationFrame(f);
  }
  var cio = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if (e.isIntersecting){ animCount(e.target); cio.unobserve(e.target); }
    });
  }, { threshold: .6 });
  $$('[data-count]').forEach(function(el){ cio.observe(el); });

  /* ---------- cursor ---------- */
  if (fine){
    var dot = $('#cDot'), ring = $('#cRing');
    if (dot && ring){
      var mx = innerWidth/2, my = innerHeight/2, rx = mx, ry = my;
      addEventListener('mousemove', function(e){ mx = e.clientX; my = e.clientY; });
      (function loop(){
        rx += (mx - rx) * .16; ry += (my - ry) * .16;
        dot.style.transform = 'translate(' + mx + 'px,' + my + 'px)';
        ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px)';
        requestAnimationFrame(loop);
      })();
      $$('a,button,input,select,textarea').forEach(function(el){
        el.addEventListener('mouseenter', function(){ ring.classList.add('big'); });
        el.addEventListener('mouseleave', function(){ ring.classList.remove('big'); });
      });
    }
  }

  /* ---------- magnetic buttons ---------- */
  $$('.magnet').forEach(function(el){
    el.addEventListener('mousemove', function(e){
      var r = el.getBoundingClientRect();
      var x = (e.clientX - r.left - r.width/2) * .18;
      var y = (e.clientY - r.top - r.height/2) * .3;
      el.style.transform = 'translate(' + x + 'px,' + y + 'px)';
    });
    el.addEventListener('mouseleave', function(){ el.style.transform = ''; });
  });

  /* ---------- scroll progress ---------- */
  var prog = $('#progress');
  if (prog){
    addEventListener('scroll', function(){
      var h = document.documentElement;
      var k = h.scrollTop / (h.scrollHeight - h.clientHeight || 1);
      prog.style.width = (k * 100) + '%';
    }, { passive: true });
  }

  /* ---------- lagos clock ---------- */
  var clockEl = $('#lagosTime');
  if (clockEl){
    var tick = function(){
      clockEl.textContent = new Intl.DateTimeFormat('en-GB', {
        timeZone: 'Africa/Lagos', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
      }).format(new Date());
    };
    tick(); setInterval(tick, 1000);
  }

  /* ---------- film modal ---------- */
  var modal = $('#filmModal');
  if (modal){
    var slides = $$('.film-slide'), fi = 0, ft = null;
    var nextSlide = function(){
      slides[fi].classList.remove('on');
      fi = (fi + 1) % slides.length;
      slides[fi].classList.add('on');
    };
    var closeFilm = function(){
      modal.classList.remove('open');
      document.body.style.overflow = '';
      clearInterval(ft);
    };
    $$('.js-film').forEach(function(b){
      b.addEventListener('click', function(){
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
        ft = setInterval(nextSlide, 2800);
      });
    });
    $('#filmClose').addEventListener('click', closeFilm);
    modal.addEventListener('click', function(e){ if (e.target === modal) closeFilm(); });
    addEventListener('keydown', function(e){ if (e.key === 'Escape') closeFilm(); });
  }

  /* ---------- hover image preview on rows ---------- */
  var prev = $('#hoverPrev'), pimg = $('#hoverImg');
  if (fine && prev && pimg){
    $$('.sys-row').forEach(function(row){
      row.addEventListener('mouseenter', function(){
        pimg.src = row.getAttribute('data-img');
        prev.classList.add('on');
      });
      row.addEventListener('mouseleave', function(){ prev.classList.remove('on'); });
    });
    addEventListener('mousemove', function(e){
      if (!prev.classList.contains('on')) return;
      var w = 340, h = 255;
      var x = Math.min(innerWidth - w - 16, e.clientX + 28);
      var y = Math.max(16, Math.min(innerHeight - h - 16, e.clientY - h/2));
      prev.style.transform = 'translate(' + x + 'px,' + y + 'px) scale(1)';
    });
  }

  /* ---------- reviews carousel ---------- */
  var revTrack = $('#revTrack');
  if (revTrack){
    var cards = $$('.rev-card'), dotsWrap = $('#revDots');
    var idx = 0;
    function visible(){
      if (innerWidth <= 760) return 1;
      if (innerWidth <= 1080) return 2;
      return 3;
    }
    function maxIdx(){ return Math.max(0, cards.length - visible()); }
    function buildDots(){
      dotsWrap.innerHTML = '';
      for (var i = 0; i <= maxIdx(); i++){
        (function(i){
          var b = document.createElement('button');
          b.setAttribute('aria-label', 'Go to slide ' + (i+1));
          b.addEventListener('click', function(){ idx = i; layout(); });
          dotsWrap.appendChild(b);
        })(i);
      }
    }
    function layout(){
      idx = Math.min(idx, maxIdx());
      var step = cards[0].getBoundingClientRect().width + 24;
      revTrack.style.transform = 'translateX(' + (-idx * step) + 'px)';
      $$('#revDots button').forEach(function(b, i){ b.classList.toggle('on', i === idx); });
    }
    $('#revPrev').addEventListener('click', function(){ idx = Math.max(0, idx - 1); layout(); });
    $('#revNext').addEventListener('click', function(){ idx = Math.min(maxIdx(), idx + 1); layout(); });
    addEventListener('resize', function(){ buildDots(); layout(); });
    buildDots(); layout();
    /* Autoplay pauses while the reader is in the carousel. The review
       bodies scroll, so sliding the track out from under someone who is
       part-way through one would be hostile. Also honours reduced-motion
       and stops entirely when the tab is hidden. */
    var timer = null;
    var reduce = matchMedia('(prefers-reduced-motion:reduce)');
    var section = revTrack.closest ? revTrack.closest('.reviews') : null;
    function play(){
      if (timer || reduce.matches || document.hidden) return;
      timer = setInterval(function(){ idx = idx >= maxIdx() ? 0 : idx + 1; layout(); }, 6000);
    }
    function pause(){ if (timer){ clearInterval(timer); timer = null; } }
    if (section){
      ['mouseenter','focusin','touchstart'].forEach(function(ev){
        section.addEventListener(ev, pause, {passive:true});
      });
      ['mouseleave','focusout'].forEach(function(ev){
        section.addEventListener(ev, play);
      });
    }
    document.addEventListener('visibilitychange', function(){
      document.hidden ? pause() : play();
    });
    play();
  }

  /* ---------- accordions (services + faq) ---------- */
  $$('[data-acc]').forEach(function(container){
    var items = $$('.acc-item, .faq-item').filter(function(i){ return container.contains(i); });
    var stage = container.getAttribute('data-stage') ? $(container.getAttribute('data-stage')) : null;
    var stageImgs = stage ? Array.prototype.slice.call(stage.querySelectorAll('img')) : [];
    items.forEach(function(item, n){
      var head = item.querySelector('button');
      var body = item.querySelector('.acc-body, .faq-a');
      head.addEventListener('click', function(){
        var isOpen = item.classList.contains('open');
        items.forEach(function(o){
          o.classList.remove('open');
          var ob = o.querySelector('.acc-body, .faq-a');
          if (ob) ob.style.maxHeight = null;
        });
        if (stageImgs.length) stageImgs.forEach(function(im){ im.classList.remove('on'); });
        if (!isOpen){
          item.classList.add('open');
          body.style.maxHeight = body.scrollHeight + 'px';
          if (stageImgs[n]){
            stageImgs[n].classList.add('on');
            /* The caption sits inside the image, so it has to follow the
               image. It was static, which meant every service showed the
               same specification line. */
            var cap = stage.querySelector('.cap');
            var text = stageImgs[n].getAttribute('data-cap');
            if (cap && text) cap.textContent = text;
          }
        }
      });
    });
    if (items[0]){ items[0].querySelector('button').click(); }
  });

  /* ---------- calculator ---------- */
  var sizeR = $('#sizeRange');
  if (sizeR){
    var usageR = $('#usageRange');
    var rates = {
      NGN: { yieldKwh: 1350, valKwh: 420, exportShare: .15, costKw: 850000, co2Kg: .55, locale: 'en-NG' },
      USD: { yieldKwh: 1200, valKwh: .16, exportShare: .30, costKw: 1000,   co2Kg: .40, locale: 'en-US' },
      GBP: { yieldKwh: 900,  valKwh: .26, exportShare: .40, costKw: 1500,   co2Kg: .20, locale: 'en-GB' }
    };
    var cur = 'NGN';
    function fmtMoney(v){
      return new Intl.NumberFormat(rates[cur].locale, { style: 'currency', currency: cur, maximumFractionDigits: 0 }).format(v);
    }
    function compute(){
      var r = rates[cur];
      var kw = parseFloat(sizeR.value);
      var usage = parseFloat(usageR.value);
      var prod = kw * r.yieldKwh;
      var self = Math.min(prod, usage);
      var exp = prod - self;
      var sav = self * r.valKwh + exp * r.valKwh * r.exportShare;
      var cost = kw * r.costKw;
      var pay = cost / sav;
      var co2 = prod * r.co2Kg / 1000;

      $('#sizeVal').textContent = kw.toFixed(1) + ' kW';
      $('#usageVal').textContent = usage.toLocaleString('en-NG') + ' kWh/yr';
      $('#savingsOut').textContent = fmtMoney(sav);
      $('#paybackOut').textContent = pay.toFixed(1) + ' YRS';
      $('#co2Out').textContent = co2.toFixed(1) + ' T/YR';

      var W = 220, H = 56, N = 25, pts = [];
      var min = -cost, max = N * sav - cost;
      for (var y = 0; y <= N; y++){
        var v = y * sav - cost;
        pts.push([ y / N * W, H - 6 - ((v - min) / (max - min)) * (H - 12) ]);
      }
      var d = pts.map(function(pt, i){ return (i ? 'L' : 'M') + pt[0].toFixed(1) + ' ' + pt[1].toFixed(1); }).join(' ');
      $('#sparkPath').setAttribute('d', d);
      $('#sparkFill').setAttribute('d', d + ' L' + W + ' ' + H + ' L0 ' + H + ' Z');
      var zy = H - 6 - ((0 - min) / (max - min)) * (H - 12);
      $('#zeroLine').setAttribute('y1', zy); $('#zeroLine').setAttribute('y2', zy);
      var payX = Math.min(1, pay / N) * W;
      var payY = H - 6 - ((pay * sav - cost - min) / (max - min)) * (H - 12);
      $('#payDot').setAttribute('cx', payX); $('#payDot').setAttribute('cy', payY.toFixed(1));
    }
    sizeR.addEventListener('input', compute);
    usageR.addEventListener('input', compute);
    $$('.cur-toggle button').forEach(function(b){
      b.addEventListener('click', function(){
        $$('.cur-toggle button').forEach(function(x){ x.classList.remove('on'); });
        b.classList.add('on');
        cur = b.getAttribute('data-cur');
        compute();
      });
    });
    compute();
  }

  /* ---------- quote form ---------- */
  var form = $('#quoteForm');
  if (form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var ok = true;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function(f){
        var field = f.closest('.f-field');
        var valid = f.value.trim() !== '';
        if (f.type === 'email' && valid) valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value);
        field.classList.toggle('bad', !valid);
        if (!valid) ok = false;
      });
      if (ok){
        form.style.display = 'none';
        $('#formSuccess').style.display = 'block';
      }
    });
  }

  /* ---------- mobile menu ----------
     The drawer is shown/hidden with a class rather than the hidden
     attribute so it can transition. Because it uses visibility:hidden
     when closed, its links are unfocusable and no inert polyfill is
     needed. Focus is moved into the drawer on open, trapped while it is
     open, and handed back to the burger on close. */
  var burger = $('#navBurger'), drawer = $('#mobileMenu'),
      scrim  = $('#navScrim'),  navBar = document.querySelector('.nav');

  if (burger && drawer && navBar){
    var FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';

    function drawerFocusables(){
      return Array.prototype.slice.call(drawer.querySelectorAll(FOCUSABLE))
        .filter(function(el){ return el.offsetParent !== null; });
    }
    function menuOpen(){ return navBar.classList.contains('menu-open'); }

    function setMenu(open, returnFocus){
      navBar.classList.toggle('menu-open', open);
      if (scrim) scrim.classList.toggle('is-open', open);
      document.body.classList.toggle('menu-lock', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (open){
        /* The drawer's own height cap cannot be expressed in CSS: it sits
           below a utility bar that may or may not be scrolled away, so the
           space beneath it is only known at open time. */
        drawer.style.maxHeight =
          Math.max(240, window.innerHeight - drawer.getBoundingClientRect().top - 12) + 'px';
        /* visibility has not flipped to visible in the same frame the class
           is added, and a visibility:hidden element cannot take focus, so
           move focus on the next frame. */
        requestAnimationFrame(function(){
          var first = drawerFocusables()[0];
          if (first) first.focus();
        });
      } else if (returnFocus){
        burger.focus();
      }
    }

    burger.addEventListener('click', function(){ setMenu(!menuOpen(), true); });
    if (scrim) scrim.addEventListener('click', function(){ setMenu(false, true); });

    /* Submenu accordions inside the drawer. */
    $$('.md-toggle').forEach(function(btn){
      btn.addEventListener('click', function(){
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        if (!panel) return;
        var isOpen = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
        if (isOpen) panel.setAttribute('hidden', ''); else panel.removeAttribute('hidden');
      });
    });

    /* Following a link closes the menu — matters for same-page anchors,
       where no navigation happens to close it for us. */
    $$('#mobileMenu a').forEach(function(a){
      a.addEventListener('click', function(){ setMenu(false, false); });
    });

    document.addEventListener('keydown', function(e){
      if (!menuOpen()) return;
      if (e.key === 'Escape'){ e.preventDefault(); setMenu(false, true); return; }
      if (e.key !== 'Tab') return;
      var items = drawerFocusables();
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      /* Keep Tab inside the drawer, including the burger itself so the
         close control stays reachable. */
      if (e.shiftKey && (document.activeElement === first || document.activeElement === burger)){
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && document.activeElement === last){
        e.preventDefault(); burger.focus();
      }
    });

    /* Crossing back to the desktop layout must not leave the page
       scroll-locked behind an invisible drawer. */
    var mq = window.matchMedia('(min-width:961px)');
    var onWide = function(e){ if (e.matches && menuOpen()) setMenu(false, false); };
    if (mq.addEventListener) mq.addEventListener('change', onWide);
    else if (mq.addListener) mq.addListener(onWide);
  }
})();
