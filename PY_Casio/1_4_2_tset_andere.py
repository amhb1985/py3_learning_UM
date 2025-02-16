
import casioplot

# Einfache Linie von (0,0) nach (127,63) zeichnen
for x in range(128):  # Bildschirmbreite: 128 Pixel
    y = int(x * 0.5)  # Linie mit Steigung 0.5
    casioplot.set_pixel(x, y, (0, 0, 0))  # Pixel setzen (schwarz)

# Bildschirm aktualisieren
casioplot.show()

#leider sie kann man nicht in der Spider IDE runnen. Vermütlich, wegen der Pacakage 