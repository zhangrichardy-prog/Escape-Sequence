# Escape Sequence

A text-based escape room game written in Python. The room is drawn with **Python Turtle** and you play through a numbered menu in the terminal, a bit like a classic RPG. You have **10 minutes** to search the room, crack the code and get through a round of trivia.

---

## How to Play

1. Run the game. A Turtle window opens and draws the room: a door, window, clock, rug, table and trash can.
2. Go back to the **terminal**. That's where you play.
3. Type the **number** of the option you want, not the word.
4. Escape before the 10-minute timer runs out!

### Rules
- Please don't crash the game on purpose.
- Don't click on or interact with the Turtle window.
- Pick options by their number.
- Have fun!

---

## Levels

### Level 1: The Room
You're locked in a room full of objects. Some hide letters, some hold riddles and clues, and some are only there to waste your time with bad jokes.

Objects you can inspect:

| # | Object | # | Object |
|---|--------|---|--------|
| 1 | Door | 8 | Trash can |
| 2 | Table | 9 | Chair |
| 3 | Plant | 10 | Shoes |
| 4 | Clock | 11 | Lamp |
| 5 | Window | 12 | Envelope |
| 6 | Rug | 13 | **Door Lock** |
| 7 | Dishes | | |

Find all the hidden letters, unscramble them into a word and type it into the **Door Lock** (option 13) to escape.

> **Hint:** Not every clue hands you a letter directly. Some are riddles, and the answer to a riddle may point to a letter. Read everything carefully.

### Level 2: Trivia Gauntlet
Answer **10 multiple-choice questions** correctly to win. Questions are picked at random from a pool of riddles and general knowledge trivia.

- Answer by typing **A, B, C or D**.
- Every **wrong answer takes 3 seconds** off your remaining time.
- The game has opinions about your wrong answers. Lots of them.

---

## Time Limit
You get **10 minutes in total** for both levels. If the clock runs out, you lose... womp womp.

---

## Requirements

- **Python 3.x**
- **turtle**, which comes with Python but needs **Tkinter**
  - Windows/macOS: usually included with Python
  - Linux: you may need to install it, e.g. `sudo apt install python3-tk`
- *(Optional)* The **Space Grotesk** font for the clock numbers. If it isn't installed, the game uses a default font.

No external packages are needed. The game only uses `turtle`, `time`, `random` and `os` from the standard library.

---

## Running the Game

```bash
python escape_sequence.py
```

On some systems use:

```bash
python3 escape_sequence.py
```

---

## Known Limitations

- The timer is only checked between actions, so the game won't end mid-prompt even if time has run out.
- Trivia questions can repeat.
- The Turtle window can look unresponsive while the game waits for terminal input. That's normal: keep playing in the terminal.

---

## Future Ideas
- More escape rooms/levels
- A real inventory system for collected letters and items
- Success rates based on your choices
- An in-game hint system
- ASCII art versions of the room

---

## Author
Made by Richard Zhang

Thanks for playing **Escape Sequence**! See you next round.
