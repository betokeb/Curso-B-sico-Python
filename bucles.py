# def run(): #la función principal
#     LIMITE = 1000 #Para definir constantes en una variable, lo que debemos hacer es escribir la variable en mayúsculas.

#     contador = 0 
#     potencia_2 = 2**contador
#     while potencia_2 < LIMITE:
#         print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#         contador = contador + 1 #estas dos lineas lo que hace es cerrar el bucle para que la función corte hasta donde esté el limite
#         potencia_2 = 2**contador 
# if __name__ == '__main__':
#     run()
 

    print('Adivina la letra secreta.\nTienes 5 intentos.')
    contador = 0
        
    while contador < 5: 
            letra = input('¿Cuál es la letra secreta?: ')
            contador+=1
            if letra == 'k':
                print('Le atinaste. La letra secreta es K.')
                break
            if contador == 5:
                print('Lo siento. Perdiste')



if __name__ == "__main__":
    run()