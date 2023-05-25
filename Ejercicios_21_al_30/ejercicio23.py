"""
Escribe un programa que solicite y muestre por pantalla los datos del punto anterior de una cantidad de
personas ingresada por el usuario.
"""

names = ""
last_name = ""
count = 0

usrRequire = int(input(f"Ingrese la cantidad de alumnos que quiere ingresar el nombre y el apellido: "))
while count < usrRequire:
  name = input(f"Ingrese el nombre del estudiante Nº {count+1}: ")
  last_name = input(f"Ingrese el apellido del estudiante Nº {count+1}: ")
  print(f"El nombre completo del estudiante Nº {count+1} es {name} {last_name}")
  count += 1

print("Fin del programa.")