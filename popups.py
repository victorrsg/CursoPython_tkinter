from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog

def test():
    fichero = FileDialog.asksaveasfile(
            title="Guardar un fichero", mode='w', defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()

    # MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

    # MessageBox.showwarning("Alerta", "Sección sólo para administradores.")

    # MessageBox.showerror("Error",  "Ha ocurrido un error inesperado.")

    # resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea salir sin guardar?")
    # if resultado == "yes":
        # root.destroy()  # Destruir, alternativa a quit """

"""   file = FileDialog.askopenfilename(
    initialdir="C:", 
    filetypes=(
        ("Ficheros de texto", "*.txt"),     #Openfile
        ("Todos los ficheros","*.*")
    ), 
    title = "Abrir un fichero."
)  """

    

root = Tk()

Button(root, text = "Clícame", command=test).pack()







root.mainloop()