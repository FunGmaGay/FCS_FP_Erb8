// Simple two-panel slider for #slide-card
document.addEventListener('DOMContentLoaded', function () {
  const card = document.getElementById('slide-card');
  if (!card) return;

  const btnShowRegister = document.getElementById('show-register-btn');
  const btnShowLogin = document.getElementById('show-login-btn');

  function showPanel(panel, push = true) {
    if (panel === 'login' || panel === 'right') {
      card.classList.add('show-right');
      if (push) updateHash('login');
      focusFirst('#slide-card .slide-right input');
    } else {
      card.classList.remove('show-right');
      if (push) updateHash('register');
      focusFirst('#slide-card .slide-left input');
    }
  }

  function updateHash(v) {
    try { history.replaceState(null, '', '#' + v); } catch (e) { location.hash = v; }
  }

  function getInitial() {
    const d = card.dataset.initialPanel;
    if (d) return d.toLowerCase();
    if (location.hash) {
      const h = location.hash.replace('#', '').toLowerCase();
      if (h === 'login' || h === 'register') return h;
    }
    return 'register';
  }

  function focusFirst(sel) {
    try { const el = document.querySelector(sel); if (el) el.focus(); } catch (e) {}
  }

  if (btnShowRegister) btnShowRegister.addEventListener('click', (e) => { e.preventDefault(); showPanel('register'); });
  if (btnShowLogin) btnShowLogin.addEventListener('click', (e) => { e.preventDefault(); showPanel('login'); });

  // init (do not push history)
  showPanel(getInitial(), false);

  window.addEventListener('popstate', () => {
    const panel = location.hash ? location.hash.replace('#', '') : getInitial();
    showPanel(panel, false);
  });
});