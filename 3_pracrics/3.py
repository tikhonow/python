#Задача №3765. Страны и города
a = {}
for i in range(int(input())):
    country, *cities = input().split()
    for i in cities:
        a[i] = country        
for i in range(int(input())):
    print(a[input()])