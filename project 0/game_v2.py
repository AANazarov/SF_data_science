import numpy as np

# загадываем число
number = np.random.randint(1, 101)

# Объявим функцию random_predict(), которая на вход будет принимать загаданное число number.

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 201)  # предполагаемое число
        if predict_number == number:
            break   # выход из цикла, если угадали
    return count

print(f"Number of attempts {random_predict()}")

# В том же файле game_v2.py напишем функцию score_game(), определяющую среднее количество попыток угадывания числа. Аргументом функции будет другая функция, с помощью которой и реализуется угадывание числа.

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    
    # Метод random.seed() задает начальные условия для генератора случайных чисел. Генератор инициализированный одними и теми же начальными условиями, выдает абсолютно идентичные случайные последовательности.
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 201, size=(1000)) # загадали список чисел

    for elem in random_array:
        count_ls.append(random_predict(elem))
    
    score = int(np.mean(count_ls)) # находим среднее количество по-пыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)





