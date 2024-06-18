import tkinter
import random

# Funktion öffnet ein neues Fenster mit der Vorwärtskalkulation
def click_vorwärts():
    neues_fenster = tkinter.Toplevel()
    neues_fenster.title("Vorwärtskalkulation")
    neues_fenster.withdraw()
    
    # Erstellung der Variablen
    Fertigungsmaterial = round(random.uniform(500.00, 25000),2)
    Materialgemeinkostensatz = round(random.uniform(5.0, 20.0),2)
    Materialgemeinkosten = Fertigungsmaterial * (Materialgemeinkostensatz/100)
    Materialkosten = round(Fertigungsmaterial + Materialgemeinkosten,2)

    Fertigungslöhne = round(random.uniform(500.00, 25000),2)
    Fertigungsgemeinkostensatz = round(random.uniform(100, 200),2)
    Fertigungsgemeinkosten = Fertigungslöhne * (Fertigungsgemeinkostensatz /100)
    Fertigungskosten = Fertigungslöhne + round(Fertigungsgemeinkosten, 3)

    Herstellkosten = Materialkosten + Fertigungskosten

    Verwaltungsgemeinkostensatz =round(random.uniform(0.0, 15.0),2)
    Verwaltungsgemeinkosten = Herstellkosten * (Verwaltungsgemeinkostensatz/100)
    Vertriebsgemeinkostensatz = round(random.uniform(0.0, 25.0),2)
    Vertriebsgemeinkosten = Herstellkosten * (Vertriebsgemeinkostensatz/100)
    Selbstkosten = round(Herstellkosten + Verwaltungsgemeinkosten + Vertriebsgemeinkosten,3)

    Gewinnzuschlagssatz = round(random.uniform(8.0, 20.0),2)
    Gewinnzuschlag = Selbstkosten * round(Gewinnzuschlagssatz/100,3)
    Barverkaufspreis = round(Selbstkosten + Gewinnzuschlag,3)

    Kundenskontosatz = round(random.uniform(0, 4),2)
    Vertreterprovisionssatz = round(random.uniform(0, 8),2)
    Kundenskonto = round(Barverkaufspreis * Kundenskontosatz/ (100 - Kundenskontosatz - Vertreterprovisionssatz),3)
    Vertreterprovision = round(Barverkaufspreis * Vertreterprovisionssatz/(100 - Kundenskontosatz - Vertreterprovisionssatz), 3)
    Zielverkaufspreis = Barverkaufspreis + Kundenskonto + Vertreterprovision

    Kundenrabattsatz = round(random.uniform(8.0, 20.0),2)
    Kundenrabatt = round(Zielverkaufspreis * Kundenrabattsatz/(100-Kundenrabattsatz),3)
    Angebotspreis = round(Zielverkaufspreis + Kundenrabatt,3)

    UstSatz = 19
    Ust = Angebotspreis *UstSatz/100
    Angebotspreis_Brutto = round(Angebotspreis + Ust,2)

    # Definition zum Lösen
    def loese_rechnung():
        lb_materialgemeinkosten_wert["text"] = f"{Materialgemeinkosten:.2f} € "
        lb_materialkosten_wert["text"] = f"{Materialkosten:.2f} €"
        lb_fertigungsgemeinkosten_wert["text"] = f"{Fertigungsgemeinkosten:.2f} €"
        lb_fertigungskosten_wert["text"] = f"{Fertigungskosten:.2f} €"
        lb_herstellkosten_wert["text"] = f"{Herstellkosten:.2f} €"
        lb_verwaltungsgemeinkosten_wert["text"] = f"{Verwaltungsgemeinkosten:.2f} €"
        lb_vertriebsgemeinkostenwert["text"] = f"{Vertriebsgemeinkosten:.2f} €"
        lb_selbstkosten_wert["text"] = f"{Selbstkosten:.2f} €"
        lb_gewinnzuschlag_wert["text"] = f"{Gewinnzuschlag:.2f} €"
        lb_barverkaufspreis_wert["text"] = f"{Barverkaufspreis:.2f} €"
        lb_kundenskontowert["text"] = f"{Kundenskonto:.2f} €"
        lb_vertreterprovision_wert["text"] = f"{Vertreterprovision:.2f} €"
        lb_zielverkaufspreis_wert["text"] = f"{Zielverkaufspreis:.2f} €"
        lb_kundenrabatt_wert["text"] = f"{Kundenrabatt:.2f} €"
        lb_angebotspreis_wert["text"] = f"{Angebotspreis:.2f} €"
        lb_ust_wert["text"] = f"{Ust:.2f} €"
        lb_angebotspreis_brutto_wert["text"] = f"{Angebotspreis_Brutto:.2f} €"

    def nochmal():
        click_vorwärts()
        neues_fenster.destroy()

    # tk Fenster
    neues_fenster = tkinter.Tk()
    neues_fenster.title("Angebotsrechnung")

    # erstelle widgets
    lb_fertigungsmaterial = tkinter.Label(neues_fenster, text="   Fertigungsmaterial", anchor="w", width=20)
    lb_fertigungsmaterial_wert = tkinter.Label(neues_fenster, text=f"{Fertigungsmaterial:.2f} €")

    lb_materialgemeinkostensatz = tkinter.Label(neues_fenster, text=f"{Materialgemeinkostensatz} %")
    lb_materialgemeinkosten = tkinter.Label(neues_fenster, text="+ Materialgemeinkosten", anchor="w", width=20)
    lb_materialgemeinkosten_wert = tkinter.Label(neues_fenster, borderwidth=2, relief="sunken", width=10)

    lb_materialkosten = tkinter.Label(neues_fenster, text="= Materialkosten", anchor="w", width=20)
    lb_materialkosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_fertigungslöhne = tkinter.Label(neues_fenster, text="+ Fertigungslöhne", anchor="w", width=20)
    lb_fertigungslöhne_wert = tkinter.Label(neues_fenster, text=f"{Fertigungslöhne:.2f} €")

    lb_fertigungsgemeinkostensatz = tkinter.Label(neues_fenster, text=f"{Fertigungsgemeinkostensatz} %")
    lb_fertigungsgemeinkosten = tkinter.Label(neues_fenster, text="+ Fertigungsgemeinkosten", anchor="w", width=20)
    lb_fertigungsgemeinkosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_fertigungskosten = tkinter.Label(neues_fenster, text="= Fertigungskosten", anchor="w", width=20)
    lb_fertigungskosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_herstellkosten = tkinter.Label(neues_fenster, text="= Herstellkosten", anchor="w", width=20)
    lb_herstellkosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_verwaltungsgemeinkosten = tkinter.Label(neues_fenster, text="+ Verwaltungsgemeinkosten", anchor="w", width=20)
    lb_verwaltungsgemeinkostensatz = tkinter.Label(neues_fenster, text=f"{Verwaltungsgemeinkostensatz} %")
    lb_verwaltungsgemeinkosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_vertriebsgemeinkosten = tkinter.Label(neues_fenster, text="+ Vertriebsgemeinkosten", anchor="w", width=20)
    lb_vertriebsgemeinkostensatz = tkinter.Label(neues_fenster, text=f"{Vertriebsgemeinkostensatz} %")
    lb_vertriebsgemeinkostenwert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_selbstkosten = tkinter.Label(neues_fenster, text="= Selbstkosten", anchor="w", width=20)
    lb_selbstkosten_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_gewinnzuschlag = tkinter.Label(neues_fenster, text="+ Gewinnzuschlag", anchor="w", width=20)
    lb_gewinnzuschlagssatz = tkinter.Label(neues_fenster, text=f"{Gewinnzuschlagssatz} %")
    lb_gewinnzuschlag_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_barverkaufspreis = tkinter.Label(neues_fenster, text="= Barverkaufspreis", anchor="w", width=20)
    lb_barverkaufspreis_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_kundenskonto = tkinter.Label(neues_fenster, text="+ Kundenskonto", anchor="w", width=20)
    lb_kundenskonto_satz = tkinter.Label(neues_fenster, text=f"{Kundenskontosatz} %")
    lb_kundenskontowert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_vertreterprovision = tkinter.Label(neues_fenster, text="+ Vertreterprovision", anchor="w", width=20)
    lb_vertreterprovisionssatz = tkinter.Label(neues_fenster, text=f"{Vertreterprovisionssatz} %")
    lb_vertreterprovision_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_zielverkaufspreis = tkinter.Label(neues_fenster, text="= Zielverkaufspreis", anchor="w", width=20)
    lb_zielverkaufspreis_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_kundenrabatt = tkinter.Label(neues_fenster, text="+ Kundenrabatt", anchor="w", width=20)
    lb_kundenrabattssatz = tkinter.Label(neues_fenster, text=f"{Kundenrabattsatz} %")
    lb_kundenrabatt_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_angebotspreis = tkinter.Label(neues_fenster, text="= Angebotspreis (Listenpreis)", anchor="w", width=20)
    lb_angebotspreis_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_ust = tkinter.Label(neues_fenster, text="+ 19% ust", anchor="w", width=20)
    lb_ustsatz = tkinter.Label(neues_fenster, text=f"{UstSatz} %")
    lb_ust_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    lb_angebotspreis_brutto = tkinter.Label(neues_fenster, text="= Angebotspreis Brutto", anchor="w", width=20)
    lb_angebotspreis_brutto_wert = tkinter.Label(neues_fenster, relief="sunken", width=10)

    bu_loesen = tkinter.Button(neues_fenster, text="Lösen", command=loese_rechnung)
    bu_nochmal = tkinter.Button(neues_fenster, text="Neue Aufgabe", command=nochmal)

    # ordne widgets im fenster an
    lb_fertigungsmaterial.grid(row=0, column=0, padx=5, pady=5)
    lb_fertigungsmaterial_wert.grid(row=0, column=2, padx=5, pady=5)

    lb_materialgemeinkosten.grid(row=1, column=0, padx=5, pady=5)
    lb_materialgemeinkostensatz.grid(row=1, column=1, padx=5, pady=5)
    lb_materialgemeinkosten_wert.grid(row=1, column=2, padx=5, pady=5)

    lb_materialkosten.grid(row=2, column=0, padx=5, pady=5)
    lb_materialkosten_wert.grid(row=2, column=2, padx=5, pady=5)

    lb_fertigungslöhne.grid(row=3, column=0, padx=5, pady=5)
    lb_fertigungslöhne_wert.grid(row=3, column=2, padx=5, pady=5)

    lb_fertigungsgemeinkosten.grid(row=4, column=0, padx=5, pady=5)
    lb_fertigungsgemeinkostensatz.grid(row=4, column=1, padx=5, pady=5)
    lb_fertigungsgemeinkosten_wert.grid(row=4, column=2, padx=5, pady=5)

    lb_fertigungskosten.grid(row=5, column=0, padx=5, pady=5)
    lb_fertigungskosten_wert.grid(row=5, column=2, padx=5, pady=5)

    lb_herstellkosten.grid(row=6, column=0, padx=5, pady=5)
    lb_herstellkosten_wert.grid(row=6, column=2, padx=5, pady=5)

    lb_verwaltungsgemeinkosten.grid(row=7, column=0, padx=5, pady=5)
    lb_verwaltungsgemeinkostensatz.grid(row=7, column=1, padx=5, pady=5)
    lb_verwaltungsgemeinkosten_wert.grid(row=7, column=2, padx=5, pady=5)

    lb_vertriebsgemeinkosten.grid(row=8, column=0, padx=5, pady=5)
    lb_vertriebsgemeinkostensatz.grid(row=8, column=1, padx=5, pady=5)
    lb_vertriebsgemeinkostenwert.grid(row=8, column=2, padx=5, pady=5)

    lb_selbstkosten.grid(row=9, column=0, padx=5, pady=5)
    lb_selbstkosten_wert.grid(row=9, column=2, padx=5, pady=5)

    lb_gewinnzuschlag.grid(row=10, column=0, padx=5, pady=5)
    lb_gewinnzuschlagssatz.grid(row=10, column=1, padx=5, pady=5)
    lb_gewinnzuschlag_wert.grid(row=10, column=2, padx=5, pady=5)

    lb_barverkaufspreis.grid(row=11, column=0, padx=5, pady=5)
    lb_barverkaufspreis_wert.grid(row=11, column=2, padx=5, pady=5)

    lb_kundenskonto.grid(row=12, column=0, padx=5, pady=5)
    lb_kundenskonto_satz.grid(row=12, column=1, padx=5, pady=5)
    lb_kundenskontowert.grid(row=12, column=2, padx=5, pady=5)

    lb_vertreterprovision.grid(row=13, column=0, padx=5, pady=5)
    lb_vertreterprovisionssatz.grid(row=13, column=1, padx=5, pady=5)
    lb_vertreterprovision_wert.grid(row=13, column=2, padx=5, pady=5)

    lb_zielverkaufspreis.grid(row=14, column=0, padx=5, pady=5)
    lb_zielverkaufspreis_wert.grid(row=14, column=2, padx=5, pady=5)

    lb_kundenrabatt.grid(row=15, column=0, padx=5, pady=5)
    lb_kundenrabattssatz.grid(row=15, column=1, padx=5, pady=5)
    lb_kundenrabatt_wert.grid(row=15, column=2, padx=5, pady=5)

    lb_angebotspreis.grid(row=16, column=0, padx=5, pady=5)
    lb_angebotspreis_wert.grid(row=16, column=2, padx=5, pady=5)

    lb_ust.grid(row=17, column=0, padx=5, pady=5)
    lb_ustsatz.grid(row=17, column=1, padx=5, pady=5)
    lb_ust_wert.grid(row=17, column=2, padx=5, pady=5)

    lb_angebotspreis_brutto.grid(row=18, column=0, padx=5, pady=5)
    lb_angebotspreis_brutto_wert.grid(row=18, column=2, padx=5, pady=5)

    bu_loesen.grid(row=19, columnspan=2, padx=5, pady=5)
    bu_nochmal.grid(row=19, column=2, padx=5, pady=5)

    neues_fenster.mainloop()

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
