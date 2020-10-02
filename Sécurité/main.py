# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import hashlib


class Lprenom:

    def __init__(self, prenom):
        self.prenom = prenom

    def Test(self):
        print("contenue de prénom = " + str(self.prenom))
        result = hashlib.md5(self.prenom.encode())
        print("The byte equivalent of hash is : ", end="")
        print(result.hexdigest())


t = Lprenom("Test")
t.Test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
