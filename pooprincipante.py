class Personaje:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
    # def esta_vivo(self):
    #     if self.vida>0:
    #         print("esta vivo")
    #     elif self.vida==0:
    #         print("esta muerto")
    # def daño (self, enemigo):
    #     #return siempre devuelve un valor del metodo y termina ejecucion
    #     return self.fuerza-enemigo.defensa
    def atributos(self):
        print(self.nombre)
        print(self.fuerza)
        print(self.inteligencia)
        print(self.defensa)
        print(self.vida)
        
    def esta_vivo(self):
        return self.vida > 0
        
    
    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")
        
    # def daño2(self, enemigo):
    #     resultado=self.fuerza-enemigo.defensa
    #     if resultado>5:
    #         print(f"el daño es grandisimo {resultado}")
    #         return resultado
    #     elif resultado<5:
    #         print(f"El daño es menor {resultado}")
    #         return resultado
    def daño(self, enemigo):
        # valoardaño=self.fuerza-enemigo.defensa
        # return valoardaño
        return self.fuerza-enemigo.defensa
    # metodo atacar definidio, self atraccion de atributos iniciados en objeto 1 llamado persona 1
    # enemigo es el objeto 2 ingresado como parametro
    # este metodo modifica la vida de persona 2
    def atacar(self,enemigo):
        #daño es una variable nueva almacena el return del metodo daño 4
        #llamando metodo daño en metodo atacar
        #recuerda para llamar a un metodo dentro de otro siempre envia los parametros
        daño=self.daño(enemigo)
        #obtiene el atributo enemigo.vida del objeto persona2 y realiza una resta dandole un nuevo valor
        # enemigo.vida recibe un nuevo valor y cambia porque le hicieron daño de 100 baja 4 a 96
        enemigo.vida=enemigo.vida-daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.nombre,"es", enemigo.vida, " esta vivo")
        else:
            enemigo.morir()

    
    

#nombre,fuerza.inteligencia.defensa.vida
persona1=Personaje("goku",10,1,5,100)
persona2=Personaje("Vegeta",8,1,3,10)
# persona1.morir()
# print(persona1.daño(persona2))
# persona1.daño2(persona2)
#llamando metodo atacar desde el objeto 1 persona 1 con parametro de otro objeto persona2
persona1.atacar(persona2)

