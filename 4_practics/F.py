# Задача F.пароль
def password_level(password):
    count = [0, 0, 0]
    if len(password) > 5:
        for i in password:
            if i.isdigit():
                count[0] = 1
            elif i.isupper():
                count[1] = 1
            elif i.islower():
                count[2] = 1
        if ((count[1] + count[2] == 1) and count[0] == 0)  or ((count[1] + count[2] == 0) and count[0] == 1):
            return ('Ненадежный пароль')
        if ((count[1] + count[2] == 2) and count[0] == 0) or ((count[1] + count[2] == 1) and count[0] == 1):
            return('Слабый пароль') 
        if (sum(count) == 3):
            return('Надежный пароль') 
    else:
        return ('Недопустимый пароль')
password=input('Введите пароль:')
print(password_level(password))
