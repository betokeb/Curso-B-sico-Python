peso_mexicano = float(input("¿Cuántos pesos mexicanos tienes?: " ))
valor_dolar = 19.95
dolares = peso_mexicano / valor_dolar
dolares = round(dolares, 2)
print(f"Tienes ${dolares} dolares")

dolares = float(input("¿Cuantos dolares tienes?: "))
valor_peso_mexicano = .050
peso_mexicano = dolares / valor_peso_mexicano
peso_mexicano = round(peso_mexicano, 2)
print(f"Tienes ${peso_mexicano} pesos mexicanos.")

