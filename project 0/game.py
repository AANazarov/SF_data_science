import numpy as np

# загадываем число
number = np.random.randint(1, 101)

# создаем счетчик  попыток
count = 0

while True:
    count += 1
    predict_number = int(input("Enter a number from 1 to 100: "))
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must be greater!")
    else:
        print(f"You guessed the number in {count} attempts! This is a number {number}")
        break