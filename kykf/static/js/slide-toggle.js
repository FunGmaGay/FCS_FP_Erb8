// Slide toggle: left (register) -> right (login)
document.addEventListener('DOMContentLoaded', function () {
  const wrapper = document.getElementById('slide-wrapper');
  if (!wrapper) return;

  const slider = document.getElementById('slide-slider');
  const btnRegister = document.getElementById('show-register-btn');
  const btnLogin = document.getElementById('show-login-btn');
  const toggles = document.querySelectorAll('.toggle-to');

  function getInitialPanel() {
    const dataPanel = wrapper.dataset.initialPanel;
    if (dataPanel) return dataPanel.toLowerCase();
    if (location.hash) {
      const h = location.hash.replace('#','').toLowerCase();
      if (h === 'register' || h === 'login') return h;
    }
    const params = new URLSearchParams(location.search);
    const q = params.get('panel');
    if (q && (q === 'register' || q === 'login')) return q;
    return 'register';
  }

  function showPanel(panel, push = true) {
    panel = (panel === 'login') ? 'login' : 'register';
    slider.classList.toggle('show-register', panel === 'register');
    slider.classList.toggle('show-login', panel === 'login');

    // update hash for deep-link/back-forward
    if (push) {
      try {
        history.pushState(null, '', '#' + panel);
      } catch (e) {
        location.hash = panel;
      }
    }

    // accessibility (move focus to the first input in the visible panel)
    try {
      const selector = (panel === 'login') ? '#slide-slider .login-panel input' : '#slide-slider .register-panel input';
      const firstInput = document.querySelector(selector);
      if (firstInput) firstInput.focus();
    } catch (e) { /* ignore */ }
  }

  if (btnRegister) btnRegister.addEventListener('click', (e) => { e.preventDefault(); showPanel('register'); });
  if (btnLogin) btnLogin.addEventListener('click', (e) => { e.preventDefault(); showPanel('login'); });
  toggles.forEach(t => t.addEventListener('click', (e) => {
    e.preventDefault();
    const tgt = e.currentTarget.dataset.target;
    showPanel(tgt);
  }));

  // handle back/forward navigation
  window.addEventListener('popstate', () => {
    const panel = (location.hash ? location.hash.replace('#','') : getInitialPanel());
    showPanel(panel, false);
  });

  // initialize (do not push history on load)
  showPanel(getInitialPanel(), false);
});