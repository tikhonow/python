numbers = filter(lambda x: not x%9, range(10,100))
print(sum(map(lambda x: x**2,numbers)))