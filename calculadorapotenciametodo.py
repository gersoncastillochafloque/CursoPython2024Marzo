def calculadorapotencia ():
    m= int(input("Introduce la base: "))
    n= int(input("Introduce la potencia a elevar: "))
    ## acumulador
    total=1
    for _ in range (n):
        total*= m
    return total

resultado =calculadorapotencia()
print("El resultado de la potencia es:", resultado)