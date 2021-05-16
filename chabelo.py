def run():
    print('Adivina la edad de Chabelo. Tienes tres intentos')
    EDAD_CHABELO = '86'
    contador = 0

    while contador < 3:
        edad = input('¿Cuántos años tiene Chabelo?: ')
        contador += 1
        if edad == EDAD_CHABELO:
            print('¡Felicidades cuatit@ Acertaste!\nGracias por participar.')               
            break
        if edad != EDAD_CHABELO:
            print('Fallaste cuatit@')
        if contador == 3:
            print('Ya no te quedan más intentos.\nGracias por participar.')







    # for i in range(6):
    #         if i == 5:
    #             print("Figaroooo")
    #             break
    #         print("Galileo")

    
#     contador = 0
#     while contador < 6:
#         print('Galileo')
#         contador += 1
#         if contador == 5:
#             break
#     print("Figaroooo")

if __name__ == '__main__':
    run()