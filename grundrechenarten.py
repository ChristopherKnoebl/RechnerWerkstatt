from tkinter import *
from tkinter import ttk
import random
random.seed()

# Erstelle tk root und gib dem ganzen einen Titel
class Hauptfenster(Tk):
    def __init__(self):
        super().__init__()

        # erstelle Naviations- und Auswahlframe
        self.frm_auswahl = Frame(self)
        self.frm_auswahl.pack()    
        Grundrechenarten(self.frm_auswahl)

class Grundrechenarten(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.anz_richtig = 0
        self.anz_falsch = 0
        self.anz_gesamt = 0
        self.rechenart = "Nicht gewählt"
#erstelle die widgets, auf die im weiteren zugegriffen wird

        self.label_auswahl = ttk.Label(master, text ="Ausgewählt wurde: ", width=40) #hier wird die Rechenart mit eingefügt (click_)
        self.entry_zahlbereich = ttk.Entry(master, width=20) # hier wird ein Eingabefeld erstellt, um den Zahlenbereich anzugeben
        self.entry_zahlbereich.grid(row=2, column=2)
        self.label_rechnung = ttk.Label(master, width=30) # hier wird die eigentliche Rechnung ausgegeben
        self.label_rechnung.grid(row=3, column=0, columnspan=2)
        self.entry_loesung = ttk.Entry(master, width=20) # hier wird ein Lösungsfeld erstellt,
        self.entry_loesung.grid(row=4, column=1)
        self.label_loes = ttk.Label(master, width=40) # hier wird die eigentliche Rechnung ausgegeben
        self.label_loes.grid(row=4, column=2, columnspan=2)
        self.label_richtig_falsch = Label(master, text=f"Du hast {self.anz_richtig} Aufgaben richtig gelöst", width=30)
        self.label_richtig_falsch.grid(row=5, column=0, columnspan=4)

        self.button_addition = ttk.Button(master, text="Addition", width=20, command= self.click_add)
        self.button_addition.grid(row=0, column=0)
        self.button_substraktion = ttk.Button(master, text="Subtraktion", width=20, command=self.click_sub)
        self.button_substraktion.grid(row=0, column=1)
        self.button_multiplikation = ttk.Button(master, text="Multiplikation", width=20, command=self.click_mul)
        self.button_multiplikation.grid(row=0, column=2)
        self.button_division = ttk.Button(master, text="Division", width=20, command=self.click_div)
        self.button_division.grid(row=0, column=3)
        self.button_berechnung = ttk.Button(master, text="Los Gehts", width=20, command=self.click_ber).grid(row=2, column=3)
        self.button_loesen = ttk.Button(master, text="Lösen Bitte", width=20, command=self.click_loes).grid(row=4, column=0)
        self.label_auswahl.grid(row=1, column=0, columnspan=2)
        self.label_zahlbereich = ttk.Label(master, text = "In welchem Bereich möchtest du Üben?").grid(row=2, column=0, columnspan=2)

# die globale Variable rechenart und das widget label_auswahl wird hier angepasst
    def click_add(self):
        self.rechenart = "Addition"
        self.label_auswahl["text"] = f"Ausgewählt wurde: {self.rechenart}"
        self.entry_zahlbereich.delete(0, 'end')
    def click_sub(self):
        self.rechenart = "Subtraktion"
        self.label_auswahl["text"] = f"Ausgewählt wurde: {self.rechenart}"
        self.entry_zahlbereich.delete(0, 'end')
    def click_mul(self):
        self.rechenart = "Multiplikation"
        self.label_auswahl["text"] = f"Ausgewählt wurde: {self.rechenart}"
        self.entry_zahlbereich.delete(0, 'end')
    def click_div(self):
        self.rechenart = "Division"
        self.label_auswahl["text"] = f"Ausgewählt wurde: {self.rechenart}"
        self.entry_zahlbereich.delete(0, 'end')

# die folgenden Methoden müssen noch in die Klasse eingefügt werden

    def click_ber(self):
        pass
    """
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
        """
    
    def click_loes():
        pass
    """
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

"""


    



# Main-Loop
if __name__ == "__main__":
    app = Hauptfenster()
    app.mainloop()

