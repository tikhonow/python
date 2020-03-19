#Задача №112227. Числа Фибоначчи
n = int(input())
a, b = 0, 1
print(b, end=' ')
for i in range (n- 1):
    print(a+b , end=' ')
    a, b = b, a + b