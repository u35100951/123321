from tkinter import *
from PIL import Image, ImageTk
win=Tk()
win.title("期末專題")
win.geometry("300x300+800+400")

img=Image.open('6.jpg')
tkimg = ImageTk.PhotoImage(img)

l1 = Label(win, image=tkimg)
l1.pack()



win.mainloop()