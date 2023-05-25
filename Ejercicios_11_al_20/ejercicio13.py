# Escribe un programa que permita al usuario ingresar dos números y muestre por pantalla cuál es el
# menor de ellos.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El numero menor es: ", num2)
elif num1 < num2:
    print("El numero menor es: ", num1)
else:
    print("Los números son iguales.")
