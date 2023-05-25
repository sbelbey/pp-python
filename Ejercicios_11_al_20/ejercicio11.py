tipoDeCambio = int(
    input(
        "Ingrese el numero de la opción según corresponda: \n1. Cambiar de pesos a dolares. \n2.Cambiar de dolares a pesos.\n"
    )
)
if (tipoDeCambio != 1) or (tipoDeCambio != 2):
    if (tipoDeCambio == 1):
        pesos = int(
            input("Ingrese la cantidad de pesos que desea convertir a dólares: "))
        dolar = int(input("Ingrese el valor de un dolar en pesos: "))
        print("La cantidad de dólares que puede comprar con sus pesos es: ", pesos/dolar)
    else:
        dolares = int(
            input("Ingrese la cantidad de dolares que desea convertir a pesos: "))
        dolar = int(input("Ingrese el valor de un dolar en pesos: "))
        print("La cantidad de dólares que puede comprar con sus pesos es: ", dolares*dolar)
else:
    print("Ingresó una opción incorrecta")
