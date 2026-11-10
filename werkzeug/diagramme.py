"""Erzeugt die statischen SVG-Diagramme für wirtschaft.html (Velowerk Ruhr GmbH).

Vorgabe Jessica, 09.11.2026. Die Daten stehen unten und sind 1:1 aus den
Tabellen in wirtschaft.html übernommen. Ausgabe: fertiges SVG-Markup zum
Einfügen in die Seite. Kein JavaScript im Browser nötig.

Aufruf im Ordner des Repositorys:
  python3 werkzeug/diagramme.py            schreibt svg-*.html nach werkzeug/ausgabe/
  python3 werkzeug/diagramme.py --pruefen  prüft die Tabellenwerte in wirtschaft.html gegen die Daten hier
                                           und ob wirtschaft.html genau diese SVG enthält
Erklärt in ANLEITUNG.md, Abschnitt 11.
"""
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent      # .../velowerk-ruhr/werkzeug
REPO = HIER.parent                          # .../velowerk-ruhr
AUSGABE = HIER / "ausgabe"
SEITE = REPO / "wirtschaft.html"


def nbsp(html):
    """Geschütztes Leerzeichen zwischen Zahl und % oder €, wie auf der Seite."""
    return re.sub(r"(\d) (%|€)", "\\1&nbsp;\\2", html)


def zahl(x, stellen=1):
    s = f"{abs(x):.{stellen}f}".replace(".", ",")
    return ("−" if x < 0 else "") + s


def saeule(x, basis, oben, breite, r=4, klasse="d-balken", titel=""):
    """Säule mit 4er-Rundung am Datenende, eckig an der Basislinie.
    oben < basis: nach oben, oben > basis: nach unten."""
    h = abs(basis - oben)
    t = f"<title>{titel}</title>" if titel else ""
    if h < 0.5:  # Wert auf der Nulllinie: keine Säule, nur die Beschriftung
        return ""
    if h < 2 * r:
        y = min(basis, oben)
        return f'<rect class="{klasse}" x="{x:.1f}" y="{y:.1f}" width="{breite}" height="{max(h, 1.5):.1f}">{t}</rect>'
    if oben < basis:  # nach oben
        d = (f"M{x:.1f},{basis:.1f}V{oben + r:.1f}Q{x:.1f},{oben:.1f} {x + r:.1f},{oben:.1f}"
             f"H{x + breite - r:.1f}Q{x + breite:.1f},{oben:.1f} {x + breite:.1f},{oben + r:.1f}V{basis:.1f}Z")
    else:  # nach unten
        d = (f"M{x:.1f},{basis:.1f}V{oben - r:.1f}Q{x:.1f},{oben:.1f} {x + r:.1f},{oben:.1f}"
             f"H{x + breite - r:.1f}Q{x + breite:.1f},{oben:.1f} {x + breite:.1f},{oben - r:.1f}V{basis:.1f}Z")
    return f'<path class="{klasse}" d="{d}">{t}</path>'


JAHRE = [2021, 2022, 2023, 2024, 2025]
FOKUS = 2023

# ---------- Konjunkturmonitor: vier Felder, gemeinsame Zeitachse ----------
KONJUNKTUR = {
    "umsatz": dict(titel="Umsatz Velowerk", einheit="in Mio. €",
                   werte=[5.40, 6.10, 5.80, 6.45, 7.24], stellen=2, suffix="",
                   bereich=(0, 8), basis=0),
    "bip": dict(titel="BIP-Wachstum Deutschland", einheit="real, in %",
                werte=[4.0, 1.9, -1.0, 0.0, 0.2], stellen=1, suffix=" %", plus=True,
                bereich=(-1.5, 4.5), basis=0),  # Destatis, PM 269 vom 30.07.2026
    "inflation": dict(titel="Inflationsrate", einheit="in %",
                      werte=[3.1, 6.9, 5.9, 2.2, 2.2], stellen=1, suffix=" %",
                      bereich=(0, 8), basis=0),
    "klima": dict(titel="Geschäftsklima Fahrradbranche", einheit="Index, 100 = neutral",
                  werte=[108, 103, 91, 99, 106], stellen=0, suffix="",
                  bereich=(85, 112), basis=100, notiz="100"),
}


def feld(schluessel, f):
    B, H = 320, 196
    oben_y, unten_y = 30, 160
    lo, hi = f["bereich"]
    s = (unten_y - oben_y) / (hi - lo)
    y = lambda v: oben_y + (hi - v) * s
    by = y(f["basis"])
    slot, breite, x0 = 56, 26, 20
    teile = []
    # Band hinter 2023
    i_f = JAHRE.index(FOKUS)
    teile.append(f'<rect class="d-band" x="{x0 + slot * i_f + 2}" y="12" width="{slot - 4}" height="{H - 12}" rx="4"/>')
    for i, (j, v) in enumerate(zip(JAHRE, f["werte"])):
        cx = x0 + slot * i + slot / 2
        x = cx - breite / 2
        top = y(v)
        txt = zahl(v, f["stellen"]) + f["suffix"]
        if f.get("plus") and v > 0:
            txt = "+" + txt
        klasse = "d-fokus" if j == FOKUS else "d-balken"
        teile.append(saeule(x, by, top, breite, klasse=klasse, titel=f"{j}: {txt}"))
        wy = top - 7 if v >= f["basis"] else top + 16
        stark = " stark" if j == FOKUS else ""
        teile.append(f'<text class="d-wert{stark}" x="{cx:.1f}" y="{wy:.1f}" text-anchor="middle">{txt}</text>')
        teile.append(f'<text class="d-jahr{stark}" x="{cx:.1f}" y="{unten_y + 30}" text-anchor="middle">{j}</text>')
    teile.append(f'<line class="d-basis" x1="{x0}" x2="{x0 + slot * 5}" y1="{by:.1f}" y2="{by:.1f}"/>')
    if f.get("notiz"):
        teile.append(f'<text class="d-notiz" x="{x0 - 4}" y="{by + 4:.1f}" text-anchor="end">{f["notiz"]}</text>')
    if f["basis"] == 0 and lo < 0:
        teile.append(f'<text class="d-notiz" x="{x0 - 4}" y="{by + 4:.1f}" text-anchor="end">0</text>')
    werte = ", ".join(f"{j}: {zahl(v, f['stellen'])}{f['suffix']}" for j, v in zip(JAHRE, f["werte"]))
    tid, did = f"t-{schluessel}", f"d-{schluessel}"
    return (f'<svg viewBox="0 0 {B} {H}" role="img" aria-labelledby="{tid} {did}">'
            f'<title id="{tid}">{f["titel"]}, {f["einheit"]}, 2021 bis 2025</title>'
            f'<desc id="{did}">{werte}. Das Jahr 2023 ist hervorgehoben.</desc>'
            + "".join(teile) + "</svg>")


# ---------- Fahrradmarkt: gestapelte Säulen ----------
MARKT = dict(gesamt=[4.7, 4.6, 4.0, 4.2, 4.4], anteil=[42, 48, 53, 55, 58])


def markt():
    B, H = 320, 236
    oben_y, unten_y = 34, 200
    s = (unten_y - oben_y) / 5.0
    slot, breite, x0, gap = 56, 40, 20, 2
    teile = ['<defs><pattern id="schraffur-rest" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             '<rect width="6" height="6" fill="#C9D0D4"/><line x1="0" y1="0" x2="0" y2="6" stroke="#5B6770" stroke-width="2"/></pattern></defs>']
    for i, (j, g, a) in enumerate(zip(JAHRE, MARKT["gesamt"], MARKT["anteil"])):
        cx = x0 + slot * i + slot / 2
        x = cx - breite / 2
        h_ges = g * s
        h_e = g * a / 100 * s
        top_e = unten_y - h_e
        top_g = unten_y - h_ges
        teile.append(f'<rect class="d-ebike" x="{x:.1f}" y="{top_e:.1f}" width="{breite}" height="{h_e:.1f}">'
                     f'<title>{j}: E-Bike-Anteil {a} %</title></rect>')
        teile.append(saeule(x, top_e - gap, top_g, breite, klasse="d-rest",
                            titel=f"{j}: Absatz gesamt {zahl(g)} Mio. Stück"))
        teile.append(f'<text class="d-innen" x="{cx:.1f}" y="{unten_y - 10:.1f}" text-anchor="middle">{a} %</text>')
        teile.append(f'<text class="d-wert" x="{cx:.1f}" y="{top_g - 7:.1f}" text-anchor="middle">{zahl(g)}</text>')
        teile.append(f'<text class="d-jahr" x="{cx:.1f}" y="{unten_y + 26}" text-anchor="middle">{j}</text>')
    teile.append(f'<line class="d-basis" x1="{x0}" x2="{x0 + slot * 5}" y1="{unten_y}" y2="{unten_y}"/>')
    desc = "; ".join(f"{j}: {zahl(g)} Mio. Stück, davon {a} % E-Bikes"
                     for j, g, a in zip(JAHRE, MARKT["gesamt"], MARKT["anteil"]))
    return (f'<svg viewBox="0 0 {B} {H}" role="img" aria-labelledby="t-markt d-markt">'
            '<title id="t-markt">Fahrradabsatz in Deutschland 2021 bis 2025, in Mio. Stück, mit Anteil der E-Bikes</title>'
            f'<desc id="d-markt">{desc}. Der Anteil der E-Bikes steigt jedes Jahr.</desc>'
            + "".join(teile) + "</svg>")


# ---------- Wechselkursbeispiel: liegende Balken ----------
KURSE = [("1 € = 1,05 USD", "schwacher Euro", 228.57),
         ("1 € = 1,12 USD", "", 214.29),
         ("1 € = 1,20 USD", "starker Euro", 200.00)]


def kurs():
    B, H = 320, 178
    s = 230 / 250  # 0 bis 250 € auf 230 Einheiten
    zeile, x0 = 56, 2
    teile = []
    for i, (k, z, eur) in enumerate(KURSE):
        y0 = 8 + i * zeile
        label = k + (f' <tspan class="d-notiz">({z})</tspan>' if z else "")
        teile.append(f'<text class="d-kat" x="{x0}" y="{y0 + 12}">{label}</text>')
        w = eur * s
        by = y0 + 20
        hb = 22
        d = (f"M{x0},{by}H{x0 + w - 4:.1f}Q{x0 + w:.1f},{by} {x0 + w:.1f},{by + 4}"
             f"V{by + hb - 4}Q{x0 + w:.1f},{by + hb} {x0 + w - 4:.1f},{by + hb}H{x0}Z")
        wert = f"{eur:.2f}".replace(".", ",") + " €"
        teile.append(f'<path class="d-balken" d="{d}"><title>{k}: {wert}</title></path>')
        teile.append(f'<text class="d-wert" x="{x0 + w + 6:.1f}" y="{by + 16}">{wert}</text>')
    desc = "; ".join(f"{k}: {eur:.2f} €".replace(".", ",") for k, _, eur in KURSE)
    return (f'<svg viewBox="0 0 {B} {H}" role="img" aria-labelledby="t-kurs d-kurs">'
            '<title id="t-kurs">Preis einer Federgabel in Euro bei drei Wechselkursen, Listenpreis 240 USD</title>'
            f'<desc id="d-kurs">{desc}. Je stärker der Euro, desto weniger kostet die Federgabel in Euro.</desc>'
            + "".join(teile) + "</svg>")


def alle():
    roh = {
        "umsatz": feld("umsatz", KONJUNKTUR["umsatz"]),
        "bip": feld("bip", KONJUNKTUR["bip"]),
        "inflation": feld("inflation", KONJUNKTUR["inflation"]),
        "klima": feld("klima", KONJUNKTUR["klima"]),
        "markt": markt(),
        "kurs": kurs(),
    }
    return {k: nbsp(v) for k, v in roh.items()}


def _zahl(text):
    """'+2,9 %' oder '−0,1 %' oder '1.395 €' -> float"""
    t = text.replace("&nbsp;", " ").replace("\xa0", " ").replace("%", "").replace("€", "")
    t = t.replace("−", "-").replace("+", "").replace(".", "").replace(",", ".").strip()
    return float(t)


def _tabellen_zeilen(html, abschnitt, caption=None):
    """Zellen der Tabelle aus <section id=abschnitt> (optional die mit dieser Überschrift)."""
    a = html.index(f'<section id="{abschnitt}"')
    e = html.index("</section>", a)
    teil = html[a:e]
    tabellen = re.findall(r"<table>.*?</table>", teil, flags=re.S)
    if caption:
        tabellen = [t for t in tabellen if caption in t]
    zeilen = []
    for tr in re.findall(r"<tr>(.*?)</tr>", tabellen[-1], flags=re.S):
        zellen = [re.sub(r"<[^>]+>", "", z).strip() for z in re.findall(r"<td[^>]*>(.*?)</td>", tr)]
        if zellen:
            zeilen.append(zellen)
    return zeilen


def tabellen_pruefen(html):
    """Vergleicht die Tabellen in wirtschaft.html mit den Daten oben im Skript."""
    fehler = 0

    def vergleich(name, tabelle, skript):
        nonlocal fehler
        if [round(x, 2) for x in tabelle] == [round(x, 2) for x in skript]:
            print(f"ok      Tabelle {name}")
        else:
            print(f"FEHLER  Tabelle {name}: Seite {tabelle}, Skript {skript}")
            fehler += 1

    z = _tabellen_zeilen(html, "konjunktur")
    jahre = [int(r[0]) for r in z]
    if jahre != JAHRE:
        print(f"FEHLER  Jahre im Konjunkturmonitor: {jahre}")
        fehler += 1
    for i, key in enumerate(["umsatz", "bip", "inflation", "klima"], start=1):
        vergleich(f"Konjunktur {key}", [_zahl(r[i]) for r in z], KONJUNKTUR[key]["werte"])
    z = _tabellen_zeilen(html, "markt")
    vergleich("Markt Absatz", [_zahl(r[1]) for r in z], MARKT["gesamt"])
    vergleich("Markt E-Bike-Anteil", [_zahl(r[2]) for r in z], MARKT["anteil"])
    z = _tabellen_zeilen(html, "aussenhandel", caption="Rechenbeispiel")
    vergleich("Wechselkurs", [_zahl(r[1]) for r in z], [k[2] for k in KURSE])
    return fehler


def pruefen():
    html = SEITE.read_text(encoding="utf-8")
    fehler = tabellen_pruefen(html)
    for k, v in alle().items():
        if v in html:
            print(f"ok      Diagramm {k}")
        else:
            print(f"FEHLT   Diagramm {k}: SVG in wirtschaft.html weicht vom Skript ab")
            fehler += 1
    print("Alles passt." if not fehler else f"{fehler} Abweichung(en).")
    return fehler


if __name__ == "__main__":
    if "--pruefen" in sys.argv:
        sys.exit(1 if pruefen() else 0)
    AUSGABE.mkdir(exist_ok=True)
    for k, v in alle().items():
        (AUSGABE / f"svg-{k}.html").write_text(v, encoding="utf-8")
    print(f"fertig: {len(alle())} Dateien in {AUSGABE.relative_to(REPO)}/")
