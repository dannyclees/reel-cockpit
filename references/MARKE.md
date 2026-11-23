# Clees & Ernster: Marke im Reel

Quelle: motion-designer-cockpit (Bereich 3 + C&E-Reel-Overlay-Stil v2, freigegeben von Danny am 18.11.2026) und copywriter-cockpit.
Ändert Danny etwas, hier eintragen und `styles/ce.json` nachziehen. Neueste Notiz gewinnt.

## Wer spricht, zu wem
- **Danny** vor der Kamera, meist auf **Luxemburgisch**. Er ist Hauptsache: Gesicht frei, Overlays darunter.
- Zielgruppe: Inhaber von Luxemburger Premium-Betrieben (Handwerk, Immobilien, hochpreisige Dienstleistungen).
- Positionierung: **planbares Anfrage-System für Luxemburger Premium-Betriebe**: psychologisch präzise Werbung + automatisierte
  Nachfassung. KI ist Werkzeug, nie Headline.
- Ansprache: **Du-Form, Du/Däin/Dir großgeschrieben** (auf Deutsch Du/Dein/Dir).

## Bewegungscharakter: schnell-direkt, gemäßigtes Rot
Ergebnisorientiert, knackig, harte Schnitte, aufgeräumt. Keine Effektshow, kein Gehopse. Tokens (in jede Komposition oben):
```js
var M = { tempo: 0.85, dur: { xs: 0.12, s: 0.25, m: 0.45, l: 0.8 },
  ease: { enter: "power4.out", exit: "power3.in", accent: "expo.out", hold: "sine.inOut", pop: "back.out(1.2)" }, stagger: 0.05 };
```
Signatur in jedem Reel: der **blaue Pinselstrich**, der mit `expo.out` unter dem Schlüsselwort aufschnappt. Immer gleich.

## Stil v2 (Pflicht, nie zurück zur flachen Version)
Die erste flache Version (einfache Pills und Karten ohne Material) hat Danny als „schlecht“ abgelehnt.
Referenz-Standbilder: Canvas „C&E Reel – Motion-Stil v2 (Standbilder)“, https://claude.ai/artifact/PF4uBzRhT18Waj8yPpkEcR
(mit dem Artifact-Tool `read` öffnen und als Vergleichstafel für `gate/JUDGE.md` nutzen).

| Element | Wert |
|---|---|
| Akzent | **ein** Blau `#2F6BFF`, Verlauf `#5A86F5 → #2F6BFF → #1A44C2` |
| Papier-Platte | Verlauf `#F7F4EE → #ECE7DD`, Kanten-Schatten `#D6CFC1 / #C9C1B1 / #B5AC9A`, großer weicher Schatten |
| Mattes Glas | `rgba(14,19,30,.58)`, Blur 28 px, 1 px Rand `rgba(255,255,255,.18)` |
| Drehung | leicht, ±1,5 bis 4° |
| Schrift | Montserrat 800 für Aussagen; IBM Plex Mono (Großbuchstaben, Sperrung 3 px) für Pills |
| Satelliten | 1–2 pro Hauptobjekt: Mono-Pill, Icon im Glas- oder Blau-Kreis, große Zahl mit kleinem Label |
| Lage | untere Bildhälfte, y ca. 820–1300 bei 1080×1920 |
| Safe Zone | oben 250, unten 620, links 90, rechts 140 px |

**Mono-Pills als Satelliten:** möglichst **ein Wort** („UFRO“, „META“, „SCHRËTT 1“ zählt als Label mit Zahl) und immer
überlappend mit dem Hauptobjekt. Eine frei stehende Pill mit 2+ Wörtern neben Danny wertet `gate/check.py` als
`text_chips_on_speaker` FAIL (aus der Vorlage übernommen, deckt sich mit J3/J17). Löst ein echter Satellit den Test aus:
kürzen oder enger ans Objekt rücken, nicht den Test abschalten.

Realismus statt Symbolen: Suchfeld mit Vorschlägen (ohne fremde Logos), Ergebnis-Karte mit Bildern, Sternen und Buttons,
Handy-Profilraster, DM-Fenster mit gesendeter Nachricht. Platzhalternamen („Däi Betrib“), nie echte Fremdfirmen.

## Offene Markenpunkte (bei Übergabe erwähnen)
- **Logo:** „ce“-Zeichen, weiß und blau auf Schwarz. Datei (am besten SVG) fehlt noch: bis dahin nur als klar markierter Platzhalter.
- **Domain im CTA:** im Memory prüfen; unklar → fragen statt raten.

## Ehrlichkeit (schützt Danny und seine Kunden)
- Keine erfundenen Zahlen, Ergebnisse, Bewertungen, Testimonials. Kundenzahlen nur, wenn freigegeben.
- Ohne Zahlen: Methode und Ablauf als Beweis zeigen (Filter, Schritte, System). Fehlt ein Beleg: sichtbarer Platzhalter.
- Keine Mitbewerber namentlich. Meta-Richtlinien: keine persönlichen Merkmale unterstellen („Hast Du Schulden?“).
- Echte Kunden-Ads nur mit Freigabe des Kunden zeigen; sonst Platzhalter-Betrieb.

## Danny-Regeln (aus seinen Notizen, wächst mit `learn.py`)
1. Stil v2 mit Material, nie flach. (18.11.2026)
2. Immer zuerst Standbilder zur Freigabe, nie direkt rendern, wenn Konzept oder Overlay-Art neu sind. (18.11.2026)
3. Danny bleibt Hauptsache: Overlays unten, Gesicht frei. (18.11.2026)
