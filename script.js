(function () {
  // ---------- Mobile drawer ----------
  const drawer = document.getElementById('drawer');
  const setDrawer = (open) => {
    drawer.classList.toggle('open', open);
    drawer.setAttribute('aria-hidden', String(!open));
  };
  document.getElementById('menuBtn').addEventListener('click', () => setDrawer(true));
  drawer.querySelector('[data-close]').addEventListener('click', () => setDrawer(false));
  drawer.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setDrawer(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setDrawer(false); });

  // ---------- Active nav section ----------
  const navLinks = document.querySelectorAll('[data-section]');
  const sections = ['hero', 'tentang', 'resume', 'proyek', 'organisasi', 'kontak']
    .map((id) => document.getElementById(id)).filter(Boolean);
  const navIO = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      navLinks.forEach((a) => a.classList.toggle('active', a.dataset.section === e.target.id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach((s) => navIO.observe(s));

  // ---------- Skill bars (level / 10) ----------
  const skills = document.querySelectorAll('.skill');
  const skillIO = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const level = +e.target.dataset.level || 0;
      const max = +e.target.dataset.max || 10;
      e.target.querySelector('.bar > div').style.width = Math.round((level / max) * 100) + '%';
      skillIO.unobserve(e.target);
    });
  }, { threshold: 0.4 });
  skills.forEach((s) => skillIO.observe(s));

  // ---------- Portfolio overlay (tap-to-reveal on touch devices) ----------
  const isTouch = window.matchMedia('(pointer: coarse)').matches;
  document.querySelectorAll('.overlay').forEach((ov) => {
    const internal = ov.getAttribute('href') === '#proyek';
    ov.addEventListener('click', (e) => {
      if (isTouch && !ov.classList.contains('show')) {
        e.preventDefault();
        document.querySelectorAll('.overlay.show').forEach((o) => o.classList.remove('show'));
        ov.classList.add('show');
        return;
      }
      if (internal) e.preventDefault();
    });
  });

  // ---------- Organisasi carousel (scroll-snap, auto-advance 10s) ----------
  const track = document.getElementById('track');
  const items = track.querySelectorAll('.testi__item');
  const dots = document.querySelectorAll('#dots button');
  let active = 0;
  const render = () => {
    items.forEach((it, i) => it.classList.toggle('active', i === active));
    dots.forEach((d, i) => { d.classList.toggle('active', i === active); d.disabled = i === active; });
  };
  const goTo = (i) => { track.scrollLeft = track.offsetWidth * i; };
  track.addEventListener('scroll', () => {
    const i = Math.round(track.scrollLeft / track.offsetWidth);
    if (i !== active) { active = i; render(); }
  }, { passive: true });
  dots.forEach((d, i) => d.addEventListener('click', () => goTo(i)));
  setInterval(() => goTo(active + 1 >= items.length ? 0 : active + 1), 10000);
  render();

  // ---------- Contact form → opens email client (works on GitHub Pages) ----------
  document.getElementById('contactForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const f = new FormData(e.target);
    const subject = 'Pesan dari website — ' + f.get('name');
    const body = f.get('message') + '\n\n— ' + f.get('name') + ' (' + f.get('email') + ')';
    window.location.href = 'mailto:rynld.andika@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });

  document.getElementById('year').textContent = new Date().getFullYear();
})();
