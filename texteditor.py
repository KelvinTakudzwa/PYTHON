import os
from tkinter import *
from tkinter import filedialog, colorchooser,font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="pick a color..or esle")
    text_area.config(fg=color[1])
def change_font():
    pass
def open_file():
    pass
def new_file():
    pass
def save_file():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def about():
    pass
def quit():
    pass

window = Tk()
window.title("text editor program")
file = None

window_height = 500
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Ariel")

font_size =StringVar(window)
font_size.set("25")
text_area = Text(window,font=(font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight = 1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame,text="color",command=change_color)
color_button.grid(row=0,column=0)

scroll_bar.pack(side=RIGHT,fill=y)
text_area.config(yacrollcommand = scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color",command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame,font_name,*font.families(),command=change_font)
font_box.grid(row=0,column=1)
window.mainloop()