import numpy as np

def gauss_seidel_method(a, b, tolerance=0.0001, max_iterations=100):
    n = len(b)
    x = np.zeros(n)  
    y = np.zeros(n)  
    
    for itr in range(max_iterations):
        for i in range(n):
            sum1 = sum(a[i][j] * x[j] for j in range(n) if j != i) 
            x[i] = (b[i] - sum1) / a[i][i] 
        
        if all(abs(x[k] - y[k]) <= tolerance for k in range(n)):
            print(f"Gauss-Seidel Solution converged in {itr + 1} iterations:")
            print(x)
            return x

        y[:] = x

    print("Gauss-Seidel method does not converge.")
    return None

A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

gauss_seidel_method(A, b)

