#Задача №111203. Шахматная доска
n,m = input()
[[(i + j + 1) % 2 for j in range(m)] for i in range(n)] 