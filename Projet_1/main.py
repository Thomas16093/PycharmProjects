# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mttkinter as tkinter
import time
from threading import Thread, Event
import random


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
        C.delete(aster[0])
        # aster[i] = 0
        del aster[0]


def move_up(temp):  # Deplacement vers le haut de la fusée
    x1, y1, x2, y2 = C.bbox("rocket")
    if y1 <= 120:
        return
    else:
        C.move(rocket, 0, -120)
        print(C.bbox("rocket"))


def move_down(temp):  # Deplacement vers le bas de la fusée
    x1, y1, x2, y2 = C.bbox("rocket")
    if y2 >= C.winfo_height() - 120:
        return
    else:
        C.move(rocket, 0, 120)
        print(C.bbox("rocket"))


class Deplacement(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        # time.sleep(0.5)
        while t1.is_alive():
            try:
                time.sleep(0.5)
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
                                # print(C.bbox(aster[i]))
            except Exception:
                break

        print("Deplacement = " + str(t1.is_alive()))
        pass


class Life(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        time.sleep(1)
        t3 = Deplacement()
        t4 = Appear()
        t3.start()
        t4.start()
        vie = 10
        while t1.is_alive() & t3.is_alive() & t4.is_alive():
            try:
                if vie != 0:
                    try:
                        x1, y1, x2, y2 = C.bbox("rocket")
                        for i in range(len(aster)):
                            # print(C.bbox(aster[i]))
                            x3, y3, x4, y4 = C.bbox(aster[i])
                            if x3 <= x2 & (y1 + 3) == y3:
                                C.delete(aster[i])
                                vie -= 1
                                print("Vie = " + str(vie))
                                del aster[i]
                                break
                            if x3 <= x2 & (y1 + 8) == y3:
                                C.delete(aster[i])
                                vie -= 1
                                print("Vie = " + str(vie))
                                del aster[i]
                                break
                            if x3 <= x2 & (y1 + 13) == y3:
                                C.delete(aster[i])
                                vie -= 1
                                print("Vie = " + str(vie))
                                del aster[i]
                                break
                            if x3 <= x2 & (y1 + 18) == y3:
                                C.delete(aster[i])
                                vie -= 1
                                print("Vie = " + str(vie))
                                del aster[i]
                                break
                    except TypeError:
                        pass
                    except IndexError:
                        pass
                else:
                    for i in range(len(aster)):
                        C.delete(aster[0])
                        del aster[0]
                        C.delete(rocket)
                    C.create_text(100, 470, text="Vous avez perdu !", fill="red")
            except RuntimeError:
                break
        t3.join()
        t4.join()
        print("Life = " + str(t1.is_alive()))
        pass


class Appear(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.event = Event()

    def run(self):
        # time.sleep(0.5)
        while t1.is_alive():
            try:
                time.sleep(2)
                Asteroid()
            except RuntimeError:
                pass

        print("Appear = " + str(t1.is_alive()))
        pass


class Application(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        app = tkinter.mtTkinter.Tk()
        app.title("Premier Jeux")
        tall_x = app.winfo_screenwidth()
        tall_y = app.winfo_screenheight()
        applier_x = 800
        applier_y = 500
        posX = (tall_x // 2) - (applier_x // 2)
        posY = (tall_y // 2) - (applier_y // 2)
        geo = "{}x{}+{}+{}".format(applier_x, applier_y, posX, posY)
        app.geometry(geo)
        global C
        C = tkinter.mtTkinter.Canvas(app, bg="blue", height=1680, width=1050, background="white")
        filename = tkinter.mtTkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\background.png")
        # background_label = tkinter.Label(app, image=filename)
        C.create_image(0, 0, image=filename, tags="background")
        image = tkinter.mtTkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\rocket.png")
        global rocket
        rocket = C.create_image(65, 50, image=image, tags="rocket")
        C.create_line(0, 105, 800, 105)
        C.create_line(0, 225, 800, 225)
        C.create_line(0, 350, 800, 350)
        C.create_line(0, 460, 800, 460)
        C.pack()
        app.bind('<Up>', move_up)
        app.bind('<Down>', move_down)
        global aste
        aste = tkinter.mtTkinter.PhotoImage(file="D:\\PycharmProjects\\Projet_1\\asteroid.png")
        global aster
        aster = list()
        app.resizable(False, False)
        Asteroid()
        app.bind('f', forget)
        app.bind('a', appear)
        app.bind('m', move)
        app.mainloop()


global C
global aster
t1 = Application()
t2 = Life()
t1.start()
t2.start()
t1.join()
t2.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
