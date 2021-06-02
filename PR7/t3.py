from t1 import create_matrix


def make_zero(matrix, rows, columns):
    n = -2
    for i in range(rows):
        n += 1
        for j in range(columns-1, n, -1):
            matrix[i][j] = 0

    for i in matrix:
        print(i)


if __name__ == '__main__':
    n, m = 4, 4
    matrix = create_matrix(m, n, 10, 99)
    make_zero(matrix, m, n)
