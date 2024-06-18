import tkinter


# Funktion öffnet ein neues Fenster mit der Vorwärtskalkulation
def click_vorwärts():
    return

# Funktion öffnet ein neues Fenster mit der Rückwärtskalkulation
def click_rückwärts():
    return

# Funktion öffnet ein neues Fenster mit der Differenzkalkulation
def click_differenz():
    return

root = tkinter.Tk()
root.title("Angebotsrechner")

bu_vorwärts = tkinter.Button(root, text="Vorwärtskalkulation", command=click_vorwärts)
bu_rückwärts = tkinter.Button(root, text="Rückwärtskalkulation", command=click_rückwärts)
bu_differenz = tkinter.Button(root, text="Differenzskalkulation", command=click_differenz)

bu_vorwärts.grid(row=0, column=0, padx=5, pady=5)
bu_rückwärts.grid(row=0, column=1, padx=5, pady=5)
bu_differenz.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
