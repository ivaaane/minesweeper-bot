import random

class Game:
    def __init__(self):
        self.size_x = 8
        self.size_y = 8
        self.bombs = 10
        self.tiles = self.size_x * self.size_y
    
    # This takes charge of all the board logic, placing bombs and numbers, and returning a list!
    def init_game(self):
        board = [[0 for i in range(self.size_x)] for i in range(self.size_y)] # Generate empty board
        bombs_placed = 0
        while bombs_placed < self.bombs:
            randx = random.randint(0,self.size_x - 1)
            randy = random.randint(0,self.size_y - 1)
            if board[randy][randx] == 0:
                board[randy][randx] = -1
                bombs_placed += 1
        for i in range(self.size_y):
            for j in range(self.size_x):
                if board[i][j] == -1:
                    continue
                count = 0
                for y in range(max(0, i-1), min(self.size_y, i+2)):
                    for x in range(max(0, j - 1), min(self.size_x, j + 2)):
                        if board[y][x] == -1:
                            count += 1
                board[i][j] = count
        self.board = board
        self.display_board = [[False for i in range(self.size_x)] for i in range(self.size_y)]
    
    # This turns the board list into fancy emojis! It's all aesthetic!
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
    
    # This takes the input of the player and reveals tiles!
    def reveal_tile(self, mode, x, y):

        if mode == "r": # If the input is revealing the tile
            self.display_board[y][x] = True

        elif mode == "f": # If the input is putting a flag
            self.display_board[y][x] = "Flag"
            
        else:
            return False # This tells the bot that an error has occurred
