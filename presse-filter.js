/* Velowerk Ruhr GmbH: Filter der Pressemitteilungen nach Thema (wirtschaft.html#presse).
   Ohne JavaScript bleibt der Filter verborgen und alle Meldungen sind sichtbar.
   Mit JavaScript:
   1. Knöpfe "Alle" und je Thema, mit Anzahl. Themen ohne Meldung erscheinen nicht.
   2. Ein Knopf ist gedrückt (aria-pressed). Die Zeile darunter meldet die Anzahl (aria-live).
   3. ?thema=energie in der Adresse wählt das Thema beim Laden (für Moodle-Links).
   4. Zeigt ein Direktlink (#presse-...) auf eine ausgeblendete Meldung, springt der Filter auf "Alle". */
(function () {
  var liste = document.querySelector('[data-presse-liste]');
  var leiste = document.querySelector('.presse-filter');
  var zahl = document.querySelector('.presse-zahl');
  if (!liste || !leiste || !zahl) return;

  var THEMEN = [
    ['geldpolitik', 'Geldpolitik'], ['tarif', 'Tarif'], ['zoll', 'Zoll'], ['energie', 'Energie'],
    ['wettbewerb', 'Wettbewerb'], ['foerderung', 'Förderung'], ['produktion', 'Produktion']
  ];
  var meldungen = Array.prototype.slice.call(liste.querySelectorAll('.presse-meldung'));
  var knoepfe = [];

  function knopf(wert, text, anzahl) {
    var li = document.createElement('li');
    var b = document.createElement('button');
    b.type = 'button';
    b.dataset.thema = wert;
    b.setAttribute('aria-pressed', 'false');
    b.innerHTML = text + '<span class="anzahl" aria-hidden="true">' + anzahl + '</span>';
    b.setAttribute('aria-label', text + ', ' + anzahl + (anzahl === 1 ? ' Meldung' : ' Meldungen'));
    b.addEventListener('click', function () { waehlen(wert, true); });
    li.appendChild(b);
    leiste.appendChild(li);
    knoepfe.push(b);
  }

  knopf('alle', 'Alle', meldungen.length);
  THEMEN.forEach(function (t) {
    var n = meldungen.filter(function (m) { return m.dataset.thema === t[0]; }).length;
    if (n > 0) knopf(t[0], t[1], n);
  });

  function name(wert) {
    for (var i = 0; i < THEMEN.length; i++) if (THEMEN[i][0] === wert) return THEMEN[i][1];
    return '';
  }

  function waehlen(wert, merken) {
    var gezeigt = 0;
    meldungen.forEach(function (m) {
      var an = wert === 'alle' || m.dataset.thema === wert;
      m.hidden = !an;
      if (an) gezeigt++;
    });
    knoepfe.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.thema === wert ? 'true' : 'false'); });
    var wort = gezeigt === 1 ? 'Meldung' : 'Meldungen';
    zahl.textContent = wert === 'alle' ? gezeigt + ' ' + wort : gezeigt + ' ' + wort + ' zum Thema ' + name(wert);
    if (merken && history.replaceState) {
      var url = new URL(location.href);
      if (wert === 'alle') url.searchParams.delete('thema'); else url.searchParams.set('thema', wert);
      url.hash = '';
      history.replaceState(null, '', url.pathname + url.search + '#presse');
    }
  }

  function ausHash() {
    var ziel = location.hash ? document.getElementById(location.hash.slice(1)) : null;
    if (ziel && ziel.classList.contains('presse-meldung') && ziel.hidden) {
      waehlen('alle', false);
      // Die Meldung war verborgen, der Browser konnte nicht hinspringen. Jetzt nachholen.
      // scrollIntoView beachtet scroll-padding-top (Kopfabstand aus menue.js).
      ziel.scrollIntoView({ block: 'start' });
    }
  }

  var start = new URLSearchParams(location.search).get('thema');
  var gueltig = knoepfe.some(function (b) { return b.dataset.thema === start; });
  waehlen(gueltig ? start : 'alle', false);
  ausHash();
  window.addEventListener('hashchange', ausHash);
  leiste.hidden = false;
  zahl.hidden = false;
})();
