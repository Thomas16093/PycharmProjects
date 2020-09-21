# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

class Domino():

    def __init__(self, r, t):
        self.A = r
        self.B = t

    def affiche_points(self):
        print("face A: " + str(self.A) + ", face B: " + str(self.B))

    def totale(self):
        return self.A + self.B

    def __repr__(self):
        print("la face est A est : " + str(self.A) + " et la B est : " + str(self.B))

class CompteBancaire():     #Exercice 2

    def __init__(self, n, s = 0):    #n = Nom et s = solde
        self.Nom = n
        self.Solde = s

    def affiche(self):
        print("Le solde du compte de " + str(self.Nom) + " est " + str(self.Solde) + " euros.")

    def retrait(self, v):   # v = value
        self.Solde -= v
        #yield lambda Solde, v: Solde - v

    def depot(self, v):     # v = value
        self.Solde += v

    def __repr__(self):
        print("C'est le compte de : " + str(self.Nom) + " Avec un solde de : " + str(self.Solde))

class TableMultiplication():    #Exercice 3

    def __init__(self, v):      #init de la table
        self.table = v
        self.var = self.calcul()
    def prochain(self):         #appelle de la fonction calcul + affichage
        print(self.var.__next__())

    def calcul(self):           #Calcul la prochaine valeur de la table
        for i in range(0,10):
            yield self.table * i

    def __repr__(self):
        print("C'est la table de " + str(self.table))

class Fraction():               #Exercice 4

    def __init__(self, v1, v2):     #Initialisation des variables de Fractions
        self.num = v1
        self.denom = v2
        self.frac = v1/v2

    def affiche(self):              # Affichage de la Fraction
        print("Valeur de la Fraction : " + str(self.num) + "/" +str(self.denom))

    def __add__(self, other):       # Addition de deux Fractions
        commun = math.gcd(self.denom, other.denom)
        if self.denom > other.denom:
            Fraction.denom = self.denom
            Fraction.num = self.num + (other.num*commun)
        else:
            Fraction.denom = other.denom
            Fraction.num = (self.num*commun) + other.num
        return Fraction(Fraction.num, Fraction.denom)

    def __truediv__(self, other):   # Division de deux Fractions
        Fraction.denom = self.denom * other.num
        Fraction.num = self.num * other.denom
        commun = math.gcd(Fraction.num, Fraction.denom)
        Fraction.num /= commun
        Fraction.denom /= commun
        return Fraction(int(Fraction.num), int(Fraction.denom))

    def __sub__(self, other):   # Soustraction de deux Fractions
        commun = math.gcd(self.denom, other.denom)
        if other.denom > self.denom:
            Fraction.denom = other.denom
            Fraction.num = (self.num*commun)- other.num
        elif self.denom > other.denom:
            Fraction.denom = self.denom
            Fraction.num = self.num - (other.num*commun)
        return Fraction(Fraction.num, Fraction.denom)

    def __mul__(self, other):   # Mulitplication de deux Fractions
        Fraction.denom = self.denom * other.denom
        Fraction.num = self.num * other.num
        commun = math.gcd(Fraction.num, Fraction.denom)
        Fraction.num /= commun
        Fraction.denom /= commun
        return Fraction(int(Fraction.num), int(Fraction.denom))

    def __repr__(self):         # Réponse de l'objet
        print("La valeur est de " + str(self.num) + "/" + str(self.denom))

class Poly():

    def __init__(self, *args):
        self.coef = []
        self.total = 0
        self.totall = 0
        self.list = args

    def coeff(self):
        for var in self.list:
            self.coef.append(var)
        print(self.coef)

    def evaluate(self, puiss):
        for i in range(puiss+1):
            if i == 0:
                self.total = self.coef[i]
            else:
                self.total = self.total + ((self.coef[i] * puiss) * i)
        print(self.total)

    def evaluatte(self, puiss):
        enumeration = enumerate(self.list)
        print(list(enumeration))
        for i in enumerate(self.list):
            print(i)
            for j in i:
                print(j)
                #self.totall = self.totall + (j*puiss)
        print(self.totall)

d = Domino(4, 6)
d.affiche_points()
x = d.totale()
print(x)
#Exercice 2
compte1 = CompteBancaire('Jean', 1000)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire('Marc')
compte2.depot(500)
compte2.affiche()
#Exercice 3
tab = TableMultiplication(3)
tab.prochain()
tab.prochain()
tab.prochain()
tab.prochain()
#Exercice 4
f = Fraction(3, 4)
f.affiche()
g = Fraction(1, 2)
g.affiche()
print("")
r1 = f + g
r1.affiche()
r2 = f / g
r2.affiche()
r3 = f - g
r3.affiche()
r4 = f * g
r4.affiche()
#Exercice 5
d.__repr__()
compte1.__repr__()
tab.__repr__()
g.__repr__()
#Exercice 6
p1 = Poly(3, 4, -2)
p1.coeff()
p1.evaluate(2)
p1.evaluatte(2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
