class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play():
    game = TicTacToe()
    x_player = "X"
    o_player = "O"
    current_player = x_player

    print("Welcome to Tic Tac Toe!")
    game.print_board()

    while game.empty_squares():
        try:
            square = int(input(f"Player {current_player}'s turn (0-8): "))
            if square not in game.available_moves():
                raise ValueError
            game.make_move(square, current_player)
            game.print_board()

            if game.current_winner:
                print(f"Player {current_player} wins!")
                return

            current_player = o_player if current_player == x_player else x_player

        except ValueError:
            print("Invalid input. Please try again.")

    print("It's a tie!")

if __name__ == "__main__":
    play()