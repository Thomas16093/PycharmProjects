# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


def renommer(incr, message, originaux, extension):
    path = os.getcwd() + "\\renommage\\"
    for filename in os.listdir(os.getcwd() + "\\renommage"):
        if filename.endswith(extension):
            print(filename)
            file = os.getcwd() + "\\renommage\\"
            file = file + filename
            # os.rename(filename, filename[7:])
            os.walk(os.getcwd() + "\\renommage")
            print(os.listdir(os.getcwd() + "\\renommage"))
            os.rename(file, path + "00" + str(incr) + " - " + message + " - " + filename[originaux:])
            print(filename)
            incr += 1
        else:
            break


incrementation = int(input("Début de l'incrémentation ? : "))
rajout = input("Message à rajouter ? : ")
suppresion = int(input("Nombre de caractères à supprimer de l'ancien ? : "))
exte = input("Extension des fichiers à renommer ? : ")
renommer(incrementation, rajout, suppresion, exte)

# essai non concluant :
"""print(os.getcwd())
path = os.walk(os.getcwd() + "\\renommage")
for files in path:
    for filename in files:
        name: str = '%s' % filename
        print(name)
""" """incr = input("A combien démarrer l'incrémentation ? : ")
message = input("Texte à rajouter ? : ")
originaux = input("quel partie du fichier original ? : ")"""
""" incr = 0o02
message = "test"
originaux = 4
newname = {}
name = name.split(",")
for e in range(0, name.count("png")):
    print(e)
    print(name[e])
    newname[e] = os.getcwd() + "\\renommage" + name[e]
print(name)
print(newname)
print("passer ici")"""
""" for files in path:
    for filename in files:
        newname = 'incr+message+%s.split(originaux).png' % filename
        print(newname)
    print("passer la")"""
