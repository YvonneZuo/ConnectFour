import collections


class ConnectFour:

    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", "X", "0", " ", " ", " "],
                      [" ", " ", "O", "O", " ", " ", " "],
                      [" ", "X", "X", "X", " ", " ", " "]]

        self.stones = ["O", "X", "O", "X", "O", "X", "O",
                       "X", "O", "X", "O", "X", "O", "X",
                       "O", "X", "O", "X", "O", "X", "O",
                       "X", "O", "X", "O", "X", "O", "X",
                       "O", "X", "O", "X", "O", "X", "O",
                       "X", "O", "X", "O", "X", "O", "X"]

        self.rows = 6
        self.columns = 7
        self.winner = None
        self.game_over = False
        self.added_stones = []

    def add_piece(self, column):
        """
        takes a single int as a parameter, and this
        is the column to place the piece. If the column is
        invalid(outside of the playing area), if the column
        is already full, or if the game already is over, It will
        raise ValueError. Otherwise it will put a a piece of
        the current player at the lowest empty row in that column.
        :param: column, int
        :return: self.board, list of list
        """
        if not isinstance(column, int):
            raise ValueError
        if column < 0 or column > 6:
            raise ValueError
        # check whether is column is full
        col_open = False
        for r in range(self.rows):
            if self.board[r][column] == " ":
                col_open = True

        if col_open and not self.game_over:
            stone = self.stones.pop()
            # print(stone)
            for r in range(self.rows):
                c = column
                if self.board[r][c] == "X" or self.board[r][c] == "O":
                    self.board[r - 1][column] = stone
                    self.added_stones.append((r - 1, column))
                    self.game_over = self.is_game_over()
                    return self.board

            self.board[self.rows - 1][column] = stone
            self.added_stones.append((self.rows - 1, column))
            self.game_over = self.is_game_over()

        else:
            raise ValueError

        return self.board

    def is_game_over(self):
        """
        returns a boolean that is True only is the game is over
        (the board is full or one player got 4 in a row, where(
        "in a row" means a straight line of four in any direction)
        :param: self
        :return: boolean
        """
        # directions = {(-1, -1): 0, (-1, 0): 0, (-1, 1): 0,
        #             (0, -1): 0, (0, 1): 0, (1, -1): 0,
        #             (1, 0): 0, (1, 1): 0}


        # directions = {(-1, -1): [], (-1, 0): [], (-1, 1): [],
        #     (0, -1): [], (0, 1): [], (1, -1): [],
        #     (1, 0): [], (1, 1): []}
        def scan(r, c, symbol, count):
            if (r not in range(self.rows) or c not in range(self.columns) or self.board[r][c] != symbol):
                return False
            count += 1

        directions = {(-1, -1): "LU", (-1, 0): "U", (-1, 1): "RP",
            (0, -1): "L", (0, 1): "R", (1, -1): "DL",
            (1, 0): "D", (1, 1): "RD"}

        directions_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (-1, 1), (1, 0), (1, 1)]

        for r in range(self.rows):
            for c in range(self.columns):
                if self.board[r][c] == "X" or self.board[r][c] == "O":
                    symbol = self.board[r][c]
                    for dire in directions:
                        nei_r, nei_c = r + dire[0], c + dire[1]
                        while (nei_r in range(self.rows) and nei_c in range(self.columns)
                           and self.board[nei_r][nei_c] == symbol):
                           direction = directions[dire]
                           if direction == "U":
                               nei_r -= 1

                        if self.board[nei_r][nei_c] == symbol



    def get_winner(self):
        """
        returns None if there not yet a winner, or if the game
        ends in a tie, otherwise it returns the player who got
        4 in a row
        :param:self
        :return:string--player who winned the game
        """
        return self.winner

    def undo(self):
        """
        removes the last piece that was played. Repeatedly
        call this method will continue to step one play
        backwards. (using stack) If there is nothing to undo
        it will raise a value error.
        :param:self
        :return: None
        """
        if self.added_stones:
            row, col = self.added_stones.pop()
            last_stone = self.board[row][col]
            self.stones.append(last_stone)
            self.board[row][col] = " "

        else:
            raise ValueError

    def __str__(self):
        """
        returns a string that represents the board.
        (6 rows and 7 columns)
        :param: self
        :return: string--representing the board
        """
        underlines = "---------------"
        output = ""
        for row in range(12):
            if row % 2 == 0:
                index = 0
                for j in range(15):
                    if j % 2 == 0:
                        output += "|"
                    else:
                        # print("row:", row)
                        # print("index:", index)
                        output += self.board[row // 2][index]
                        index += 1
            else:
                # print("odd line")
                output += underlines
            output += "\n"

        return output
