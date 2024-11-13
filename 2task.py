import pandas as pd
import matplotlib.pyplot as plt

# Завантаження CSV-файлу
file_path = '/mnt/data/inflation_data.csv'
data = pd.read_csv(file_path)

# Попередня обробка даних: фільтрація відповідних рядків для США та України, та отримання значень для графіків
data = data.dropna(subset=['Country Name'])  # Видалення рядків з NaN у стовпці "Country Name"
years = [str(year) for year in range(2004, 2024)]  # Роки у вигляді рядків для відповідності з колонками

# Підготовка даних для побудови графіка
usa_data = data[data['Country Name'] == 'United States'][[f'{year} [YR{year}]' for year in years]].values.flatten()
ukraine_data = data[data['Country Name'] == 'Ukraine'][[f'{year} [YR{year}]' for year in years]].values.flatten()

# Перетворення років на список цілих чисел для побудови графіка
years_int = list(range(2004, 2024))

# 2.1. Лінійний графік інфляційних даних для обох країн
plt.figure(figsize=(10, 6))
plt.plot(years_int, usa_data, label='Сполучені Штати', marker='o')
plt.plot(years_int, ukraine_data, label='Україна', marker='o')
plt.xlabel('Рік')
plt.ylabel('Інфляція, споживчі ціни (%)')
plt.title('Тренди інфляції для Сполучених Штатів та України (2004-2023)')
plt.legend()
plt.grid(True)
plt.show()

# 2.2. Стовпчаста діаграма для інфляційних значень обраної країни
def plot_inflation_bar_chart():
    # Введення назви країни користувачем
    country_name = input("Введіть назву країни для побудови діаграми: ")
    
    # Фільтрація даних на основі введеної країни
    if country_name not in data['Country Name'].values:
        print(f"Країну '{country_name}' не знайдено в даних.")
        return

    country_data = data[data['Country Name'] == country_name][[f'{year} [YR{year}]' for year in years]].values.flatten()
    
    # Побудова стовпчастої діаграми
    plt.figure(figsize=(10, 6))
    plt.bar(years_int, country_data, color='skyblue')
    plt.xlabel('Рік')
    plt.ylabel('Інфляція, споживчі ціни (%)')
    plt.title(f'Рівні інфляції для {country_name} (2004-2023)')
    plt.xticks(years_int, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Виклик функції для побудови стовпчастої діаграми на основі введеної країни
plot_inflation_bar_chart()

