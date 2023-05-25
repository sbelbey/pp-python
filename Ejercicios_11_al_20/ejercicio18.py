# Del punto anterior, escribe un programa que calcule el descuento anual a realizarse.
# Si el sueldo anual es mayor a $1.000.000, el descuento es del %3, sino debe aplicarse un descuento del %1.
# El programa debe mostrar el monto a descontar.

EXPHOURS = 1500
CHEHOURS = 1200
EXPBONUS = 18
CHEBONUS = 12
MAXDISC = 3
MINDISC = 1


workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

if (workedHours < 193):
    if (workedHours > 120):
        grossSalary = workedHours * EXPHOURS
        bonusAmount = EXPBONUS * grossSalary / 100
    else:
        grossSalary = workedHours * CHEHOURS
        bonusAmount = CHEBONUS * grossSalary / 100

    if (grossSalary*12 > 1000000):
        salaryWDiscount = grossSalary - (MAXDISC*grossSalary/100)
    else:
        salaryWDiscount = grossSalary - (MINDISC*grossSalary/100)

    print(
        f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas.\n Su salario con los descuentos aplicados es {salaryWDiscount}. \n Su bonificación es {bonusAmount}, y el total a cobrar es {salaryWDiscount + bonusAmount}.')
else:
    print(f'Usted es un explotador laboral, haga sus propios cáculos.')
