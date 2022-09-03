"""
Tests for connect_four game
tests all its functions, including
construtor, __str__, add_piece,
is_game_over, get_winner and undo.
"""
import unittest
from connect_four import ConnectFour


class connect_fout_test(unittest.TestCase):
    def test_init(self):
        """
        tests the constructor of connect_four
        the board should be initialized with
        6 rows and 7 columns
        :return: None
        """
        board = ConnectFour()
        actual_row = len(board.board)
        expected_row = 6
        self.assertEqual(actual_row, expected_row)

        actual_col = len(board.board[0])
        expected_col = 7
        self.assertEqual(actual_col, expected_col)

    def test_add_piece(self):
        """
        tests add_piece function
        should raise valueError when
        the column is out of range
        or is not integer or is full
        :return: None
        """
        board = ConnectFour()
        try:
            board.add_piece("k")
        except ValueError:
            pass

        try:
            board.add_piece(9)
        except ValueError:
            pass

        board.board = [["X", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", "O", " ", " ", " "]]
        try:
            board.add_piece(0)
        except ValueError:
            pass

    def test_is_game_over(self):
        """
        tests is_game_over function
        in three directions, diagonal,
        vertical and horizontal.
        Should return true when game
        is over, otherwise return false
        :return:
        """
        board = ConnectFour()
        # test vertical row
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "]]
        self.assertTrue(board.is_game_over())

        # test diagonal row
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", "O", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["O", "O", "O", " ", " ", " ", " "]]
        self.assertTrue(board.is_game_over())

        # test horizontal row
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["O", "O", "O", "O", " ", " ", " "]]
        self.assertTrue(board.is_game_over())

        # test false
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["O", "O", "O", " ", " ", " ", " "]]
        self.assertFalse(board.is_game_over())

    def test_get_winner(self):
        """
        tests get_winner function
        should return None when not
        yet a winner, or if the game ends
        in a tie, otherwise it returns
        the player who got 4 in a row
        :return: None
        """
        # test get winner "O"
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", "O", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["O", "O", "O", " ", " ", " ", " "]]
        board.is_game_over()
        self.assertEqual(board.get_winner(), "O")

        # test get winner "X"
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", "O", " ", " ", " "]]
        board.is_game_over()
        self.assertEqual(board.get_winner(), "X")

        # test get winner None
        board = ConnectFour()
        board.board = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", " ", " ", " ", " "],
                       ["X", "O", "O", "O", " ", " ", " "]]
        board.is_game_over()
        self.assertEqual(board.get_winner(), None)

    def test_undo(self):
        """
        tests the undo function
        should remove the last piece that was
        played. If there is nothing to undo
        should raise valueError
        :return:
        """
        # test when no stone was played
        board = ConnectFour()
        try:
            board.undo()
        except ValueError:
            pass

        # test to undo one piece
        board = ConnectFour()
        board.added_stones = [(0, 5)]
        board.undo()
        self.assertEqual(board.added_stones, [])

    def test_str(self):
        board = ConnectFour()
        expected = ("| | | | | | | |\n" + "---------------\n") * 6
        actual = board.__str__()
        self.assertEqual(expected, actual)
