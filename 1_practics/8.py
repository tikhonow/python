#Задача №3851. Кегельбан
N,K = input().split()
row =  ['I'] * int(N)
for i in range(int(K)):
    a,b = [int(s) for s in input().split()]
    for k in range(a -1,b):
        row[k]='.'
print(''.join(row))