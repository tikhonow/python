#Задача №111385. Сапер
n, m, k    = [int(i) for i in input().split()]
game_field = [[0] * (m + 2) for i in range(n + 2)]
for i in range(k):
    x, y   = [int(i) for i in input().split()]
    game_field[x][y] = '*'
    for a in range(x-1, x + 2):
        for b in range(y-1, y + 2):
            if (game_field[a][b] != "*"):
                game_field[a][b] += 1 
for i in range(1,n + 1):
    for j in range(1,m + 1): 
        print(game_field[i][j], end=' ')
    print()
