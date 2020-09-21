# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def chiffrePortebonheur(nb):  # Calcul si res == 1 -> Chiffre Porte-Bonheur
    while int(nb) > 10:
        temp = 0
        for i in nb:
            temp = temp + int(i) * int(i)
        nb = str(temp)
        print(nb)
    if nb == '1':
        print("Chiffre porte bonheur : " + str(nb))
    else:
        print("Chiffre non porte-bonheur : " + str(nb))


def g():  # Generateur des premiers alphabets minuscule
    alpha = ""
    for i in range(97, 123):
        if i == 122:
            alpha = alpha + chr(i)
        else:
            alpha = alpha + chr(i) + ", "

    print(alpha)


def g2(incr):  # Generateur et duplicateur alphabets minuscule
    alpha = ""
    for i in range(97, 123):
        j = 0
        while j < incr:
            if i == 122 and j == (incr - 1):
                alpha = alpha + chr(i)
            else:
                alpha = alpha + chr(i) + ", "
            j += 1

    print(alpha)


def PowerSet(PoSet):
    liste = PoSet
    seq = PoSet
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for x in PowerSet(seq[1:]):
            yield [seq[0]] + x
            yield x


def decorateur(func):
    def compteur(x):
        compteur.calls += 1
        return func(x)

    compteur.calls = 0

    return compteur


@decorateur
def test(x):
    return x + 1


chiffrePortebonheur("914")
g()
g2(2)
A = [1, 2, 3]
r = [x for x in PowerSet(A)]
r.sort(key=len)
print(r)
print("Avant d'appeler la fonction : " + str(test.calls))
test(1)
test(2)
test(5)
print("Après nb : " + str(test.calls))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
