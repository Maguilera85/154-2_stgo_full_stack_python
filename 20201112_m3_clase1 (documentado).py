# clases y objetos

# Ser vivo


altura_ser_vivo1 = 20
peso_ser_vivo1 = 30


altura_ser_vivo2 = 30
peso_ser_vivo2 = 40


def alimentarse(altura, peso):
    altura  = altura +2
    peso = peso + 3
    return altura, peso


altura_ser_vivo1, peso_ser_vivo1 = alimentarse(altura_ser_vivo1, peso_ser_vivo1)
print("Servivo 1 : ", altura_ser_vivo1, peso_ser_vivo1)

altura_ser_vivo2, peso_ser_vivo2 = alimentarse(altura_ser_vivo2, peso_ser_vivo2)
print("Servivo 2 : ", altura_ser_vivo2, peso_ser_vivo2)
    

    ## Programación con orientación a objetos (OOP in english y español == POO)


class SerVivo:

    ## datos iniciales del objeto:

    altura = 1 ##  Se llaman atributos
    peso = 2  ## van al inicio de la clase
    color_pelo = "Albino"
    # Mediante el uso de un metodo (verbo, acción, funcion, que haga algo, etc)
    # Los atributos son modificados y sus valores iniciales cambian
    
    
    def alimentarse(self,cantidad): 

        #  Con self nos referimos a que este será cambiado por el nombre
        #  que el objeto tenga

        self.altura = self.altura + 0.3 * cantidad #  para poder cambiar el valor de los 
        self.peso = self.peso + 0.4 * cantidad # atributos debemos primero mencionarlos
        # luego volver a mencionarlos y generar la operación que querramos
        # que haga.


    ## esto no instancia al objeto solo imprime a que tipo
print(SerVivo) ## de elemento pertenece

## en las siguientes lineas [neo = SerVivo()]
## Estamos instanciando o dandole "vida" al  objeto como tal

neo = SerVivo()  ## Le digo a tal cosa (neo en este caso) que es un ser vivo
trinity = SerVivo() ## mediante el uso de la clase SerVivo()
morfeo = SerVivo()

# Luego de ser creados podemos hacer que estos se alimenten 
# Utilizando el metodo creado dentro de la clase (alimentarse)

#### La forma de definir las cantidad de veces que quieres que se realice un metodo es:####

neo.alimentarse(20) ## De esta manera podemos realizar el método alimentarse de manera
trinity.alimentarse(15) ## eficiente sin tener que repetir la misma linea de comando
morfeo.alimentarse(10)## "n" veces, basta con agregar un valor entero.

## esto es logrado ya que ahora el metodo alimentarse recibe como parametro
## una cantidad en número, en caso contrario tendrian que utilizar la forma
## descrita más abajo.


## si te preguntas por que tira error en las lineas de abajo es debido
## a que esta esperando recibir un parametro numerico llamado cantidad.

########## este seria un forma casi rudimentaria para alimentar al objecto#########

neo.alimentarse() # En este proceso podemos apreciar
neo.alimentarse() # Como el objeto en cuestion se alimenta
neo.alimentarse() # mediante el uso del metodo alimentarse()

trinity.alimentarse()
trinity.alimentarse()
trinity.alimentarse()

morfeo.alimentarse()
morfeo.alimentarse()
morfeo.alimentarse()

## todo este proceso puede se mejorado
'''
        | |      | |          | |
        | |      | |          | |
        | |      | |          | |
        V V      V V          V V 
'''
## Después de la creación de los objetos 
## Esto es una manera arbitraría de hacer las modificaciones, se recomienda el uso de metodos
## los datos o atributos iniciales podemos modificarlos, Ejem: 
#morfeo.peso = 20
#morfeo.altura = 15


## a continuación daré inicio a la impresion de lo hecho anteriormente:
##  neo = SerVivo(), etc.

print("Neo peso: ", neo.peso, "Altura: ", neo.altura, "colo de pelo: ", neo.color_pelo ) 
print("Trinity peso: ", trinity.peso, "Altura: ", trinity.altura, "colo de pelo: ", trinity.color_pelo)
print("Morfeo peso: ", morfeo.peso, "Altura: ", morfeo.altura, "colo de pelo: ", morfeo.color_pelo)

### Recuerda que para imprimir alguno de los atributos, debes asociar a que 
### objeto te estas refieriendo ejem:  trinity(nombre del objeto).color_pelo(atributo)