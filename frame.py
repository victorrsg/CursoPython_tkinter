from tkinter import *
from turtle import left, right, width

root= Tk() # Creación de raíz
root.title("Titulo de ventana")
root.resizable(1,1) # Redimensionar la ventana
root.iconbitmap('.\hola.ico')

# Hijo de root, no ocurre nada
frame = Frame(root, width=480,height=320)   

# Empaqueta el frame en la raíz

#frame.pack(side="left", anchor="e")     # Alinea a la izquierda el frame -- Anchor: e-> aliena al este w-> alinea al oeste...
frame.pack(fill="both", expand=1)
# Como no tenemos ningún elemento dentro del frame, 
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background
frame.config(bg="lightblue")     


frame.config(cursor="")         # Tipo de cursor
frame.config(relief="sunken")   # relieve del frame hundido
frame.config(bd=25)             # tamaño del borde en píxeles

root.config(bg="blue")          # color de fondo, background
root.config(cursor="pirate")    # tipo de cursor (arrow defecto)
root.config(relief="sunken")    # relieve del root 
root.config(bd=25)              # tamaño del borde en píxeles

#Abajo del todo
root.mainloop()
