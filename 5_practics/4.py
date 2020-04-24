class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum([self.coefficients[i]*x**i for i in range(len(self.coefficients))])

    def __add__(self, p):
        a = self.coefficients
        b = p.coefficients
        if len(a) < len(b):
            a += [0]*(len(b)-len(a))
        else:
            b += [0]*(len(a)-len(b))
        return Polynomial([a[i]+b[i] for i in range(len(a))])

       
print('Main 1')
poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))
print('Main 2') 
poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1
print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))