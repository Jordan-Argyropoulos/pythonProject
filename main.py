# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('entrer un chiffre entre 1 à 3 ou zero pour terminer')
a = eval(input())
while a:
    if a == 1:
    print("Message valeur = 1")
    elif a == 2:
    print("Message valeur = 2")
    elif a == 3:
    print("Message valeur = 3")
    else:
    print("un nbr entre 1 et 3 svp")
    a = eval(input())