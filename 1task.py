import numpy as np
import matplotlib.pyplot as plt

# Задаємо діапазон значень для x
x = np.linspace(1, 10, 500)

# Визначаємо функцію Y(x)
y = 5 * np.sin(x) * (np.cos(x**2 + 1/x))**2

# Налаштовуємо графік
plt.figure(figsize=(10, 6))
plt.plot(x, y, color="blue", linewidth=2, linestyle="-", label="Y(x) = 5 * sin(x) * cos(x^2 + 1/x)^2")

# Додаємо назву графіка та підписи осей
plt.title("Графік функції Y(x)")
plt.xlabel("X")
plt.ylabel("Y(x)")

# Додаємо легенду
plt.legend()

# Відображаємо графік
plt.grid()
plt.show()
