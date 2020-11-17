
class Carroceria:
    
    def __init__(self, color, largo, ancho, alto):
        self.color = color
        self.largo = largo
        self.ancho = ancho
        self. alto = alto


# Auto "TIENE" una carrocería diamante negro
class Auto:

    def __init__(self, color, largo, 
                    ancho, alto, num_asientos, 
                    cilindraje, num_ruedas, combustible):
        self.num_asientos = num_asientos
        self.cilindraje = cilindraje
        self.num_ruedas = num_ruedas
        self.combustible = combustible
        self.carroceria = Carroceria(color, largo, ancho, alto)
        self.velocidad = 0

    def acelerar(self, cantidad):
        print("Acelerando")

    def frenar(self, cantidad):
        print("Frenando")

# bodega tiene una carrocería en este ejemplo pero con diamante blanco
class Bodega():

    def __init__(self, metros, ubicacion, rol):
        self.metros = metros
        self.ubicacion = ubicacion
        self.rol = rol
        self.elementos_almacenados = []

    def almacenar(self, elemento):
        self.elementos_almacenados.append(elemento)

auto_1 = Auto("rojo", 4, 1.8, 1.7, 5, 3800, 4, 95)
print(auto_1.carroceria.color)
carroceria_repuesto = Carroceria("Blanca", 4, 1.8, 1.7)
print(carroceria_repuesto.color)

bodega_1 = Bodega(1000, "avenida 10 de Julio", "12309-1234")
bodega_1.almacenar(carroceria_repuesto)
bodega_1.almacenar(auto_1)
for elemento in bodega_1.elementos_almacenados:
    print("Elemento almacenado:", elemento)

class AutodeCarreras(Auto):

    def __init__(self, num_alerones):
        super().__init__("negro", 3, 1.5, 1, 1, 7000, 4, 99)
        self.num_alerones = num_alerones

auto_de_carreras_1 = AutodeCarreras(2)
print("Tipo del auto de carreras: ", type(auto_de_carreras_1))
for elemento in dir(auto_de_carreras_1):
    print(elemento)

auto_de_carreras_1.acelerar(3)
auto_de_carreras_1.frenar(4)


class Dado():

    lados = 6

    def __init__(self, color):
        self.color = color

class Dados():

    def __init__(self, numero):
        self.componentes = self.armar_conjunto(numero)
    
    def armar_conjunto(self, numero):
        componentes = []
        for n in range(0,numero):
            componentes.append(Dado("blanco"))
        return componentes

conjunto_de_dados = Dados(9)
print(  conjunto_de_dados.componentes  )

class Dados02:
    def __init__(self):
        self.componentes = None

    def agregar_dados(self, *dados):
        self.componentes.extend(dados)

dado_1 = Dado("rojo")
dado_2 = Dado("amarillo")
dado_3 = Dado("verde")


conjunto_de_dados = Dados()
conjunto_de_dados.agregar_dados(dado_1, dado_2, dado_3)



