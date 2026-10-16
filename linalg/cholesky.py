from math import sqrt


def find_R(A):
    n = len(A)
    R = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(A)):
        sum_previous_r = 0
        for j in range(i):
            sum_previous_r += (R[j][i]) ** 2

        R[i][i] = sqrt(A[i][i] - sum_previous_r)

        for k in range(i + 1, len(A)):
            sum_previous_r = 0
            for j in range(i):
                sum_previous_r += R[j][i] * R[j][k]

            R[i][k] = (A[i][k] - sum_previous_r) / R[i][i]

    return R


# A = [[2, 2, 1], [2, 5, 1], [1, 1, 2]]

# A = [
#     [1, -2, 2],
#     [-2, 5, -3],
#     [2, -3, 30],
# ]

# print(find_R(A))
