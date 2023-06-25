def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def is_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def is_board_full(board):
    return all(x != " " for x in board)

def get_valid_input(board):
    while True:
        user_input = input("Enter a position (1-9): ")
        if not user_input.isdigit():
            print("Please enter a valid number.")
        elif int(user_input) < 1 or int(user_input) > 9:
            print("Please enter a number between 1 and 9.")
        elif board[int(user_input) - 1] != " ":
            print("That position is already taken.")
        else:
            return int(user_input) - 1

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = players[0]

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        position = get_valid_input(board)
        board[position] = current_player
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break
        else:
            current_player = players[1] if current_player == players[0] else players[0]

play_game()