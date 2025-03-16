import math

def berechne_richtungswinkel(dy, dx, quadranten):
    """ Berechnet den Richtungswinkel basierend auf dem Quadranten. """
    grundwinkel = math.atan2(dy, dx) * 200 / math.pi  # Umrechnung von Bogenmaß nach Gon
    
    if quadranten == 1:
        return grundwinkel  # Keine Anpassung nötig
    elif quadranten == 2:
        return grundwinkel + 200  # 2. Quadrant
    elif quadranten == 3:
        return grundwinkel + 200  # 3. Quadrant
    elif quadranten == 4:
        return grundwinkel + 400  # 4. Quadrant
    else:
        raise ValueError("Ungültiger Quadrant. Bitte 1, 2, 3 oder 4 eingeben.")

def berechne_strecke(dy, dx):
    """ Berechnet die Strecke zwischen den Punkten. """
    return math.sqrt(dy**2 + dx**2)

def main():
    print("Willkommen zum Koordinatenrechner!")
    
    # Vordefinierte Werte für Tests (anstelle von input, da input() nicht unterstützt wird)
    testwerte = [
        (1, 0, 0, 4, 3),  # Quadrant 1, Beispielkoordinaten
        (2, 0, 0, -4, 3), # Quadrant 2
        (3, 0, 0, -4, -3),# Quadrant 3
        (4, 0, 0, 4, -3)  # Quadrant 4
    ]
    
    for quadrant, y1, x1, y2, x2 in testwerte:
        print(f"\nTestfall: Quadrant {quadrant}, Start: ({y1}, {x1}), Ende: ({y2}, {x2})")
        
        dy = y2 - y1
        dx = x2 - x1
        
        richtungswinkel = berechne_richtungswinkel(dy, dx, quadrant)
        strecke = berechne_strecke(dy, dx)
        
        print("Ergebnisse:")
        print(f"Richtungswinkel: {richtungswinkel:.2f} gon")
        print(f"Strecke: {strecke:.2f} Einheiten")
        
        print("Verwendete Formeln:")
        print("Richtungswinkel = atan2(dy, dx) * 200 / pi + Anpassung je nach Quadrant")
        print("Strecke = sqrt(dy^2 + dx^2)")

if __name__ == "__main__":
    main()
