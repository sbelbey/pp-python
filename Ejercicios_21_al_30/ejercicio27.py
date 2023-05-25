"""
Escribe un programa que permita ingresar las edades de las personas, 
hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingresadas 
y el total de personas ingresadas.
"""

accu = 0 
count = 0

while True:
  accu += int(input(f"Ingrese la edad de la persona: "))
  count += 1
  
  while True:
    val = int(input(f"Desea seguir ingresando edades? \n 1. Si \n 2. No\n"))
    
    if val != 1 or val != 2:
      break  
    
    print("Ingrese una respuesta válidad.")
      
  if val == 2:
    break
  
print (f"La cantidad de personas ingresadas es {count}, y el promedio de edad es {accu/count}.")