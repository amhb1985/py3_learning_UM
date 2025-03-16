import math

def berechne_richtungswinkel(dy, dx, quadranten):
    """ Berechnet den Richtungswinkel basierend auf dem Quadranten. """
    t = math.atan2(dy, dx) * 200 / math.pi  # Umrechnung von Bogenmaß nach Gon
    
    if quadranten == 1:
        return t  # Keine Anpassung nötig
    elif quadranten == 2:
        return t + 200  # 2. Quadrant
    elif quadranten == 3:
        return t + 200  # 3. Quadrant
    elif quadranten == 4:
        return t + 400  # 4. Quadrant
    else:
        raise ValueError("Ungültiger Quadrant. Bitte 1, 2, 3 oder 4 eingeben.")

def berechne_strecke(dy, dx):
    """ Berechnet die Strecke zwischen den Punkten. """
    return math.sqrt(dy**2 + dx**2)

def berechne_probe(y2, x2, y1, x1, t, s):
    """ Berechnet die Probe für die gegebenen Werte. """
    return (y2 + x2) - (y1 + x1) - (s * math.sqrt(2) * math.sin((t + 50) * math.pi / 200))

def main():
    print("Willkommen zum Koordinatenrechner!")
    
    y1 = float(input("Gib die Anfangskoordinate Y (A) ein: "))
    x1 = float(input("Gib die Anfangskoordinate X (A) ein: "))
    y2 = float(input("Gib die Endkoordinate Y (E) ein: "))
    x2 = float(input("Gib die Endkoordinate X (E) ein: "))
    
    quadrant = int(input("In welchem Quadranten befindet sich der Endpunkt? (1/2/3/4): "))
    if quadrant not in [1, 2, 3, 4]:
        raise ValueError("Ungültiger Quadrant. Bitte 1, 2, 3 oder 4 eingeben.")
    
    dy = y2 - y1
    dx = x2 - x1
    
    t = berechne_richtungswinkel(dy, dx, quadrant)
    s = berechne_strecke(dy, dx)
    probe = berechne_probe(y2, x2, y1, x1, t, s)
    
    print("\nErgebnisse:")
    print(f"Richtungswinkel t: {t:.2f} gon")
    print(f"Strecke s: {s:.2f} Einheiten")
    print(f"Probe: {probe:.2f}")
    
    print("\nVerwendete Formeln:")
    print("t = arc tan (dy/dx) + Anpassung je nach Quadrant")
    print("s = sqrt(dy^2 + dx^2)")
    print("Probe: (Y2 + X2) - (Y1 + X1) = s * sqrt(2) * sin(t + 50 gon)")

if __name__ == "__main__":
    main()



# Probe ist Falsch!