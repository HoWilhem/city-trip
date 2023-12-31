from tkinter import *
from city import *
import webbrowser




fenetre=Tk()
fenetre.geometry("500x500")
fenetre.title("Interface")
fenetre["bg"]="red"


def lancer():
    webbrowser.open("carte.html")
    fenetre.destroy()

bouton=Button(fenetre,text="Commencer",bg="black",fg="white",command=lancer)
bouton.pack()

fenetre.mainloop()


