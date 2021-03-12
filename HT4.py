#Ejercicio 1
frutas = {'platano':1.35, 'manzana': 0.80, 'pera':0.85, 'naranja': 0.70}
fruta = input("Que fruta desea: ").lower()
peso = float(input("¿Cuanto kilos desea? --->  "))

if fruta in frutas:
    print(peso, 'kilos de ', fruta, ' cuestan Q.', round( frutas[fruta]*peso, 2))
    print("---------------------------------------------------------------\n")
else:
    print("Ya no hay ", fruta," en existencia")
    print("---------------------------------------------------------------\n")
    


#EJERCICIO 2
def tablas(nume):
    archivo = open(f"tabla-{nume}.txt","w")
    for numero in range(1,11):
        archivo.write(f"{nume} * {numero} = {nume * numero}\n")
        print(f"{nume} * {numero} = {nume * numero}")
    archivo.close()

num = int(input("Ingrese le numero de la tabla( 1 - 10 ) ----->  "))
print(" ")
if num <= 0 or num > 10:
    print(f"El numero {num} no está dentro del rango (1 - 10)")
else:
    tablas(num)