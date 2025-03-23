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
    print("Koordinaten eingeben:")
    try:
        y1 = float(input("Y(A): "))
        x1 = float(input("X(A): "))
        y2 = float(input("Y(E): "))
        x2 = float(input("X(E): "))
        
        quadrant = int(input("Quadrant (1-4): "))
        if quadrant not in [1, 2, 3, 4]:
            print("Fehler: Quadrant ungültig.")
            return
        
        dY = y2 - y1
        dX = x2 - x1
        
        t = berechne_richtungswinkel(dY, dX, quadrant)
        s = berechne_strecke(dY, dX)
        
        print("dY:", dY, "dX:", dX)
        print("t:", round(t, 2), "gon")
        print("s:", round(s, 2))
    
    except:
        print("Fehler: Ungültige Eingabe.")

main()
#its running!!!
#aber Berechnen in der 2te und 3te Quadrant  ist Falsch!
#vermütlich für erste und 4 te Quadrant ist richtig.

#hat aber falche rechnen wegen der quadrant

#so wegen jedesmal Verninden TR, finde ich einen Online oder offline IDE für Micro Python:
#gibt es weniger Online-Emolatoren (da etwa älter ist)
#1.MicroPython WebREPL: https://micropython.org/webrepl/
#2.Online Python Compiler (repl.it):https://replit.com/

#für offline :
#MicroPython 1.9.4 für deine Plattform 
#so letz do it again
#

