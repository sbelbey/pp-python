# Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas
# y muestre por pantalla el resultado, considerando lo siguiente:
# a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
# b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
# c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100.

EXPHOURS = 1500
CHEHOURS = 1200
MINHOURS = 1100


workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

if (workedHours < 193):
    if (workedHours > 120):
        grossSalary = workedHours * EXPHOURS
    elif (80 <= workedHours <= 120):
        grossSalary = workedHours * CHEHOURS
    else:
        grossSalary = workedHours * MINHOURS

    print(
        f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas.')

else:
    print(f'Usted es un explotador laboral, haga sus propios cáculos.')
