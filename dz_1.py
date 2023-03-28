"""
завдання 1
зробіть так щоб при роботі програми виводилися винятки у консоль.

завдання 2
записати у файл рандомні числа. зчитати з файлу ці числа та підрахувати кількість одиниць та вивести у консоль.
"""

import random

try:
    with open('capibara.txt', 'w') as file:
        for i in range(50):
            random_number = random.randint(0, 50)
            file.write(str(random_number) + '\n')

    ones_count = 0
    with open('capibara.txt', 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                if number == 1:
                    ones_count += 1
                else:
                    raise ValueError(f"Число не одиниця, {number}")
            except ValueError as e:
                print(f"Помилка: {e}")
    print(f"Кількість одиниць у файлі: {ones_count}")

except IOError as e:
    print(f"Помилка вводу-виводу: {e}")
except Exception as e:
    print(f"Невідома помилка: {e}")