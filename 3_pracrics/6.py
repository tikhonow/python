#Задача №3769. Продажи (D)
import sys
shop = {}
for i in sys.stdin:
    name, *item = i.split()
    if name in shop:
            shop[name].append(item)
    else:
        shop[name] = [item]
for name in shop:
for name, item in sorted(shop.items()):
    print(key +":")
    s = {}
    for val in item:
        s[val[0]] = s.get(val[0], 0) + int(val[1])
    for key in sorted(s.keys()):
        print(key, end=" ")
        print(s[key])