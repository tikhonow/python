#H. Вложенная сортировка
def sorted2(data, key = lambda x: -x):
    data_sorted = sorted([sorted(i, key=key) for i in data], key=lambda x: x[-1])
    return(data_sorted)

data = [[6, 5, 4], [3, 2], [1]]
key = lambda x: x
print(sorted2(data, key=key))
