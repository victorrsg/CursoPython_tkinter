from pydoc import text
from tkinter import *
from tkinter import font
from turtle import left, width
from typing import TextIO

# configuración de la raíz
root= Tk()

# Variables dinámicas
texto=StringVar("Un nuevo texto")

# conf marco
frame=Frame(root,width=480,height=320)
frame.pack()

label=Label(frame,text="Hola")
#label.pack()
label.place(x=100,y=100)

label.config(bg="green",fg="blue", font=("Verdana",24))
label.config(textvariable=texto) 

"""
imagen=PhotoImage(file=".\imagen.gif")
Label(root,image=imagen,bd=0).pack(side="left")
"""

# Finalmente bucle de la app
root.mainloop()