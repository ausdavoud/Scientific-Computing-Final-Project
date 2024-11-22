from math import sqrt


def mat_sub(A, B, add=False) -> list[list[int]]:
    coefficient = -1 + (+2) * add
    n = len(A)
    m = len(B[0])
    C = [[0 for i in range(m)] for j in range(n)]

    print_matrix(A)
    print_matrix(B)
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + (coefficient * B[i][j])

    return C


def mat_mul(A, B) -> list[list[int]]:
    m = len(A)
    n = len(B[0])
    l = len(B)
    C = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            sum_of_product = 0
            for k in range(l):
                element_mul = A[i][k] * B[k][j]
                sum_of_product += element_mul
            C[i][j] = sum_of_product
    return C


def transpose(A) -> list[list[int]]:
    m = len(A)
    n = len(A[0])
    B = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    return B


def mat_mul_constant(A, c) -> list[list[int]]:
    n = len(A)
    m = len(A[0])
    C = [[c * A[j][i] for i in range(m)] for j in range(n)]

    return C


def find_norm_2(e):
    norm = 0
    for i in range(len(e)):
        squared = e[i][0] ** 2
        norm += squared

    return sqrt(norm)


def construct_e(n):
    e = [[0] for _ in range(n)]
    e[0][0] = 1
    return e


def construct_I(n):
    I = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    return I


def print_matrix(A):
    print("-" * (4 + len(A)))
    for row in A:
        print(row)
    print("-" * (4 + len(A)))


# A = [[1, 2], [4, 5], [6, 8]]

# B = [[2, 3], [3, 5]]

# print_matrix(mul_mat(A, B))
# print_matrix(transpose(A))

