# Re Reflexión - ESTUDIAR!!

class Pelota:
    radio = 11

pelota_futbol_0 = Pelota()
print(pelota_futbol_0.radio)

pelota_futbol_A = Pelota()
print(pelota_futbol_A.radio)
pelota_futbol_A.radio = 13
print(pelota_futbol_A.radio)

Pelota.radio = 15
print(pelota_futbol_0.radio)
print(pelota_futbol_A.radio)


# getters y setters
#Concepto
class Pelota00:

    def __init__(self, radio):
        self.radio = radio
        self.volumen = (4*3.1415 * self.radio **3)/3
    

pelota_futbol_1 = Pelota00(11) # según FIFA
print("Radio: ", pelota_futbol_1.radio) # GET radio
print("Volumen: ", pelota_futbol_1.volumen)

pelota_futbol_1.radio = 13 # SET radio
print("Radio: ", pelota_futbol_1.radio)
print("Volumen: ", pelota_futbol_1.volumen)


#getters y setters en forma tradicional de otros lenguajes
class Pelota01:

    def __init__(self, radio):
        self.__radio = radio  # name mangling
        self.volumen = (4*3.1415 * self.__radio **3)/3

    def get_radio(self): # getter
        print("Radio se ha consultado!")
        return self.__radio
    
    def set_radio(self, radio): # setter
        self.__radio = radio
        self.volumen = (4*3.1415 * self.__radio **3)/3

pelota_futbol_B = Pelota01(11)

# Si trato de consultar la variable __radio ocurre error
try:
    print(pelota_futbol_B.__radio)
except Exception as e:
    print("ERROR:", e)
    print("No pude acceder a atributo __a porque está encapsulado, Use getters y setters por favor")

print("Valor del atributo encapsulado: ",   pelota_futbol_B.get_radio()  ) # forma de obtener dato encapsulado
print("Volumen: ",   pelota_futbol_B.volumen  )

# cambiar el atributo encapsulado
pelota_futbol_B.set_radio(100)
print("Valor del atributo encapsulado luego de modificar con set_radio(): ",   pelota_futbol_B.get_radio()  )
print("Volumen: ",   pelota_futbol_B.volumen  )


# Hasta aquí todo opera como esperado según otros lenguajes 
# Tenemos atributo privado
# Pero ...... Cuidado! porque... 

# EXPERIMENTOS INTERESANTES (UN PARENTESIS)
# asigno una variable a la instancia que le llamo __radio
pelota_futbol_B.__radio = 40
print(pelota_futbol_B.__radio) # pude setearlo porque creamos una variable de instancia __radio en esta línea
print(pelota_futbol_B._Pelota01__radio) # este es el nombre con el que Python escondió la variable encapsulada
pelota_futbol_B._Pelota01__radio = 0
print(pelota_futbol_B._Pelota01__radio) # El dato sí se puede acceder pero está escondido en otro nombre
###################################################################


# GETTERS Y SETTERS EN ESTILO PYTHONICO
class Pelota02:

    def __init__(self, radio):
        self.__radio = radio
        self.volumen = (4*3.1415 * self.__radio **3)/3
    
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        print("Setteando atributo encapsulado radio y calculando volument!!!")
        self.__radio = radio
        self.volumen = (4*3.1415 * self.__radio **3)/3

pelota_futbol_pythonica = Pelota02(11)

print("Valor del atributo encapsulado: ",   pelota_futbol_pythonica.radio  ) # forma de obtener dato encapsulado
print("Volumen: ",   pelota_futbol_pythonica.volumen  )

# cambiar el atributo encapsulado
pelota_futbol_pythonica.radio = 100
print("Valor del atributo encapsulado luego de modificar con .radio: ",   
                pelota_futbol_pythonica.radio  )
print("Volumen: ",   pelota_futbol_pythonica.volumen  )


# Composición , Interacción entre Objetos de distintas clases

class Financiera:

    def __init__(self, nombre, rut, saldo_institucional, direccion):
        self.nombre = nombre
        self.id = id
        self.saldo_institucional = saldo_institucional
        self.__direccion = direccion
        self.__clientes = []
        self.__numero_de_consultas = 0

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def clientes(self):
        print("Atención alguien está consultando la lista de Clientes!!!")
        self.__numero_de_consultas += 1
        return self.__clientes
    
    @property
    def numero_de_consultas(self):
        return self.__numero_de_consultas

    def agregar_clientes(self, *clientes):
        self.__clientes.extend(clientes)

    def eliminar_clientes(self, cliente):
        pass

    def transferir(self, monto, origen, destino):
        pass


class Cliente:

    def __init__(self, id, nombre, run, saldo):
        self.id = id
        self.nombre = nombre
        self.run = run
        self.saldo = saldo

    def depositar(self, monto):
        pass

    def girar(self, monto):
        pass


cliente1 = Cliente(1, "Luis", "12.121.121-1", 20000000)
cliente2 = Cliente(2, "Cristian", "8.121.121-1", 30000000)
cliente3 = Cliente(3, "Alba", "17.111.111-1", 90000000)

financiera1 = Financiera("AwakelabFin", "96.232.343-3", 10000000000, "salvador 8")

financiera1.agregar_clientes(cliente1, cliente2, cliente3)

for n in range(40):
    for cliente in financiera1.clientes:
        print(cliente.id, cliente.nombre, cliente.run, cliente.saldo)

print(financiera1.numero_de_consultas)