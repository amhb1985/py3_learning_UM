
#this is the example for test pythons script inside of casio fx-CG5
#thsi script writing with the AI:
def mass_stab():
    print("Masstab_M")
    print("1: M berechnen?")
    print("2: Stre.Natur SN?")
    print("3: Stre.auf Karte SK?")

    try:
        wahl = int(input("Welche?1,2,3:"))

        if wahl == 1: #Masstab berechnen
            SN = float(input("Str.Natur(SN):"))
            SK = float(input("Str.auf_Karte(SK):"))
            if SK > 0:
                M = SN / SK
                print("MasStab_M ist 1:", M)
            else:
                print("Fehler:SK muss grosser als 0!")

        elif wahl == 2:  #Strecke in der Natur berechnen
            SK = float(input("Str.Karte(SK):"))
            M = float(input("Masstab_M ist (1:M): "))
            if M > 0:
                SN = SK * M
                print("Str.Natur(SN):", SN)
            else:
                print("Fehler:Masstab muss grosser als 0 !")

        elif wahl == 3:  #Strecke auf der Karte berechnen
            SN = float(input("Str.Natur(SN):"))
            M = float(input("MaasStab_M ist (1:M):"))
            if M > 0:
                SK = SN / M
                print("Str.Karte(SK):", SK)
            else:
                print("Fehler:MaasStab muss grosser als 0!")

        else:
            print("Ungultige Auswahl.Wahl 1,2,3.")

    except ValueError:
        print("Fehler:Bitte gib gultige Zahl ein.")


# Testaufruf der Funktion
mass_stab()

#ende

#P4: erste Fehler Kommt wegen der Buchstaben ß oder ss
#P5: so es sollte noch mal für micro py testen.
#P6: Das andere Problem lag auf dem klene Bildschrim von fx-CG50: weswgen muss zusammenfassn und möglischewrweise Scripten verkutzen.  