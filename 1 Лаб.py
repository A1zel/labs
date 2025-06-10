def read_matrix_from_file(filename, N):
    matrix = []
    with open(filename, 'r') as file:
        for _ in range(N):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()


def is_symmetric_area1(matrix, N):
    mid = N // 2
    for i in range(mid):
        for j in range(mid):
            if matrix[i][j] != matrix[i][mid + j]:
                return False
    return True


def swap_areas_symmetrically(matrix, N):
    mid = N // 2
    for i in range(mid):
        for j in range(mid):
            matrix[i][j], matrix[mid + i][mid + j] = matrix[mid + i][mid + j], matrix[i][j]


def swap_areas_nonsymmetrically(matrix, N):
    mid = N // 2
    area2 = []
    area4 = []

    # Собираем элементы областей
    for i in range(mid):
        for j in range(mid, N):
            area2.append(matrix[i][j])
    for i in range(mid, N):
        for j in range(mid):
            area4.append(matrix[i][j])

    # Меняем местами
    area2, area4 = area4, area2

    # Записываем обратно
    idx2 = 0
    idx4 = 0
    for i in range(mid):
        for j in range(mid, N):
            matrix[i][j] = area2[idx2]
            idx2 += 1
    for i in range(mid, N):
        for j in range(mid):
            matrix[i][j] = area4[idx4]
            idx4 += 1


def transpose_matrix(matrix, N):
    result = [[0] * N for _ in
