"""
Escribe un programa que permita:
a. Ingresar una lista de compras, con su precio individual y la suma total del costo de todos los
productos.
b. Ingresar una cantidad de participantes entre los cuales se va a dividir la compra.
c. Mostrar por pantalla lo que cada uno debe aportar.
"""

products = []
price = []

while True:
  products.append(input(f"Ingrese el producto a comprar: "))
  price.append(int(input(f"Ingrese el precio del producto: ")))
  
  while True:
    val = int(input(f"Desea seguir ingresando edades? \n 1. Si \n 2. No\n"))
    
    if val != 1 or val != 2:
      break  
    
    print("Ingrese una respuesta válidad.")
      
  if val == 2:
    break
  
totalPrice = sum(price)

print(f"El costo total de los productos es: {totalPrice}")

peopleQty = int(input(f"¿Entre cuantas personas se debe dividir la cuenta?: "))

print(f"El costo total por persona es: {totalPrice / peopleQty}")