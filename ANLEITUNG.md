# Velowerk Ruhr GmbH – Website-Anleitung

Fiktives Modellunternehmen für den BWR-Unterricht (Anlage C2, FHR).
Alle Unternehmensdaten sind frei erfunden und urheberrechtlich unbedenklich selbst erstellt. Ausnahme: BIP-Wachstum, Inflationsrate und Leitzinsen im Konjunkturmonitor und im Ruhr Kurier sind echte Werte. BIP: Destatis, Pressemitteilung Nr. 269 vom 30.07.2026. Inflation: Destatis, Verbraucherpreisindex, Jahreswerte. Leitzinsen: EZB. Hinweis für Lehrkräfte: Destatis hat das BIP-Wachstum 2024 im Juli 2026 von −0,5 % auf 0,0 % korrigiert. Ältere Quellen nennen deshalb −0,5 %. Der Ruhr Kurier vom 12. Juni 2026 zitiert bewusst nur 2025.

---

## 1. Website auf GitHub Pages veröffentlichen (einmalig, ca. 15 Min.)

1. Kostenloses Konto auf **github.com** anlegen (z.B. Benutzername `ebbk-bwr`)
2. Oben rechts auf **„+“ → „New repository“** klicken
3. Repository-Name: `velowerk-ruhr` → Haken bei **„Public“** → **„Create repository“**
4. Auf **„uploading an existing file“** klicken
5. **Alle Dateien und Ordner aus diesem ZIP** per Drag & Drop in das Fenster ziehen
   (wichtig: `index.html` muss auf der obersten Ebene liegen, die Ordner `bilder/` und `dokumente/` mitsamt Inhalt)
   Seit November 2026 gehören dazu auch die Skripte `menue.js`, `presse-filter.js` und `aktuell.js`
   sowie der Ordner `werkzeug/` mit `diagramme.py`. Den Ordner `werkzeug/ausgabe/` nicht hochladen.
6. Unten auf **„Commit changes“** klicken
7. Im Repository auf **„Settings“ → „Pages“** (linkes Menü)
8. Unter „Branch“: **`main`** auswählen, Ordner **`/ (root)`** → **„Save“**
9. Nach 1–2 Minuten ist die Seite erreichbar unter:
   **https://BENUTZERNAME.github.io/velowerk-ruhr/**

Optional: Eigene Domain (z.B. velowerk-ruhr.de, ca. 10 €/Jahr bei IONOS/Strato)
lässt sich unter Settings → Pages → „Custom domain“ verbinden.

## 2. Eigene Bilder einsetzen

Alle Bildplatzhalter liegen im Ordner `bilder/`. Einfach das eigene Foto
**unter exakt demselben Dateinamen** ablegen – fertig, kein HTML-Code anfassen:

| Datei                | Inhalt                          |
|----------------------|---------------------------------|
| rad-110.jpg ... rad-620.jpg | Produktfotos (12 Modelle) |
| team-*.png           | Porträts (9 Personen, freigestellt) |
| werk.jpg             | Firmengebäude (Startseite)      |
| logo.png             | Firmenlogo: rundes Emblem, freigestellt (600 × 600 px) |
| logo-88.png/.webp, logo-176.png/.webp | verkleinerte Fassungen von logo.png für Kopf und Favicon, bei neuem Logo neu erzeugen |
| logo.svg             | altes Piktogramm, nicht mehr verwendet (Archiv). Einziges Logo ist logo.png |

Bildnachweis: Alle Bilder der Website sind KI-generiert, außer team-frank.png (echtes Foto).
Die Seiten tragen dazu den Hinweis „KI-generiert“ (Klasse `bildnachweis`).
Wer ein Bild austauscht, passt den Hinweis an.

Empfohlene Größen: Produkte 1200×800 px, Team 600×600 px (quadratisch).

**Wichtig bei Personenfotos:** Keine echten Schüler-/Kollegenfotos ohne
schriftliche Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 22 KunstUrhG) –
KI-generierte Gesichter oder Illustrationen sind die unkomplizierteste Lösung.

## 3. Inhalte ändern

Jede Seite ist eine eigene HTML-Datei – direkt auf github.com bearbeitbar
(Datei anklicken → Stift-Symbol → ändern → „Commit changes“):

| Datei            | Inhalt                                              |
|------------------|-----------------------------------------------------|
| index.html       | Startseite, Unternehmensporträt                     |
| produkte.html    | Sortiment (14 Artikel)                              |
| preisliste.html  | UVP-Liste, Rabattstaffel, Boni, Skonto              |
| team.html        | Führungsteam, Organigramm, Beauftragte              |
| stammdaten.html  | Stammdatenblatt, Kontakt                            |
| intern.html      | Gesellschaftsvertrag, Bilanz, GuV, Debitoren, Kreditoren |
| styles.css       | Farben und Gestaltung (zentral für alle Seiten)     |

## 4. PDFs hinterlegen

PDF-Dateien (Preislisten, Aufgabenblätter, Belege) in den Ordner `dokumente/`
hochladen und in einer HTML-Datei verlinken, z.B.:
`<a href="dokumente/beleg-01.pdf">Beleg 01</a>`

Auf der Preislisten-Seite sind zwei Beispiel-Links bereits vorbereitet.

## 5. Eckdaten des Modellunternehmens (Kurzreferenz)

- **Firma:** Velowerk Ruhr GmbH, Helenenstraße 12, 45143 Essen
- **HRB:** Amtsgericht Essen, HRB 14823 (fiktiv)
- **Stammkapital:** 300.000 € (K. Brandt 200.000 € / Dr. S. Roloff 100.000 €)
- **Geschäftsführung:** Martin Frank
- **Bilanzsumme Berichtsjahr:** 2.240.000 € · **Jahresüberschuss:** 420.000 €
- **Kontensystematik:** Debitoren 24001 ff. · Kreditoren 44001 ff.

## 6. VWL-Nutzung: Zuordnung zum Bildungsplan (Heft 44014/2018, Anlage C2 WuV)

| Website-Element (Seite „Wirtschaft“ / Intern) | Anforderungssituation VWL |
|---|---|
| Velowerk im Wirtschaftskreislauf (Sektoren-Tabelle, monetäre/reale Ströme) | AS 1.1, 1.4 |
| Marktdaten + Elastizitäts-Beispiel (Flitzer vs. Emscher) | AS 1.2, 2.1 |
| Wettbewerber-Tabelle, Fusions-Pressemeldung (Kartellamt/GWB) | AS 4.1 |
| Konjunkturmonitor (Umsatz, BIP, Inflation, Geschäftsklima 2021–2025) | AS 3.3, 6.1 |
| Produktionsfaktoren-Karten (Arbeit/Boden/Kapital, Faktorkombination) | AS 3.1 |
| Außenhandel + Wechselkurs-Rechenbeispiel (USD-Import) | AS 2.2, 4.3 |
| Pressemeldung EZB-Leitzinserhöhung/Investition (verschoben) | AS 6.1, 6.3 |
| Pressemeldung Tarifabschluss/Personalkosten | AS 5.2 |
| Pressemeldung Pedelec-Förderung der Stadt Essen (Subvention) | AS 6.2 |
| Inflationsdaten im Konjunkturmonitor, Preisliste (Preiserhöhungen) | AS 1.3, 4.2 |
| Lagebericht 2025 (intern, PDF) – verbindet BWL-Jahresabschluss und VWL-Umfeld | AS 3.2, 3.3, 6.1 |

Tipp: Vor jeder neuen Unterrichtsreihe kann eine passende neue Pressemitteilung
auf der Wirtschaft-Seite ergänzt werden (wirtschaft.html, Abschnitt "presse").

### Direktlinks zu den Pressemitteilungen (für Moodle)

Jede Pressemitteilung hat eine eigene Sprungmarke. Link: `wirtschaft.html#` plus Kennung.
Die ganze Liste: `wirtschaft.html#presse`

| Kennung | Pressemitteilung |
|---|---|
| `presse-2026-11-auslastung` | Montage fast voll ausgelastet, Lieferzeit bis sechs Wochen (6. November 2026) |
| `presse-2026-11-nordrad-cyclonix` | Aus der Branche: NordRad-Cyclonix erhöht die Preise (4. November 2026) |
| `presse-2026-10-strompreis` | Ökostromtarif steigt um 18 % (8. Oktober 2026) |
| `presse-2026-06-ezb` | EZB erhöht Leitzins, Investition verschoben (18. Juni 2026) |
| `presse-2026-04-us-zoelle` | Neue US-Zölle auf Federgabeln (3. April 2026) |
| `presse-2026-02-tarifabschluss` | Tarifabschluss Metallbranche (20. Februar 2026) |
| `presse-2026-01-pedelec-foerderung` | Pedelec-Förderung der Stadt Essen (15. Januar 2026) |
| `presse-2025-12-fusion` | Fusion NordRad und Cyclonix, Kartellamt (10. Dezember 2025) |

Beispiel: https://ebbk-essen.github.io/velowerk-ruhr/wirtschaft.html#presse-2026-06-ezb

### Moodle-Links nach Thema

Der Newsroom kann nach Thema filtern. Ein Link mit `?thema=` zeigt nur dieses Thema:
`wirtschaft.html?thema=zoll#presse`

Themen: `geldpolitik`, `tarif`, `zoll`, `energie`, `wettbewerb`, `foerderung`
(dazu `produktion`, sobald es eine Meldung dazu gibt). Ein Direktlink auf eine
einzelne Meldung (`#presse-...`) zeigt die Meldung immer, auch wenn ein Filter aktiv ist.
Ohne JavaScript ist der Filter unsichtbar, dann stehen alle Meldungen untereinander.

### Neue Meldung anlegen

Neueste Meldung oben in die Liste `<div data-presse-liste>` in wirtschaft.html setzen.
Vorlage (Wörter in Großbuchstaben ersetzen):

```html
<article class="karte presse-meldung" id="presse-JJJJ-MM-thema" data-thema="THEMA">
  <div class="presse-zeile"><span class="presse-art">Pressemitteilung</span><span class="etikett">THEMA-NAME</span></div>
  <h3>ÜBERSCHRIFT</h3>
  <p><time class="ortsmarke" datetime="JJJJ-MM-TT">Essen, T. MONAT JJJJ.</time> TEXT IN KURZEN SÄTZEN.</p>
  <p>Geschäftsführer Martin Frank: „ZITAT.“</p>
  <p class="presse-fuss"><a class="direktlink" href="#presse-JJJJ-MM-thema">Direktlink zu dieser Meldung</a></p>
</article>
```

- `data-thema` muss genau einer der Werte aus der Liste `THEMEN` in `presse-filter.js` sein
  (`geldpolitik`, `tarif`, `zoll`, `energie`, `wettbewerb`, `foerderung`, `produktion`),
  klein und ohne Umlaut. Sonst taucht die Meldung unter keinem Filterknopf auf, nur unter „Alle“.
  Ein neues Thema zuerst dort in `THEMEN` ergänzen.
- Die Ortsmarke steht fett am Anfang des ersten Absatzes, mit Punkt am Ende.
- Der Direktlink zeigt auf die eigene id. Daraus kopiert man den Moodle-Link.
- Meldung über andere Unternehmen: `class="karte presse-meldung branche"` und als Art „Aus der Branche“.
- Danach die Kennung oben in die Liste eintragen.

## 7. Neuausrichtung Produktion (Juni 2026)

Velowerk positioniert sich als industrieller Serienfertiger ("Fahrradwerk", nicht mehr
"Manufaktur"). Neue Sektion "Produktion" auf produkte.html#produktion mit Zuordnung
Produktgruppe → Fertigungstyp/Organisationstyp (BWR, HF 3 Leistungserstellung):
Fließfertigung (Volumenmodelle), Gruppenfertigung (MTB/Pedelecs), Reihenfertigung
(Rahmenbau, inkl. Lackierung; neue Lackieranlage geplant, vertagt), Kleinserie statt Einzelfertigung (»Margarethe«),
Werkstattfertigung nur Prototypen/Service; dazu Vorrats- vs. Auftragsfertigung.

## 8. Ausbau Juni 2026: Neue Seiten und Unterrichtsmaterial

Neue Seiten: impressum.html, datenschutz.html, kontakt.html (Footer-Links auf allen
Seiten), karriere.html (3 Stellenanzeigen -> Bewerbungstraining, HF 5 / Deutsch),
nachhaltigkeit.html (externe Effekte, Kreislaufwirtschaft -> VWL/Kompetenzerwartung
Teil 2 Bildungsplan), ueber-uns.html (Zeitstrahl 1996-2026 -> HF 1 Unternehmens-
entwicklung). Hauptnavigation um "Karriere" erweitert.

Interner Bereich neu:
- dokumente/beleggeschaeftsgang.pdf: 6 Belege (Anfrage, Angebot, Bestellung, AB,
  Lieferschein ohne Preise, Rechnung) - Vorfall: Debitor 1001 Zweirad Bergmann,
  25x Art. 220 + 10x Art. 610, 27 % Rabatt, 19 % USt, 2 % Skonto.
  Buchungssatz Rechnung: Forderungen 30.513,09 an Umsatzerloese 25.641,25
  und Umsatzsteuer 4.871,84.
- dokumente/briefvorlage-din5008.docx: Geschaeftsbrief-Vorlage (Word).

## 9. Haendlerstimmen / Bewertungen (bewertungen.html)

- B2B-konsistent: Bewertungen stammen von Handelskunden (Debitoren), nicht von
  Endkunden -> Unterrichtsfrage B2B vs. B2C.
- Pruefhinweis nach § 5b Abs. 3 UWG eingebaut (Echtheitspruefung von Bewertungen) ->
  Aufhaenger fuer das Thema Fake-Bewertungen/Lauterkeitsrecht.
- Schueler-Abgabe: Formular mit Sterne-Auswahl. Da GitHub Pages statisch ist, wird
  die Bewertung (a) lokal im Browser gespeichert und unter "Neue Bewertungen"
  angezeigt (nur auf dem jeweiligen Geraet) und (b) als formatierter Text zum
  Kopieren ausgegeben -> Schueler senden ihn per Moodle/E-Mail an die Lehrkraft.
- Veroeffentlichen: Gute Einsendungen als neue <div class="karte">-Bloecke im
  Abschnitt "Geprueefte Bewertungen" in bewertungen.html einfuegen (bestehende
  Karte kopieren, Texte ersetzen) und Datei neu zu GitHub hochladen.

## 10. Aktuell-Band austauschen (index.html)

Auf der Startseite steht zwischen Kopf und Hero ein schmales Band „Aktuell“ mit
einem Satz und einem Link auf eine Meldung im Newsroom. Es ist ein einzelner,
kommentierter Block in index.html (`<!-- ===== AKTUELL-BAND ... -->` bis
`<!-- ===== Ende AKTUELL-BAND ===== -->`).

Austauschen:
1. Datum zweimal ändern: `datetime="JJJJ-MM-TT"` und der sichtbare Text `TT.MM.JJJJ`.
2. Den Satz in `<p class="aktuell-text">` ersetzen. Ein Satz, höchstens 90 Zeichen.
3. Im Link `href="wirtschaft.html#presse-..."` die Kennung der Meldung eintragen.

4. Im Link auch `aria-label="Zur Meldung: ..."` an den neuen Satz anpassen.
5. Im `<aside>` das Ablaufdatum `data-bis="JJJJ-MM-TT"` setzen.

Ablaufdatum: Das kleine Skript `aktuell.js` (nur auf index.html eingebunden) blendet
das Band nach dem Tag in `data-bis` von selbst aus. Beispiel: `data-bis="2026-12-31"`
zeigt das Band bis einschließlich 31.12.2026. Ohne `data-bis` bleibt es stehen.

Sofort ausblenden: beim `<aside class="aktuell-band" ...>` das Wort `hidden` ergänzen,
also `<aside class="aktuell-band" aria-label="Aktuelle Meldung" data-bis="..." hidden>`.
Wieder zeigen: `hidden` löschen und ein Datum in der Zukunft setzen. Alternativ den ganzen Block löschen.
Der Volltext einer Meldung steht nur auf wirtschaft.html. Das Band verlinkt nur.

### Archiv auf news.html

Der Abschnitt „Archiv“ auf news.html ist mit `hidden` ausgeblendet, solange es keine
ältere Ausgabe gibt (`<section id="archiv" hidden>`). Sobald eine zweite Ausgabe des
Ruhr Kurier dazukommt: dort einen Link auf die ältere Ausgabe eintragen und `hidden` löschen.

## 11. Diagramme auf wirtschaft.html (werkzeug/diagramme.py)

Die Diagramme in den Abschnitten Fahrradmarkt, Konjunkturmonitor und Außenhandel
sind fertiges SVG im HTML. Sie brauchen kein JavaScript und keine Bibliothek.
Unter jedem Diagramm steht die Tabelle unter „Daten anzeigen“.

Ändern sich Zahlen:
1. Die Tabelle in wirtschaft.html ändern.
2. Dieselben Zahlen oben in `werkzeug/diagramme.py` eintragen (KONJUNKTUR, MARKT, KURSE).
3. Im Ordner des Repositorys `python3 werkzeug/diagramme.py` aufrufen. Das Skript
   schreibt die SVG-Dateien nach `werkzeug/ausgabe/`.
4. Den Inhalt der passenden Datei in wirtschaft.html gegen das alte `<svg ...>...</svg>` tauschen.
5. Zur Kontrolle `python3 werkzeug/diagramme.py --pruefen` aufrufen. Es liest die
   Tabellenwerte aus wirtschaft.html, vergleicht sie mit den Zahlen im Skript und prüft,
   ob alle Diagramme in wirtschaft.html zum Skript passen. Am Ende steht „Alles passt.“
   oder die Liste der Abweichungen.

Der Ordner `werkzeug/ausgabe/` ist nur eine Arbeitskopie und muss nicht hochgeladen werden.
