# Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas
# y muestre por pantalla el resultado, counsiderando qe, si el empleado trabajo más de 120hs en el mes,
# se le paga $1.500 más una bonificación del %18,
# de lo contrario, se le paga $1.300 más una bonificación del %15.
# El programa debe mostrar el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif)


EXPHOURS = 1500
CHEHOURS = 1200
EXPBONUS = 18
CHEBONUS = 12

workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

if (workedHours > 120):
    grossSalary = workedHours * EXPHOURS
    bonusAmount = EXPBONUS * grossSalary / 100
else:
    grossSalary = workedHours * CHEHOURS
    bonusAmount = CHEBONUS * grossSalary / 100

print(
    f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas. Su bonificación es {bonusAmount}, y el total a cobrar es {grossSalary + bonusAmount}.')
