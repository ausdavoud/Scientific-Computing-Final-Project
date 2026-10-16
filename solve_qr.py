from linalg.matrix import mat_mul, print_matrix
from linalg.qr import find_qr, solve_qr

A = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
b = [[1], [2], [3]]

Q, R = find_qr(A)
print_matrix(Q)
print_matrix(R)
print_matrix(mat_mul(Q, R))

print_matrix(solve_qr(A, b))
