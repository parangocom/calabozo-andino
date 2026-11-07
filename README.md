# Calabozo Andino

A small, beginner-level **text-based role-playing game** written in Python,
inspired by classic interactive-fiction games such as *Zork*. It is a personal
learning project, not a game engine or a finished commercial-style game.

> **Language note:** the game itself (story text and commands) is in **Spanish**.
> This README is in English; a short command reference is given below.

## Overview

You are thrown into a dungeon (*el calabozo*). You move between a handful of
rooms by typing commands, pick up items, and try to reach one of the endings.
Rooms, items and exits are stored in Python dictionaries, and the game runs in
a simple input loop in the terminal.

## Features

Implemented in `scripts/game.py`:

- 5 rooms (El Calabozo, El Pasillo, La Capilla, La Torre, El Monte) defined in a dictionary, connected by north / south / east / west exits.
- Text commands: `ir <direction>` to move and `recoger <item>` to pick up an item.
- A status display each turn showing the current room, the inventory and any visible item.
- 3 items placed in rooms: `machete`, `aguardiente`, `llave` (key).
- An inventory list that updates when items are picked up.
- Three possible endings:
  - **Escape:** reach La Capilla carrying both the `llave` and the `aguardiente`.
  - **Victory over the enemy:** enter El Monte carrying the `machete` (the enemy is La Patasola).
  - **Defeat:** enter El Monte without the `machete`.
- Optional background music played with PyGame's mixer (only if the audio file is present, see [Audio](#audio)).
- Screen clearing between turns.

Not implemented: saving, combat beyond the single encounter above, multiple
items per room, an inventory-use command, or a graphical interface (PyGame is
only used for audio).

### Command reference

| Command | Meaning | Example |
|---|---|---|
| `ir norte` / `sur` / `este` / `oeste` | Go north / south / east / west | `ir norte` |
| `recoger <objeto>` | Pick up an item in the room | `recoger machete` |

Commands are lowercase and case-sensitive.

## Technologies

- **Python 3** (the notebook metadata records Python 3.13.7; the script was also checked on Python 3.12)
- **PyGame** (`pygame.mixer`) for background music
- **Python dictionaries** for rooms, exits, items and the enemy
- **Jupyter Notebook** for an early version of the game logic (see [Development notes](#development-notes))

## Project structure

```text
calabozo-andino/
├── media/
│   └── audio/
│       └── README.md          # explains the (excluded) music file
├── scripts/
│   ├── game.py                # the game: run this
│   └── game_draft.ipynb       # earlier, simpler notebook version
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Install [Python 3](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** in the installer.
2. Download or clone this repository and open a terminal in its folder.
3. (Recommended) create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows (PowerShell):  .venv\Scripts\Activate.ps1
   # macOS / Linux:         source .venv/bin/activate
   ```
4. Install the dependency:
   ```bash
   pip install -r requirements.txt
   ```
   (Only `pygame` is required to run the game.)

## How to run

From the repository root:

```bash
python scripts/game.py
```

The script finds the audio folder relative to its own location, so it can be
launched from any working directory. On some systems the command is `python3`
(or `py` on Windows).

Type commands such as `ir norte` or `recoger machete` and press Enter.
Quick way to see an ending: `recoger machete`, `ir norte`, `ir oeste`, `ir sur`.

### Audio

The original version of the game plays the song **"Calabozo de Mis Penas"** by
**Olimpo Cárdenas** (album *La Guitarra y Sus Ídolos*, 1993) as background music.

- Listen to the original on Spotify: <https://open.spotify.com/intl-fr/track/4kk61J6NcsHidYWxC6b48t>
- All rights to the song and its recording belong to their respective rights holders.
- The audio file is **not included** in this repository and is not redistributed here.
  The author of this repository has no affiliation with the artist.

The game runs normally without the file (no sound). To hear the music locally,
or to use your own, see [`media/audio/README.md`](media/audio/README.md).

## Development notes

`scripts/game_draft.ipynb` is a Jupyter Notebook containing an earlier and
simpler version of the game logic. Compared with `game.py` it has no PyGame
audio, no La Capilla room, no enemy encounter and no working endings (its
second cell contains a `break` outside a loop, which is a syntax error), and it
still contains debugging `print` statements. It is
kept for reference only; **`game.py` is the version to run.** Saved cell outputs
were cleared before publication. The notebook is unfinished and is not meant to be
run as a complete game (opening it requires Jupyter, e.g. `pip install notebook`;
this is not needed for the game).

### Known limitations

- Entering El Monte ends the game immediately (there is no choice to fight or flee).
- Unknown commands are silently ignored.
- Input handling is minimal (e.g. Ctrl+D / Ctrl+Z at the prompt raises an error).

## Future improvements

*These are ideas only; none of them exist yet.*

- Show a help message for unknown commands.
- Support several items per room and a command to use items.
- Move the room data into a separate file (e.g. JSON).
- Add an English version of the text.

## Author

Pablo Arango Combariza
