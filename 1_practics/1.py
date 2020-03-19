#Задача №112149. Расстояние
import math
x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(i) for i in input().split()]
print(round((math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))), 3))