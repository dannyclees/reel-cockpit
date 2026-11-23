# Luxemburgisch: Transkript, Untertitel, Schreibweise

Danny spricht meist Luxemburgisch. Die Vorlage war auf Englisch gebaut; das hier hält den Schnitt für LB sauber.

## Transkription
- Sprache setzen: `export REEL_LANG=lb` (Standard). Für deutsche oder französische Reels `de` bzw. `fr`.
- **Nie ein `*.en`-Modell** (small.en, medium.en): die verstehen nur Englisch.
- Hauptdurchgang: `large-v3` (Standard in `captions.py` und `transcribe.py`, ca. 3 GB beim ersten Lauf).
- Tiefer Wiederholungs-Check in 3-s-Fenstern: `medium` (Standard über `REEL_DEEP_MODEL`), weil large-v3 dort zu langsam ist.
- Whisper kann Luxemburgisch nur mäßig: Er rutscht oft ins Deutsche („ich“ statt „ech“, „ist“ statt „ass“) oder verhört Namen.
  Darum ist **Korrigieren Pflicht**, nicht optional: das ganze Transkript lesen, bevor Untertitel gesetzt werden.
- Rutscht er stark ins Deutsche, mit `--language lb` erneut laufen lassen; als Gegenprobe einen anderen Transkriptionsdienst
  testen (z. B. ElevenLabs Scribe über den Connector, falls verbunden) und das bessere Ergebnis nehmen. Wortzeiten müssen bleiben.

## Fehlhörer-Wörterbuch (wächst mit jedem Reel)
Mit `scripts/fix_words.py work/words_raw.json --fix '{...}'` anwenden. Feste Einträge:
```json
{"Klees": "Clees", "Clés": "Clees", "Ernsta": "Ernster", "Meeta": "Meta", "Tiktok": "TikTok"}
```
Nur Einzelwörter (fix_words ersetzt Wort für Wort; „Ernst“ nicht eintragen, das ist auch ein echtes Wort). Neue Fehlhörer hier ergänzen.

## Schreibweise im Bild und in Untertiteln
- Nach **lod.lu** (Lëtzebuerger Online Dictionnaire) und **spellchecker.lu** prüfen. Unsicher → Wort markieren und Danny fragen.
- Du/Däin/Dir/Dech großgeschrieben (C&E-Regel).
- n-Regel (Eifeler Regel) beachten: das End-n fällt vor den meisten Konsonanten weg („en Ufro“, aber „e Betrib“).
- Untertitel geben wieder, was er sagt, nicht eine deutsche Übersetzung. Englische Fachwörter (Ads, Lead, Funnel) bleiben, wie gesagt.
- Für eine deutsche oder französische Fassung: eigene Untertitelspur, nie gemischt in einer Zeile.

## Füllwörter und Neuansätze
Typisch: „äh“, „ähm“, „also“, „jo“, „bon“, „gell“, „voilà“, „wéi gesot“. Schneiden, wenn sie den Satz nicht tragen.
„Bon,“ als bewusster Satzanfang darf bleiben, wenn es Danny-Ton ist.
`repeat_check.py` vergleicht jetzt mit Umlauten und Akzenten (ä, ë, é); vorher fielen sie aus dem Vergleich.

## Tempo
Luxemburgisch hat längere Wörter als Englisch. Die Studienregel „4+ Wörter/s“ gilt hier nicht 1:1: 3,2+ Wörter/s ohne Pausen
über 0,2 s ist das Ziel. Wichtiger als die Zahl: keine tote Luft, keine Pause vor der Pointe.
