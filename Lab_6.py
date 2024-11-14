import numpy as np

# Матриця прибутків
F = np.array([
    [8, 2, 4],
    [6, 7, 4],
    [4, 7, 5],
    [3, 5, 6]
])

# Імовірності станів економічного середовища
P = np.array([1/2, 1/3, 1/6])

# Розрахунок критерію Байєса
bayes_criteria = F @ P  # множення матриці на вектор ймовірностей
best_bayes_index = np.argmax(bayes_criteria)
best_bayes_value = bayes_criteria[best_bayes_index]

print("Критерій Байєса:")
print("Оптимальний проект за критерієм Байєса:", best_bayes_index + 1)
print("Значення критерію Байєса для оптимального проекту:", best_bayes_value)

# Розрахунок дисперсії для кожного проекту
mean_values = bayes_criteria  # середні значення (очікування) для кожного проекту
variance_criteria = np.sum(((F - mean_values[:, None]) ** 2) * P, axis=1)  # дисперсії для кожного проекту
best_variance_index = np.argmin(variance_criteria)
best_variance_value = variance_criteria[best_variance_index]

print("\nДисперсійний критерій:")
print("Оптимальний проект за дисперсійним критерієм:", best_variance_index + 1)
print("Значення дисперсії для оптимального проекту:", best_variance_value)

# Компромісне рішення: вибір проекту з найменшою сумою нормованих значень критеріїв
normalized_bayes = (bayes_criteria - bayes_criteria.min()) / (bayes_criteria.max() - bayes_criteria.min())
normalized_variance = (variance_criteria - variance_criteria.min()) / (variance_criteria.max() - variance_criteria.min())
compromise_criteria = normalized_bayes + normalized_variance
best_compromise_index = np.argmin(compromise_criteria)

print("\nКомпромісне рішення:")
print("Оптимальний проект за компромісним критерієм:", best_compromise_index + 1)
print("Значення компромісного критерію для оптимального проекту:", compromise_criteria[best_compromise_index])
