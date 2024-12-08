# Игровое поле
board = [" " for _ in range(9)]


# Функция для вывода поля в консоле
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Проверка на победу
def check_winner():
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
        (0, 4, 8), (2, 4, 6)  # диагонали
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] != " ":
            return board[pos[0]]
    return None


# Проверка на ничью
def is_draw():
    return " " not in board


# Основной игровой процесс
def main():
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Игрок 1: X | Игрок 2: O")
    print_board()

    current_player = "X"
    try:
        while True:
            # Запрос ввода
            try:
                move = int(input(f"Ход игрока {current_player} (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("Некорректный ввод. Попробуйте ввести другое число.")
                    continue
            except ValueError:
                print("Пожалуйста, введите число от 1 до 9.")
                continue

            # Выполнение хода
            board[move] = current_player
            print_board()

            # Проверка завершения игры
            winner = check_winner()
            if winner:
                print(f"Победил игрок {winner}")
                break
            elif is_draw():
                print("Ничья")
                break

            # Смена игрока
            current_player = "O" if current_player == "X" else "X"
            # Прерывание игры
    except KeyboardInterrupt:
        print("\nИгра была прервана.")
        exit()

# Запуск игры
if __name__ == "__main__":
    main()
