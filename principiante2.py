class Personaje:
    def __init__(self,nombre,edad,peso,estatura,vida):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.estatura=estatura
        self.vida=vida
    #si deseo tener los atributos sin modificar en gerson 10 5 1 solo pongo self
    def atributos(self):
        print(self.nombre)
        print(self.edad)
        print(self.peso)
        print(self.estatura)
    def powerup(self,edad,peso,estatura):
        self.edad=self.edad+edad
        self.peso=self.peso+peso
        self.estatura=self.estatura+estatura
    def esta_vivo(self):
        return self.edad>0
    # en lugar de traer un atributo como parametro trae un objeto y luego en el mismo metodo trae su parametro
    def daño(self,enemigo):
        return self.vida-enemigo.peso
#atributos que se agregan al metodo self init
goku=Personaje("Gerson",10,5,1,100)
vegeta=Personaje("Luis",10,5,3,1)
print(goku.daño(vegeta))
#metodo para imprimir
#print(goku.esta_vivo())
# goku.powerup(10,5,1)
# goku.atributos()