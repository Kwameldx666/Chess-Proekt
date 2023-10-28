import chess
import random

def enhanced_heuristic_evaluation(board: chess.Board, last_evaluation=None, last_move=None) -> int:
    material_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }

    if last_evaluation is None or last_move is None:
        # If no last evaluation or move provided, calculate from scratch
        score = 0
        for piece_type in material_values.keys():
            score += len(board.pieces(piece_type, chess.WHITE)) * material_values[piece_type]
            score -= len(board.pieces(piece_type, chess.BLACK)) * material_values[piece_type]
        return score
    else:
        # Incrementally update the score
        score = last_evaluation
        captured_piece = board.piece_at(last_move.to_square)
        if captured_piece:
            score += material_values.get(captured_piece.piece_type, 0) * (
                1 if captured_piece.color == chess.WHITE else -1)
        return score

def mini_max(board: chess.Board, depth: int, alpha: int, beta: int, maximizing_player: bool) -> int:
    if depth == 0 or board.is_game_over():
        return enhanced_heuristic_evaluation(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval_ = mini_max(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_)
            alpha = max(alpha, eval_)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval_ = mini_max(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_)
            beta = min(beta, eval_)
            if beta <= alpha:
                break
        return min_eval

class ChessNode:
    def __init__(self, board: chess.Board, parent=None):
        self.board = board
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

class ChessMCTS:
    def __init__(self, iterations=1000):
        self.iterations = iterations

    def select(self, node):
        while node.children:
            if any(child.visits == 0 for child in node.children):
                return next(child for child in node.children if child.visits == 0)
            node = max(node.children, key=lambda child: self.ucb1(node, child))
        return node

    def ucb1(self, parent, child):
        if child.visits == 0:
            return float('inf')
        return child.value / child.visits + (2 * parent.visits * child.visits) ** 0.5

    def expand(self, node):
        for move in node.board.legal_moves:
            new_board = node.board.copy()
            new_board.push(move)
            node.children.append(ChessNode(new_board, node))

    def enhanced_simulate_with_minimax(self, node):
        board_copy = node.board.copy()
        return mini_max(board_copy, 2, float('-inf'), float('inf'), board_copy.turn == chess.WHITE)


    def backpropagate(self, node, result):
        while node:
            node.visits += 1
            node.value += result
            node = node.parent

    def MCTS_1(self, board: chess.Board):
        root = ChessNode(board)
        for _ in range(self.iterations):
            leaf = self.select(root)
            if not leaf.board.is_game_over():
                self.expand(leaf)
                simulation_result = self.enhanced_simulate_with_minimax(leaf)
                self.backpropagate(leaf, simulation_result)

        best_child = max(root.children, key=lambda child: child.value)
        return best_child.board.peek()  # Return the best move
