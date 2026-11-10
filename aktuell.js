/* Velowerk Ruhr GmbH: Aktuell-Band auf index.html.
   Ist das Datum in data-bis vorbei, blendet das Skript das Band mit hidden aus.
   Ohne JavaScript bleibt das Band sichtbar. Erklärt in ANLEITUNG.md, Abschnitt 10. */
(function () {
  var band = document.querySelector('.aktuell-band[data-bis]');
  if (!band) return;
  var bis = new Date(band.getAttribute('data-bis') + 'T23:59:59');
  if (!isNaN(bis.getTime()) && new Date() > bis) band.hidden = true;
})();
