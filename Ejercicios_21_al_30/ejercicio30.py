"""
Escribe un programa que calcule las ganancias mensuales de un profesional, correspondientes a 20 días
de trabajo, teniendo en cuenta:
a. Debe ingresar el monto total por prestación realizada.
b. El programa debe descontar el 10,5% correspondiente a impuestos.
c. El programa debe mostrar por pantalla el importe bruto y neto, diario y mensual.
d. El programa debe mostrar el importe pagado en impuestos diarios y mensual.
"""

income = []
incomeWDiscont = []
taxTotal = 0

for day in range(2):
  income.append(0)
  bene = 1
  while True:
    income[day] += int(input(f"Ingrese el monto de la prestación {bene} del día {day + 1}: "))
    bene += 1
    while True:
      val = int(input(f"Desea seguir ingresando prestaciones para el día {day + 1}? \n 1. Si \n 2. No\n"))
      
      if val == 1 or val == 2:
        break
        
      print("Ingrese una respuesta válidad.")
      
    if val == 2:
      break

total= sum(income)

for day in income:
  print(f"Importe bruto diario {day} y neto diario: {day-day*0.105}")
  print(f"El importe pagado en impuestos diarios es: {day*0.105}")
  taxTotal += day*0.105

print(f"Total bruto: {total}, total neto: {total-total*0.105}. Total de impuestos: {taxTotal}")