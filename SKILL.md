---
name: reel-cockpit
description: Reel-Schnitt für Clees & Ernster – macht aus Dannys Rohaufnahme (meist Luxemburgisch, vor der Kamera) ein fertiges 9:16-Reel für TikTok, Instagram, Facebook und Meta-Ads im festen C&E-Stil v2. Findet die Reels in einer langen Aufnahme, synchronisiert Kamera und separates Mikro, schneidet Versprecher, Wiederholungen und Neuansätze nach Gehör, setzt Wort-für-Wort-Untertitel auf Luxemburgisch, Overlays aus Papier und Glas mit blauem Pinselstrich, Sound mit sichtbarer Ursache, mischt auf -14 LUFS und liefert erst nach bestandener Qualitätsprüfung. Dannys Notizen werden zu Regeln. Immer nutzen bei /reel-cockpit, „schneid mein Reel", „mach ein Reel daraus", „Reels aus diesem Video", „Untertitel aufs Reel", „Reel für TikTok/Insta/Meta", „C&E-Reel" oder wenn eine Rohaufnahme von Danny zum Kurzvideo werden soll.
---

# Reel-Cockpit (Clees & Ernster)

Rohaufnahme rein, fertiges Reel raus. Auftraggeber ist Danny (Clees & Ernster, Performance Marketing & KI, Luxemburg). Die Reels laufen
organisch auf TikTok, Instagram und Facebook und als Meta-Ads. Zielgruppe: Inhaber von Luxemburger Premium-Betrieben (Handwerk,
Immobilien, hochpreisige Dienstleistungen). Jedes Reel ist zugleich Arbeitsprobe: Es muss zeigen, dass C&E Werbung macht, die zündet.

Basis ist das MIT-lizenzierte „Shorts Studio“ (Regeln aus 1.971 gemessenen Reels). Die Messregeln gelten weiter. Look, Sprache,
Plattformen und Geschmack kommen von C&E und Danny. **Wo eine C&E-Regel einer Studienregel widerspricht, gewinnt C&E.**

S = dieser Skill-Ordner. E = `$S/engine`. Gearbeitet wird in einem Projektordner P = `reels/<datum>-<thema>/` (`P/work/`, `P/deliver/`).

## Wissensbasis – lies, was der Auftrag braucht
- `references/MARKE.md` – C&E-Stil v2, Tokens, Ton, Ehrlichkeitsgrenzen. **Immer lesen.**
- `references/PLATTFORMEN.md` – TikTok, Instagram, Facebook, Meta-Ads: Maße, Safe Zones, Längen, Cover, Varianten. **Immer lesen.**
- `references/LUXEMBURGISCH.md` – Transkription, Schreibweise, Füllwörter, Untertitel auf LB/DE/FR. **Bei jeder LB-Aufnahme.**
- `references/PRINCIPLES.md` + `references/BASELINE.md` – 99 Prinzipien und 19 Messregeln. **Vor dem ersten Layout lesen.**
- `references/HOOKS.md` – Hook-Rezepte, inkl. C&E-Varianten. `references/CLIPS.md` – Reels in langen Aufnahmen finden.
- `references/RULES.md`, `references/LAYOUTS.md`, `references/AUDIO.md`, `references/CHECKS.md` – Regeln, plan.json, Ton, alle Prüfungen.
- `gate/JUDGE.md` – die Augenprüfung (C&E-Fassung). **Vor jeder Übergabe.**

Nachbar-Skills: **copywriter-cockpit** liefert Hooks, Skripte und Posttexte (Farbtypen Rot/Gelb/Grün/Blau). **motion-designer-cockpit**
liefert Standbilder-Freigabe, aufwendige Overlays und ProRes-Lieferung für DaVinci. Dieser Skill macht den Schnitt und das Reel.

## 0. Fragen (einmal, eine Nachricht)
Schick `references/questions.md` (7 Fragen). Überspring, was Danny schon gesagt hat. „go“ heißt: alle Standards.
Dann `bash $S/scripts/doctor.sh` und beheben, was es meldet.

## 1. Quellen
- Kamera + separates Mikro/Bildschirmaufnahme: `python3 $S/scripts/sync.py --video cam.mov --audio mic.wav --out work/` (auf die ms).
- Lange Aufnahme: Transkript (Schritt 2.4), dann Reels finden (`references/CLIPS.md`), dann
  `python3 $S/scripts/clip_cut.py synced.mp4 --words work/words_raw.json --clips clips.json --out work/clips`.

## 2. Der Schnitt (nach Gehör, nicht nach Lesen)
Sprache: `export REEL_LANG=lb` (Standard; `de`, `fr`, `en` möglich). Nie ein `*.en`-Modell für Luxemburgisch.
1. `python3 $S/scripts/captions.py <clip> --out work` (whisper large-v3, LB). Transkript lesen, **Fehlhörer sofort korrigieren**
   (`scripts/fix_words.py`, Wörterbuch in `references/LUXEMBURGISCH.md`). Luxemburgisch hört Whisper schlecht: jede Zeile prüfen.
2. `python3 $S/scripts/repeat_check.py work/words_raw.json --audio <clip>` findet Stottern, Wiederholungen, Neuansätze. Immer den
   LETZTEN Take behalten. Füllwörter („äh“, „ähm“, „also“, „jo“, „bon“, „gell“) gehören in die Drops, wenn sie den Satz nicht tragen.
3. Drops an leisen Stellen schneiden: `python3 $S/scripts/silence_cut.py <clip> --out work/cut1 --words work/words_raw.json --drop drops.json --min-silence 0.6`.
4. Stimme einmal säubern, auf dem Schnitt: `python3 $S/scripts/auphonic.py work/cut.mp4 --out work/cut.mp4` (optional, stark empfohlen).
5. Schnitt neu transkribieren, korrigieren, `repeat_check.py` nochmal: 0 Funde, sonst nachschneiden.
Ziel: 25 bis 50 s, keine tote Luft, erstes Wort bei 0,0 s. Luxemburgisch spricht sich langsamer als Englisch: 3,2+ Wörter/s reicht.

## 3. Gesicht, Blick nach unten, Kamerasprünge
- `$S/bin/face_track work/cut.mp4 work/face.json 10` (Apple Vision, nur auf dem Mac; ohne Mac: Gesichtsbox aus `scripts/frames.sh`-Standbildern ablesen).
- Blick nach unten (Kopf 9°+ unter normal für 0,2 s+) → `work/eyes_down.json`. Grenzfälle per Bildstreifen mit eigenen Augen prüfen.
- Jede Schnittstelle → `work/joins.json`. Nie ein nackter Jump Cut: Layoutwechsel, Grafik oder zweite Einstellung darüber.

## 4. Layout aus den Sätzen
Standard für C&E: **Danny bleibt Hauptsache.** Vollbild-Danny, Overlays in der unteren Hälfte (y 820–1300), Gesicht frei.
Split (Beweis oben, Danny unten) nur, wenn es echten Beweis gibt: Ads-Manager, Anfrage-Formular, echte Kunden-Ad (freigegeben).
- Eine Idee pro Einstellung, 2 bis 5 s, keine unter 1,5 s. Wechsel am Satzende oder AUF dem Wort, das die nächste Einstellung zeigt.
- Frame 0: Danny spricht, eine klare Headline steht (2 bis 6 Wörter). Beweis zuerst, wenn es Beweis gibt.
- Welten-Engine (`edit.json`): vor dem Bauen `python3 $S/scripts/layout_check.py <P>` → LAYOUT OK.

## 5. Overlays im C&E-Stil v2
Stil: `styles/ce.json` in den `"style"`-Block von `plan.json` kopieren (`"material": "ce"` schaltet Papier, Glas und Pinselstrich an).
**Neues Konzept oder neue Overlay-Art: erst 4–5 Standbilder zur Freigabe** (motion-designer-cockpit), nie direkt rendern.
- Material statt Fläche: Papier-Platte mit Kante oder mattes Glas, leicht gedreht (±1,5–4°). Nie flache Pills ohne Material.
- 1–2 Satelliten pro Hauptobjekt (Mono-Pill, Icon im Glas- oder Blau-Kreis, große Zahl mit kleinem Label).
- Realismus: echte Oberflächen nachbauen (Suchfeld, Ergebnis-Karte, Handy-Profilraster, DM-Fenster) mit Platzhalternamen
  („Däi Betrib“), nie echte Fremdfirmen. Höchstens 3 Wörter + 1 Zahl pro Grafik. `**Wort**` bekommt den blauen Pinselstrich.
- Text im Bild auf Luxemburgisch (Schreibweise nach lod.lu), Du/Däin groß.
Graphik-Typen und Aufbau: `references/LAYOUTS.md`, Beispiel `examples/edit-plan.json`.

## 6. Bauen, rendern, Ton
```bash
python3 $S/scripts/edit_build.py --cut work/cut.mp4 --words work/words.json --plan plan.json --out work/edit
python3 $S/scripts/export_edit.py --project work/edit --work work --out deliver/reel.mp4 --quality high [--nle]
python3 $S/scripts/mix.py deliver/reel.mp4 --out deliver/reel-final.mp4 [--music <lizenzierter Track>]
```
`--nle` legt zusätzlich ein Overlay-`.mov` mit Alpha, eine XML-Timeline und eine `.srt` für DaVinci/Premiere ab.
Ton: -14 LUFS, Spitzen unter -1 dBTP, Musik ca. 14 dB unter der Stimme. Musik ist optional (56 % der viralen Reels haben keine).
Epidemic Sound nur mit dem **eigenen C&E-Abo** (`references/AUDIO.md`); die IDs im Sound-Kit stammen aus der Vorlage und müssen
mit Dannys Konto neu geladen werden. Vor „Confirm & Download“ immer Danny fragen.
Fortgeschritten (Welten-Engine mit `edit.json` + `scenes.js`): `python3 $E/shared/run.py <P> --only trim,prep,gen,check`.
Im Upload fehlen dafür `engine/short/render.sh` und `engine/pack/pack.py` – bis sie nachgereicht sind, den Weg oben nehmen.

## 7. Prüfung: nichts geht raus, bevor sie besteht
```bash
python3 $S/scripts/gate.py --project work/edit --final deliver/reel-final.mp4      # Standardweg (plan.json)
python3 $S/scripts/qa.py <P> --video deliver/reel-final.mp4 --accents "#2F6BFF"    # Welten-Engine (edit.json, design.json)
```
Jedes FAIL beheben, neu laufen lassen. Dann den Kontaktbogen (2 Bilder/s) mit dem Read-Tool ansehen und `gate/JUDGE.md`
durchgehen: leere oder graue Frames, zu kleine Grafiken, Text über dem Gesicht, etwas in der Safe Zone, falsch geschriebenes
Luxemburgisch, erfundene Zahl. Ein Check, der bei einem schlechten Frame PASS sagt, ist falsch: Check reparieren, Regel aufschreiben.

## 8. Übergabe
- `deliver/reel-final.mp4` mit `SendUserFile`, dazu eine Zeile: Länge, Sprache, Hook-Typ, für welche Plattform.
- Dateiname: `CE_<Thema>_<Hook>_9x16_<Länge>s_vN.mp4`. Für Meta-Feed zusätzlich 4:5, wenn gewünscht (`references/PLATTFORMEN.md`).
- Cover-Frame (Titel in der mittleren 3:4-Zone) und Posttext (aus copywriter-cockpit) mitliefern.
- Annahmen nennen (Logo-Platzhalter, ungeprüfte LB-Schreibweise, Musiklizenz).
- Ein konkreter nächster Schritt: z. B. 4 Hook-Varianten (eine pro Farbtyp) für einen Meta-A/B-Test.

## 9. Notizen werden Regeln
Jede Notiz von Danny wörtlich speichern: `python3 $S/scripts/learn.py note "<seine Worte>" --short <name>`.
Kommt eine Notiz zweimal, wird sie Regel (`learn.py promote`), eine Frage in `gate/JUDGE.md` und eine Zeile in `references/MARKE.md`.
Alles liegt in `~/.reel-cockpit/` (außerhalb des Skills, Updates löschen es nicht). Das Template reparieren, nicht nur das Video.
