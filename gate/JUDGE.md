# JUDGE.md: die Augenprüfung (Ebene 2 der Qualitätsprüfung), C&E-Fassung

`check.py` / `gate.py` messen, was Code messen kann. Diese Fragen decken ab, was Code nicht sieht: Bedeutung, Geschmack, Klischees.
Die Fragen stammen aus zwei Quellen: Urteile, die sich in der Vorlage (Shorts Studio) über viele Runden bewährt haben, und Dannys
eigene Freigaben und Ablehnungen (C&E-Stil v2, 18.11.2026). Neue Notizen von Danny kommen hier als Frage dazu, mit Datum.

## So läuft es
1. Erst `gate.py` laufen lassen. Es schreibt einen Kontaktbogen (2 Bilder/s, durchgefallene Frames rot umrandet).
2. Vergleichstafel: der Canvas „C&E Reel – Motion-Stil v2 (Standbilder)“ (https://claude.ai/artifact/PF4uBzRhT18Waj8yPpkEcR).
   Mit dem Artifact-Tool lesen und im Kopf behalten. Daneben die abgelehnte flache Version: einfache Pills und Karten ohne Material.
3. Kontaktbogen in Szenen teilen (eine Szene = eine Bildidee, meist 1 bis 4 s).
4. Jede FAIL-Frage pro Szene mit JA oder NEIN beantworten. JA = gut. Ein NEIN = FAIL, mit Zeit. So urteilen, wie Danny auf dem Handy
   urteilt: Musst Du erklären, warum es funktioniert, ist es ein NEIN.
5. In `<out>/judge.json` schreiben: `[{"t0": 4.0, "t1": 5.5, "q": "J5", "answer": "NO", "why": "Pfeil zeigt ins Leere"}]`.
6. Raus geht es nur bei GATE PASS und keinem NEIN. Grenzfall = NEIN. Nicht nett zur eigenen Arbeit sein.

## FAIL-Fragen (JA = gut)
| # | Frage |
|---|---|
| J1 | **Ein Held.** Ist pro Szene EIN zusammenhängendes Objekt die Hauptsache, statt gestapelter Karten oder einer kleinen Karte im Leeren? |
| J2 | **Echt statt Platzhalter-Grau.** Sind Oberflächen echt nachgebaut (Suchfeld, Ergebnis-Karte, DM-Fenster, Handy-Raster), nie graue Balken oder Wireframes? |
| J3 | **Zeigen statt nachplappern.** Zeigt die Grafik die Idee, statt nur das gerade gesagte Wort zu tippen oder ein Label-Chip zu setzen? |
| J4 | **Keine KI-Klischees.** Frei von Funkelsternen, durchgestrichenen Icons, Neustart-Pfeilen als Metapher, leuchtenden Kugeln? |
| J5 | **Zeiger zeigen.** Berührt jeder Pfeil, Cursor, Ring genau das, worum es geht? |
| J6 | **Es passiert etwas.** Verändert sich die Grafik, während Danny spricht (Aufbau, Reveal, Ergebnis), statt nur dazustehen? |
| J7 | **Ruhiger Beweis.** Sind Zahlen und Belege ein klares Bild (eine Zahl, ein echter Screen), nicht Chips, Stempel, Avatar-Ringe? |
| J8 | **Fortschritt ist ein Bild.** Wird ein Ablauf als Bewegung gezeigt (Schritte füllen sich, eine Liste hakt ab), nicht als Zähler? |
| J9 | **C&E-Blau.** Ist `#2F6BFF` (oder sein Verlauf) als echter Akzent in der Grafik sichtbar, und nur dieses eine Akzent-Blau? |
| J10 | **Luft.** Klarer Abstand um jedes Element, nichts klebt am Rand, Untertitel frei von Grafiken? |
| J11 | **Typo.** Höchstens 3 Wörter + 1 Zahl pro Grafik, Montserrat 800 für Aussagen, IBM Plex Mono nur in Pills, Schlüsselwort mit blauem Pinselstrich? |
| J12 | **Ruhige Kamera.** Steht Dannys Bild still (keine Zoom-Rein-Raus-Übergänge, kein Driften), jeder Jump Cut durch Layoutwechsel oder Grafik gedeckt? |
| J13 | **Dannys Gesicht.** Ist es sichtbar, frei und im Objektiv, sobald er im Bild ist? Nie verdeckt, nie stummes Starren, nie Blick nach unten? |
| J14 | **Passt und folgt.** Passt die Grafik zu dem, was er gerade sagt, und landet sie auf dem Wort (±2 Frames)? |
| J15 | **Würde ein Studio das ausliefern?** Passt der Frame zur v2-Tafel und gehört er zu den Frames davor und danach (ein Bildsystem)? |
| J16 | **Kontinuität.** Wächst jede Grafik aus der vorigen (dieselben Elemente bewegen, sinken, gruppieren sich), statt hart zu etwas Fremdem zu springen? |
| J17 | **Material statt Fläche.** Sind Overlays Papier-Platte mit Kante oder mattes Glas, leicht gedreht, mit 1–2 Satelliten? Nie die flache Pill-Version, nie Vollbild-Farbblöcke. |
| J18 | **Konkretes Beispiel.** Zeigt die Grafik einen echten, konkreten Fall („Däi Betrib kritt 3 Ufroen“) statt eines abstrakten Labels oder Icon-Kacheln? |
| J19 | **Safe Zone.** Liegt nichts Wichtiges in oben 250 / unten 620 / rechts 140 / links 90 px? Overlays in y 820–1300? |
| J20 | **Luxemburgisch richtig.** Ist jeder Text im Bild und jede Untertitelzeile nach lod.lu geschrieben, Du/Däin groß, Namen richtig (Clees & Ernster)? |
| J22 | **Studio-Qualität.** Ist das Hauptobjekt plastisch gebaut (Licht, Schatten, Material, Textur) statt einer Strichzeichnung oder flacher Formen? Würde es neben einem Apple- oder Stripe-Spot bestehen? (Danny, 23.11.2026: „mega minderwertig“) |
| J21 | **Ehrlich.** Ist jede Zahl, jedes Ergebnis und jeder Kundenname echt und freigegeben, oder klar als Platzhalter erkennbar? Keine Fremdfirma? |

## WARN-Fragen (Forschung, blockieren allein nicht; in die Fix-Liste)
| # | Frage |
|---|---|
| W1 | Frame 0: große Headline oder ein echter Screen sichtbar? |
| W2 | Untertitel 1 bis 3 Wörter, das gesprochene Wort hervorgehoben? |
| W3 | Ein fester Schritt-Label an derselben Stelle bei jedem Beat („1. Ufro“)? |
| W4 | Echte Oberfläche als EINE schwebende Karte auf ruhigem Grund? |
| W5 | Wenn eine Zahl zählt: ist das Hochzählen der Held (40–90 % der Breite)? |
| W6 | Harte Schnitte zwischen Einstellungen; die Bewegung lebt im Bild, nicht in Effekt-Übergängen? |
| W7 | Etwas ändert sich alle 0,5–1 s früh, alle 1–1,5 s später? |
| W8 | Das Bild baut sich auf (Linien zeichnen sich, Teile setzen sich zusammen), statt ganz einzublenden? |
| W9 | Funktioniert das Reel ohne Ton (Meta)? |

## Wertung
- Ein NEIN bei J1 bis J21 = FAIL für die Szene. Beheben, neu rendern, `gate.py` und diese Prüfung nochmal.
- WARNs in die Fix-Liste. Drei oder mehr WARNs in einem Reel: mindestens den billigsten vor der Übergabe beheben.
- Neues Urteil von Danny: Frage hier ergänzen oder ändern, mit seinem Zitat und Datum, und in `references/MARKE.md` eintragen.
  Neueste Notiz gewinnt.
