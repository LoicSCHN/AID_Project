from pathlib import Path
import model
from algo import *
import os
from tkinter import *

#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("797x600")
window.configure(bg = "#272727")

#-----------FONCTIONS---------#

def generer():
    if entry_1.get("1.0",'end-1c') != "" :
        entry_1.delete("1.0",'end-1c')
        entry_2.delete("1.0",'end-1c')
        entry_4.delete("1.0",'end-1c')
        entry_5.delete("1.0",'end-1c')
        entry_6.delete("1.0",'end-1c')
        entry_7.delete("1.0",'end-1c')
        entry_8.delete("1.0",'end-1c')
        entry_9.delete("1.0",'end-1c')
    print(entry_3.get("1.0",'end-1c'))
    n = entry_3.get("1.0",'end-1c')
    os.system("python build/gen.py {}".format(n))
    launchAlgo()
    
def launchAlgo():
    print("algo")
    prefEtudiant = pd.read_csv("fichierEleves.csv", header=None, sep = ",").values.tolist() 
    prefEtablissement = pd.read_csv("fichierEtablissements.csv", header=None, sep = ",").values.tolist()
    
    entry_1.insert(END, prefEtudiant)
    entry_2.insert(INSERT, "Pref etablissement : ")
    entry_2.insert(END, prefEtablissement)
    res = attribution(len(prefEtudiant), prefEtudiant, prefEtablissement)
    entry_4.insert(INSERT, "Prio aux élèves : ")
    entry_4.insert(END, res)
    res2 = attribution(len(prefEtudiant), prefEtablissement, prefEtudiant)
    entry_5.insert(INSERT, "Prio aux etablissement : ")
    entry_5.insert(END, res2)
    affichageSatisfaction(prefEtudiant,prefEtablissement, res, res2 )

def affichageSatisfaction(prefEtudiant,prefEtablissement, res, res2 ):
    satEtuprioEta = etudiantSatisfaction(res2, prefEtudiant)  #Changer res pour la prio
    satEtaprioEta = etablissmentSatisfaction(res2, prefEtablissement)
    satEtuprioEtu = etudiantSatisfaction(res, prefEtudiant)
    satEtaprioEtu = etablissmentSatisfaction(res, prefEtablissement)
    entry_6.insert(INSERT, "eta : ")
    entry_6.insert(END, satEtaprioEta)
    entry_7.insert(INSERT, "etu : ")
    entry_7.insert(END, satEtuprioEta)
    entry_8.insert(INSERT, "eta : ")
    entry_8.insert(END, satEtaprioEtu)
    entry_9.insert(INSERT, "etu : ")
    entry_9.insert(END, satEtuprioEtu)
    return "OK"

#----------------INTERFACE---------------#
canvas = Canvas(
    window,
    bg = "#272727",
    height = 600,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)



canvas.create_text(
    70.0,
    30.0,
    anchor="nw",
    text="Nombre d’étudiant : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generer,
    relief="flat"
)
button_1.place(
    x=347.0,
    y=26.0,
    width=75.0,
    height=26.0
)

entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=231.0,
    y=30.0,
    width=101.0,
    height=18.0
)


#-----------RESULTATS---------------#

canvas.create_text(
    69.0,
    81.0,
    anchor="nw",
    text="Résultats",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    67.99053955078125,
    100.5,
    729.0094604492188,
    101.5,
    fill="#FFFFFF",
    outline="")
#----------------PREFERENCES (affichage)-----------#
canvas.create_text(
    70.0,
    120.0,
    anchor="nw",
    text="Préférences étudiant : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
)    

entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=69.0,
    y=150.0,
    width=307.0,
    height=100.0
)
canvas.create_text(
    422.0,
    120.0,
    anchor="nw",
    text="Préférences établissement : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
)   

entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=422.0,
    y=150.0,
    width=307.0,
    height=100.0
)

#----------------RESULTATS (affichage)-----------#

canvas.create_text(
    69.0,
    290.0,
    anchor="nw",
    text="Priorité aux établissements : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
) 
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=69.0,
    y=320.0,
    width=307.0,
    height=100.0
)
canvas.create_text(
    422.0,
    290.0,
    anchor="nw",
    text="Priorité aux élèves : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
)   
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=422.0,
    y=320.0,
    width=307.0,
    height=100.0
)

#------------ Satisfactions---------------#
#---PRIORITE ETABLISSEMENTS---#
canvas.create_text(
    69.0,
    440.0,
    anchor="nw",
    text="Satisfaction des établissements : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
) 
entry_6 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=69.0,
    y=465.0,
    width=307.0,
    height=30.0
)
canvas.create_text(
    69.0,
    505.0,
    anchor="nw",
    text="Satisfaction des élèves : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
)   
entry_7 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=69.0,
    y=530.0,
    width=307.0,
    height=30.0
)

#---PRIORITE ELEVES---#

canvas.create_text(
    422.0,
    440.0,
    anchor="nw",
    text="Satisfaction des établissements : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
) 
entry_8 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=422.0,
    y=465.0,
    width=307.0,
    height=30.0
)
canvas.create_text(
    422.0,
    505.0,
    anchor="nw",
    text="Satisfaction des élèves : ",
    fill="#FFFFFF",
    font=("Inter SemiBold", 14 * -1)
)   
entry_9 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=422.0,
    y=530.0,
    width=307.0,
    height=30.0
)



window.resizable(False, False)
window.mainloop()
