import tkinter as tk
from tkinter import messagebox
class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        
    def calcular_total(self):
        return self.precio*self.cantidad
    
    
class FacturaApp:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Facturacion")
        self.productos=[]
        
        self.label_nombre=tk.Label(ventana,text="Nombre del producto")
        self.label_nombre.grid(row=0,column=0,padx=3,pady=3)
        
        self.entrada_nombre=tk.Entry(ventana)
        self.entrada_nombre.grid(row=0,column=1,padx=3,pady=3)
        
        self.label_precio=tk.Label(ventana,text="Precio")
        self.label_precio.grid(row=1,column=0,padx=3,pady=3)
        
        self.entrada_precio=tk.Entry(ventana)
        self.entrada_precio.grid(row=1,column=1,padx=3,pady=3)
        
        self.label_cantidad=tk.Label(ventana,text="Cantidad")
        self.label_cantidad.grid(row=2,column=0,padx=3,pady=3)
        
        self.entrada_cantidad=tk.Entry(ventana)
        self.entrada_cantidad.grid(row=2,column=1,padx=3,pady=3)
        
        self.button_agregar=tk.Button(ventana,text="Agregar Producto",command=self.agregar_producto)
        self.button_agregar.grid(row=3,column=0,columnspan=2,padx=3,pady=3)
        
        self.button_factura=tk.Button(ventana,text="Facturar",command=self.generar_factura)
        self.button_factura.grid(row=4,column=0,columnspan=2,padx=3,pady=3)
        
        self.label_factura=tk.Label(ventana,text="")
        self.label_factura.grid(row=5,column=0,columnspan=2,padx=3,pady=3)
        
        self.label_lista=tk.Label(ventana,text="")
        self.label_lista.grid(row=6,column=0,columnspan=2,padx=3,pady=3)
        
    
    def agregar_producto(self):
        #obtengo los datos de entrada
        nombre=self.entrada_nombre.get()
        precio=float(self.entrada_precio.get())
        cantidad=int(self.entrada_cantidad.get())
        #creando objeto producto con los datos de entrada
        producto=Producto(nombre,precio,cantidad)
        #agarro mi lista llamada self.productos declarada arriba y agrego metodo append
        #para agregar datos a mi lista
        self.productos.append(producto)
        messagebox.showinfo("Producto agregado","Producto agregado correctamente")
        #para borrar entradas limpiar
        self.entrada_nombre.delete(0,tk.END)
        self.entrada_precio.delete(0,tk.END)
        self.entrada_cantidad.delete(0,tk.END)
        
        #cadena_datos = f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}"
        #self.label_lista.config(text=cadena_datos)
        self.actualizar_productos()
        
    def actualizar_productos(self):
        
        
        # \n significa un espaciado hacia abajo o salto de linea despues de la palabra lista de productos
        #creacion de variable con una cadena 
        info_productos_titulo="Lista de productos:\n\n"
        #variable de tipo lista que almacena las variables de nombre precio y cantidad del objeto producto 
        #for lo usamos para recorrer la lista asi la mostrara y se actualizara cada vuelta del bucle
        # for producto significa que tomara el valor ddel objeto producto en la lista llamada self productos y lo recorrera
        info_productos = [f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}" for producto in self.productos]
        #join hace que todas las cadenas se junten en una sola tanto nombre precio y cantidad 
        #ademas convierte a los int en tipo cadena como lo son precio y cantidad
        texto_productos = "\n\n".join(info_productos)

        # Actualizar el texto del Label
        #
        self.label_lista.config(text=f"{info_productos_titulo}{texto_productos}")
    
    
    def generar_factura(self):
        #funcion que general el total de la factura suma de productos
        factura=0
        total=sum(producto.calcular_total() for producto in self.productos)
        #para visualizar la factura
        factura="Factura:\n\n"
        for producto in self.productos:
            factura += f"{producto.nombre}:${producto.precio} x {producto.
            cantidad} = ${producto.calcular_total()}\n"
       
        factura +="\n Total a pagar:$" + str(total)
        self.label_factura.config(text=factura)
        
        messagebox.showinfo("Calculo hecho mire el total de la factura","Factura impresa")
        
#creando ventana principal
#objeto ventanaprincipal que hereda de tkinter sus propiedades
# tengo que poner esto para que despues recien pueda heredar propiedades
# de la clase factura
ventanaprincipal=tk.Tk()
#objeto app que hereda los atributos de la clasee app y del objeto ventana principal
app= FacturaApp(ventanaprincipal)
ventanaprincipal.mainloop()

        
        