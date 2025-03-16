
import math

def bestimme_quadrant(dy, dx):
    if dx > 0 and dy >= 0:
        return 1, 0  # 1. Quadrant, kein Offset
    elif dx <= 0 and dy > 0:
        return 2, 200  # 2. Quadrant, +200 gon
    elif dx < 0 and dy <= 0:
        return 3, 200  # 3. Quadrant, +200 gon
    elif dx >= 0 and dy < 0:
        return 4, 400  # 4. Quadrant, +400 gon

def berechne_richtungswinkel(dy, dx, offset):
    grundwinkel = math.atan2(dy, dx) * 200 / math.pi  # atan2 direkt verwenden
    richtungswinkel = grundwinkel + offset
    return richtungswinkel % 400  # Sicherstellen, dass der Winkel zwischen 0-400 gon liegt

def berechne_strecke(dy, dx):
    return math.sqrt(dy**2 + dx**2)

def main():
    y1 = float(input("Gib die Anfangskoordinate Y ein: "))
    x1 = float(input("Gib die Anfangskoordinate X ein: "))
    y2 = float(input("Gib die Endkoordinate Y ein: "))
    x2 = float(input("Gib die Endkoordinate X ein: "))
    
    dy = y2 - y1
    dx = x2 - x1
    
    quadrant, offset = bestimme_quadrant(dy, dx)
    richtungswinkel = berechne_richtungswinkel(dy, dx, offset)
    strecke = berechne_strecke(dy, dx)
    
    print("\n--- Ergebnisse ---")
    print(f"Quadrant: {quadrant}")
    print(f"Richtungswinkel: {richtungswinkel:.2f} gon")
    print(f"Strecke: {strecke:.2f}")
    print("\n--- Formeln ---")
    print("Richtungswinkel = atan2(dy, dx) * 200 / π + Offset")
    print("Strecke = sqrt(dy² + dx²)")

main()

#test_01_ok...
#01 _problem: Mehr beschreibung

