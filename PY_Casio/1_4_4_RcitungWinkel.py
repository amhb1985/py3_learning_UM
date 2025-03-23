import math

def berechne_richtungswinkel(dY, dX):
    t = math.atan2(dY, dX) * 200 / math.pi
    if t < 0:
        t += 400
    return t

def berechne_strecke(dY, dX):
    return math.sqrt(dY * dY + dX * dX)

def main():
    print("Enter coordinates:")
    try:
        y1 = float(input("Y(A): "))
        x1 = float(input("X(A): "))
        y2 = float(input("Y(E): "))
        x2 = float(input("X(E): "))
        
        dY = y2 - y1
        dX = x2 - x1
        
        t = berechne_richtungswinkel(dY, dX)
        s = berechne_strecke(dY, dX)
        
        print("dY:", dY, "dX:", dX)
        print("t:", round(t, 2), "gon")
        print("s:", round(s, 2))
        print("in mPy : atan2(dY, dX) * 200 / pi")
        print("Richtungswinkel: arc tan(dY/dX) ")

        print("Strecke: sqrt(dY^2 + dX^2)")
    
    except:
        print("Error: Invalid input.")

main()

