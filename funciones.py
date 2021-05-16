# def imprimir_mensaje():
#     print('Mensaje especial:')
#     print('Estoy aprendiendo a usar funciones')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estas')
#     print(mensaje)
#     print('Adiós')


# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#      conversacion('Elegiste la opción 3')
# else:
#     print('Escribe la opción correcta')


def suma(a, b):
    print('se suman dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)


# def saludar():
#     print('Hola')
#     print('¿Cómo estas?')
#     print('¡Es un gusto volver a verte!')

# def despedir():
#     print('Espero que la hayas pasado bien')
#     print('Adiós')

# saludar()
# despedir()

################################


#La función mul_dos_suma_cinco() multiplica un número por dos y luego le suma cinco
# Como está escrita ahora mismo, el número que opera siempre es el número "3"

# def mul_x_suma_y(numero, x, y):
#     print(numero * x + y)

# mul_x_suma_y(100, 4, 22)

#Cambia la función para que, en vez de 3, opere cualquier número.
#Para esto, crea un parámetro que se llame "numero"
#Luego cambia el número "3" por la variable "numero"
#Luego, usa como argumento "100" al llamar la función
#Si en pantalla ves el número "205", ¡lo hiciste bien!


# def saludar(nombre="Usuario", apellido="Nuevo", empresa="Banco XYZ"):
#     print("Hola, " + nombre + " " + apellido + ".")
#     print("Bienvenido a " + empresa + ".")
#     print("¡Es un gusto volver a verte!")

# #Argumentos posicionales
# saludar("Andres", "Perez", "Banco ABC")

# #Argumentos de palabra clave (Keyword arguments)
# saludar(empresa="Banco DEF", apellido="Ruiz", nombre="Jose")

# #Argumentos por defecto
# saludar()


#Abajo tienes la función "crearHojaDeCalculo"
#La función toma como parámetro "nombre"
#Esta solo imprime que una Hoja de Cálculo se está creando

# def CrearHojadeCalculo(nombre, CantidadDeFilas=1000):
#     print("Creando una hoja de cálculo llamada " + nombre + " con " + str(CantidadDeFilas) + " filas.")

# CrearHojadeCalculo("Ahorros")
# CrearHojadeCalculo("Datos", CantidadDeFilas=10)

#Agrega un parámetro que se llame "cantidadDeFilas"
#Agrega por defecto el valor "1000" al parámetro "cantidadDeFilas"

#Cambia el print dentro de la función para que imprima lo siguiente:
#'Creando una hoja de cálculo llamada "nombre" con "cantidadDeFilas" filas'
#En "nombre" y "cantidadDeFilas", usar las variables correspondientes
#Recuerda concatenar y usar el método str() en la "cantidadDeFilas"

#Finalmente, llama la función con el nombre "Ahorros"
#Debería imprimir el texto:
#"Creando una hoja de cálculo llamada Ahorros con 1000 filas".

#Ahora llama la función con el nombre "Datos" y con 10 filas.
#Debería imprimir el texto:
#"Creando una hoja de cálculo llamada Datos con 10 filas".

# def multiplicar (a,b):
#     return a*b #Return: signfica que cuando yo esté en mi programa principal y llame a la funcion multiplicar con dos argumentos, significa que en este caso se va a multiplicar pero con return lo va a devolver en el programa principal

# resultado = multiplicar(10,5) + 5
# print(resultado)    



#La función "calcularEdad" calcula la edad de una persona
#Lo hace restando el año actual menos el año de nacimiento

# def calcularEdad(añoActual, añoDeNacimiento):
#     edad = añoActual - añoDeNacimiento
#     return edad

# miEdad = calcularEdad(2021,1990)
# edadDeMiAmigo = calcularEdad(2021, 1995)

# print("Tengo " + str(miEdad) + " años y mi mejor amigo tiene " + str(edadDeMiAmigo) + " años.")

#Agrega una línea en la función que devuelva la variable "edad"

#Luego, afuera de la función, llámala con el año actual y tu año de nacimiento
#Guarda el valor de llamar a esa función en la variable "miEdad"

#Vuelve a llamar la función con el año actual y el año de nacimiento de tu mejor amigo(a).
#Guarda el valor de llamar a esta función en la variable "edadDeMiAmigo"

#Imprime el siguiente texto:
#"Tengo X años y mi mejor amigo(a) tiene Y años."
#Donde X es tu edad guardada en la variable "miEdad"
#Donde Y es la edad de tu mejor amigo(a) en la variable "edadDeMiAmigo"