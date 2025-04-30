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

def alpha_beta(board, is_X_turn, alpha, beta):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if is_full(board):
        return 0

    if is_X_turn:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = alpha_beta(board, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = alpha_beta(board, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def get_best_move_alpha_beta(board):
    best_move = None
    best_score = -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = alpha_beta(board, False, -float("inf"), float("inf"))
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Contoh main sederhana: AI (X) vs Human (O)
if __name__ == "__main__":
    board = [" "] * 9
    print("Index posisi kotak:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")
    print_board(board)

    while True:
        # Human (O) move
        while True:
          try:
              move = int(input("Masukkan posisi (0-8) untuk O: "))
              if 0 <= move <= 8:
                if board[move] == " ":
                  break  # Exit the inner loop if the move is valid
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

        # AI (X) move
        ai_move = get_best_move_alpha_beta(board)
        if ai_move is not None:
            board[ai_move] = "X"
            print(f"AI (X) memilih posisi {ai_move}")
            print_board(board)
            if check_winner(board, "X"):
                print("AI (X) MENANG!")
                break
            if is_full(board):
                print("Permainan SERI!")
                break
        else:
            print("Tidak ada langkah tersisa.")
            break