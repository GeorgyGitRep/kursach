def rotate_matrix(matrix,k):
    n = len(matrix)
    
    # Создаем новую матрицу для повернутой версии
    rotated_matrix = [[k for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-1-i] = matrix[i][j]
    
    return rotated_matrix

# Считываем матрицу из stdin
n = int(input("Введите размер матрицы n: "))
matrix = []
for _ in range(n):
    row = list(map(int, input().split()[:n]))
    matrix.append(row)

print(rotate_matrix(matrix, 0))
Array = []
def sn(matrix):
    
    k = 0
    while len(Array) < n*n:
        for i in range(n):
            Array.append(matrix[0][i])
        print(Array)
        matrix = matrix[1:n][:]
        print(*matrix)
        k = k + 1
        matrix = rotate_matrix(matrix,k)
        print(matrix)
sn(matrix)