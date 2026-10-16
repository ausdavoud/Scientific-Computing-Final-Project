from copy import deepcopy

from .triangular import upper_triangular
from .matrix import (
    construct_e,
    construct_I,
    find_norm_2,
    mat_mul,
    mat_mul_constant,
    mat_sub,
    print_matrix,
    transpose,
)


def house_holder_u(u):
    n = len(u)
    I = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    u_transpose = transpose(u)

    u_u_transpose = mat_mul(u, u_transpose)
    u_transpose_u = mat_mul(u_transpose, u)[0][0]

    u_fraction = mat_mul_constant(u_u_transpose, 2 / u_transpose_u)

    H = mat_sub(I, u_fraction)

    return H


def find_u(X):
    n = len(X)
    x_1 = X[0][0]
    sign = 1 if x_1 >= 0 else -1
    norm_x = find_norm_2(X)
    e = construct_e(n)

    norm_mul_e = mat_mul_constant(e, norm_x)
    sign_mul_norm_mul_e = mat_mul_constant(norm_mul_e, sign)
    u = mat_sub(X, sign_mul_norm_mul_e, True)

    return u


def find_x(A, start):
    C = []
    n = len(A)
    for i in range(start, n):
        C.append([A[i][start]])

    return C


def make_H(H_hat, n):
    step = n - len(H_hat)
    H = [[0 for i in range(n)] for j in range(n)]
    for i in range(step):
        H[i][i] = 1

    for i in range(step, n):
        for j in range(step, n):
            H[i][j] = H_hat[i - step][j - step]

    return H


def find_qr(A):
    n = len(A)
    R = deepcopy(A)
    Q_transpose = construct_I(n)
    for i in range(n - 1):
        X = find_x(R, start=i)
        u = find_u(X)
        H_hat = house_holder_u(u)
        H = make_H(H_hat, n)
        Q_transpose = mat_mul(H, Q_transpose)
        R = mat_mul(H, R)

    Q = transpose(Q_transpose)

    return Q, R


def solve_qr(A, b):
    Q, R = find_qr(A)
    Q_transpose = transpose(Q)
    Q_transpose_b = mat_mul(Q_transpose, b)
    X = upper_triangular(R, Q_transpose_b)
    return X

