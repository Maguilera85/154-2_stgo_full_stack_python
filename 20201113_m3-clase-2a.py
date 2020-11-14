
# relexión/investigación experimental sobre atributos de clase y atributos de instancia
class SerVivo0():
    pass

print("dir de clase SerVivo0: ", dir(SerVivo0), " Tipo: ", type(SerVivo0))

ameba = SerVivo0()
print("dir de instancia ameba: ", dir(ameba), "Tipo: ", type(ameba))

# Definimos atributo de instancia
SerVivo0.altura = 20

# Creamos otros seres vivos de clase SerVivo0
protozoo = SerVivo0()
fungi = SerVivo0()

print(ameba.altura, protozoo.altura, fungi.altura)

# ameba asigna 5 a un atributo de instancia
ameba.altura = 5

print(ameba.altura, protozoo.altura, fungi.altura)

SerVivo0.altura = 20
# a pesar de asignar 20 a atributo de clase nuevamente, ameba conserva su valor de altura
# pues ya fué creado como atributo de instancia
print(ameba.altura, protozoo.altura, fungi.altura)


SerVivo0.altura = 60
print(ameba.altura, protozoo.altura, fungi.altura)

print(dir(ameba))

print("Atributos de instancia ameba: ", ameba.__dict__)
print("Busquemos el atributo de clase llamado altura dentro de ameba: ", ameba.__class__.__dict__)

SerVivo0.altura = 40

print("Atributos de instancia ameba: ", ameba.__dict__['altura'])
print("Busquemos el atributo de clase llamado altura dentro de ameba: ", ameba.__class__.__dict__['altura'])


# volvemos a  nuestra realidad del curso
# la última clase de Ser Vivo que habíamos creado fué:

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
yoda = SerVivo2(110, 7)


print(luke.color_pelo, leiah.color_pelo, yoda.color_pelo)
SerVivo2.color_pelo = "Rubio"
print(luke.color_pelo, leiah.color_pelo, yoda.color_pelo)

print(luke.peso, leiah.peso, yoda.peso)
SerVivo2.peso = 50
print(luke.peso, leiah.peso, yoda.peso)
print(SerVivo2.peso)

# sobrecarga de métodos con *args y con **kwargs

class Opciones: 
    opciones_predeterminadas = { 'port': 21, 
                        'host': 'localhost', 
                        'username': None, 
                        'password': None, 
                        'debug': False, }

    def __init__(self, **kwargs):
        self.opciones = dict(Opciones.opciones_predeterminadas)
        self.opciones.update(kwargs) 

    def __getitem__(self, key):
        print("Hola. Estás usando __getitem__()")
        return self.opciones[key]

opciones1 = Opciones(username="jperez", 
                        password="xxxx",
                        debug=True, 
                        apellido="Perez", 
                        direccion="los alamos 45")
print(dir(opciones1))
print(opciones1.opciones_predeterminadas)
print(opciones1.opciones)
print(opciones1.opciones['apellido'])

print(opciones1["apellido"])



'''
# tips para ejercicio de Financiera

class Cliente:
    
    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo
    
    def girar(self, monto):
        ###

    def abonar(self, monto):
        ### 
    
    def mostrar_saldo(self):
        ###

class Financiera:
    
    def __init__(self, nombre, id, saldo_institucional, clientes):
        self.nombre = nombre
        self.id = id
        self.saldo_institucional = saldo_institucional
        self.clientes = clientes
    
    def agregar_cliente(self):
        ##

    def eliminar_cliente(self):
        ##
    
    def transferir(self, desde_id, hacia_id, monto):
        #buscar clientes con los ids requeridos
        #reducir el saldo en el valor del monto  transferido desde cliente desde_id
        #aumentar el saldo en el valor del monto transferido a cliente hacia_id

    def giros_totales(self):
        ##

    def abonos_totales(self):
        ##

    def mostrar_saldo_institucional(self):
        ##


clientes = []
cliente1 = Cliente("Luisa Lain", 1, 3000000)
cliente2 = Cliente("Luis Lain", 2, 3000000)
cliente3 = Cliente("Superman", 3, 3000000)
cliente4 = Cliente("Superwoman", 4, 3000000)
clientes.append(cliente)

financiera1 = Financiera("FinDeSuFelicidad", 1, 1000000000, clientes)

'''