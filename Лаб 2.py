import numpy as np
import matplotlib.pyplot as plt


def read_matrix_from_file(filename, n):
    try:
        with open(filename, 'r') as file:
            matrix = []
            for _ in range(n):
                row = list(map(int, file.readline().split()))
                matrix.append(row)
        return np.array(matrix)
    except FileNotFoundError:
        print("Файл не найден!")
        return None


def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def swap_regions_symmetrically(matrix, size):
    temp = matrix[:size, :size].copy()
    matrix[:size, :size] = matrix[:size, size:]
    matrix[:size, size:] = temp


def swap_regions_nonsymmetrically(matrix, size):
    temp_c = matrix[size:, :size].copy()
    temp_e = matrix[:size, size:].copy()
    matrix[size:, :size] = temp_e
    matrix[:size, size:] = temp_c


def create_lower_triangular(matrix):
    return np.tril(matrix)


def plot_matrix_heatmap(matrix, title):
    plt.figure()
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.grid(False)
    plt.show()


def plot_matrix_histogram(matrix, title):
    plt.figure()
    plt.hist(matrix.flatten(), bins=20)
    plt.title(title)
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.show()


def plot_matrix_surface(matrix, title):
    plt.figure()
    X, Y = np.meshgrid(range(matrix.shape[0]), range(matrix.shape[1]))
    plt.plot_surface(X, Y, matrix, cmap='viridis')
    plt.title(title)
    plt.show()


def main():
    K = int(input("Введите значение K: "))
    N = int(input("Введите размер матрицы N: "))

    # Создание матрицы A
    A = read_matrix_from_file('matrix.txt', N)
    if A is None:
        A = np.random.randint(-10, 10, size=(N, N))

    # Разделение на подматрицы
    size = N // 2
    B = A[:size, :size]
    E = A[:size, size:]
    C = A[size:, :size]
    D = A[size:, size:]

    # Создание матрицы F
    F = A.copy()

    # Проверка на симметричность и обмен областей
    if is_symmetric(A):
        swap_regions_symmetrically(F, size)
    else:
        swap_regions_nonsymmetrically(F, size)

    # Вычисление определителя и суммы диагональных элементов
    det_A = np.linalg.det(A)
    diag_sum_F = np.trace(F)

    # Вычисление выражения
    if det_A > diag_sum_F:
        result = np.dot(np.linalg.inv(A), A.T) - K * np.linalg.inv(F)
    else:
        G = create_lower_triangular(A)
        result = (np.dot(A.T, G) - np.dot(F.T)) * K

    # Вывод результатов
    print("Матрица A:")
    print(A)
    print("\nМатрица F:")
    print(F)
    print("\nРезультат вычисления:")
    print(result)

    # Построение графиков
    plot_matrix_heatmap(F, "Тепловая карта матрицы F")
    plot_matrix_histogram(F, "Гистограмма значений матрицы F")
    plot_matrix_surface(F, "Поверхностный график матрицы F")
