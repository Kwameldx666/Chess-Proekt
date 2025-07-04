from Evaluation import Evaluation  # Импортирование модуля Evaluation

MAX, MIN = 100000, -100000  # Определение максимального и минимального значений для оценки

# Функция для выполнения алгоритма минимакс
# depth - текущая глубина поиска
# maximizingPlayer - True, если текущий игрок максимизирует оценку, иначе False
# alpha и beta - значения для альфа-бета отсечения
# board - текущее состояние шахматной доски
# firstMove - True, если это первый ход в игре
def minimax(depth, maximizingPlayer, alpha, beta, board, firstMove):

    # Условие завершения. Достигнут конец дерева поиска (листовой узел)
    if (depth == 0) or (board.is_game_over()):

        if maximizingPlayer:
            eval = Evaluation(board, "W")  # Вычисление оценки для белых фигур
        else:
            eval = Evaluation(board, "B")  # Вычисление оценки для черных фигур

        return eval.result()  # Возврат результата оценки

    # Весь код с этой точки выполняется только, если дерево поиска еще не достигло листового узла

    if maximizingPlayer:

        best = MIN  # Инициализация лучшей оценки для максимизирующего игрока
        # Перебор всех возможных ходов текущего игрока
        for i in board.legal_moves:

            board.push(i)  # Применение хода на доске

            if checkmate(board) and firstMove:
                return i  # Если это шах и мат, возвращаем этот ход

            val = minimax(depth - 1, False, alpha, beta, board, False)  # Рекурсивный вызов для минимизирующего игрока
            board.pop()  # Отмена хода на доске

            if val > best:
                best = val
                best_move_white = i  # Сохранение лучшего хода для белых

            alpha = max(alpha, best)  # Обновление альфа

            # Alpha Beta Pruning (отсечение)
            if beta <= alpha:
                break

        if firstMove:
            print(best_move_white)  # Если это первый ход, вернуть лучший ход для белых
            return best_move_white
        else:
            return best  # Вернуть лучшую оценку для максимизирующего игрока

    else:

        best = MAX  # Инициализация лучшей оценки для минимизирующего игрока
        for i in board.legal_moves:

            board.push(i)  # Применение хода на доске

            if checkmate(board) and firstMove:
                return i  # Если это шах и мат, возвращаем этот ход

            val = minimax(depth - 1, True, alpha, beta, board, False)  # Рекурсивный вызов для максимизирующего игрока
            board.pop()  # Отмена хода на доске

            if val < best:
                best = val
                best_move_black = i  # Сохранение лучшего хода для черных

            beta = min(beta, best)  # Обновление бета

            # Alpha Beta Pruning (отсечение)
            if beta <= alpha:
                break

        if firstMove:
            return best_move_black  # Если это первый ход, вернуть лучший ход для черных
        else:
            return best  # Вернуть лучшую оценку для минимизирующего игрока

# Функция для проверки наличия шах и мат
def checkmate(board):
    if board.is_checkmate():
        return True
    else:
        return False




