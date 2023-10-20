#Ciclos

#Ciclo for

frutas = ["manzana", "pera", "mango"]
for fruta in frutas:
    print(fruta)

lista = []

for i in range(20):
    lista.append(i)
    #if i % 2 == 0:
    #    lista.append(i)

print(lista)

#len nos da el tamaño de la lista

for i in range(lista[0],len(lista),2):
    print(lista[i])

#Ciclo while

contador = 10
while contador < 10:
    print("Estoy en el ciclo while")
    print(contador)
    contador += 1

#Ciclo while con break
#Emulando un do while
contador = 10
while True:
    print("Contador: ",contador)
    #contador += 1 # contador = contador + 1, 10 + 1 
    if contador == 10:
        break
    contador += 1
    

