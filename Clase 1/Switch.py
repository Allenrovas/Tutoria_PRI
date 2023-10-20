#Ejemplo switch case

def IngresoEdad():
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        return edad
    except:
        print("La edad debe ser un numero entero")
        IngresoEdad()

mi_edad = IngresoEdad()

#EMULANDO SWITCH CASE

def adulto_joven():
    print("Adulto joven")

def adulto():
    print("Adulto")

def adulto_mayor():
    print("Adulto mayor")

def menor_edad():
    print("Menor de edad")

def default():
    print("La edad debe ser un numero entero positivo")


def switch(edad):
    if edad >= 0 and edad < 18:
        menor_edad()
    elif edad >= 18:
        if edad < 30:
            adulto_joven()
        elif edad >= 30 and edad < 60:
            adulto()
        else:
            adulto_mayor()
    else:
        default()

switch(mi_edad)