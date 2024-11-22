from tkinter import *
import time
#from PIL import ImageTk, Image

WIDTH = 500
HEIGHT = 500

xVelocity = 1
yVelocity =1
window =Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

backgroundimage =Image(file='me.jpg') # background pic
background = canvas.create_image(0,0,image=backgroundimage,anchor=NW)

photoimage =Image(file='me.jpg')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

imagewidth = photoimage.width()
imageheight = photoimage.height()
#img = ImageTk.PhotoImage(Image.open("me.jpg"))  
#l=Label(image=img)
#l.pack()

while True:
    coordiantes = canvas.coords(myimage)
    print(coordinates)
    if(coordiantes[0]>=(WIDTH-imagewidth) or coordiantes[0]<0):
        xVelocity = -xVelocity
    if(coordiantes[1]>=(WIDTH-imageheight) or coordiantes[1]<0):
        yVelocity = -yVelocity    
    canvas.move(myimage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
    


window.mainloop()