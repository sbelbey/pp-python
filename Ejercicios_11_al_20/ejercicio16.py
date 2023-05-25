# Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y
# muestre por pantalla el resultado, considerando que, si el empleado trabajo más de 120hs en el mes, se le paga
# $1.500, de lo contrario, se le paga $1.300.

workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

if (workedHours > 120):
    print(
        f'El sueldo del empleado es: {workedHours*1500}, siendo {workedHours} las horas trabajadas.')
else:
    print(
        f'El sueldo del empleado es: {workedHours*1200}, siendo {workedHours} las horas trabajadas.')
