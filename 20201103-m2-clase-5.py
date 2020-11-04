nombres = ['Juan', 'Rosa', 'Margarita', 'Raúl']

lista = [10, "Hola", 40, "Este es otro texto", (3,4), [1,2,3,4,5]]



# creación de lista
lista2 = []
for n in range(0,10):
    print("La lista actual es: ", lista2)
    try:
        numero = float(input("\nIngrese un número: "))
        lista2.append(numero)
    except Exception as e:
        print("Usted no ingresó un número, trate nuevamente!")
        continue

print("La lista final es: ", lista2)

# indexación de elementos
print("Elemento de índice 8: ", lista2[8])

# modificar la lista
lista2[8] = "Soy un reemplazante"
print("Elemento de índice 8 modificado: ", lista2)

# a diferencia de las tumplas que se comportan asi - genera Error
#tupla2 = tuple(lista2)
#print(tupla2)
#tupla2[8] = "Soy un reemplazante"

# largo de una lista
print("largo de la lista2 es: ", len(lista2))

# operación + en listas
lista3 = ["Nombre", "Apellido", "Edad", 4]
lista_suma = lista2 + lista3
print("lista2 + lista3: ", lista_suma)

# segmentando listas
#intervalos por ejemplo enteros [0, 100[

#todo es :
sublista = lista2[:]
print(sublista)

#hasta una posicion de elemento
sublista = lista2[:5]
print(sublista)

#desde una posicion de elemento
sublista = lista2[3:]
print(sublista)

#desde y hasta
sublista = lista2[3:7]
print(sublista)

# insertar elemento
lista2.insert(7, "Soy un aparecido")
print("Lista con inserción en posición 7", lista2)

# buscar elemento 5.0
num = 5.0
if num in lista2:
    print("Encontrado el numero: ", num)
    print("El indice es: ", lista2.index(num))
else:
    print("El numero no se encuentra")

# ordenar la lista
lista_numeros = [3,4,56,2,3,7,234, 345, 2345, 6531, 14]
lista_numeros.sort()
print(lista_numeros)
lista_numeros.sort(reverse=True)
print(lista_numeros)

# agregar múltiples elementos
lista_numeros = lista_numeros + [1,2,3,4,5]
print(lista_numeros)
lista_numeros.append([100, 200, 300, 400])
print(lista_numeros)

# eliminar elemento en posición específica
lista_numeros.pop(2)
print(lista_numeros)




