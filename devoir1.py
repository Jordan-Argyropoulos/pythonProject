# Devoir: boucle for et while
# calculer les 10 premieres années de la capitalisation d'un montant à 2% d'interet de 2021 à 2031
# c = 12500€, i = 2% (année 1 C1 = C * (1+i%) ... etc
# 2021 : 12500
# 2022 : ...

i = 0.02
c = 12500
for a in range(2021, 2032):
    c = c * (1 + i)
    print(a, ':', c, '€')
    print("\n")

i = 0.02
c = 12500
a = 2021
while a <= 2031:
    c = c * (1 + i)
    print(a, ':', c, '€')
    a += 1
    print("\n")
