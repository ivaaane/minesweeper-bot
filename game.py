import random

class Game:
    def __init__(self):
        self.size_x = 8
        self.size_y = 8
        self.bombs = 10
        self.tiles = self.size_x * self.size_y
        self.turns = 0
        self.board = [["Null" for i in range(self.size_x)] for i in range(self.size_y)]
        self.display_board = [[False for i in range(self.size_x)] for i in range(self.size_y)]
    
    # This takes charge of all the board logic, placing bombs and numbers, and returning a list!
    def init_game(self):
        self.board = [[0 for i in range(self.size_x)] for i in range(self.size_y)]
        bombs_placed = 0
        while bombs_placed < self.bombs:
            randx = random.randint(0,self.size_x - 1)
            randy = random.randint(0,self.size_y - 1)
            if self.board[randy][randx] == 0:
                self.board[randy][randx] = -1
                bombs_placed += 1
        for i in range(self.size_y):
            for j in range(self.size_x):
                if self.board[i][j] == -1:
                    continue
                count = 0
                for y in range(max(0, i-1), min(self.size_y, i+2)):
                    for x in range(max(0, j - 1), min(self.size_x, j + 2)):
                        if self.board[y][x] == -1:
                            count += 1
                self.board[i][j] = count
    
    # This takes the input of the player and reveals tiles!
    def reveal_tile(self, mode, a, b):
        letters = {
            "a":0,
            "b":1,
            "c":2,
            "d":3,
            "e":4,
            "f":5,
            "g":6,
            "h":7,
            }

        if int(b) >= 0 and int(b) <= self.size_y + 1 and a in "abcdefgh":
            y = letters[a]
            x = int(b) - 1
        else: return False

        if mode == "r": # Reveal
            self.display_board[y][x] = True
            self.turns += 1
            if self.turns == 1:
                while not self.board[y][x] == 0:
                    self.init_game()
            self.chain_reveal()
            return True

        elif mode == "f": # Flag
            self.display_board[y][x] = "Flag"
            self.turns += 1
            return True

        return False

    # This is used to automatically reveal tiles around a value of '0'!
    def chain_reveal(self):
        for count in range(self.size_x * self.size_y):
        
            for i in range(self.size_y):
                for j in range(self.size_x):
                    
                    if self.display_board[i][j] and self.board[i][j] == 0:
                        for y in range(max(0, i-1), min(self.size_y, i+2)):
                            for x in range(max(0, j - 1), min(self.size_x, j + 2)):
                                
                                if not self.board[y][x] == -1:
                                    
                                     self.display_board[y][x] = True
                                     
    # This turns the board list into fancy emojis!
    def print_board(self):
        symbols = {1:"1️⃣",2:"2️⃣",3:"3️⃣",4:"4️⃣",5:"5️⃣",6:"6️⃣",7:"7️⃣",8:"8️⃣",0:"🟦",-1:"💥"}
        gui = {1:"🇦",2:"🇧",3:"🇨",4:"🇩",5:"🇪",6:"🇫",7:"🇬",8:"🇭"}

        self.board_str = "⬛⬛1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣⬛⬛\n"
        for i in range(12): self.board_str += "⬛"
        
        count = 1
        for idx, i in enumerate(self.board):
            line = "\n" + gui[count] + "⬛"
            for jdx, j in enumerate(i):
                
                if self.display_board[idx][jdx] == True:
                    line += symbols[j]
                elif self.display_board[idx][jdx] == False:
                    line += "⬜"
                else:
                    line += "🚩"
                
            line += "⬛" + gui[count]
            self.board_str += line
            count += 1
        self.board_str += "\n"
        for i in range(12): self.board_str += "⬛"
        self.board_str += "\n⬛⬛1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣⬛⬛"
