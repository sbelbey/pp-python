# Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
# indicando por pantalla si el alumno aprobó o debe recursar la materia.

nota1 = float(input('Ingrese la primera nota: '))
nota2 = float(input('Ingrese la segunda nota: '))
nota3 = float(input('Ingrese la tercera nota: '))
promedio = (nota1 + nota2 + nota3) / 3

if (promedio >= 6):
    print('Usted ha aprobado la materia.', promedio, 'es su promedio', sep=" ")
else:
    print('Usted debe cursar.', promedio, 'es su promedio', sep=" ")
