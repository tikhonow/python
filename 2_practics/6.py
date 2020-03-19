#Задача №111385. Сапер
n, m, k    = [int(i) for i in input().split()]
game_field = [[0] * m for i in range(n)]
for i in range(k):
    x, y   = [int(i) for i in input().split()]
    game_field[x - 1][y - 1] = '*'
    for a in range(x-2, x + 1):
        for b in range(y-2, y + 1):
            if (game_field[a][b] != "*"):
                game_field[a][b] += 1 
for i in range(n):
    for j in range(m): 
        print(game_field[i][j], end=' ')
    print()
