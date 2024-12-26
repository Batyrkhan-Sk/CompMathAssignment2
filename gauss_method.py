import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    
    # Forward elimination
    for k in range(n-1):
        if A[k, k] == 0:
            print(f"Warning: Column {k} has zero pivot element.")
            return None
        
        for i in range(k+1, n):
            c = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= c * A[k, j]
            b[i] -= c * b[k]

    # Back substitution
    x = np.zeros(n)
    x[-1] = b[-1] / A[-1, -1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i, j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i, i]

    return x

A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

solution = gaussian_elimination(A, b)

print("Solution:", solution)
