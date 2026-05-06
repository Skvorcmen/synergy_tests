import random


def create_random_matrix(rows, cols, min_val=-50, max_val=50):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix


def print_matrix(matrix, name="Матрица"):
    print(f"\n{name}:")
    for row in matrix:
        formatted_row = [f"{num:4d}" for num in row]
        print("[" + ", ".join(formatted_row) + "]")


def add_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 > 0 else 0
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]) if rows2 > 0 else 0

    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Матрицы должны иметь одинаковую размерность для сложения!")

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


matrix_1 = create_random_matrix(10, 10, -50, 100)
matrix_2 = create_random_matrix(10, 10, -80, 120)

print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")

matrix_3 = add_matrices(matrix_1, matrix_2)

print_matrix(matrix_3, "Матрица 3 (Сумма матриц 1 и 2)")

matrix_a = create_random_matrix(4, 3, -20, 30)
matrix_b = create_random_matrix(4, 3, -10, 40)

print_matrix(matrix_a, "Матрица A (4×3)")
print_matrix(matrix_b, "Матрица B (4×3)")

matrix_c = add_matrices(matrix_a, matrix_b)
print_matrix(matrix_c, "Матрица C = A + B (4×3)")
