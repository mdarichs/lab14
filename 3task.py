 import json
import matplotlib.pyplot as plt

# Ім'я файлу для збереження результатів
json_file = 'task_b_result.json'

# Ініціалізація даних для прикладу
initial_data = [
    {"surname": "Ivanenko", "items": 3, "weight": 4.5},
    {"surname": "Petrenko", "items": 2, "weight": 8.0},
    {"surname": "Shevchenko", "items": 4, "weight": 26.0},
    {"surname": "Koval", "items": 1, "weight": 2.5},
    {"surname": "Bondar", "items": 5, "weight": 15.0},
    {"surname": "Tkachenko", "items": 3, "weight": 18.0},
    {"surname": "Kravchenko", "items": 2, "weight": 4.0},
    {"surname": "Boyko", "items": 6, "weight": 30.0},
    {"surname": "Kucher", "items": 1, "weight": 6.0},
    {"surname": "Moroz", "items": 3, "weight": 9.5}
]

# Функція для запису початкових даних у файл JSON
def initialize_json_file():
    with open('baggage_data.json', 'w') as f:
        json.dump(initial_data, f, indent=4)

# Завдання b: Кількість пасажирів у трьох категоріях за вагою
def task_b():
    # Читання даних із файлу JSON
    with open('baggage_data.json', 'r') as f:
        data = json.load(f)

    # Підрахунок пасажирів за категоріями ваги
    categories = {"less_than_5kg": 0, "between_5_and_25kg": 0, "more_than_25kg": 0}
    for entry in data:
        if entry['weight'] < 5:
            categories["less_than_5kg"] += 1
        elif 5 <= entry['weight'] <= 25:
            categories["between_5_and_25kg"] += 1
        else:
            categories["more_than_25kg"] += 1

    # Запис результатів у файл
    with open(json_file, 'w') as f:
        json.dump(categories, f, indent=4)

# Виконання завдання b та побудова кругової діаграми
initialize_json_file()  # Ініціалізація файлу з даними, якщо ще не створений
task_b()  # Створення файлу task_b_result.json з результатами

# Читання результатів із JSON файлу для побудови діаграми
with open(json_file, 'r') as f:
    categories = json.load(f)

# Дані для діаграми
labels = ['Менше 5 кг', 'Від 5 до 25 кг', 'Більше 25 кг']
sizes = [categories["less_than_5kg"], categories["between_5_and_25kg"], categories["more_than_25kg"]]
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Розподіл пасажирів за вагою багажу')
plt.show()
