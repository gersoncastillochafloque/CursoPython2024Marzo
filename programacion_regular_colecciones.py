"""
    Una collecion en Python es una estructura de datos que 
    me permite almacenar mas de un dato a la vez.
"""
producto="Televisor" 
precio=1200
igv=0.18

lista_productos=["televisor","computador","parlantes",200,20,10] #lista
#print(lista_productos[0])
#metodos de lista
#append (agrega un valor al final de la lista)
#lista_productos.append("Laptop")
#insert /agrega valor a la lista segun numero de posicion
#lista_productos.insert(2,"teclado")
#sobrepone elemento encima de otro
#lista_productos[2]="mouse"
#elimina elemento de la lista por su posicion
#lista_productos.pop(2)
#elimina el mismo dato por el nombre
#lista_productos.remove("parlantes")
#recorremos lista con for y con condicional

#for elemento in lista_productos: #desempaquetar
    #if elemento=="televisor":
        #continue #ignora el elemento
    #elif elemento==200:
        #break #interrumpe el bucle y se sale de el
    #else:
        #print(elemento)
#print(lista_productos)
#reemplazar de forma mutable la lista
#lista_productos[3] = 4000
#reemplazando por numero de indice en lista
lista_productos[2:4] =["coches", 20]
print(lista_productos)