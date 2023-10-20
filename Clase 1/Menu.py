def Suma():
    print("Suma")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("El resultado es: ", resultado)
    MenuInicial()

def Resta():
    print("Resta")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("El resultado es: ", resultado)
    MenuInicial()

def Multiplicacion():
    print("Multiplicación")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print("El resultado es: ", resultado)
    MenuInicial()

def Division():
    print("División")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado es: ", resultado)
    MenuInicial()




def MenuInicial():
    seleccion = 0
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    seleccion = int(input("Seleccione una opción: "))
    if seleccion == 1:
        Suma()
    elif seleccion == 2:
        Resta()
    elif seleccion == 3:
        Multiplicacion()
    elif seleccion == 4:
        Division()
    elif seleccion == 5:
        print("Gracias por usar la calculadora")
    else:
        print("Opción incorrecta")
        MenuInicial()



MenuInicial()