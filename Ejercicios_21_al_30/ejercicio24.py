"""Escribe un programa que calcule el promedio general de una clase."""

quant = int(input(f"Ingrese la cantidad de alumnos que tiene la clase: "))
count = 0
acc = 0

while count < quant:
  acc += int(input(f"Ingrese la nota del alumno Nº {count + 1}: "))
  count += 1

print(f"El promedio final de la clase es {acc / quant}")