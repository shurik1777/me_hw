def print_board(board):  #  доска
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col):
    # Проверяем строку
    for i in range(len(board)):
        if board[row][i] == "Q":
            return False

    # Проверяем столбец
    for i in range(len(board)):
        if board[i][col] == "Q":
            return False

    # Проверяем диагонали
    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == "Q":
                    return False

    return True

def solve(board, col):
    # Если все ферзи успешно размещены, то выводим доску
    if col == len(board):
        print_board(board)
        print("\n")
        return True

    solved = False

    # Выбираем строку для ферзя в текущем столбце
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = "Q"

            # Рекурсивно размещаем оставшиеся ферзи на доске
            solved = solve(board, col + 1) or solved

            # Удаляем ферзя, если он не решил проблему для оставшихся ферзей
            board[row][col] = "_"

    return solved

board = [["." for _ in range(8)] for _ in range(8)]

solve(board, 0)
