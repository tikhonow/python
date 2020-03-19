#Задача №112344. Строка палиндром
string =''.join(input(). split())
if string == string[::-1]:
    print("YES")
else:
    print("NO")