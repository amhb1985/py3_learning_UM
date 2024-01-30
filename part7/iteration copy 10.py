#we can change the colour of our imagae with this script:

#1- import package
import image


#2. inpuut the imagae
img = image.Image("luther.jpg")

#3.set imgage window and frame , 
win = image.ImageWin(img.getWidth(), img.getHeight())

#4. command to draw and delay time
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation


#5. use one Loop to regular command to changing the colours
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

#6. set the final image draw
img.draw(win)
win.exitonclick()
