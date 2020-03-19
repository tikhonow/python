#Задача №111370. Транспонировать прямоугольную матрицу
n, m   = [int(i) for i in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(n)] 
for i in range(m):
    for j in range(n): 
        print(matrix[j][i], end=' ')
    print()