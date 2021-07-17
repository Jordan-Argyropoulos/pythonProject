#
#
#

a = 4
b = 3.1415
c: bool = True
d = "Bonjour le monde"

print('\n', a, b, c, d)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print("Avant:", a, b)
a, b = b, a
print("Après:", a, b)

if a > 0:
    print('Positif')
elif a == 0:
    print('null')
else:
    print('Negatif')

i = 0
while c:
    print(d)
    c = False
else:
    print("Fini")

while i < 10:
    i += 1
    print(i)

print('FOR')

for i in range(10):  # for( i=0; i<10; i++)
    print(i)

print('Range 10', range(10))

ent = 14 // 3
mod = 14 % 3

print("Equalité = ", 14, 3, ent, mod, 14, '=', ent * 3 + mod, '?')

#
# Ecrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.
# while + for
i = 0
while i <= 20:
    print(i * 7)
    i += 1

for i in range(20):
    print(i, 'X 7 =', i * 7)

#
# Ecrivez un programme qui affiche la conversion des euros en $, la table des euros étant géométrique (X2) (ie: 1,2,
# 4,8,16,32,...512) taux de reconversion 1.50 $ = 1€ format de sortie:  1 euros = 1.50 dollar ...

a = 1
for i in range(1, 10):
    print(a * 1.5)
    a = a * 2

i = 1
while i <= 512:
    print(i * 1.5)
    i = i * 2

# Devoir: boucle for et while
# calculer les 10 premieres années de la capitalisation d'un montant à 2% d'interet de 2021 à 2031
# c = 12500€, i = 2% (année 1 C1 = C * (1+i%) ... etc
# 2021 : 12500
# 2022 : ...
