<div align="center">
  <img src="assets/logo.png" alt="Logo" width="90" height="90" style="border-radius: 50%;">
  <h3>Minesweeper Bot</h3>
  <p>💥 Play Minesweeper from Discord! 💥</p>
</div>

## About

<div align="center">
  <img src="assets/screenshot.png" alt="Screenshot" width="50%">
</div>

Play the classic Minesweeper game on your server with this Discord bot! You can control the game
with turn-based commands just as the original, play in parallel with your friends and try to get
the biggest score. Featuring an 8×8 procedurally generated board with 10 mines to discover and evade.

## Usage

**[To add this bot to your server, click this link]().**

### How to play

The provided instructions will teach you how to interact with this bot. If you don't know how to play vanilla
Minesweeper, I recommend [this article](https://minesweepergame.com/strategy/how-to-play-minesweeper.php).

* Start a new game with the `/start` command. The GUI is composed of the board, displayed with emojis,
the left tiles counter, the turn counter, and the name of the user.

* Reveal cells with `/r <row> <column>`. You'll need to provide the coordinates of your cell: they're
displayed in the border of the board, the rows being represented with letters and columns with numbers.
For example, `/r a 0` will reveal the cell in the top left side.

* Your first reveal will always be in an empty cell for safety.

* Same as `/r`, you can place flags with `/f <row> <column>`. Tip: if a number cell has as many flags around
its 8 touching cells as the number displays, you can *reveal the number cell* to automatically reveal the
remaining cells.

* The game advances one turn after each action. If you win or lose, a notification will display.

* You can always cancel your game with `/cancel`.

Use `/help` to view the instructions from the server.

## Roadmap

- [x] Make bot.
- [ ] Add scoreboard.
- [ ] Add customizable size.
- [ ] Replace emojis with sprites.

## Contributing

If you want to make this project better ~~than what I could ever do~~, contributions are always welcome!

### Requirements

The project runs in Python 3 and the library Discord.py

```bash
pip install discord.py
```

### Steps

1. Install the required Discord.py library. `pip install discord.py`
2. Fork the project and clone it. `git clone https://github.com/YOUR-USERNAME/minesweeper-bot`
3. Make a new branch and work on it. `git checkout -b new-feature`
4. Commit the changes. `git commit -m "Added the Thing."`
5. Push the branch. `git push origin new-feature`
6. Open a pull request.

## Acknowledgments

* [Discord.py](https://discordpy.readthedocs.io/en/stable/) | framework
* [Create Your Own Discord Bot in Python 3.10 Tutorial (2022 Edition)](https://www.youtube.com/watch?v=hoDLj0IzZMU) | tutorial
* [Best README Template](https://github.com/othneildrew/Best-README-Template) | template
* [Robert Donner's original Minesweeper](https://archive.org/details/win3_Mineswee) | original creator
* [Iván :3](https://github.com/ivaaane) | creator