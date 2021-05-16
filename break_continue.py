def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue #lo que está diciendo que a partir de 'continue' lo que está después no se va a ejecutar y pasas al siguiente valor
        print(contador)

    for i in range (10000):
        print(i)
        if i == 5678:
            break #palabra clave que detiene la función hasta que se cumpla el parametro. Corta el ciclo

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)



if __name__ == '__main__':
    run()
