#Factorial de un número
# 5! = 5 * 4 * 3 * 2 * 1
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

'''Contador = 0
def factorial(n):
    global Contador
    Contador += 1
    print("Contador: ", Contador)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# factorial(6)
# 6 * factorial(5)
# 6 * 5 * factorial(4)
# 6 * 5 * 4 * factorial(3)
# 6 * 5 * 4 * 3 * factorial(2)
# 6 * 5 * 4 * 3 * 2 * factorial(1)
# 6 * 5 * 4 * 3 * 2 * 1 * factorial(0)
    
#Ingresa un número
n = int(input("Ingrese un número: "))

#Calcula el factorial
resultado = factorial(n)
print("El factorial de", n, "es", resultado)'''
# alt + 39 '


#Recursividad indirecta
Contador1 = 0
Contador2 = 0

def factorial_1(n):
    global Contador1
    Contador1 += 1
    print("Contador1: ", Contador1)
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
    
def factorial_recursivo(n):
    global Contador2
    Contador2 += 1
    print("Contador2: ", Contador2)
    if n == 0:
        return 1
    else:
        return n * factorial_1(n - 1)
    
#Ingresa un número
n = int(input("Ingrese un número: "))
#Calcula el factorial
resultado = factorial_1(n)
print("El factorial de", n, "es", resultado)
