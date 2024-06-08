import random

class Game:
    def __init__(self):
        self.size_x = 8
        self.size_y = 8
        self.bombs = 10
        self.tiles = self.size_x * self.size_y
        self.active = False
    
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
    
    def print_board(self):
        symbols = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣",
            4: "4️⃣",
            5: "5️⃣",
            6: "6️⃣",
            7: "7️⃣",
            8: "8️⃣",
            0: "🟦",
            -1: "💥",
        }
        gui = {
            1: ":regional_indicator_a:",
            2: ":regional_indicator_b:",
            3: ":regional_indicator_c:",
            4: ":regional_indicator_d:",
            5: ":regional_indicator_e:",
            6: ":regional_indicator_f:",
            7: ":regional_indicator_g:",
            8: ":regional_indicator_h:",
        }

        self.board_str = "⬛⬛1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣⬛⬛\n"
        for i in range(12): self.board_str += "⬛"
        
        count = 1
        for i in self.board:
            line = "\n" + gui[count] + "⬛"
            for j in i:
                line += symbols[j]
            line += "⬛" + gui[count]
            self.board_str += line
            count += 1
        self.board_str += "\n"
        for i in range(12): self.board_str += "⬛"
        self.board_str += "\n⬛⬛1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣⬛⬛"