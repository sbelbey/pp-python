"""
Teniendo en cuenta el punto anterior, el programa debe:
a. Permitir ingresar, el monto que el integrante hubiese aportado anteriormente, previo a la
división y calcular el saldo a favor o adeudado, informando por pantalla cuál es el caso.
"""

products = []
price = []

while True:
  products.append(input(f"Ingrese el producto a comprar: "))
  price.append(int(input(f"Ingrese el precio del producto: ")))
  
  while True:
    val = int(input(f"Desea seguir ingresando productos? \n 1. Si \n 2. No\n"))
    
    if val == 1 or val == 2:
      break 
    
    print("Ingrese una respuesta válidad.")
      
  if val == 2:
    break
  
totalPrice = sum(price)

print(f"El costo total de los productos es: {totalPrice}")

peopleQty = int(input(f"¿Entre cuantas personas se debe dividir la cuenta?: "))
ammount = totalPrice / peopleQty

print(f"El costo total por persona es: {ammount}")

for person in range(peopleQty):
  contribution = int(input("Ingrese la cantidad abonada por la primera persona: "))
  
  if contribution < ammount:
    print(f"La persona debe aportar: {abs(contribution - ammount)}")
  elif contribution > ammount:
    print(f"La persona tiene un saldo a favor de: {abs(ammount - contribution)}")
  else:
    print("La pesona aportó el monto justo.")
  