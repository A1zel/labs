from itertools import permutations


def generate_optimized_combinations():
    # Создаем претендентов с рейтингами
    candidates = {
        'Ж1': 5, 'Ж2': 3, 'Ж3': 6,
        'М1': 4, 'М2': 2, 'М3': 1
    }

    max_score = 0
    best_combination = []

    # Генерируем все перестановки
    for perm in permutations(candidates.keys()):
        # Проверяем условия
        if (perm[0][0] == 'Ж' and perm[1][0] == 'Ж' and
                perm[2][0] == 'М' and perm[3][0] == 'М'):
            # Вычисляем сумму рейтингов
            score = sum(candidates[candidate] for candidate in perm)
            if score > max_score:
                max_score = score
                best_combination = perm

    print(f"Лучшая комбинация: {best_combination}")
    print(f"Сумма рейтингов: {max_score}")
    return best_combination, max_score


# Замеряем время выполнения
start_time = time.time()
optimized_result = generate_optimized_combinations()
print(f"Время выполнения: {\time.time() - start_time} секунд")
