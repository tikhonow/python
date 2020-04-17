n = int(input('Введите количество групп: '))
all_ =[]
group = {}
#A. Задачи
for i in range(n):
    m = int(input('Введите коичество студентов в группе: '))
    for j in range(m):
        surname,points = input('Введите данные студента: ').split()
        group[surname] = int(points)
    all_.append(group)
status = []
for i in all_:
    if any(student[1] > 1 for student in i.items()):
        status.append(1)
    else:
        status.append(0)

if all(status) == 1:
    print('Да')
else:
    print('Нет')