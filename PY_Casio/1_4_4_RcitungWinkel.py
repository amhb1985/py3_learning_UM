import math

def berechne_richtungswinkel(dY, dX, quadrant):
    t = math.atan2(dY, dX) * 200 / math.pi  
    if quadrant == 1:
        return t  
    elif quadrant == 2 or quadrant == 3:
        return t + 200  
    elif quadrant == 4:
        return t + 400  
    else:
        return None  

def berechne_strecke(dY, dX):
    return math.sqrt(dY * dY + dX * dX)

def main():
    try:
        y1 = float(input("Y (A): "))
        x1 = float(input("X (A): "))
        y2 = float(input("Y (E): "))
        x2 = float(input("X (E): "))
        
        quadrant = int(input("Quadrant (1-4): "))
        if quadrant not in [1, 2, 3, 4]:
            print("Fehler: Ungültiger Quadrant.")
            return
        
        dY = y2 - y1
        dX = x2 - x1
        
        t = berechne_richtungswinkel(dY, dX, quadrant)
        s = berechne_strecke(dY, dX)
        
        print("\nErgebnisse:")
        print("dY:", dY, "dX:", dX)
        print("t:", round(t, 2), "gon")
        print("s:", round(s, 2))
        
        print("\nFormeln:")
        print("t = arc tan (dY/dX) + Anpassung je nach Quadrant")
        print("s = sqrt(dY^2 + dX^2)")
    
    except ValueError:
        print("Fehler: Ungültige Eingabe.")

if __name__ == "__main__":
    main()
