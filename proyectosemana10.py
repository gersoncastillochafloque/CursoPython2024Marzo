import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#Creacion clase producto con su constructor
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
 #creacion metodo calcular precio total       
    def calcular_total(self):
        return self.precio * self.cantidad
# creacion clase para mostrar interfaz grafica secundaria solo como prueba 
class ventanaSecundaria:
    def __init__(self, ventana_padre):
        self.ventana_secundaria = tk.Toplevel(ventana_padre)
        self.ventana_secundaria.title = ("Ventana secundaria")
        
        self.etiqueta = tk.Label(self.ventana_secundaria, text="widget de la ventana secundaria")
        self.etiqueta.pack(padx=10, pady=10)    
# creacion clase para ventana principal y widgets 
class FacturaApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Facturacion")
        self.productos = []
        
        self.label_nombre = tk.Label(ventana, text="Nombre del producto")
        self.label_nombre.grid(row=0, column=0, padx=3, pady=3)
        
        self.entrada_nombre = tk.Entry(ventana)
        self.entrada_nombre.grid(row=0, column=1, padx=3, pady=3)
        
        self.label_precio = tk.Label(ventana, text="Precio")
        self.label_precio.grid(row=1, column=0, padx=3, pady=3)
        
        self.entrada_precio = tk.Entry(ventana)
        self.entrada_precio.grid(row=1, column=1, padx=3, pady=3)
        
        self.label_cantidad = tk.Label(ventana, text="Cantidad")
        self.label_cantidad.grid(row=2, column=0, padx=3, pady=3)
        
        self.entrada_cantidad = tk.Entry(ventana)
        self.entrada_cantidad.grid(row=2, column=1, padx=3, pady=3)
        
        self.button_agregar = tk.Button(ventana, text="Agregar Producto", command=self.agregar_producto)
        self.button_agregar.grid(row=3, column=0, columnspan=2, padx=3, pady=3)
        
        self.button_factura = tk.Button(ventana, text="Facturar", command=self.generar_factura)
        self.button_factura.grid(row=4, column=0, columnspan=2, padx=3, pady=3)
        
        # Crear el Treeview para la lista de productos
        self.tree_productos = ttk.Treeview(ventana, columns=("Nombre", "Precio", "Cantidad"), show='headings')
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Cantidad", text="Cantidad")
        self.tree_productos.grid(row=5, column=0, columnspan=2, padx=3, pady=3)
        
        # Crear el Treeview para la factura
        self.tree_factura = ttk.Treeview(ventana, columns=("Nombre", "Precio", "Cantidad", "Total"), show='headings')
        self.tree_factura.heading("Nombre", text="Nombre")
        self.tree_factura.heading("Precio", text="Precio")
        self.tree_factura.heading("Cantidad", text="Cantidad")
        self.tree_factura.heading("Total", text="Total")
        self.tree_factura.grid(row=6, column=0, columnspan=2, padx=3, pady=3)

        self.botonventana = tk.Button(ventana, text="boton para ventana secundaria", command=self.abrir_ventana_secundaria)
        self.botonventana.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        
        self.button_imprimir = tk.Button(ventana, text="Imprimir PDF", command=self.imprimir_pdf)
        self.button_imprimir.grid(row=8, column=0, columnspan=2, padx=3, pady=3)
    #metodo para agregar producto
    def agregar_producto(self):
        #obtengo los datos de entrada
        nombre = self.entrada_nombre.get()
        precio = float(self.entrada_precio.get())
        cantidad = int(self.entrada_cantidad.get())
        #if precio is None or cantidad is None:
        #messagebox.showerror("Error","El precio y la cantidad deben ser numeros")
        #return
            
        #creando objeto producto con los datos de entrada
        producto = Producto(nombre, precio, cantidad)
        #agarro mi lista llamada self.productos declarada arriba y agrego metodo append
        #para agregar datos a mi lista
        # Insertar el producto en la posición correcta para mantener la lista ordenada por nombre
        index = 0
        while index < len(self.productos) and self.productos[index].nombre < producto.nombre:
            index += 1
        self.productos.insert(index, producto)
        
        messagebox.showinfo("Producto agregado", "Producto agregado correctamente")
        #para borrar entradas limpiar
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
        self.actualizar_productos()
        #cadena_datos = f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}"
        #self.label_lista.config(text=cadena_datos)
        #coloco el metodo actualizar productos para que lo haga despues de tocar el boton de agregar
    def actualizar_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        
        for producto in self.productos:
            self.tree_productos.insert("", "end", values=(producto.nombre, producto.precio, producto.cantidad))
    
    def generar_factura(self):
        for item in self.tree_factura.get_children():
            self.tree_factura.delete(item)
        
        total = sum(producto.calcular_total() for producto in self.productos)
        for producto in self.productos:
            self.tree_factura.insert("", "end", values=(producto.nombre, producto.precio, producto.cantidad, producto.calcular_total()))
        
        messagebox.showinfo("Calculo hecho mire el total de la factura", f"Total a pagar: ${total}")
    #metodo para imprimir pdf y formatos
    def imprimir_pdf(self):
        c = canvas.Canvas("factura.pdf", pagesize=letter)
        width, height = letter
        
        c.setFont("Helvetica", 12)
        c.drawString(30, height - 30, "Lista de Productos:")
        y = height - 50
        
        for producto in self.productos:
            c.drawString(30, y, f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
            y -= 20
        
        y -= 20  # Espacio extra antes de la factura
        
        c.drawString(30, y, "Factura:")
        y -= 20
        
        total = sum(producto.calcular_total() for producto in self.productos)
        for producto in self.productos:
            c.drawString(30, y, f"{producto.nombre} - Precio: {producto.precio} x Cantidad: {producto.cantidad} = Total: {producto.calcular_total()}")
            y -= 20
        
        c.drawString(30, y, f"Total a pagar: ${total}")
        
        c.save()
        messagebox.showinfo("PDF Generado", "El PDF se ha generado y guardado como factura.pdf")
    
    def abrir_ventana_secundaria(self):
        ventana_secundaria = ventanaSecundaria(self.ventana)
#creando ventana principal
#objeto ventanaprincipal que hereda de tkinter sus propiedades
# tengo que poner esto para que despues recien pueda heredar propiedades
# de la clase factura
ventanaprincipal = tk.Tk()
#objeto app que hereda los atributos de la clasee app y del objeto ventana principal
app = FacturaApp(ventanaprincipal)
ventanaprincipal.mainloop()

