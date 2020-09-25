import os
import tkinter


def renommer(path, incr, message, originaux, extension):  # Récupère les options et renomme
    global label_run
    display = ""
    if path[-1] != '\\':
        path = path+'\\'
    print(os.listdir(path))
    display = display + str(os.listdir(path)) + "\n"
    label_run.configure(text=display)
    for filename in os.listdir(path):
        if filename.endswith(extension):  # filtre par extension
            print(filename + " et longueur = " + str(len(filename)))
            display = display + str(filename) + " et longueur = " + str(len(filename)) + "\n"
            label_run.configure(text=display)
            file = path + filename
            os.walk(path)
            if message == "":
                if originaux > (len(filename) - 4):
                    os.rename(file,
                              path + "00" + str(incr) + filename[originaux:] + extension)
                else:
                    os.rename(file, path + "00" + str(incr) + filename[originaux:])
            else:
                if originaux > (len(filename) - 4):
                    os.rename(file,
                              path + "00" + str(incr) + " - " + message + " - " + filename[originaux:] + extension)
                else:
                    os.rename(file, path + "00" + str(incr) + " - " + message + " - " + filename[originaux:])
            print(filename)
            display = display + str(filename) + "\n"
            label_run.configure(text=display)
            incr += 1
        else:
            break


def Renommage():
    global entry_folder, entry_incr, entry_rajout, entry_suppr, entry_exte
    path = entry_folder.get()
    incrementation = int(entry_incr.get())
    rajout = str(entry_rajout.get())
    suppresion = int(entry_suppr.get())
    exte = str(entry_exte.get())
    renommer(path, incrementation, rajout, suppresion, exte)


app = tkinter.Tk()
app.title("Renommage de Fichiers")
tall_x = app.winfo_screenwidth()
tall_y = app.winfo_screenheight()
applier_x = 800
applier_y = 600
posX = (tall_x // 2) - (applier_x // 2)
posY = (tall_y // 2) - (applier_y // 2)
geo = "{}x{}+{}+{}".format(applier_x, applier_y, posX, posY)
app.geometry(geo)

# entrée chemin du fichier
label_folder = tkinter.Label(app, text="Chemin du fichier : ").grid(column=0, row=0, sticky=tkinter.W)
entry_folder = tkinter.Entry(app, width=60)
entry_folder.grid(column=1, row=0)

# entrée incrémentation
label_incr = tkinter.Label(app, text="Début de L'incrémentation ? : ").grid(column=0, row=1, sticky=tkinter.W)
entry_incr = tkinter.Entry(app, width=3)
entry_incr.grid(column=1, row=1)

# entrée message rajouté
label_rajout = tkinter.Label(app, text="Message à rajouter ? : ").grid(column=0, row=2, sticky=tkinter.W)
entry_rajout = tkinter.Entry(app)
entry_rajout.grid(column=1, row=2)

# entrée caractère à supprimer
label_suppr = tkinter.Label(app, text="Nombre de caractères à supprimer de l'ancien ? : ").grid(column=0, row=3,
                                                                                                sticky=tkinter.W)
entry_suppr = tkinter.Entry(app, width=3)
entry_suppr.grid(column=1, row=3)

# entrée extension du fichier
label_exte = tkinter.Label(app, text="Extension des fichiers à renommer ? : ").grid(column=0, row=4, sticky=tkinter.W)
entry_exte = tkinter.Entry(app, width=4)
entry_exte.grid(column=1, row=4)

# bouton renommage et quitter
label_fill = tkinter.Label(app).grid(column=0, row=5)
button_valider = tkinter.Button(app, text="Renommer", command=Renommage).grid(column=0, row=6, sticky=tkinter.S)
button_quit = tkinter.Button(app, text="Quitter", command=app.quit).grid(column=0, row=7, sticky=tkinter.S)

# affichage du run dans la fenêtre
label_run = tkinter.Label(app, text="")
label_run.grid(column=0, row=8)

app.grid_columnconfigure(1, weight=1)

app.mainloop()
"""incrementation = int(input("Début de l'incrémentation ? : "))
rajout = input("Message à rajouter ? : ")
suppresion = int(input("Nombre de caractères à supprimer de l'ancien ? : "))
exte = input("Extension des fichiers à renommer ? : ")
renommer(incrementation, rajout, suppresion, exte)"""
