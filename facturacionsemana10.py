import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_total(self):
        return self.precio * self.cantidad

class ventanaSecundaria:
    def __init__(self, ventana_padre):
        self.ventana_secundaria = tk.Toplevel(ventana_padre)
        self.ventana_secundaria.title = ("Ventana secundaria")
        
        self.etiqueta = tk.Label(self.ventana_secundaria, text="widget de la ventana secundaria")
        self.etiqueta.pack(padx=10, pady=10)    
    
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
    
    def agregar_producto(self):
        nombre = self.entrada_nombre.get()
        precio = float(self.entrada_precio.get())
        cantidad = int(self.entrada_cantidad.get())
        
        producto = Producto(nombre, precio, cantidad)
        
        index = 0
        while index < len(self.productos) and self.productos[index].nombre < producto.nombre:
            index += 1
        self.productos.insert(index, producto)
        
        messagebox.showinfo("Producto agregado", "Producto agregado correctamente")
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
        self.actualizar_productos()
    
    def actualizar_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        
        for producto in self.productos:
            self.tree_productos.insert("", "end", values=(producto.nombre, producto.precio, producto.cantidad))
    
    def generar_factura(self):
        for item in self.tree_factura.get_children():
            self.tree_factura.delete(item)
        
        total = sum(producto.calcular_total() for producto in self.productos)
        factura = "Factura:\n\n"
        for producto in self.productos:
            self.tree_factura.insert("", "end", values=(producto.nombre, producto.precio, producto.cantidad, producto.calcular_total()))
        
        factura += "\nTotal a pagar: $" + str(total)
        messagebox.showinfo("Calculo hecho mire el total de la factura", factura)
        
    def abrir_ventana_secundaria(self):
        ventana_secundaria = ventanaSecundaria(self.ventana)

ventanaprincipal = tk.Tk()
app = FacturaApp(ventanaprincipal)
ventanaprincipal.mainloop()
