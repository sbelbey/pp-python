# Escribe un programa que permita al usuario ingresar dos números y muestre por pantalla cuál es el
# mayor de ellos.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El numero mayor es: ", num1)
elif num1 < num2:
    print("El numero mayor es: ", num2)
else:
    print("Los números son iguales.")
