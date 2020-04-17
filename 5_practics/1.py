#A.Dt
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0
 
    def add_right(self, a):
        self.right += a
 
    def add_left(self, a):
        self.left += a
 
    def result(self):
        if self.left == self.right:
            return '='
        if self.left > self.right:
            return 'L'
        if self.left < self.right:
            return 'R'

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())