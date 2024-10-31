import numpy as np

# Матриця витрат (тис. грн)
F = np.array([
    [3, 6, 5, 6],
    [1, 3, 9, 5],
    [4, 1, 4, 8]
])

# Ймовірності станів економічного середовища
probabilities = np.array([0.2, 0.3, 0.25, 0.25])

# Критерій Ходжеса-Лемана
def hodges_lehmann(F, probabilities):
    expected_losses = F @ probabilities  # Вектор очікуваних втрат
    min_losses = F.min(axis=1)  # Мінімальні втрати для кожного рішення
    hodges_lehmann_values = 0.5 * (expected_losses + min_losses)
    optimal_decision = np.argmin(hodges_lehmann_values)
    return hodges_lehmann_values, optimal_decision

# Модифікований критерій Байєса
def modified_bayes(F, probabilities):
    expected_losses = F @ probabilities
    optimal_decision = np.argmin(expected_losses)
    return expected_losses, optimal_decision

# Модифікований критерій Гурвіца
def modified_hurwicz(F, alpha=0.5):
    min_losses = F.min(axis=1)
    max_losses = F.max(axis=1)
    hurwicz_values = alpha * min_losses + (1 - alpha) * max_losses
    optimal_decision = np.argmin(hurwicz_values)
    return hurwicz_values, optimal_decision

# Розрахунок результатів
hl_values, hl_decision = hodges_lehmann(F, probabilities)
bayes_values, bayes_decision = modified_bayes(F, probabilities)
hurwicz_values, hurwicz_decision = modified_hurwicz(F)

# Виведення результатів
print("Критерій Ходжеса-Лемана:")
print("Значення:", hl_values)
print("Найкраще рішення:", hl_decision + 1)

print("\nМодифікований критерій Байєса:")
print("Значення:", bayes_values)
print("Найкраще рішення:", bayes_decision + 1)

print("\nМодифікований критерій Гурвіца:")
print("Значення:", hurwicz_values)
print("Найкраще рішення:", hurwicz_decision + 1)
