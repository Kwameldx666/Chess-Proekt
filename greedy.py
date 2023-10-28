from Evaluation import Evalualtion  # Импортируем класс Evalualtion из модуля Evaluation

# Функция для реализации жадного алгоритма выбора хода
# board - текущее состояние шахматной доски
# player - "W" для белых и "B" для черных
# firstMove - True, если это первый ход в игре, в противном случае False
def greedy_algorithm(board, player):
    best_move = None  # Лучший ход
    best_value = -100000 if player == "W" else 100000  # Начальное значение лучшей оценки

    # Перебираем все легальные ходы для текущего игрока
    for move in board.legal_moves:
        board.push(move)  # Применяем ход на доске
        eval = Evalualtion(board, player)  # Создаем экземпляр класса Evalualtion и вычисляем оценку
        current_value = eval.result()  # Получаем оценку текущего состояния доски
        board.pop()  # Отменяем ход на доске

        # Проверяем, является ли текущий ход лучшим из найденных до сих пор
        if (player == "W" and current_value > best_value) or (player == "B" and current_value < best_value):
            best_value = current_value
            best_move = move

    return best_move  # Возвращаем только лучший ход для последующих ходов

# Здесь оставлена заглушка для класса Evalualtion, так как он не определен в предоставленном коде.
