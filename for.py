def run():
    # contador = 1
    # print(contador)
    # while contador < 1000:
    #     contador += 1 #una opción de "contador = contador + 1", es agregar antes del signo igual un "+"
    #     print(contador)


    # a = range (1000) #Es un rango, en este caso del 0 al 1000. Estamos convirtiendo este rango en una lista.
    # print(a)


    # for contador in range(1, 1001): #se lee: para el contador que va del rango del 1 al 1,001, la variable contador en el ciclo va a ir tomando los valores del rango. 
    #                             #En este caso se agrega 1,0001 por que la consola siempre toma un numero anterior del valor que pones.
    #     print(contador)


    # for i in range(10):
    #     print(11 * i)




    print("Tablas de multiplicar")
    tabla = int(input("Introduce la tabla de multiplicar que quieres ver: "))
    print(" ")
    print(f"La tabla del {tabla} es:")
    for contador in range(1, 11):
        resultado = tabla*contador
        print(f"{tabla} X {contador} = {resultado}")
        

if __name__ == "__main__":
    run()



