from tkinter import *
import tkinter.font as tkfont
from random import *

class Plusoumoins:

    def supprimercontenu(self): # permet de supprimer tout le contenu d'une fenetre
        for contenu in self.fenetre.winfo_children():
            contenu.destroy()

    def new_pom(self):
        self.reponse = randint(0,100)
        print(self.reponse) # triche
        self.game = False
        self.tentative = 0
        self.pom_principal()

    def set_taille(self):
        self.taille = tkfont.Font(size=30)
        self.taillebouton = tkfont.Font(size=20)

    def pom(self, essaie):
        self.tentative += 1
        self.game = True
        if self.reponse > int(essaie):
            self.info = "Trop petit"
        if self.reponse < int(essaie):
            self.info = "Trop grand"
        if self.reponse == int(essaie):
            self.pom_principal("victoire")

    def pom_principal(self, arg=0):
        self.supprimercontenu()

        titre = Label(self.fenetre, font=self.taille, text="PLUS OU MOINS")
        titre.place(x=90, y=10)

        if arg == "victoire":

            victory = Label(self.fenetre, text="Victoire en "+str(self.tentative)+" coups !", font=self.taillebouton)
            victory.place(x=120, y=80)

            victory_button = Button(self.fenetre, text="Recommencer...", font=self.taillebouton, command=self.new_pom)
            victory_button.place(x=140, y=140)

            self.fenetre.mainloop()

        else:

            # Champs pour entrer le code
            self.champ_saisie = Entry(self.fenetre, font=self.taillebouton, justify="center")
            self.champ_saisie.place(x=100, y=70)
            self.champ_saisie.focus()

            # Appuyer sur ENTRER pour valider
            self.champ_saisie.bind("<Key>", self.touche_pom_recup)

            # Bouton valider
            valider = Button(self.fenetre, text="Valider", font=self.taillebouton, command=self.pom_verif)
            valider.place(x=195, y=127)

            # Affichage info
            if self.game == True:
                information = Label(self.fenetre, text=self.info, font=self.taillebouton)
                information.place(x=185, y=200)

            self.fenetre.mainloop()

    def touche_pom_recup(self, event):
        if event.keysym == "Return":
            self.pom_verif()

    def pom_verif(self):
        global reponse_user
        reponse_user = self.champ_saisie.get() # on récupère le contenu du champs de saisie
        self.pom(reponse_user)
        self.pom_principal()

    def start(self):
        self.fenetre = Tk()
        self.fenetre.title("Plus ou moins")
        self.fenetre.geometry("500x270")

        self.set_taille()

        self.new_pom()

if __name__ == '__main__':
    Plusoumoins().start()
