# Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar
# y el sueldo neto (bruto + bonif), considerando:
# a. Si trabajo más de 120hs, la bonificación es de %18
# b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
# c. Si trabajo menos de 80 horas, la bonificación es de %13.

EXPHOURS = 1500
CHEHOURS = 1200
MINHOURS = 1100
EXPBONUS = 18
CHEBONUS = 15
MINBONUS = 13
# MAXDISC = 3
# MINDISC = 1


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

    # if (grossSalary > 1000000):
    #     salaryWDiscount = grossSalary - (MAXDISC*grossSalary/100)
    # else:
    #     salaryWDiscount = grossSalary - (MINDISC*grossSalary/100)

    print(
        f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas.\n El total a cobrar es {grossSalary + bonusAmount}.')

else:
    print(f'Usted es un explotador laboral o un tonto, haga sus propios cáculos.')
