from tkinter import *


ventana = Tk()

ventana.title = "Texto caja grande"

ventana.geometry("100x100")

frame = Frame()


frame.pack()

scrollY = Scrollbar(frame)
scrollY.pack(side=RIGHT,fill=Y)
texto = Text(frame)
texto.config(width=50,height=50,bg="red")
texto.pack(expand=YES,fill=BOTH)
texto.insert(0.0,"Texto inicial")
texto.config(yscrollcommand=scrollY.set)
scrollY.config(command=texto.yview)
ventana.mainloop()