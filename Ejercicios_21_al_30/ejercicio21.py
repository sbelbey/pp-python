# Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, 
# escribe un programa que calcule el descuento anual a realizarse, considerando:

# a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
# b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
# c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
# d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto
#   anual a descontarse y las horas trabajadas en todo el año.

EXPHOURS = 1500
CHEHOURS = 1200
MINHOURS = 1100
EXPBONUS = 18
CHEBONUS = 15
MINBONUS = 13
SUPERDISC = 5
MAXDISC = 3
MINDISC = 1


workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

if (0 < workedHours < 193):
  
    if (workedHours > 120):
        grossSalary = workedHours * EXPHOURS
        bonusAmount = EXPBONUS * grossSalary / 100
    elif (80 <= workedHours <= 120):
        grossSalary = workedHours * CHEHOURS
        bonusAmount = CHEBONUS * grossSalary / 100
    else:
        grossSalary = workedHours * MINHOURS
        bonusAmount = MINBONUS * grossSalary / 100

    if (grossSalary * 12 > 2000000):
        salaryWDiscount = grossSalary - (SUPERDISC*grossSalary/100)
    elif (1000000 <= workedHours * 12 <= 2000000):
        salaryWDiscount = grossSalary - (MAXDISC*grossSalary/100)
    else:
        salaryWDiscount = grossSalary - (MINDISC*grossSalary/100)

    print(
        f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas.\n Su salario con los descuentos aplicados es {salaryWDiscount}. \n Su bonificación es {bonusAmount}, y el total a cobrar es {salaryWDiscount + bonusAmount}.')

else:
    print(f'Usted es un explotador laboral o un tonto, haga sus propios cáculos.')
