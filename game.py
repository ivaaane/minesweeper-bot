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
            1: ":one:",
            2: ":two:",
            3: ":three:",
            4: ":four:",
            5: ":five:",
            6: ":six:",
            7: ":seven:",
            8: ":eight:",
            0: ":blue_square:",
            -1: ":boom:",
        }
        self.board_str = ""
        for i in self.board:
            line = ""
            for j in i:
                line += symbols[j]
            line += "\n"
            self.board_str += line