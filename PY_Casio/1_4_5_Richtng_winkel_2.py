#das ist nicht fuer TR 

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
    
    y1 = float(input("Gib die Anfangskoordinate Y ein: "))
    x1 = float(input("Gib die Anfangskoordinate X ein: "))
    y2 = float(input("Gib die Endkoordinate Y ein: "))
    x2 = float(input("Gib die Endkoordinate X ein: "))
    
    quadrant = int(input("In welchem Quadranten befindet sich der Endpunkt? (1/2/3/4): "))
    if quadrant not in [1, 2, 3, 4]:
        raise ValueError("Ungültiger Quadrant. Bitte 1, 2, 3 oder 4 eingeben.")
    
    dy = y2 - y1
    dx = x2 - x1
    
    richtungswinkel = berechne_richtungswinkel(dy, dx, quadrant)
    strecke = berechne_strecke(dy, dx)
    
    print("\nErgebnisse:")
    print(f"Richtungswinkel: {richtungswinkel:.2f} gon")
    print(f"Strecke: {strecke:.2f} Einheiten")
    
    print("\nVerwendete Formeln:")
    #print("Richtungswinkel = atan2(dy, dx) * 200 / pi + Anpassung je nach Quadrant")
    print("Richtungswinkel = arc tan (dy/dx) + Anpassung je nach Quadrant")
    print("Strecke = sqrt(dy^2 + dx^2)")

if __name__ == "__main__":
    main()

#probleme:
# 1. ist Formel gleiche wie in der Formel samelung?? 
#Richtungswinkel = atan2(dy, dx) * 200 / pi + Anpassung je nach Quadrant
# Die Ergibnisse ist gleich!! weswegen Formel ist gleiche. 
#es sollte in der lätzte Beschribung für
#Richtungswinkel = atan2(dy, dx) * 200 / pi + Anpassung je nach Quadrant
# korregieren nach:
#Richtungswinkel = arc tan (dy/dx) + Anpassung je nach Quadrant
#

#2. Probe Fehlt !!!
#3. eine Kurtze Version für TachenRechne Bildschrimsformat