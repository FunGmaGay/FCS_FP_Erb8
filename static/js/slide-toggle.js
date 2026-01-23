// Slide toggle (overlay pattern), namespaced to #slide-wrap
document.addEventListener('DOMContentLoaded', function () {
  const wrap = document.getElementById('slide-wrap');
  if (!wrap) return;

  const signUpBtn = document.getElementById('signUp');
  const signInBtn = document.getElementById('signIn');

  function setPanel(panel, push = true) {
    if (!wrap) return;
    if (panel === 'login' || panel === 'signin' || panel === 'sign-in') {
      wrap.classList.remove('right-panel-active');
      if (push) updateHash('login');
      focusFirstInput('#slide-wrap .sign-in-container input');
    } else {
      wrap.classList.add('right-panel-active');
      if (push) updateHash('register');
      focusFirstInput('#slide-wrap .sign-up-container input');
    }
  }

  function updateHash(val) {
    try { history.replaceState(null, '', '#' + val); } catch (e) { location.hash = val; }
  }

  function getInitialPanel() {
    const data = wrap.dataset.initialPanel;
    if (data) return data.toLowerCase();
    if (location.hash) {
      const h = location.hash.replace('#', '').toLowerCase();
      if (h === 'login' || h === 'register') return h;
    }
    return 'register';
  }

  function focusFirstInput(selector) {
    try {
      const el = document.querySelector(selector);
      if (el) el.focus();
    } catch (e) {}
  }

  if (signUpBtn) signUpBtn.addEventListener('click', (e) => { e.preventDefault(); setPanel('register'); });
  if (signInBtn) signInBtn.addEventListener('click', (e) => { e.preventDefault(); setPanel('login'); });

  // initialize (do not push on load)
  setPanel(getInitialPanel(), false);

  // handle back/forward
  window.addEventListener('popstate', () => {
    const panel = location.hash ? location.hash.replace('#','') : getInitialPanel();
    setPanel(panel, false);
  });
});