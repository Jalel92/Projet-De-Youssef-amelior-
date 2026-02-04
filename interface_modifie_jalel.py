from tkinter import *
import calendar # Bibliothèque externe 1 : pour générer les matrices de mois
import datetime # Bibliothèque externe 2 : pour manipuler les dates système

page = Tk()
page.title("Calendrier")
page.geometry("700x500")

big_text = Label(
    page,
    text="Calendrier",
    font=("Helvetica", 20),
    fg="green"
)
big_text.pack(pady=10)

consigne = Label(
    page,
    text="Entrez votre budget total :",
    font=("Helvetica", 13),
    fg="black"
)
consigne.pack(pady=10)

# Frame pour contenir les boutons
frame_boutons = Frame(page)
frame_boutons.pack(pady=10)

result_label = Label(
    page,
    text="",
    font=("Helvetica", 12),
    fg="black"
)
result_label.pack(pady=10)

def click1() :
    maintenant = datetime.datetime.now() # Récupération de l'objet date complet
    result_label.config(
    text=f"Date : {maintenant.strftime('%d/%m/%Y')}",
    fg="black")        

button1 = Button(
    frame_boutons,
    text="Voir la date d'aujourd'hui",
    font=("Helvetica", 12,"bold"),
    bg="green",
    fg="white",
    command=click1
)
button1.pack(side=LEFT, padx=5)

# 🎯 Variables pour les entries
entry1 = None
entry2 = None

def click3() :
    # 🔴 ERREUR 1 : Tu essaies de récupérer les valeurs AVANT que l'utilisateur ne les entre
    # 🔴 Il faut récupérer les valeurs ICI, pas dans click2()
    month = int(entry1.get()) 
    year = int(entry2.get())
    
    mois = Label(
    page,
    text=calendar.month(year, month),
    font=("Helvetica", 13),
    fg="black"
    )
    mois.pack(pady=10)

def click2() :
    global entry1, entry2  # 🎯 Utiliser les variables globales
    
    # 🎯 Afficher les deux entries
    if entry1 is None:  # Créer seulement si elles n'existent pas encore
        mois = Label(
        page,
        text="Entrez le mois (1-12) :",
        font=("Helvetica", 13),
        fg="black"
        )
        mois.pack(pady=10)

        entry1 = Entry(page, width=20)
        entry1.pack(pady=2)

        annee = Label(
        page,
        text="Entrez l'année :",
        font=("Helvetica", 13),
        fg="black"
        )
        annee.pack(pady=10)
        entry2 = Entry(page, width=20)
        entry2.pack(pady=2)

        button = Button(
            page,
            text="Cliquez pour voir le résultat",
            font=("Helvetica", 12,"bold"),
            bg="green",
            fg = "white",
            command=click3  # 🔴 ERREUR 2 : Il manquait command=click3
        )
        button.pack(pady=10)

        # 🔴 ERREUR 3 : Ces lignes étaient au mauvais endroit !
        # Tu ne peux pas récupérer les valeurs AVANT que l'utilisateur ne les tape
        # Ces lignes ont été déplacées dans click3()
        # month = int(entry1.get()) 
        # year = int(entry2.get()) 




button2 = Button(
    frame_boutons,
    text="Voir un mois",
    font=("Helvetica", 12,"bold"),
    bg="green",
    fg="white",
    command=click2
)
button2.pack(side=LEFT, padx=5)


page.mainloop()