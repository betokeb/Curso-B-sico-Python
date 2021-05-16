# def saludar(nombre): #funcion que incluye a una variable. A este se le llama parámetro.
# 			print ("Hola " + nombre + ".")
# 			print ("¿Cómo estas")

# saludar("Alberto")

def saludar(nombre, apellido, empresa = "Banco XYZ"):
    print("Hola, " + nombre + " " + apellido + ".")
    print("Bienvenido a " + empresa + ".")
    print("¡Es un gusto volver a verte!")

#Argumentos por defecto
saludar("Roberto", "González", "Banco ABC" )