import time
import random


# STRINGS

'''
for n in range(0, 3):
    cadena_de_caracteres = input("Ingrese Texto: ")
    print("Estamos analizando su texto, por favor espere...")
    tiempo_espera = random.randint(4, 6)
    time.sleep(tiempo_espera)
    print("Su texto es muy interesante. Hemos aprendido mucho\n")
    time.sleep(2)
'''

string1 = "40.5"
numero1 = 10 

# operador + como concatenador
operador_forma1 = string1 + str(numero1)
print(operador_forma1)

# operador + como suma numérica
operador_forma2 = numero1 + float(string1)
print(operador_forma2)

# leer y operar numéricamente
numero_leido = float(input("Ingrese un número: "))
resultado = numero_leido + 10
print("La suma es: " + str(resultado))
print("La suma es: " + "resultado")

# segmentar strings
#obtener elementos desde dentro de un string
string2 = "Yo soy un string dos"
print("")
print("Extracción de elemento posición 5 de string " + string2 + " es " + string2[5])

print(string2[2:7])
print(string2[3:])
print(string2[:8])
print(string2[:])

# largo de un string
print(len(string2))

# iterar sobre strings
for letra in string2:
    print(letra)

# algunos métodos para strings
print(string2.upper())

# reemplazar
string_con_reemplazo = string2.replace("y", "XX")
print(string_con_reemplazo)
#ATENCION: El string no se puede modificar!
print(string2)
#no puedo reasignar elementos de un string
try:
    string2[5] = "F"
    print(string2)
except Exception as e:
    print("ERROR: ", e)
    print("Se ha producido un Error porque Strings no se pueden modificar")

# buscar en un string
print(string2.find("soy"))

# DICCIONARIOS

#lista_demo = []

diccionario1 = { "nombre": "Walter", "apellido": "Bastías", "edad": 20  }
print(diccionario1)

print(diccionario1["apellido"])

diccionario2 = {"nombres": ["Walter", "Carla", "Sofía"], 
                "apellidos": ["Bastías", "Moreno", "Díaz"],
                "edades": [20, 30, 40]}

print(diccionario2["nombres"])
print(diccionario2["nombres"][1])

diccionario3 = {"nombres": ["Walter", "Carla", "Sofía"], 
                "apellidos": ["Bastías", "Moreno", "Díaz"],
                "edades": [20, 30, 40],
                "datos": [{"direccion": "Av. Italia 453", "telefono": "5600000000", "rut": "00.000.000-0"},
                        {"direccion": "Av. eee 453", "telefono": "560033330", "rut": "00.000.033-0"},
                        {"direccion": "Av. rrrr 453", "telefono": "5604444000", "rut": "00.000.330-0"}
                        ] }

# obtener nombre, apellido, edad y telefono de Carla
print(diccionario3["nombres"][1], 
        diccionario3["apellidos"][1], 
        diccionario3["edades"][1], 
        diccionario3["datos"][1]["telefono"])

# ejemplo de estadísticas de conteo de palabras en un texto

#conteos = {}
conteos = dict()
linea = input("Ingrese un Texto:\n ")
palabras = linea.split() # lista de palabras
print("Palabras: ", palabras)
print("Contando palabras...")
time.sleep(5)
for palabra in palabras:
    conteos[palabra] = conteos.get(palabra, 0) + 1
print(conteos)

