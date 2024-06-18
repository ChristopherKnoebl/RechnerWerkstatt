from tkinter import *
from tkinter import ttk
import random
random.seed()


# Erstelle tk root und gib dem ganzen einen Titel
root = Tk()
root.resizable(True, True)
root.title("Übe das Kopfrechnen")


anz_richtig = 0
anz_falsch = 0
anz_gesamt = 0
rechenart = "Nicht gewählt"
#erstelle die widgets, auf die im weiteren zugegriffen wird


label_auswahl = ttk.Label(root, text ="Ausgewählt wurde: ", width=40) #hier wird die Rechenart mit eingefügt (click_)
entry_zahlbereich = ttk.Entry(root, width=20) # hier wird ein Eingabefeld erstellt, um den Zahlenbereich anzugeben
entry_zahlbereich.grid(row=2, column=2)
label_rechnung = ttk.Label(root, width=30) # hier wird die eigentliche Rechnung ausgegeben
label_rechnung.grid(row=3, column=0, columnspan=2)
entry_loesung = ttk.Entry(root, width=20) # hier wird ein Lösungsfeld erstellt,
entry_loesung.grid(row=4, column=1)
label_loes = ttk.Label(root, width=40) # hier wird die eigentliche Rechnung ausgegeben
label_loes.grid(row=4, column=2, columnspan=2)
label_richtig_falsch = Label(root, text=f"Du hast {anz_richtig} Aufgaben richtig gelöst", width=30)
label_richtig_falsch.grid(row=5, column=0, columnspan=4)

# die globale Variable rechenart und das widget label_auswahl wird hier angepasst
def click_add():
    global rechenart
    rechenart = "Addition"
    label_auswahl["text"] = f"Ausgewählt wurde: {rechenart}"
    entry_zahlbereich.delete(0, 'end')
def click_sub():
    global rechenart
    rechenart = "Subtraktion"
    label_auswahl["text"] = f"Ausgewählt wurde: {rechenart}"
    entry_zahlbereich.delete(0, 'end')
def click_mul():
    global rechenart
    rechenart = "Multiplikation"
    label_auswahl["text"] = f"Ausgewählt wurde: {rechenart}"
    entry_zahlbereich.delete(0, 'end')
def click_div():
    global rechenart
    rechenart = "Division"
    label_auswahl["text"] = f"Ausgewählt wurde: {rechenart}"
    entry_zahlbereich.delete(0, 'end')

def click_ber():
    global a, b, c
    zahlbereich = int(entry_zahlbereich.get())
    a = random.randint(1,zahlbereich)
    b = random.randint(1, zahlbereich)

    if rechenart == "Addition":
        c = a + b
        label_rechnung["text"] = f"Die Aufgabe ist: {a} + {b}:"

    elif  rechenart == "Subtraktion":
        c = a - b
        label_rechnung["text"] = f"Die Aufgabe ist: {a} - {b}:"

    elif  rechenart == "Multiplikation":
        c = a * b
        label_rechnung["text"] = f"Die Aufgabe ist: {a} * {b}:"

    elif  rechenart == "Division":
        if b == 0:
            b = random.randint(1, zahlbereich)
        c = a / b
        label_rechnung["text"] = f"Die Aufgabe ist: {a} / {b}:"

    elif rechenart == "Nicht gewählt":
        label_rechnung["text"] = "Gib bitte eine Rechenart ein"
       # print(f"Die Aufgabe ist: {a} + {b}:")
       # vorschlag = int(input("Vorschlag? "))
#
       # def testen(vorschlag):
       #     if vorschlag == c:
       #         test = print(f"Richtig, das Ergebnis ist {c}")
       #         return test
       #     else:
       #         test = print("Hey, das Ergebnis ist leider nicht richtig")
       #         return testen(int(input("Neuer Vorschlag: ")))
   
def click_loes():
    global anz_richtig
    global anz_falsch
    global anz_gesamt
    loesung_user = int(entry_loesung.get())
    if loesung_user == c:
        label_loes["text"] = f"Richtig, das Ergebnis ist {c}"
        anz_richtig += 1
        anz_gesamt = anz_richtig + anz_falsch
        label_richtig_falsch["text"] = f"Du hast {anz_richtig} Aufgaben von {anz_gesamt} richtig gelöst"
        click_ber()
    else:
        label_loes["text"]= f"Hey, das Ergebnis ist leider nicht richtig"
        anz_falsch += 1
        anz_gesamt = anz_richtig + anz_falsch
        label_richtig_falsch["text"] = f"Du hast {anz_richtig} Aufgaben von {anz_gesamt} richtig gelöst"

        


button_addition = ttk.Button(root, text="Addition", width=20, command= click_add)
button_addition.grid(row=0, column=0)
button_substraktion = ttk.Button(root, text="Subtraktion", width=20, command=click_sub)
button_substraktion.grid(row=0, column=1)
button_multiplikation = ttk.Button(root, text="Multiplikation", width=20, command=click_mul)
button_multiplikation.grid(row=0, column=2)
button_division = ttk.Button(root, text="Division", width=20, command=click_div)
button_division.grid(row=0, column=3)
button_berechnung = ttk.Button(root, text="Los Gehts", width=20, command=click_ber).grid(row=2, column=3)
button_loesen = ttk.Button(root, text="Lösen Bitte", width=20, command=click_loes).grid(row=4, column=0)
label_auswahl.grid(row=1, column=0, columnspan=2)
label_zahlbereich = ttk.Label(root, text = "In welchem Bereich möchtest du Üben?").grid(row=2, column=0, columnspan=2)




root.mainloop()
