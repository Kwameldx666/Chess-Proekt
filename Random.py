import chess
import random
def complex_random_move(board):
    """
    Returns a move based on a more advanced criteria that makes seemingly random
    but strategic moves.
    """
    king_threat_moves = []
    pawn_advance_moves = []
    captures = []
    safe_moves = []
    development_moves = []
    center_moves = []
    other_moves = []

    center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]

    # If the king is under check, consider only moves that take the king out of check
    if board.is_check():
        for move in board.legal_moves:
            if board.is_capture(move):
                king_threat_moves.append(move)
            else:
                safe_moves.append(move)
        if king_threat_moves:
            return random.choice(king_threat_moves)
        else:
            return random.choice(safe_moves)

    for move in board.legal_moves:
        if board.is_capture(move):
            captures.append(move)
        elif not board.gives_check(move):
            safe_moves.append(move)
        if move.from_square in [chess.B1, chess.G1, chess.B8, chess.G8]:
            development_moves.append(move)
        if move.to_square in center_squares:
            center_moves.append(move)
        if board.piece_at(move.from_square).piece_type == chess.PAWN:
            pawn_advance_moves.append(move)
        else:
            other_moves.append(move)

    if captures:
        return random.choice(captures)
    elif safe_moves:
        return random.choice(safe_moves)
    elif development_moves:
        return random.choice(development_moves)
    elif center_moves:
        return random.choice(center_moves)
    elif pawn_advance_moves:
        return random.choice(pawn_advance_moves)
    else:
        return random.choice(other_moves)