def solve_system(A, b):
    """Решение системы Ax = b методом Гаусса"""
    n = len(A)
    
    #создаем расширенную матрицу [A|b]
    M = [A[i] + [b[i]] for i in range(n)]
    
    #прямой ход
    for i in range(n):
        #нормализация строки
        pivot = M[i][i]
        for j in range(i, n+1):
            M[i][j] /= pivot
        
        #обнуление ниже
        for k in range(i+1, n):
            factor = M[k][i]
            for j in range(i, n+1):
                M[k][j] -= factor * M[i][j]
    
    #обратный ход
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]
    
    return x

def determinant(A):
    """Вычисление определителя методом Гаусса"""
    n = len(A)
    M = [row[:] for row in A]
    det = 1.0
    
    for i in range(n):
        pivot = M[i][i]
        det *= pivot
        
        for k in range(i+1, n):
            factor = M[k][i] / pivot
            for j in range(i, n):
                M[k][j] -= factor * M[i][j]
    
    return det

def inverse_matrix(A):
    """Нахождение обратной матрицы методом Гаусса"""
    n = len(A)
    
    #создаем [A|I]
    M = []
    for i in range(n):
        M.append(A[i] + [1.0 if j == i else 0.0 for j in range(n)])
    
    #Прямой ход + обратный ход
    for i in range(n):
        # Нормализация
        pivot = M[i][i]
        for j in range(2*n):
            M[i][j] /= pivot
        
        #обнуление других строк
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(2*n):
                    M[k][j] -= factor * M[i][j]
    
    #извлекаем обратную матрицу
    inv = []
    for i in range(n):
        inv.append(M[i][n:])
    
    return inv

if __name__ == "__main__":
    print("МЕТОД ГАУССА")
    print("=" * 50)
    
    # 1. Пример системы из задания 1
    print("\n1. РЕШЕНИЕ СИСТЕМЫ УРАВНЕНИЙ:")
    A1 = [
        [0.75, -7.71, -5.83, 8.58],
        [1.00, -3.96, -6.58, -5.81],
        [-8.43, -2.23, -5.23, -8.18],
        [1.84, 7.79, 7.51, -4.96]
    ]
    b1 = [8.52, -6.00, 3.90, 8.28]
    
    solution = solve_system(A1, b1)
    print("Решение системы:")
    for i, val in enumerate(solution, 1):
        print(f"x{i} = {val:.6f}")
    
    # 2. Пример определителя
    print("\n2. ВЫЧИСЛЕНИЕ ОПРЕДЕЛИТЕЛЯ:")
    A2 = [
        [6.44, 1.90, 0.35, -0.08],
        [0.96, -2.75, 8.36, 0.38],
        [-8.92, -0.86, -5.25, -1.23],
        [-1.99, 5.24, 3.35, 0.03]
    ]
    
    det = determinant(A2)
    print(f"Определитель = {det:.6f}")
    
    # 3. Пример обратной матрицы
    print("\n3. ОБРАТНАЯ МАТРИЦА:")
    A3 = [
        [8.47, 4.22, 4.07, -8.10],
        [-0.85, 8.28, -7.34, -0.87],
        [-4.06, -7.36, -2.61, 5.49],
        [4.03, 5.18, 2.97, -6.97]
    ]
    
    inv = inverse_matrix(A3)
    print("Обратная матрица:")
    for i in range(len(inv)):
        print(" ".join([f"{x:10.4f}" for x in inv[i]]))
    
    # 4.Система из задания 6
    print("\n4. СИСТЕМА ИЗ ЗАДАНИЯ 6:")
    A4 = [
        [5.38, 7.33, -0.24, -0.49, -8.41],
        [2.81, -4.69, -6.13, -3.05, -5.19],
        [7.60, 4.78, 8.59, 0.98, 6.72],
        [-8.44, -8.53, 5.76, -8.34, 4.96],
        [0.61, 4.63, -4.04, 1.72, 3.61]
    ]
    b4 = [4.27, 5.77, 3.70, 5.95, -6.77]
    
    solution4 = solve_system(A4, b4)
    print("Решение системы 5x5:")
    for i, val in enumerate(solution4, 1):
        print(f"x{i} = {val:.6f}")
    
    # 5.Определитель из задания 6
    print("\n5. ОПРЕДЕЛИТЕЛЬ ИЗ ЗАДАНИЯ 6:")
    A5 = [
        [-6.32, 4.51, -3.84, -7.38],
        [4.22, -4.13, -4.16, -6.56],
        [1.90, -2.56, 6.36, -1.93],
        [7.29, -1.49, 1.79, 6.36]
    ]
    
    det5 = determinant(A5)
    print(f"Определитель = {det5:.6f}")
    
    # 6.Обратная матрица из задания 6
    print("\n6. ОБРАТНАЯ МАТРИЦА ИЗ ЗАДАНИЯ 6:")
    A6 = [
        [-0.70, -2.39, -4.08, -3.94],
        [6.11, 8.00, 1.65, -1.61],
        [0.38, 1.83, 5.88, 8.00],
        [6.65, -7.51, -5.84, -5.62]
    ]
    
    inv6 = inverse_matrix(A6)
    print("Обратная матрица:")
    for i in range(len(inv6)):
        print(" ".join([f"{x:10.4f}" for x in inv6[i]]))