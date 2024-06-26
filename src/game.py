import random

class Game:
    def __init__(self):
        self.active = False

    def init_stats(self):
        self.size_x = 10
        self.size_y = 10
        self.bombs = 15
        self.tiles = self.size_x * self.size_y
        self.turns = 0
        self.board = [["Null" for i in range(self.size_x)] for i in range(self.size_y)]
        self.display_board = [[False for i in range(self.size_x)] for i in range(self.size_y)]
        self.active = True

    # This takes charge of all the board logic, placing bombs and numbers, and returning a list!
    def create_board(self):
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
    def reveal_tile(self, a, b):
        letters = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
        if int(b) >= 0 and int(b) <= self.size_y and a in "abcdefghij":
            y = letters[a]
            x = int(b)
        else: return False
        
        self.display_board[y][x] = True
        self.turns += 1
        if self.turns == 1:
            while self.board[y][x] != 0:
                self.create_board()
        self.chain_reveal_num(x, y)
        self.chain_reveal_zero()
        return True

    # This places flags in the board!
    def place_flag(self, a, b):
        letters = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,}
        if int(b) >= 0 and int(b) <= self.size_y and a in "abcdefgh":
            y = letters[a]
            x = int(b)
        else: return False
        if self.display_board[y][x] == False:
            self.display_board[y][x] = "Flag"
        else: return False
        self.turns += 1
        return True

    # This is used to automatically reveal tiles around a value of '0'!
    def chain_reveal_zero(self):
        for count in range(self.size_x * self.size_y):
        
            for i in range(self.size_y):
                for j in range(self.size_x):
                    
                    if self.display_board[i][j] and self.board[i][j] == 0:
                        for y in range(max(0, i - 1), min(self.size_y, i + 2)):
                            for x in range(max(0, j - 1), min(self.size_x, j + 2)):
                                
                                if self.board[y][x] != -1:
                                     self.display_board[y][x] = True

     # This is used to automatically reveal all tiles around a number that already has enough flags placed around!           
    def chain_reveal_num(self, x, y):
        if self.board[y][x] > 0:
            count = 0
            for i in range(max(0, y - 1), min(self.size_y, y + 2)):
                for j in range(max(0, x - 1), min(self.size_x, x + 2)):
                    if self.display_board[i][j] == "Flag":
                        count += 1
            if count >= self.board[y][x]:
                for i in range(max(0, y - 1), min(self.size_y, y + 2)):
                    for j in range(max(0, x - 1), min(self.size_x, x + 2)):
                        if (self.display_board[i][j] != "Flag") and (self.board[i][j] != -1):
                            self.display_board[i][j] = True

    # This turns the board list into fancy emojis for the embed!
    def print_board(self):
        symbols = {1:"1️⃣",2:"2️⃣",3:"3️⃣",4:"4️⃣",5:"5️⃣",6:"6️⃣",7:"7️⃣",8:"8️⃣",0:"🟦",-1:"💥"}
        gui = {1:"🇦",2:"🇧",3:"🇨",4:"🇩",5:"🇪",6:"🇫",7:"🇬",8:"🇭",9:"🇮",10:"🇯"}

        self.board_str = "⬛⬛0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣⬛⬛\n"
        for i in range(14): self.board_str += "⬛"
        
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
        for i in range(14): self.board_str += "⬛"
        self.board_str += "\n⬛⬛0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣⬛⬛"
