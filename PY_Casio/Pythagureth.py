# for the Pytagureth inn der fx-CG50 calculator:
def pythagoras():
    print("Berechnen Δ Pythagoras:")
    print("1: Hypotenuse c")
    print("2: Kathete a kleine")
    print("3: Kathete b grosse")
    
    try:
        # Benutzerauswahl
        wahl = int(input("Waehle 1, 2, 3: "))

        if wahl == 1:  # Hypotenuse c berechnen
            a = float(input("a ist:"))
            b = float(input("b ist: "))
            c = (a * a + b * b) ** 0.5
            print("c2 = a2 + b2")
            print("Hypotenuse c:", c)

        elif wahl == 2:  # Kathete a berechnen
            c = float(input("c ist: "))
            b = float(input("b ist: "))
            if c > b:
                a = (c * c - b * b) ** 0.5
                print("a2  = c2 - b2")
                print("a ist:", a)
            else:
                print("Fehler: c muss grosser als b!")

        elif wahl == 3:  # Kathete b berechnen
            c = float(input("c ist: "))
            a = float(input("a ist: "))
            if c > a:
                b = (c * c - a * a) ** 0.5
                print("b2= c2 - a2")
                print("b ist:", b)
            else:
                print("Fehler:c muss grosser als a!")

        else:
            print("Ungueltige Auswahl.Waehle 1, 2 oder 3.")

    except ValueError:
        print("Fehler: Bitte gib eine gultige Zahl ein.")

pythagoras()

