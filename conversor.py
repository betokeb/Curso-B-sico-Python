
def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuantos pesos " + tipo_pesos + " tienes?: "))
    valor_dolar 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(f"Tienes ${dolares} dolares")    

menu = """ 
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')

