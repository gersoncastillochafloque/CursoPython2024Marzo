a, b = 0, 1
while a < 10:
    print(a)
   #primera vuelta
   #a = 0
   #b = 1
   #2vuelta
   # a = 1
   # b = 1 # a + b = 0 +1 anterior vuelta
   #3 vuelta
   # a = 1
   # b = 2
   #4 vuelta
   # a = 2
   # b = 3
   #5 vuelta
   # a = 3
   # b = 5
   #6 vuelta
   # a = 5
   # b = 8
   #7 vuelta
   # a = 8
   # b = 13
   # 8 vuelta
   # a = 13 se sale del bucle no cumple condicion
   
  
    a, b = b, a+b
    # a = b
    # b = a+b
    