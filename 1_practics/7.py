#Задача №1460. Суперсдвиг
import math
n = int(input())
sequence = [int(i) for i in input().split()]
k = int(input())
if math.fabs(k) > len(sequence):
    k = k % len(sequence)
if k == 0:
    k = len(sequence)
print(*([int(sequence[i]) for i in range(n-k,n) if k > 0]),end=' ')
print(*([int(sequence[i]) for i in range(n-k)   if k > 0]))
print(*([int(sequence[i]) for i in range(-k,n)  if k < 0]),end=' ')
print(*([int(sequence[i]) for i in range(0,-k)  if k < 0]))