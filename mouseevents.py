from tkinter import *

def doSomething(event):
    print("mouse coordinates: " + str(event.x)," "+str(event.y))
    
window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
window.bind("<Button-2>",doSomething) #mouse click
window.bind("<Button-3>",doSomething) #right mouse click
window.bind("<ButtonRealease>",doSomething)
window.bind("<Enter>",doSomething)
window.bind("<Leave>",doSomething)
window.bind("<Motion>",doSomething)
window.mainloop()



