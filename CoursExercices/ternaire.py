# b = input()
# x = 4 if b > 8 else x = 9

for i in range(10):
    print(i, end='  ')

def my_gen(maxi):
    cnt = 0
    while cnt < maxi:
        yield cnt
        cnt += 1

print('\nGenerateur')
for i in my_gen(25):
    print(i, end='  ')

def my_cut(l, nbr):
    for i in range(0, len(l), nbr):
        yield l[i:i+nbr]

liste = ['Paul','Eric','Jean','Albert','François','Desire','Jordan', 'Robert','Arthur','Toto']
print('\n Générateur ')
for l in my_cut(liste, 3):
    print(l)

def facto(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

for n in range(9):
    print('Factorielle de {}!={}'.format(n, facto(n)))

nbr = int(input('Entrez un nombre : '))
fact = 1
for i in range(1, nbr+1):
  fact = fact * i
print (nbr,'! = ',fact)
