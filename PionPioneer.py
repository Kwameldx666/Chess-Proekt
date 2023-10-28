from Evaluation import Evalualtion
import  chess

def minimax_without_alpha_beta(board, depth, is_maximizing):
    if (depth == 0) or (board.is_game_over()):
        player = "W" if is_maximizing else "B"
        eval_instance = Evalualtion(board, player)
        return eval_instance.result()

    moves = list(board.legal_moves)

    if is_maximizing:
        max_eval = float('-inf')
        for move in moves:
            board.push(move)
            eval_value = minimax_without_alpha_beta(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval_value)
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            board.push(move)
            eval_value = minimax_without_alpha_beta(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval_value)
        return min_eval

def get_best_move(board, depth=3):
    is_maximizing = board.turn == chess.WHITE  # True if it's white's turn to move

    best_eval = -float('inf') if is_maximizing else float('inf')
    best_move = None

    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        board.push(move)
        if is_maximizing:
            current_eval = minimax_without_alpha_beta(board, depth - 1, False)
            if current_eval > best_eval:
                best_eval = current_eval
                best_move = move
        else:
            current_eval = minimax_without_alpha_beta(board, depth - 1, True)
            if current_eval < best_eval:
                best_eval = current_eval
                best_move = move
        board.pop()

    return best_move