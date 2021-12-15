print("Hello World!")

val = "Abracadabra"
num = input("Enter a number between 1 and 100: ")
N = int(num)
X = 1
if 1 <= N <= 100:
    while X <= N:
        print(X, val)
        X = X + 1
else:
    print("ERROR!")
