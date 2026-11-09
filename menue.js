/* Velowerk Ruhr GmbH: Kopf und Menü.
   1. Misst die Höhe des festen Kopfs (und der festen Seitenleiste auf wirtschaft.html).
      Daraus folgt der Abstand beim Springen und beim Tab-Durchlauf, damit der Fokus
      nie unter dem Kopf verschwindet (WCAG 2.4.11).
   2. Menü am Handy und Tablet (unter 1280 px): natives popover. Öffnen, Schließen und Escape erledigt
      der Browser. Das Skript hält aria-expanded aktuell, gibt den Fokus an den Knopf zurück
      und schließt das Menü, wenn der Fokus es verlässt oder das Fenster auf Desktopbreite wächst. */
(function () {
  var wurzel = document.documentElement;
  var kopf = document.querySelector('header.site');
  var seitenNav = document.querySelector('.seiten-nav');

  function messen() {
    if (!kopf) return;
    var h = kopf.offsetHeight;
    var extra = 0;
    if (seitenNav && getComputedStyle(seitenNav).position === 'sticky') extra = seitenNav.offsetHeight;
    wurzel.style.setProperty('--kopf-hoehe', h + 'px');
    wurzel.style.setProperty('--sprung-abstand', (h + extra + 16) + 'px');
  }
  messen();
  window.addEventListener('resize', messen);
  window.addEventListener('load', messen);

  var knopf = document.querySelector('.menue-knopf');
  var menue = document.getElementById('hauptmenue');
  if (!knopf || !menue || typeof menue.hidePopover !== 'function') return;

  menue.addEventListener('toggle', function (e) {
    var offen = e.newState === 'open';
    knopf.setAttribute('aria-expanded', offen ? 'true' : 'false');
    if (!offen) {
      var aktiv = document.activeElement;
      if (!aktiv || aktiv === document.body || menue.contains(aktiv)) knopf.focus();
    }
  });

  // Verlässt der Fokus per Tab das offene Menü, schließt es. Sonst läge der Fokus unter dem Menü.
  menue.addEventListener('focusout', function (e) {
    var ziel = e.relatedTarget;
    if (ziel && ziel !== knopf && !menue.contains(ziel) && menue.matches(':popover-open')) {
      menue.hidePopover();
    }
  });

  var desktop = window.matchMedia('(min-width: 1280px)');
  function pruefen() {
    if (desktop.matches && menue.matches(':popover-open')) menue.hidePopover();
  }
  if (desktop.addEventListener) desktop.addEventListener('change', pruefen);
})();
