import gettext

'''
c1 = "befreit"
c2 = "baeche"
c3 = "eise"
c4 = "sind"
c5 = "strom"
c6 = "und"
c7 = "vom"

mydict = {c1:"liberated", c2:"brooks", c3:"ice", c4:"are", c5:"river", c6:"and", c7:"from"}

print(mydict.keys())
print(mydict.values())

phrase = "vom eise befreit sind strom und baeche"
print(phrase)

translated_string = " ".join([mydict.get(e, "") for e in phrase.split(" ")])
print (translated_string)'''

try:
    gettext.find("test")
    traduction = gettext.translation('fr', localedir='locale', languages=['fr'])
    traduction.install()
except:
    gettext.install('test')


def display():
    print("Hello everybody on {}".format("DVP"))
    print("Please have fun")


if __name__ == "__main__":
    display()
