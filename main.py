import requests

print("hola mundo")

lista = []

for i in range(1, 101):
    lista.append(i)

print(lista)
print("Nadie dice nada")


def suma(a,b):
    return a+b

tupla_ejemplo = ('Carla', 'F')
print(tupla_ejemplo)

lista = [10, "Hola", 40, "Este es otro texto", (3,4), [1,2,3,4,5], suma]
funcion_suma = lista[6]
print(funcion_suma(2,4))

# agrega al final otro elemento exótico a la lista
lista.append(requests)

print(lista)

# inserto en posición específica un nuevo elemento
lista.insert(1, "Nuevo elemento insertado")
print(lista)


# for e if en base a listas

amigos = [('Carla', 'F', 34, 3, 4, 5, 6, 7), 
            ('José', 'M', 33, 3, 4, 5, 6, 7), 
            ('Pedro', 'M', 18, 3, 4, 5, 6, 7),
            ('Sergio', 'M', 12, 3, 4, 5, 6, 7), 
            ('Rodrigo', 'M', 23, 3, 4, 5, 6, 7), 
            ('Francisca', 'F', 34, 3, 4, 5, 6, 7),
            ('Gorka', 'M', 90, 3, 4, 5, 6, 7), 
            ('Felipe', 'NB', 80, 3, 4, 5, 6, 7), 
            ('Julia', 'TS', 40, 3, 4, 5, 6, 7),
            ('Giovanna', 'M', 20, 3, 4, 5, 6, 7)]

for estructura_amigo in amigos:
    if estructura_amigo[1] == 'M':
        termino = 'o'
    elif estructura_amigo[1] == 'F':
        termino = 'a'
    else:
        termino = 'ue'
    print('Hola amig' + termino + ' ' 
            + estructura_amigo[0] + ' tienes ' 
            + str(estructura_amigo[2]) + ' años')


# for e if en base a diccionarios
amigos_2 = { 'a': {'nombre': 'Carla', 'genero': 'F', 'edad': 34}, 
            'b': {'nombre': 'José', 'genero': 'M', 'edad': 33},
            'c': {'nombre': 'Pedro', 'genero': 'M', 'edad': 18},
            }

print(amigos_2['c'])
print(amigos_2['c']['nombre'])


# ejemplo de notas

notas = [3.5, 4.0, 5, 6.7, 7, 3.4, 5.5]

acumulador = 0
contador = 0
for nota in notas:
    acumulador = acumulador + nota
    contador = contador + 1

promedio = acumulador / contador
print(acumulador, contador)
print(str.format('El promedio es: {:.2f}', float(promedio)))
print('El promedio es: ' + str(round(promedio, 2)))
print('El promedio es:', round(promedio, 2))

