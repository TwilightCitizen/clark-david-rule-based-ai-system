"""
A simple console-based Tic-Tac-Toe game (human vs computer) using only native Python.
Functional style, minimal dependencies, and small, focused functions.
"""

def display_board(board):
    print("\n  0 1 2")

    for i, row in enumerate(board): print(f"{i} " + " ".join(row))

    print()

def empty_board():
    return [[" ", " ", " "] for _ in range(3)]

def prompt_human():
    return input("Enter your move as 'row col' (or 'q' to quit): ").strip()

def human_input_quit(move):
    return move.lower() == 'q'

def human_input_invalid(parts):
    is_invalid = len(parts) != 2 or not all(p.isdigit() for p in parts)

    if is_invalid: print("Invalid input. Please enter row and column numbers (e.g., 1 2).")

    return is_invalid

def human_input_out_of_bounds(board, row, col):
    if not (0 <= row < 3 and 0 <= col < 3):
        print("Row and column must be between 0 and 2.")

        return True

    return False

def human_input_spot_taken(board, row, col):
    if board[row][col] != " ":
        print("That cell is already taken. Try again.")

        return True

    return False

def human_input_rejected(board, row, col):
    return (
        human_input_out_of_bounds(board, row, col) or
        human_input_spot_taken(board, row, col)
    )

def get_human_move(board):
    while True:
        move = prompt_human()

        if human_input_quit(move): return None, None
        
        parts = move.split()

        if human_input_invalid(parts): continue

        row, col = map(int, parts)

        if (human_input_rejected(board, row, col)): continue

        return row, col

def get_computer_move(board):
    # Simple rule: pick the first available cell (can be improved)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j
            
    return None, None

def make_move(board, row, col, player):
    board[row][col] = player

def get_all_rows(board):
    return [row for row in board]

def get_all_columns(board):
    return [[board[i][j] for i in range(3)] for j in range(3)]

def get_all_diagonals(board):
    return [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

def get_all_lines(board):
    return [
        *get_all_rows(board),
        *get_all_columns(board),
        *get_all_diagonals(board)
    ]

def is_winner(line):
    return line[0] != " " and line[0] == line[1] == line[2]

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def check_winner(board):
    lines = get_all_lines(board)

    for line in lines: 
        if is_winner(line): return line[0]

    if is_draw(board): return "draw"
    
    return None

def is_human_turn(current):
    return current == "X"

def human_quit(row):
    did_quit = row is None

    if did_quit: print("You quit the game.")

    return did_quit

def player_from_symbol(symbol):
    return "human" if symbol == "X" else "computer"

def show_winner(board):
    winner = check_winner(board)

    if winner:
        display_board(board)

        if winner == "draw":
            print("It's a draw!")
        else:
            print(f"The {player_from_symbol(winner)} wins!")

    return winner

def swap_current_player(current):
    return "O" if current == "X" else "X"

def process_turn(board, current):
    did_quit = False

    if is_human_turn(current):
        row, col = get_human_move(board)
        did_quit = human_quit(row)

    else:
        print("Computer's turn...")

        row, col = get_computer_move(board)

    return [did_quit, row, col]


def play_game():
    board = empty_board()
    current = "X"  # Human is X, computer is O

    while True:
        display_board(board)

        did_quit, row, col = process_turn(board, current)

        if did_quit: break

        make_move(board, row, col, current)

        if show_winner(board): break

        current = swap_current_player(current)

if __name__ == "__main__": play_game()
