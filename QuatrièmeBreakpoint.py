# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

x = int(input("x = "))
fichier = open("data.txt", mode="w")
for e in range(0, x):
    temp = input("Chaine de caractère %d: " % e)
    fichier.write(temp + "\n")
fichier.close()

fichier = open("data.txt", mode="r")
arrobase = "@"
dot = "."
tour = 0
for e in fichier.readlines():
    if tour == 0:
        fichier.seek(0)
        tour = tour + 1
    temp = fichier.readline()
    if (arrobase in temp) and (temp[len(temp) - 5] == dot):
        print("Chaine OK : %s" % temp)
    else:
        print("Chaine NOK : %s" % temp)
fichier.close()


def compterMots(chaine):
    chaine = chaine.split()
    print(chaine)
    chaine2 = {}
    """for e in chaine:
        print(e)
        if e in chaine2:
            chaine2.index(e)[1] += 1
        else:
            chaine2.append([e,0])
    chaine2.index("phrase")[1] += 1
    return chaine2"""
    for e in chaine:
        if e in chaine2:
            chaine2[e] += 1
        else:
            chaine2[e] = 1
    return chaine2


chaine = "Ceci est une phrase test pour compter les mots présent dans la phrase"
print(compterMots(chaine))


def cube(w):
    return w ** 3


def volumeSphere(rayon):
    volume = float(((4 * 3.14) * cube(rayon)) / 3)
    return volume


rayon = float(input("Quel est le rayon de la sphère ? : "))
print("Le volume de la sphère est : %f" % volumeSphere(rayon))


def somme(arg1, arg2, arg3):
    total = arg1 + arg2 + arg3
    return total


valeur = (2, 4, 6)
retour = somme(valeur[0], valeur[1], valeur[2])

print("La somme est : %s" % retour)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
