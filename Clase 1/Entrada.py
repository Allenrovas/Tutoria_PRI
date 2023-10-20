#Input y Outpu

#Input

def Ingreso():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        print("Hola",nombre,"tienes una edad de:",edad)
    except:
        print("La edad debe ser un numero entero")
        Ingreso()



Ingreso()

print("Fin del programa")