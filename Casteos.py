# Conversión entre tipos de datos
#Pasando a flotante
entero = 10
flotante = float(entero)

print(entero)
print(flotante)

#Pasando a string
stringCas = str(entero)

print(stringCas)

#Pasando a entero
variable_pi = 3.65
entero_pi = int(variable_pi)

print(variable_pi)
print(entero_pi)

edad = "25"
edad_entero = int(edad)

print(edad)
print(edad_entero)

# Aproximar

numero = 3.64159265

#Aproximar a 2 decimales 

apr_2_decimales = round(numero,2)

#Aproximar a 1 decimales

apr_1_decimales = round(numero,1)

#Aproximar a entero 

apr_entero = round(numero)

print("Numero original: ",numero)
print("Dos decimales: ",apr_2_decimales)
print("Un decimal: ",apr_1_decimales)
print("Entero: ", apr_entero)