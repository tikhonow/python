#G. Пин-код
def check_pin(pincode):
    
    a, b, c = int(pincode[0]), pincode[1], int(pincode[2])
    
    def check_a(a):
        d = 2
        while a % d != 0:
            d += 1
        if d == int(pincode[0]):
            return 1
    
    
    def check_b(b):
        if b == b[::-1]:
            return 1
    
    
    def check_c(c):
        s = 1
        c_ = 0
        while s < c:
            s *= 2
            if s == c:
                c_ = 1
            else:
                c_ = 0
        return c_
    control_sum = check_a(a) + check_b(b) + check_c(c)
    if control_sum > 2:
        return('Корректен')
    else:
        return('Некоректен')



pincode = input('Введите пин - код:').split('-')
print(check_pin(pincode))
