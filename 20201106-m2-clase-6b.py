import time

# ===================================================
# concenpto de decorators para funciones en python
#
#@complemento
#def alguna_funcion(a,b,c):
#    resultado = a + b + c
#    return resultado

#mejora funcion avance
def avance(n):
    for j in range(0,7):
        for i in range(0,n):
            time.sleep(0.02)
            print(".", end = "", flush = True)
    print("")


def empaquetar(fn):
    def fn_aumentada():
        fn()
        print("Empaquetando el producto")
        avance(5)
        print("El producto está lista para ser despachado!!!")
    return fn_aumentada

def potenciar_preparacion(fn):
    def fn_aumentada():
        fn()
        print("Agregando Crema")
        avance(6)
        print("Crema Agregada")
    return fn_aumentada


def producir_cafe():
    print("\nMoliendo, y mezclando café con agua")
    avance(6)
    print("Café terminado!\n")


def producir_postre():
    print("\nMezclando ingredientes para postre")
    avance(3)
    print("Horneando el postre")
    avance(4)
    print("Postre terminado\n")


#usando las funciones simples
producir_cafe()
producir_postre()

#modificando la funcion simple
producir_cafe_con_extra = potenciar_preparacion(producir_cafe)
producir_cafe_con_extra()

#otra forma de usar la funcion simple modificada con potenciar_preparacion
potenciar_preparacion(producir_cafe)()

#aplicando modificacion a la funcion con otro modificador (empaquetar)
#forma1
producir_cafe_empaquetado = empaquetar(producir_cafe)
producir_cafe_empaquetado()

#forma2
empaquetar(producir_cafe)()

#modificando funciones en cadena
producir_postre_con_crema_y_empaquetado = empaquetar(potenciar_preparacion(producir_cafe))
producir_postre_con_crema_y_empaquetado()


# ejemplo previo que hace lo mismo que el decorador que se explica a continuación
def producir_te():
    print("\nMoliendo, y mezclando té con agua")
    avance(6)
    print("Té terminado!\n")

producir_te = empaquetar(potenciar_preparacion(producir_te))
producir_te()

#introduccion de concepto de decorator
@empaquetar
@potenciar_preparacion
def producir_te():
    print("\nMoliendo, y mezclando té con agua")
    avance(6)
    print("Té terminado!\n")

producir_te() # usando la funcion decorada




# ===================================================
# ejemplo útil de decoradores para funciones en python
print("\n\nEjemplo Medición Tiempo de Ejecución con Decorator")
def medir_tiempo_ejecucion(fn):
    def fn_aumentada(*args):
        t0 = time.time()
        resultado_original = fn(args[0])
        t1 = time.time()
        tiempo_transcurrido = t1-t0
        return resultado_original, tiempo_transcurrido
    return fn_aumentada

@medir_tiempo_ejecucion
def sumador_lista(lista):
    acumulador = 0
    for elemento in lista:
        acumulador = acumulador + elemento
    return acumulador

@medir_tiempo_ejecucion
def crear_lista(arg):
    return list(arg)

lista1, tiempo_crear_lista = crear_lista(range(0,100000000))
print("Tiempo crear lista: ", tiempo_crear_lista)

suma, tiempo_sumador = sumador_lista(lista1)
print("Tiempo de sumador: ", tiempo_sumador)
print("La suma es: ", suma)
print("El tiempo total de ejecucion es: ", tiempo_sumador + tiempo_crear_lista)


