# Velowerk Ruhr GmbH – Website-Anleitung

Fiktives Modellunternehmen für den BWR-Unterricht (Anlage C2, FHR).
Alle Daten sind frei erfunden und urheberrechtlich unbedenklich selbst erstellt.

---

## 1. Website auf GitHub Pages veröffentlichen (einmalig, ca. 15 Min.)

1. Kostenloses Konto auf **github.com** anlegen (z.B. Benutzername `ebbk-bwr`)
2. Oben rechts auf **„+" → „New repository"** klicken
3. Repository-Name: `velowerk-ruhr` → Haken bei **„Public"** → **„Create repository"**
4. Auf **„uploading an existing file"** klicken
5. **Alle Dateien und Ordner aus diesem ZIP** per Drag & Drop in das Fenster ziehen
   (wichtig: `index.html` muss auf der obersten Ebene liegen, die Ordner `bilder/` und `dokumente/` mitsamt Inhalt)
6. Unten auf **„Commit changes"** klicken
7. Im Repository auf **„Settings" → „Pages"** (linkes Menü)
8. Unter „Branch": **`main`** auswählen, Ordner **`/ (root)`** → **„Save"**
9. Nach 1–2 Minuten ist die Seite erreichbar unter:
   **https://BENUTZERNAME.github.io/velowerk-ruhr/**

Optional: Eigene Domain (z.B. velowerk-ruhr.de, ca. 10 €/Jahr bei IONOS/Strato)
lässt sich unter Settings → Pages → „Custom domain" verbinden.

## 2. Eigene Bilder einsetzen

Alle Bildplatzhalter liegen im Ordner `bilder/`. Einfach das eigene Foto
**unter exakt demselben Dateinamen** ablegen – fertig, kein HTML-Code anfassen:

| Datei                | Inhalt                          |
|----------------------|---------------------------------|
| rad-110.jpg ... rad-620.jpg | Produktfotos (12 Modelle) |
| team-*.jpg           | Mitarbeiterfotos (6 Personen)   |
| werk.jpg             | Firmengebäude (Startseite)      |
| logo.svg             | Firmenlogo                      |

Empfohlene Größen: Produkte 1200×800 px, Team 600×600 px (quadratisch).

**Wichtig bei Personenfotos:** Keine echten Schüler-/Kollegenfotos ohne
schriftliche Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 22 KunstUrhG) –
KI-generierte Gesichter oder Illustrationen sind die unkomplizierteste Lösung.

## 3. Inhalte ändern

Jede Seite ist eine eigene HTML-Datei – direkt auf github.com bearbeitbar
(Datei anklicken → Stift-Symbol → ändern → „Commit changes"):

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

| Website-Element (Seite „Wirtschaft" / Intern) | Anforderungssituation VWL |
|---|---|
| Velowerk im Wirtschaftskreislauf (Sektoren-Tabelle, monetäre/reale Ströme) | AS 1.1, 1.4 |
| Marktdaten + Elastizitäts-Beispiel (Flitzer vs. Emscher) | AS 1.2, 2.1 |
| Wettbewerber-Tabelle, Fusions-Pressemeldung (Kartellamt/GWB) | AS 4.1 |
| Konjunkturmonitor (Umsatz, BIP, Inflation, Geschäftsklima 2021–2025) | AS 3.3, 6.1 |
| Produktionsfaktoren-Karten (Arbeit/Boden/Kapital, Faktorkombination) | AS 3.1 |
| Außenhandel + Wechselkurs-Rechenbeispiel (USD-Import) | AS 2.2, 4.3 |
| Pressemeldung EZB-Leitzinssenkung/Investition | AS 6.1, 6.3 |
| Pressemeldung Tarifabschluss/Personalkosten | AS 5.2 |
| Pressemeldung Pedelec-Förderung der Stadt Essen (Subvention) | AS 6.2 |
| Inflationsdaten im Konjunkturmonitor, Preisliste (Preiserhöhungen) | AS 1.3, 4.2 |
| Lagebericht 2025 (intern, PDF) – verbindet BWL-Jahresabschluss und VWL-Umfeld | AS 3.2, 3.3, 6.1 |

Tipp: Vor jeder neuen Unterrichtsreihe kann eine passende neue Pressemitteilung
auf der Wirtschaft-Seite ergänzt werden (wirtschaft.html, Abschnitt "presse").

## 7. Neuausrichtung Produktion (Juni 2026)

Velowerk positioniert sich als industrieller Serienfertiger ("Fahrradwerk", nicht mehr
"Manufaktur"). Neue Sektion "Produktion" auf produkte.html#produktion mit Zuordnung
Produktgruppe → Fertigungstyp/Organisationstyp (BWR, HF 3 Leistungserstellung):
Fließfertigung (Volumenmodelle), Gruppenfertigung (MTB/Pedelecs), Reihenfertigung
(Rahmenbau, inkl. neuer Lackieranlage), Kleinserie statt Einzelfertigung (»Margarethe«),
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
