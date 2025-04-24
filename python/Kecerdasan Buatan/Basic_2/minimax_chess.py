import chess

# Skor untuk masing-masing bidak
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # tak ternilai, jadi 0 biar ga kacau evaluasinya
}

# Fungsi evaluasi posisi papan (penjumlahan material)
def evaluate_board(board):
    eval = 0
    for piece_type in piece_values:
        eval += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        eval -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return eval

# Minimax dengan depth terbatas
def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if is_maximizing:
        max_eval = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

# Main game loop
def play_game():
    board = chess.Board()
    depth_limit = 2  # Bisa dinaikin buat lebih kuat
    while not board.is_game_over():
        print(board, "\n")

        if board.turn == chess.WHITE:
            print("White (AI) thinking...")
            _, move = minimax(board, depth_limit, True)
        else:
            print("Black (AI) thinking...")
            _, move = minimax(board, depth_limit, False)

        if move is None:
            print("No legal moves!")
            break

        board.push(move)

    print(board)
    print("Game Over:", board.result())

if __name__ == "__main__":
    play_game()