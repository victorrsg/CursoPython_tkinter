
from cProfile import label
from tkinter import *
def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def multiplicar():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def dividir():
    r.set(float(n1.get()) / float(n2.get()))
    borrar()

def elevar():
    r.set(float(n1.get()) ** float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")
    

root=Tk()
root.config(bd=10)

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root,text="Número 1").pack()
Entry(root,justify="center", textvariable=n1).pack()
Label(root,text="Número 2").pack()
Entry(root,justify="center", textvariable=n2).pack()

Label(root,text="").pack()
Button(root,text="Sumar", command=sumar).pack()
Label(root,text="").pack()
Button(root,text="restar", command=restar).pack()
Label(root,text="").pack()
Button(root,text="multiplicar", command=multiplicar).pack()
Label(root,text="").pack()
Button(root,text="dividir", command=dividir).pack()
Label(root,text="").pack()
Button(root,text="elevar", command=elevar).pack()

Label(root,text="\nResultado").pack()
Entry(root,justify="center", textvariable=r, state="disabled").pack()






#Fin
root.mainloop()