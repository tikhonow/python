#Задача №3763. Права доступа
actions, file_permissions = {'read': 'R','write': 'W','execute': 'X',}, {}
for i in range(int(input())):
    name_file, *options = input().split()
    file_permissions[name_file] = set(options) 
for i in range(int(input())):
    action, file = input().split()
    print('OK') if actions[action] in file_permissions[name_file] else print('Access denied')