
def IngresoEdad():
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        return edad
    except:
        print("La edad debe ser un numero entero")
        IngresoEdad()

mi_edad = IngresoEdad()

if mi_edad >= 0 and mi_edad < 18:
    print("Menor de edad")
elif mi_edad >= 18:
    if mi_edad < 30:
        print("Adulto joven")
    elif mi_edad >= 30 and mi_edad < 60:
        print("Adulto")
    else:
        print("Adulto mayor")
else:
    print("La edad debe ser un numero entero positivo")

    