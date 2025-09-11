"""
A simple console-based Tic-Tac-Toe game (human vs computer) using only native Python.
Functional style, minimal dependencies, and small, focused functions.
"""

def display_board(board):
    print("\n  0 1 2")

    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

    print()

def empty_board():
    return [[" ", " ", " "] for _ in range(3)]

def get_human_move(board):
    while True:
        move = input("Enter your move as 'row col' (or 'q' to quit): ").strip()

        if move.lower() == 'q':
            return None, None
        
        parts = move.split()

        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            print("Invalid input. Please enter row and column numbers (e.g., 1 2).")
            continue

        row, col = map(int, parts)

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

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

def check_winner(board):
    lines = (
        # Rows
        board[0], board[1], board[2],

        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    )

    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
        
    if all(cell != " " for row in board for cell in row):
        return "draw"
    
    return None

def play_game():
    board = empty_board()
    current = "X"  # Human is X, computer is O

    while True:
        display_board(board)

        if current == "X":
            row, col = get_human_move(board)
            if row is None:
                print("You quit the game.")
                break
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)

        make_move(board, row, col, current)
        winner = check_winner(board)

        if winner:
            display_board(board)

            if winner == "draw":
                print("It's a draw!")
            elif winner == "X":
                print("Congratulations, you win!")
            else:
                print("Computer wins!")

            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    play_game()
