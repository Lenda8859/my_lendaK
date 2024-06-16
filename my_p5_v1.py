import random

def input_player_names():
    """
    Функция для ввода имен игроков.
    Возвращает кортеж с именами игроков.
    """
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    return (player1, player2)

def roll_dice():
    """
    Функция для броска кубика (генерация случайного числа от 1 до 6).
    Возвращает результат броска.
    """
    return random.randint(1, 6)

def determine_winner(player1, score1, player2, score2):
    """
    Функция для определения победителя на основе результатов бросков.
    Возвращает имя победителя или строку "Ничья".
    """
    if score1 > score2:
        return player1
    elif score2 > score1:
        return player2
    else:
        return "Ничья"

def game_core(player1, player2):
    """
    Функция, реализующая основную логику игры:
    броски кубика поочередно для каждого игрока,
    определение победителя и вывод результата.
    """
    print(f"Игра начинается между {player1} и {player2}!")

    score1 = roll_dice()
    score2 = roll_dice()

    print(f"{player1} выбросил {score1}")
    print(f"{player2} выбросил {score2}")

    winner = determine_winner(player1, score1, player2, score2)

    if winner != "Ничья":
        print(f"Победитель: {winner}!")
    else:
        print("Ничья!")

def main():
    """
    Основная функция для организации игры.
    """
    players = input_player_names()
    game_core(players[0], players[1])

if __name__ == "__main__":
    main()