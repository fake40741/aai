# Tic-Tac-Toe using Minimax Algorithm
#T.C=O(b^d) S.C=O(d)
board = [' ' for _ in range(9)]
# Display the board
def print_board():
    print()
    for i in range(3):
        print(" " + board[i * 3] + " | " +
              board[i * 3 + 1] + " | " +
              board[i * 3 + 2])
        if i < 2:
            print("---|---|---")
    print()
# Check if a player has won
def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in win_positions:
        if all(board[i] == player for i in position):
            return True
    return False
# Check for draw
def is_draw():
    return ' ' not in board
# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)

        return best_score
    else:
        best_score = 999

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)

        return best_score
# AI Move
def ai_move():
    best_score = -999
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'
# Human Move
def human_move():
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1

            if 0 <= position < 9 and board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a valid number.")

# Main Game
print("TIC-TAC-TOE")
print("You are X and AI is O.")

print("\nPositions are:")
print("1 | 2 | 3")
print("---|---|---")
print("4 | 5 | 6")
print("---|---|---")
print("7 | 8 | 9")

while True:
    print_board()
    human_move()

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

# Algorithm
# 1. Initialize a 3 × 3 board.
# 2. Accept the human player's move (X).
# 3. Check whether the human wins or the game is a draw.
# 4. The AI (O) evaluates all possible moves using Minimax.
# 5. The AI chooses the move with the highest score.
# 6. Repeat until a player wins or the game ends in a draw.
# Complexity
# - Time: \(O(b^d)\), where \(b\) is the branching factor and \(d\) is the search depth.
# - Space: \(O(d)\) auxiliary recursion space.
# Viva tip: O is the maximizing player, X is the minimizing player, +1 means AI wins, -1 means the human wins, and 0 means a draw.