from itertools import permutations


def generate_combinations_functional():
    candidates = ['Ж1', 'Ж2', 'Ж3', 'М1', 'М2', 'М3']
    valid_combinations = []

    # Генерируем все перестановки
    for perm in permutations(candidates):
        # Проверяем условия
        if (perm[0][0] == 'Ж' and perm[1][0] == 'Ж' and
                perm[2][0] == 'М' and perm[3][0] == 'М'):
            valid_combinations.append(perm)

    for comb in valid_combinations:
        print(comb)
    return valid_combinations


# Замеряем время выполнения
start_time = time.time()
functional_result = generate_combinations_functional()
print(f"Время выполнения: {time.time() - start_time} секунд")
