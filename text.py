from tkinter import *


#Raiz
root=Tk()

texto=Text(root)
texto.pack()
texto.config(width=30,height=10, font=("Consolas",12),padx=10,pady=10, selectbackground="red")


#Fin
root.mainloop()