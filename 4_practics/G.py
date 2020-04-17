def check_pin(pincode):
    control_sum = 0
    a, b, c = int(pincode[0]),pincode[1], int(pincode[2])

    d = 2
    while a % d != 0:
        d += 1
    if d == int(pincode[0]):
        control_sum += 1
    if b == b[::-1]:
        control_sum += 1
    s = 1
    x = 0
    while s <= c:
        s *= 2
        x+=1
        if s == c:
            control_sum += 1
            break
    else:
        control_sum = 0
    if control_sum == 3:
        return('Корректен')
    else:
        return('Некоректен')
pincode = input('Введите пин - код:').split('-')
print(check_pin(pincode))