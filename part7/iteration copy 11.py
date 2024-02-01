#the Image Processing¶

'''
7.8.2

Image Objects:

Image(filename)
img = image.Image(“cy.png”)
Create an Image object from the file cy.png.

EmptyImage()
img = image.EmptyImage(100,200)
Create an Image object that has all “White” pixels

getWidth()
w = img.getWidth()
Return the width of the image in pixels.

getHeight()
h = img.getHeight()
Return the height of the image in pixels.

getPixel(col,row)
p = img.getPixel(35,86)
Return the pixel at column 35, row 86.

setPixel(col,row,p)
img.setPixel(100,50,mp)
Set the pixel at column 100, row 50 to be mp.
'''



#because of the bug we comand the import 
#import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())