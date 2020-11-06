import modulos as mod 
import time

mod.play_me()

# 1 ==================================================================
# función simple con dos parámetros y con variable global
def sumador_de_dos_numeros(a, b):
    producto = a + b
    global nombre1 # hace visible nombre1 en el programa principal
    nombre1 = "Esteban"
    if producto == 40:
        return "Adivinaste el número secreto!!!"
    print("Imprime a desde la función: ", a)
    print("Imprime b desde la función: ", b)
    print("Imprime producto desde la función: ", producto)
    hora_actual = time.time()
    return producto, hora_actual, "XXXXXXXX" 

num1 = 30
num2 = 25

resultado, tiempo, texto = sumador_de_dos_numeros(num1, num2)
print("resultado: ", resultado, tiempo, texto)


try:
    print("num1: ", num1)
    print("nombre1: ", nombre1) # variable global definda dentro de función
    print("a: ", a) # variable local definda dentro de función
    print("b: ", b) # variable local definda dentro de función
    print("producto: ", producto) # variable local definda dentro de función
except Exception as e:
    print("ERROR: ", e)
    print("Alguno de estos prints arrojó un error")

# ==================================================================


# 2 ==================================================================
# función void

logo = """
   ##   #    #   ##   #    # ###### #        ##   #####  
  #  #  #    #  #  #  #   #  #      #       #  #  #    # 
 #    # #    # #    # ####   #####  #      #    # #####  
 ###### # ## # ###### #  #   #      #      ###### #    # 
 #    # ##  ## #    # #   #  #      #      #    # #    # 
 #    # #    # #    # #    # ###### ###### #    # ##### 
"""

def imprimir_logo(veces, texto):
    for n in range(0, veces):
        print(n, texto)
imprimir_logo(3, logo) # invocar a la función

def sumar():
    print(5 + 10)
sumar() # invocar la función

def tiempo_actual():
    print(time.time())
tiempo_actual() # invocar la función

# ==================================================================


# 3 ==================================================================
# funciones con parametros por defecto

# función estandar de python: print, sin redefinir sus parametros por defecto
print("Soy", "Programador", "Y", "soy", "feliz")

# función estandar de python redefiniendo sus parámetros por defecto
print("Soy", "Programador", sep="%", end="")
print("Otra Cosa")

# cómo definir función con parametros por defecto
def unir_textos(texto1, texto2, conector = " "):
    resultado = texto1 + conector + texto2
    calculo = 1.380649E-23*len(texto1)*len(texto2)
    return resultado, calculo

variable_a_imprimir, numero = unir_textos("Hola", "Mundo")
print(variable_a_imprimir, numero)

variable_a_imprimir, numero = unir_textos("Hola", "Mundo", conector = "&&&&")
print(variable_a_imprimir, numero)

variable_a_imprimir, numero = unir_textos("Hola", "Mundo", conector = "????")
print(variable_a_imprimir, numero)

# ==================================================================


# 4 ==================================================================
# función con argumentos múltiples no predefinidos

def sumar(nombre, apellido, *args):
    acumulador = 0
    print("Nombre", nombre)
    print("Apellido", apellido)
    for elemento in args:
        acumulador = acumulador + float(elemento)
    return acumulador

resultado_suma = sumar("Guido", "Van Rossum", 1, 2 ,3 ,6 ,4 ,8.9 ,3 ,34 ,23 , 34, 56)
print(resultado_suma)
print(sumar("a", "b"))

# 5 ==================================================================
# función con argumentos de cantidad indeterminada y especificados por nombre

def conjunto_de_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)
    return kwargs

lo_retornado = conjunto_de_datos(animal="elefante", planeta="tierra", galaxia="E4X2", agno="1920")
print(lo_retornado)

# ==================================================================

# 6 ==================================================================
# funciones como argumentos

def otra_funcion(numero):
    resultado = numero**2
    return resultado


def otra_funcion_mas(numero):
    resultado = numero + 100
    return resultado


def super_funcion(numero, otra_funcion):
    resultado = numero*10 + otra_funcion(numero)
    return resultado

super_resultado = super_funcion(40, otra_funcion)
print("Super Resultado 1: ", super_resultado)

super_resultado = super_funcion(40, otra_funcion_mas)
print("Super Resultado 2: ", super_resultado)

# ==================================================================