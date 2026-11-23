# Reel-Cockpit (Clees & Ernster)

Aus Dannys Rohaufnahme wird ein fertiges 9:16-Reel für TikTok, Instagram, Facebook und Meta-Ads: geschnitten nach Gehör,
mit Untertiteln auf Luxemburgisch, Overlays im C&E-Stil v2 und einer Qualitätsprüfung, die vor der Übergabe bestehen muss.

## Was drin ist
- `SKILL.md`: der Ablauf (Fragen → Schnitt → Gesicht → Layout → Overlays → Bauen → Prüfung → Übergabe → Notizen werden Regeln).
- `references/`: C&E-Marke (`MARKE.md`), Plattformen (`PLATTFORMEN.md`), Luxemburgisch (`LUXEMBURGISCH.md`), dazu die Messregeln
  der Vorlage (`PRINCIPLES.md`, `BASELINE.md`, `CHECKS.md`, `HOOKS.md`, `RULES.md`, `LAYOUTS.md`, `AUDIO.md`, `CLIPS.md`).
- `styles/ce.json`: der feste C&E-Stil (Blau #2F6BFF, Montserrat 800, Papier und Glas). Die vier neutralen Presets bleiben als Reserve.
- `scripts/`: Schnitt, Sync, Untertitel, Bauen, Export, Mix, Prüfung. `engine/`: die Welten-Engine. `gate/`: visuelle Prüfung + `JUDGE.md`.

## Einrichten
1. Ordner nach `~/.claude/skills/reel-cockpit/` kopieren (oder als Skill in claude.ai hochladen).
2. In Claude Code: **„schneid mein Reel“**. Beim ersten Mal prüft `scripts/doctor.sh`, was fehlt (Node 22+, ffmpeg, Python + numpy, whisper).
3. Optional: Auphonic-Key in `.env` (`AUPHONIC_API_KEY=...`), nie in den Chat.

## Bekannte Lücken (aus dem Upload)
- `engine/short/render.sh`, `engine/pack/pack.py`, `scripts/sfx_mix.py`, `scripts/make_bed.py` und die Sound-Dateien fehlen.
  Der Standardweg (`edit_build.py` → `export_edit.py` → `mix.py` → `gate.py`) ist vollständig; die Welten-Engine noch nicht.
- `bin/face_track` und `gate/bin/vision` sind Apple-Silicon-Programme (nur Mac).
- Die Epidemic-IDs im Sound-Kit stammen aus der Vorlage (Jack Roberts) und gelten nur nach Neu-Download mit dem C&E-Abo.

Basis: „Shorts Studio“ (MIT-Lizenz, siehe `LICENSE`), angepasst für Clees & Ernster.
