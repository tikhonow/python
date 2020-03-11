def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Введите номер числа: "))
for i in range(1, n +1, 1):
    print(fibonacci(i))