"""
Interactive center for connect four game
It will execute the game and allow the
player to play. It will print out the board
and prompt the user to play a piece or undo
the preivous paly. If the input is Q, it will
print out the final state of the board and give
a message about the winner.
"""
from connect_four import ConnectFour


def main():
    board = ConnectFour()
    print(board)
    print("Play a piece, or undo the previous play?")
    stop = False

    while not stop and not board.game_over:
        command = input("U: undo, P: play, Q: quit\n")
        if command == "U":
            try:
                board.undo()
            except ValueError:
                print("Sorry, no stones to undo.")
                continue
            print(board)
        if command == "P":
            try:
                col = int(input("choose a column(0-6): "))
                board.add_piece(col)
            except ValueError:
                print("Sorry, column should be integer and within 0-6.")
                continue
            print(board)
        if command == "Q":
            print(board)
            print("Game over")
            print("Winner is", board.get_winner())
            stop = True

    if board.game_over:
        print(board)
        print("Game over")
        print("Winner is", board.get_winner())


main()
