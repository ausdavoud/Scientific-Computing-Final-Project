def upper_triangular(A, b):
    n = len(A[0])
    X = [[0] for _ in range(n)]

    for i in range(len(A) - 1, -1, -1):
        if A[i][i] == 0:
            raise ValueError(f"Matrix is 0 at row {i}, column {i}.")

        sum_previous_x = 0
        for j in range(i + 1, len(X)):
            sum_previous_x += A[i][j] * X[j][0]
        X[i][0] = 1 / A[i][i] * (b[i][0] - sum_previous_x)

    return X


def lower_triangular(A, b):
    n = len(A[0])
    X = [[0] for _ in range(n)]
    for i in range(len(A)):
        if A[i][i] == 0:
            raise ValueError(f"Matrix is 0 at row {i}, column {i}.")
        
        sum_previous_x = 0
        for j in range(i):
            sum_previous_x += A[i][j] * X[j][0]
        X[i][0] = 1 / A[i][i] * (b[i][0] - sum_previous_x)

    return X
