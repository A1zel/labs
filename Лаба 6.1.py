def generate_combinations_basic():
    # Создаем список претендентов
    candidates = ['Ж1', 'Ж2', 'Ж3', 'М1', 'М2', 'М3']

    # Перебираем все возможные комбинации
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        for n in range(6):
                            # Проверяем условия:
                            # 2 женщины на первую позицию
                            # 2 мужчины на вторую позицию
                            # 2 любых на третью позицию
                            if (candidates[i][0] == 'Ж' and candidates[j][0] == 'Ж' and
                                    candidates[k][0] == 'М' and candidates[l][0] == 'М' and
                                    i != j and k != l):
                                combination = [candidates[i], candidates[j],
                                               candidates[k], candidates[l],
                                               candidates[m], candidates[n]]
                                if len(set(combination)) == 6:
                                    print(combination)


# Замеряем время выполнения
import time

start_time = time.time()
generate_combinations_basic()
print(f"Время выполнения: {time.time() - start_time} секунд")
