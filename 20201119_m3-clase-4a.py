##############################################################################
# Herencia Simple
##############################################################################


print("\n"+79*"#")
class SerVivo00:
    print("Soy SerVivo00!")

class SerVivo01(SerVivo00):
    print("Soy SerVivo01!")

ser_vivo = SerVivo01()

print("\n"+79*"#")
class SerVivo00Mutacion01:
    print("Soy SerVivo00Mutacion01")

class SerVivo00Mutacion02:
    print("Soy SerVivo00Mutacion02")

class SerVivo02(SerVivo01, SerVivo00Mutacion02, SerVivo00Mutacion01):
    print("Soy SerVivo02")

ser_vivo_2 = SerVivo02()


print("\n"+79*"#")





exit()


class P:
    def __init__(self):
        self.a=0
        self.b=100
    
    def aumentar_a(self, cantidad):
        self.a += cantidad
        return self.a

    def disminuir_a(self, cantidad):
        self.a -= cantidad
        return self.a


class D(P):
    pass

objeto_p = D()

print(objeto_p.a)

print(objeto_p.aumentar_a(10))
print(objeto_p.disminuir_a(2))


##################################################


class Primera:

    def _init__(self):
        self.a = 10000
        self.otro = 20000

class P(Primera):
    def __init__(self):
        self.a=10
        self.b=20
    
    def aumentar_a(self, cantidad):
        self.a += cantidad
        return self.a

    def disminuir_a(self, cantidad):
        self.a -= cantidad
        return self.a

class Q(Primera):
    def __init__(self):
        self.a=100
        self.b=200
    
    def aumentar_a(self, cantidad):
        self.a += cantidad
        return self.a

    def disminuir_a(self, cantidad):
        self.a -= cantidad
        return self.a

class D(Q, P):
    pass

objeto_p = D()

print(objeto_p.a)

print(objeto_p.aumentar_a(10))
print(objeto_p.disminuir_a(2))
print(D.__mro__)





class P:
    def __init__(self, a_inicial, b_inicial):
        self.a=0
        self.b=100
    
    def aumentar_a(self, cantidad):
        self.a += cantidad
        return self.a

    def disminuir_a(self, cantidad):
        self.a -= cantidad
        return self.a


class D(P):
    pass

objeto_p = D()

print(objeto_p.a)

print(objeto_p.aumentar_a(10))
print(objeto_p.disminuir_a(2))


exit()


class CuentaBancaria:

    def __init__(self, numero, cliente, monto_inicial):
        self.numero = numero
        self.cliente = cliente
        self.monto_inicial
    
    def abonar(self, monto):
        self.monto += monto
        return self.monto

    def girar(self, monto):
        self.monto -= monto
        return self.monto


class CuentaAhorro(CuentaBancaria):
    de
    pass

class CuentaCorriente(CuentaBancaria):
    pass

c=CuentaAhorro()



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