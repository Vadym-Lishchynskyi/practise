from t1 import create_matrix


def change_quarters(matrix, rows, columns):
    print()

    for j in range(rows // 2):
        for i in range(columns // 2, columns):
            matrix[j][i], matrix[j + rows // 2][i - columns // 2] = matrix[j + rows // 2][i - columns // 2], matrix[j][i]

    for k in matrix:
        print(k)


if __name__ == '__main__':
    n, m = 6, 4
    matrix = create_matrix(m, n, 10, 99)
    change_quarters(matrix, m, n)
