#Задача №1456. Шеренга
n = int(input())
count = 0
height = [int(i) for i in input().split()]
Petits_height = int(input())
for i in range(n):
    if height[i] >= Petits_height:
        count += 1
print(count + 1)