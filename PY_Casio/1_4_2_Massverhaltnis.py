
#this is the example for test pythons script inside of casio fx-CG5
#thsi script writing with the AI:
def mass_stab():
    print("Berechnung Maßstab:")
    print("1: Maßstab M berechnen")
    print("2: Strecke in der Natur SN berechnen")
    print("3: Strecke auf der Karte SK berechnen")

    try:
        wahl = int(input("Wähle 1, 2 oder 3: "))

        if wahl == 1:  # Maßstab berechnen
            SN = float(input("Strecke in der Natur (SN): "))
            SK = float(input("Strecke auf der Karte (SK): "))
            if SK > 0:
                M = SN / SK
                print("Maßstab M ist 1:", M)
            else:
                print("Fehler: SK muss größer als 0 sein!")

        elif wahl == 2:  # Strecke in der Natur berechnen
            SK = float(input("Strecke auf der Karte (SK): "))
            M = float(input("Maßstab M (1:M): "))
            if M > 0:
                SN = SK * M
                print("Strecke in der Natur (SN):", SN)
            else:
                print("Fehler: Maßstab muss größer als 0 sein!")

        elif wahl == 3:  # Strecke auf der Karte berechnen
            SN = float(input("Strecke in der Natur (SN): "))
            M = float(input("Maßstab M (1:M): "))
            if M > 0:
                SK = SN / M
                print("Strecke auf der Karte (SK):", SK)
            else:
                print("Fehler: Maßstab muss größer als 0 sein!")

        else:
            print("Ungültige Auswahl. Wähle 1, 2 oder 3.")

    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein.")


# Testaufruf der Funktion
mass_stab()

#erste Fehler Kommt wegen der Buchstaben ß oder ss