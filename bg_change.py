from tkinter import *
import random

root= Tk()
root.title("Background color change")
root.geometry("600x400")

dictionary = {"color":["maroon1","Lawn green","magenta1","magenta1","purple1","purple2","violet","springgreen1","springgreen2","chocolate1","cyan"]}

def bg_change():
    random_no = random.randint(0,10)
    print(dictionary["color"][random_no])
    root.configure(background = dictionary["color"][random_no])
    
btn = Button(root,text="Click to chang Bg Color!", command= bg_change)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()