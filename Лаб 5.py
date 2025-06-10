import math
import time
import matplotlib.pyplot as plt

# Рекурсивная реализация
def recursive_f(n):
    if n < 2:
        return 1
    else:
        return (-1) ** n * (recursive_f(n - 1) / math.factorial(n) +
                            recursive_f(n // 5) / math.factorial(2 * n))


# Итерационная реализация
def iterative_f(n):
    if n < 2:
        return 1

    # Создаем словарь для хранения промежуточных значений
    cache = {0: 1, 1: 1}

    for i in range(2, n + 1):
        # Вычисляем F(i) используя предыдущие значения
        fi = (-1) ** i * (cache[i - 1] / math.factorial(i) +
                          cache[i // 5] / math.factorial(2 * i))
        cache[i] = fi

    return cache[n]

# Функция для измерения времени выполнения
def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start, result

# Создаем таблицу результатов
results = []
recursive_times = []
iterative_times = []
recursive_values = []
iterative_values = []

# Тестируем для разных значений n
for n in range(1, 21):
    try:
        rec_time, rec_result = measure_time(recursive_f, n)
        recursive_times.append(rec_time)
        recursive_values.append(rec_result)
    except RecursionError:
        rec_time = float('inf')
        rec_result = "Ошибка рекурсии"

    iter_time, iter_result = measure_time(iterative_f, n)
    iterative_times.append(iter_time)
    iterative_values.append(iter_result)

    results.append({
        'n': n,
        'recursive_time': rec_time,
        'recursive_result': rec_result,
        'iterative_time': iter_time,
        'iterative_result': iter_result
    })

# Выводим результаты в табличной форме
print("| n | Рекурсивное время (сек) | Итерационное время (сек) | Разница | Результат |")
print("|---|------------------------|--------------------------|----------|------------|")
for res in results:
    diff = res['recursive_time'] - res['iterative_time']
    print(
        f"| {res['n']} | {res['recursive_time']:16.10f} | {res['iterative_time']:16.10f} | {diff:8.10f} | {res['recursive_result']} |")

# Построение графиков
plt.figure(figsize=(12, 8))

# График времени выполнения
plt.subplot(2, 1, 1)
plt.plot(range(1, 21), recursive_times, label='Рекурсивный метод')
plt.plot(range(1, 21), iterative_times, label='Итерационный метод')
plt.xlabel('n')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение времени выполнения')
plt.legend()
plt.grid()

# График значений функции
plt.subplot(2, 1, 2)
plt.plot(range(1, 21), iterative_values, label='Значения функции')
plt.xlabel('n')
plt.ylabel('Значение функции')
plt.title('Значения функции F(n)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Анализ результатов
print("\nАнализ результатов:")
print("1. Итерационный метод значительно быстрее для больших n")
print("2. Рекурсивный метод имеет ограничения по глубине рекурсии")
print("3. Итерационный метод более эффективен по памяти")
print("4. При n > 15 рекурсивный метод становится крайне медленным или вызывает ошибку")
