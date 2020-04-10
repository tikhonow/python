#Задача №1460. Суперсдвиг
import math
n = int(input())
sequence = [i for i in input().split()]
k = int(input())
if k > 0:
    print(' '.join(sequence[n-(k%n):] + sequence[:n-(k%n)]))
else:
    print(' '.join(sequence[(-k)%n:] + sequence[:(-k)%n]))