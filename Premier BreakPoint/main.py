# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

temps = 6.892
distance = 19.7
vitesse = distance / temps
print("vitesse = %.1f" % vitesse)
nom = input("Quel est ton nom ? ")
"""age_str = input("Quel est ton age ? ")
age = int(age_str)"""
age = int(input("Quel est votre age ? "))
print("Son nom est : %s et son age est : %d ans" % (nom, age))
flot = input("Quel est la valeur du flottant ? ")
flottant = float(flot)
if math.sqrt(flottant) > 0:
    print("Ce nombre à un racine qui est : %f" % math.sqrt(flottant))
else:
    print("%s n'a pas de racine." % flot)
mot1 = input("Quel est le premier mot ? ")
mot2 = input("Quel est le deuxième mot ? ")
if mot1<mot2:
    print("Le mot le plus petit est le mot 1 : %s" %mot1)
else:
    print("le mot le plus petit est le mot 2 : %s" %mot2)
pSeuil = 2.3
vSeuil = 7.41
pCourant = input("Quel est la pression courante ? ")
vCourant = input("Quel est le volume courant ? ")
pCourant = float(pCourant)
vCourant = float(vCourant)
if (vCourant>vSeuil) & (pCourant>pSeuil):
    print("arrêt immédiat")
elif vCourant>vSeuil:
    print("Diminuer le volume de l'enceinte")
elif pCourant>pSeuil:
    print("Augmenter le volume de l'enceinte")
else:
    print("Tout va bien")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
