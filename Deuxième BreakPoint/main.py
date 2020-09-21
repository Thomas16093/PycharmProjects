# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

mail = input("Saisisser une chaine de caractères : ")
arrobase = "@"
if (arrobase in mail) & (mail.endswith(".com")):
    print("C'est un email valide")
else:
    print("Cette chaine ne contient pas d'email valide")

message = "test"
temp = ""
for e in range(10):
    temp = temp + message + " "
print(temp)
temp = ""
for e in range(len(message)):
    temp = temp + message[e] + " "
print(temp)

a = 0
b = 10
while a < b - 1:
    a = a + 1
print(a)

a = 0
b = 10
if b < 0:
    print(b)
else:
    while b > 0:
        b = b - 1
    print(b)

test = False
while not test:
    saisie = int(input("Rentrer un entier de 1 à 10 inclus : "))
    if (saisie > 0) & (saisie < 11):
        test = True
    else:
        test = False

chaine = "chaine de caractères"
l = [1, 2, 4, 8]
temp = ""
for e in range(len(chaine)):
    temp = temp + chaine[e] + " "
print(temp)
temp = ""
for e in range(len(l)):
    temp = temp + str(l[e]) + " "
print(temp)

for e in range(1, 15, 3):
    print(e)

n = int(input("Nombre de nombre pairs : "))
n2 = n
e = 0
while n > 0:
    e += 2
    print(e)
    n -= 1
for e in range(0, 15, 2):
    if e == 0:
        ""
    elif n2 > 0:
        print(e)
        n2 -= 1
    else:
        break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
