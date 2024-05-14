"""
    Una collecion en Python es una estructura de datos que 
    me permite almacenar mas de un dato a la vez.
    diccionario trabajan con claves para cada valor (key-value)
"""
mi_diccionario={}
mi_diccionario=dict() #constructor

mi_diccionario={
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Londres"
}
print(mi_diccionario["edad"])
#.items para saber clave y valor
for k,v in mi_diccionario.items():
    #unir cadenas con variables f=formato"cadena {variable}"
    print(f"La clave {k} y el valor es {v}")
