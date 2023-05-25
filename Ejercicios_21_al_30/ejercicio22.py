# Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.
"""
  EJERCICIO RESUELTO CON FOR Y ARRAYS
names = []

for i in range(5):
  names.append(input('Ingrese el nombre y el apellido de la persona: '))

for name in names:
  print(name)
  
"""

# EJERCICIO RESULETO CON WHILE

names = ""
last_name = ""
count = 0

while count < 5:
  name = input(f"Ingrese el nombre del estudiante Nº {count+1}: ")
  last_name = input(f"Ingrese el apellido del estudiante Nº {count+1}: ")
  print(f"El nombre completo del estudiante Nº {count+1} es {name} {last_name}")
  count += 1

print("Fin del programa.")