# Escribe un programa que calcule el promedio de 5 notas de un alumno, si el promedio es mayor a 9, el
# programa debe mostrar por pantalla el siguiente mensaje “El alumno posee excelencia académica”.

nota1 = float(input('Ingrese la primera nota: '))
nota2 = float(input('Ingrese la segunda nota: '))
nota3 = float(input('Ingrese la tercera nota: '))
nota4 = float(input('Ingrese la tercera nota: '))
nota5 = float(input('Ingrese la tercera nota: '))
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (promedio > 9):
    print('El alumno posee excelencia académica',
          promedio, 'es su promedio', sep=" ")
