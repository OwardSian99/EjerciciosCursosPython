
#Hoja de trabajo 1 - Oward Sian
#Creando la adivinanza
def juego(intento = 1):
	respuesta = input("¿De que color es la fruta que estoy pensado?  ")
	print("\n")
	if respuesta != "naranja":
		if intento < 3:
			print("Fallaste; intentalo de nuevo")
			intento +=1
			juego(intento)
		else:
			print("\nPerdiste")
	else:
		print("Ganaste")
juego()


#creando la serie de fibonacci
print("\n\n")
def fibonacci(n):
	if n < 0:
		print("El numero es menor a cero")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print("Ingrese un numero entero para calcular la serie de fibonacci")
y = int(input())
print("El resultado de la  serie de fibonacci es: ")
print(fibonacci(y))



#Creando el factorial
print("\n\n")
def factorial(n):
    if n >= 1:
        return n*factorial(n-1)
    else:
        return 1        


print("Ingrese un numero para calcular su factorial")
x = int(input())
print("El factorial es: ")
print(factorial(x))