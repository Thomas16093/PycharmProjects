# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from threading import Thread
import tkinter
import random
import time


def Asteroid():  # Apparition des Asteroids
    ran = int(random.random() * 4)
    print(ran)
    for i in range(ran):
        pos = int(random.random() * 4)
        if pos == 1:
            x = C.create_image(740, 55, image=aste, tags="asteroid" + str(i))
            aster.append(x)
        elif pos == 2:
            x = C.create_image(740, 170, image=aste, tags="asteroid" + str(i))
            aster.append(x)
        elif pos == 3:
            x = C.create_image(740, 285, image=aste, tags="asteroid" + str(i))
            aster.append(x)
        else:
            x = C.create_image(740, 400, image=aste, tags="asteroid" + str(i))
            aster.append(x)


def appear(temp):
    Asteroid()


def move(temp):  # Deplacements des Asteroids
    for i in range(len(aster)):
        if aster[i] != 0:
            x1, y1, x2, y2 = C.bbox(aster[i])
            if x1 < 0:
                C.delete(aster[0])
                del aster[0]
                break
            else:
                if aster[i] != 0:
                    C.move(aster[i], -50, 0)
                    print(C.bbox(aster[i]))


def forget(temp):  # supprimer les asteroids de l'affichage
    for i in range(len(aster)):
        print(aster)
        C.delete(aster[0])
        # aster[i] = 0
        del aster[0]
    print("\n")


def move_up(temp):  # Deplacement vers le haut de la fusée
    x1, y1, x2, y2 = C.bbox("rocket")
    if y1 <= 120:
        return
    else:
        C.move(rocket, 0, -120)


def move_down(temp):  # Deplacement vers le bas de la fusée
    x1, y1, x2, y2 = C.bbox("rocket")
    if y2 >= C.winfo_height() - 120:
        return
    else:
        C.move(rocket, 0, 120)


class Test_thread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        tps = 0
        while True:
            if tps < 20:
                time.sleep(0.5)
                tps += 5
                print("Thread à attendu : " + str(tps))
            else:
                break


class Application(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        app = tkinter.Tk()
        app.title("Premier Jeux")
        tall_x = app.winfo_screenwidth()
        tall_y = app.winfo_screenheight()
        applier_x = 800
        applier_y = 460
        posX = (tall_x // 2) - (applier_x // 2)
        posY = (tall_y // 2) - (applier_y // 2)
        geo = "{}x{}+{}+{}".format(applier_x, applier_y, posX, posY)
        app.geometry(geo)
        global C
        C = tkinter.Canvas(app, bg="blue", height=1680, width=1050)
        filename = tkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\background.png")
        background_label = tkinter.Label(app, image=filename)
        C.create_image(0, 0, image=filename, tags="background")
        image = tkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\rocket.png")
        global rocket
        rocket = C.create_image(65, 50, image=image, tags="rocket")
        C.create_line(0, 105, 800, 105)
        C.create_line(0, 225, 800, 225)
        C.create_line(0, 350, 800, 350)
        C.pack()
        app.bind('<Up>', move_up)
        app.bind('<Down>', move_down)
        global aste
        aste = tkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\asteroid.png")
        global aster
        aster = [0, 0, 0, 0]
        app.resizable(False, False)
        Asteroid()
        app.bind('f', forget)
        app.bind('a', appear)
        app.bind('m', move)
        app.mainloop()


Appli = Application()
Compteur = Test_thread()
Appli.start()
Compteur.start()
Appli.join()
Compteur.join()

"""import random
import sys
from threading import Thread
import time


class Afficheur(Thread):
    Thread chargé simplement d'afficher une lettre dans la console.

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        Code à exécuter pendant l'exécution du thread.
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1


# Création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
