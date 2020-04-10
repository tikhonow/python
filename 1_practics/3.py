#Задача №112212. Чётные цифры
print(len( [int(i) for i in input().split() if int(i)%2 == 0]))