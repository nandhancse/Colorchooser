from tkinter import*
from tkinter import colorchooser

def color():
    col =colorchooser.askcolor()
    print(col)
    hexcolor=col[1]
    print(hexcolor)
    window.config(bg=hexcolor)


window =Tk()
window.geometry("300x300")

button = Button(window,text='Click for colors',font=('Impact',15),command=color)
button.pack()


window.mainloop()