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
