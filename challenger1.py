"""
CREAR PROGRAMA PARA AUTOMATIZAR LA PLANILLA DE SUELDOS DE UNA EMPRESA 
1 SE DEBE TENER ALGUNOS EMPLEADOS YA REGISTRADOS EN DICCIONARIOS (3)
2 SE DEBE TENER LA POSIBILIDAD DE PODER INGRESAR NUEVOS EMPLEADOS
3 SE DEBE CALCULAR LA SUMA DE SUELDOS Y SE DEBE OBTENER EL PROMEDIO DEL MES

    
"""
#HACIENDO LA 1
#constante
pago_hora=20

#lista para almacenar mi diccionario
trabajadores=[
{"codigo":"Trabajador_01","ht":40}, #indice0
{"codigo":"Trabajador_02","ht":50}, #indice1
{"codigo":"Trabajador_03","ht":60}  #indice2
]
#HACIENDO LA 2
def registro_empleado(codigopar,horapar):
    nuevo_empleado = {
        "codigo":codigopar,
        "ht":horapar
    }
    trabajadores.append(nuevo_empleado)
    print(trabajadores)
    
#estos datos trabajador04 y 90 se almacenan en los parametros de
#registro de empleados que es mi lista trabajadores.

#HACIENDO LA 3
def listar_empleado():
    #try para evitar el error de convertir de sting a int se valida el codigo
    try:
        global pago_hora
        suma_sueldos=0
        #en empleado se guarda cada registro del diccionario
        for index,empleado in enumerate(trabajadores):#funcion enumerate devuelve indice de los valores
        #multiplicacion de constantes 40*20 en primer registro y asi sigue
            sueldo_trabajador=trabajadores[index]["ht"]*pago_hora
            suma_sueldos = suma_sueldos+sueldo_trabajador #en cada vuelta suma
        #return para que me devuelva un valor en especifico del metodo
        return f"La suma de los sueldos de mi plantilla es {suma_sueldos} y el promedio es {suma_sueldos/len (trabajadores)}" #len cuenta cantidad de elementos en la lista
    # exception captura el error y lo guarda en err 
    # para cuando eres programador y sale un error en tu codigo te avisa
    except Exception as err:
        print(f"Ocurrio un error {err}")


print(listar_empleado())
    
    
    
#registro_empleado("Trabajador_04",90)
#el while es para insertar varios registros a la vez
while True:
    try:
        codigo=input("Ingrese codigo:")
        ht=int(input("Ingrese las Horas Trabajadas:"))
        registro_empleado(codigo,ht)
        resp=input("¿desea continuar?")
        if resp=="n":
            break
    #si colocas err inyectado en corchetes el usuario vera el error
    except Exception as err:
        print(f"Ocurrio un error {err}")
    
    #mostrar datos en especifico
    #except ValueError:
        #print("Debes ingresar datos correctos")
    else:
        print(listar_empleado())










