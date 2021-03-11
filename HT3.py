#EJERCICIO 1
def descuento(precio, descuento):
   
    return precio - precio * descuento
    
    
def iva(precio,iva):

    return  precio + precio * 0.12

def canasta(producto, descontar):
    total = 0
    total2= 0
    for precio, descuento in producto.items():
        total = total +  descontar(precio, descuento)
    total2 = iva(total,iva)
    return total2

producto = {1000:0.05, 500:0.35, 100:0.15, 150:0.10, 230:0.18}

print('Total de compra (Con descuentos + IVA): ',canasta(producto , descuento))


#EJERCICIO 2

def funcionlista(funcion, list):
    lista = []
    for i in list:
        lista.append(funcion(i))
    return lista

def cuadrado(n):
    return n*n

print(funcionlista(cuadrado, [5,10,15,20,1,2,3,4,5]))