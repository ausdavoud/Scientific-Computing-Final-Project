from cholesky import find_R
from triangular import lower_triangular, upper_triangular

from B.utils import find_norm_2, mat_mul, mat_sub, print_matrix, transpose


def find_min_square(A, b):
    A_transpose = transpose(A)
    A_transpose_A = mat_mul(A_transpose, A)

    b_bar = mat_mul(A_transpose, b)
    print_matrix(b_bar)

    R = find_R(A_transpose_A)
    R_transpose = transpose(R)

    Y = lower_triangular(R_transpose, b_bar)
    X = upper_triangular(R, Y)

    return X


def find_error_vector(A, X, b):
    # Find AX
    AX = mat_mul(A, X)

    # Find AX - b
    diff = mat_sub(AX, b)

    return diff


A = [[-3, 1], [1, 1], [-7, 1], [5, 1]]

b = [[70], [21], [110], [-35]]

print_matrix(X := find_min_square(A, b))

print_matrix(e := find_error_vector(A, X, b))

print(find_norm_2(e))
