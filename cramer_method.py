import numpy as np

def cramer_method(A, b):
    n = len(A)
    
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        print("The determinant of A is 0.")
        return None
    
    solution = []
    k = 1
    m = 1
    
    while k <= n:
        D = A.copy()
        
        j = 1
        while j <= n:
            i = 1
            while i <= n:
                if i > n:
                    break
                if j == m:
                    D[i - 1, j - 1] = b[i - 1]
                else:
                    D[i - 1, j - 1] = A[i - 1, j - 1]
                i += 1
            j += 1
        
        det_D = np.linalg.det(D)
        
        x_k = det_D / det_A
        solution.append(x_k)
        
        k += 1
        m += 1
    
    formatted_solution = [float(x) for x in solution]
    print("Solution:", formatted_solution)


A = np.array([[3, -5, 47, 20],
              [11, 16, 17, 10],
              [56, 22, 11, -18],
              [17, 66, -12, 7]])

b = np.array([18, 26, 34, 82])

cramer_method(A, b)
