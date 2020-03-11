import math
x1, x2 = [float(i) for i in input().split()]
y1, y2 = [float(i) for i in input().split()]
print(round((math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))), 3))