# Initialize the board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Function to print the board (for visual reference)
def print_board():
    symbols = {1: "X", -1: "O", 0: " "}
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * 9)

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if abs(sum(board[i])) == 3:  # Row check
            return board[i][0]
        if abs(sum(board[j][i] for j in range(3))) == 3:  # Column check
            return board[0][i]
    # Diagonal checks
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]
    return 0  # No winner

# Check if there are empty cells
def is_full(board):
    return all(cell != 0 for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner != 0:
        return winner  # Return 1 if the computer wins, -1 if the human wins
    if is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # Check for empty cell
                    board[i][j] = 1  # Computer move
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0  # Undo move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # Check for empty cell
                    board[i][j] = -1  # Human move
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0  # Undo move
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the computer
def best_move():
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Check for empty cell
                board[i][j] = 1  # Computer move
                score = minimax(board, 0, False)
                board[i][j] = 0  # Undo move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Game loop
print("Initial board:")
print_board()
while True:
    # Human's turn
    x, y = map(int, input("Enter your move (row col): ").split())
    if board[x][y] == 0:
        board[x][y] = -1  # Human move
        if check_winner(board) == -1:
            print("Human wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

    # Computer's turn
    move = best_move()
    if move:
        board[move[0]][move[1]] = 1
        print("Computer's move:")
        print_board()
        if check_winner(board) == 1:
            print("Computer wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
    else:
        print("It's a draw!")
        break

