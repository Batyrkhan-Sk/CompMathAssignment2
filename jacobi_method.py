import numpy as np

def jacobi_method(a, b, tolerance=0.0001, max_iterations=100):
    n = len(b)
    x = np.zeros(n) 
    x_new = np.zeros(n) 

    for itr in range(max_iterations):
        for i in range(n):
            sum1 = sum(a[i][j] * x[j] for j in range(n) if j != i)  
            x_new[i] = (b[i] - sum1) / a[i][i]  
        
        if all(abs(x_new[i] - x[i]) <= tolerance for i in range(n)):
            print(f"Jacobi Solution converged in {itr + 1} iterations:")
            print(x_new)
            return x_new

        x[:] = x_new

    print("Jacobi method does not converge.")
    return None
A = np.array([
    [3, -5, 47, 20],
    [11, 16, 17, 10],
    [56, 22, 11, -18],
    [17, 66, -12, 7]
], dtype=float)

b = np.array([18, 26, 34, 82], dtype=float)

jacobi_method(A, b)
