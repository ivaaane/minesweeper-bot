# Discord Minesweeper

Play Minesweeper from Discord!

## Usage

### Host

The bot needs to be self-hosted. Create a new Discord bot profile and generate a token. Then follow:

```sh
# get the code
git clone https://github.com/ivaaane/minesweeper-bot.git
cd minesweeper-bot

# store token
touch src/.env
echo "DISCORD_TOKEN={insert_your_token}" > src/.env

# start bot
python src/main.py
```

### How to play

> The provided instructions will teach you how to interact with this bot. If you don't know how to play vanilla
Minesweeper, I recommend [this article](https://minesweepergame.com/strategy/how-to-play-minesweeper.php).

* Start a new game with the `/start` command. The interface is composed of the board, displayed with emojis,
the left tiles counter, the turn counter, and the name of the user.

* Reveal cells with `/r <row> <column>`. You'll need to provide the coordinates of your cell: they're
displayed in the border of the board, the rows being represented with letters and columns with numbers.
For example, `/r a 0` will reveal the cell in the top left side.

* Your first reveal will always be in an empty cell for safety.

* Same as `/r`, you can place flags with `/f <row> <column>`. If a number cell has as many flags as its display number as neighbour,
revealing the cell will automatically reveal the rest of neighbours.

* The game advances one turn each action. You will be notified if you win or lose.

* Cancel your game with `/cancel`.

Use `/help` to view the instructions from the server.
