from random import randint


def create_matrix(rows: int, columns: int, min_num=0, max_num=100):
    matrix = [[randint(min_num, max_num) for i in range(columns)] for j in range(rows)]

    for i in matrix:
        print(i)

    return matrix


def least_of_huge(m=None):
    if m is None:
        m = create_matrix(5, 10)
    return min([max(x) for x in m])


if __name__ == '__main__':
    matrix = create_matrix(5, 10)
    print(least_of_huge(matrix))
