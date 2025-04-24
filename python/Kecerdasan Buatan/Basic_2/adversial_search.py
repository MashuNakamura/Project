def print_board(board):
    for i in range(3):
        print(board[i*3] + '|' + board[i*3+1] + '|' + board[i*3+2])
    print()

def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6],
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_full(board):
    return all(cell != " " for cell in board)

def minimax(board, is_X_turn):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if is_full(board):
        return 0

    if is_X_turn:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                if score < best_score:
                    best_score = score
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# ---- MAIN GAME LOOP ----
board = [" "]*9
print("Posisi index kotak pada papan:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8\n")

print_board(board)

while True:
    # 1. Human (O) move
    while True:
        try:
            move = int(input("Masukkan posisi (0-8) untuk O: "))
            if 0 <= move <= 8:
              if board[move] == " ":
                break
              else: 
                print("Kotak sudah terisi, pilih yang lain.")
            else:
                print("Masukkan angka antara 0 dan 8.")
        except ValueError:
            print("Masukkan angka yang valid.")
    board[move] = "O"
    print_board(board)
    if check_winner(board, "O"):
        print("Kamu (O) MENANG!")
        break
    if is_full(board):
        print("Permainan SERI!")
        break

    # 2. AI (X) move
    ai_move = get_best_move(board)
    board[ai_move] = "X"
    print(f"AI (X) memilih posisi {ai_move}")
    print_board(board)
    if check_winner(board, "X"):
        print("AI (X) MENANG!")
        break
    if is_full(board):
        print("Permainan SERI!")
        break