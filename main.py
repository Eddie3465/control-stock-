from tkinter import *

root = Tk()

root.title("mi primera ventana")

root.geometry("400x400")

root.resizable(False,False)


def Ingresar():
    t1 = int(Cantidad.get())
    t2 = float(Precio.get())
    total = t1 * t2
    listaProductos.insert(END,"  Nom: "+nombre.get()+"   Cant: "+Cantidad.get()+"  Pres: "+Precio.get()+f"  Total: {round(total)}")
    nombre.delete(0,"end")
    Cantidad.delete(0,"end")
    Precio.delete(0,"end")

def Eliminar():
    listaProductos.delete(ANCHOR)



productos = Label(root,text="productos")
productos.pack()

listaProductos = Listbox(root,width=50,bd=2)
listaProductos.pack()


lbNombre = Label(root,text="Nombre: ").place(x=50,y=200)

lbCantidad = Label(root,text="Cantidad: ").place(x=50,y=240)

lbPrecio = Label(root,text="Precio: ").place(x=50,y=280)

#--------------------------------

nombre = Entry(root,bd=2)
nombre.place(x=120,y=200)

Cantidad = Entry(root,bd=2)
Cantidad.place(x=120,y=240)

Precio = Entry(root,bd=2)
Precio.place(x=120,y=280)

#--------------------------------

boton = Button(root,text="Ingresar",command = Ingresar)
boton.place(x=50,y=350)

boton1 = Button(root,text="Eliminar",command = Eliminar)
boton1.place(x=150,y=350)



root.mainloop()