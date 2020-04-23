#Задача №3771. Родословная: подсчет уровней 
n = int(input())
dic = {}
for i in range(n - 1):
    child, parent = input().split()
    if parent not in dic:
        dic[parent] = None
    dic[child] = parent
for key, value in sorted(dic.items()):
    level = 0
    print(key, end = ' ')
    while key in dic:
        level += 1
        key = dic[key] # опускаемся к корню - потомок становится родителем
    print(level - 1)