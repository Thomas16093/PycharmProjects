# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

liste = [17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
"del liste[liste.index(38)]"
print(liste)
#for e in range(1, 3):
#    print(liste[e])
print(liste(1:3))
for e in range(0, 2):
    print(liste[e])
for e in range(2, len(liste)):
    print(liste[e])
for e in range(0, len(liste)):
    print(liste[e])

chaine1 = input("Quel chaine à inversé ? ")
chaine2 = " "
for e in chaine1:
    chaine2 = e + chaine2
print(chaine2)

palin = input("Quel chaine testé ? ")
test = ""
pa = False
for e in palin:
    test = e + test
for e in range(0, len(palin)):
    if palin[e] == test[e]:
        pa = True
    else:
        pa = False
        break
if pa == True:
    print("Palyndrome")
else:
    print("Pas palydrome")

mail = input("Entrer un email : ")
arrobase = "@"
dot = "."
if (arrobase in mail) & (mail[len(mail) - 4] == dot):
    print("Chaine OK")
else:
    print("Chaine NOK")

truc = []
#machin = ["", "", "", "", ""]
machin = [0.0 for i in range(5)]
print(truc)
print(machin)  # pas sure

for e in range(0, 4):
    print(e)
for e in range(4, 8):
    print(e)
for e in range(2, 9, 2):
    print(e)
chose = [0, 1, 2, 3, 4, 5]
if chose[3]:
    print("3 appartient à chose")
else:
    print("3 n'appartient pas à chose")
if chose[6]:
    print("6 appartient à chose")
else:
    print("6 n'appartient pas à chose")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
