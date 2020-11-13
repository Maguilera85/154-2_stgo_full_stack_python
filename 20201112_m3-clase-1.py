# clases y objetos

# seres vivos según nuestros aprendizajes actuales
altura_ser_vivo1 = 10
peso_ser_vivo1 = 20

altura_ser_vivo2 = 30
peso_ser_vivo2 = 50

def alimentarse(altura, peso):
    altura = altura + 1
    peso = peso + 2
    return altura, peso

altura_ser_vivo1, peso_ser_vivo1 = alimentarse(altura_ser_vivo1, peso_ser_vivo1)
print("Servivo 1: ", altura_ser_vivo1, peso_ser_vivo1)
altura_ser_vivo2, peso_ser_vivo2 = alimentarse(altura_ser_vivo2, peso_ser_vivo2)
print("Servivo 2: ", altura_ser_vivo2, peso_ser_vivo2)

# seres vivos con nueva forma de ver el mundo OOP Orientada a Objetos

class SerVivo:
    altura = 1
    peso = 2
    color_pelo = "Albino"

    def alimentarse(self, cantidad):
        self.altura = self.altura + 0.3 * cantidad
        self.peso = self.peso + 0.4 * cantidad

    
print(SerVivo)

neo = SerVivo()
trinity = SerVivo()
morfeo = SerVivo()

neo.alimentarse(20)
trinity.alimentarse(50)
morfeo.alimentarse(10)

print("Neo Peso: ", neo.peso, " Altura:", neo.altura, "Pelo: ", neo.color_pelo)
print("Trinity Peso: ", trinity.peso, " Altura:", trinity.altura, "Pelo: ", trinity.color_pelo)
print("Morfeo Peso: ", morfeo.peso, " Altura:", morfeo.altura, "Pelo: ", morfeo.color_pelo)

print(   dir(neo)   )



class SerVivo2(object):
    color_pelo = "Albino"

    def __init__(self, altura, peso):
        #la creación del objeto en detalle ya está implementada en 
        #python, por lo tanto con init solo inicializamos atributos
        #para la creación del objeto
        self.altura = altura
        self.peso = peso

    def alimentarse(self, cantidad):
        self.altura = self.altura + 0.3 * cantidad
        self.peso = self.peso + 0.4 * cantidad

    def __del__(self):
        #como matar un objeto ya está implementado en python
        #Solo le agregamos que nos informe que ha muerto
        print("Ha muerto con:", self.altura, "y ", self. peso)



luke = SerVivo2(170, 80)
leiah = SerVivo2(165, 70)
yoda = SerVivo2(110, 70)

luke.alimentarse(30)
leiah.alimentarse(40)
yoda.alimentarse(60)

print("Luke Peso: ", luke.peso, " Altura:", luke.altura, "Pelo: ", luke.color_pelo)
print("Leiah Peso: ", leiah.peso, " Altura:", leiah.altura, "Pelo: ", leiah.color_pelo)
print("Yoda Peso: ", yoda.peso, " Altura:", yoda.altura, "Pelo: ", yoda.color_pelo)


class Contador:

    def __init__(self):
        self.valor = 0
    
    def incrementar(self):
        self.valor += 1
    
    def decrementar(self):
        self.valor = self.valor -1

    def __del__(self):
        print("He muerto")


contador1 = Contador()
contador2 = Contador()

contador1.incrementar()
contador1.incrementar()
contador1.incrementar()

contador2.decrementar()

print(contador1.valor)
print(contador2.valor)


del(contador1)
