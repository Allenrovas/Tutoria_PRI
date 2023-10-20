
def bubble_sort(lista_desordenada):
    noNumeros = len(lista_desordenada)
    for i in range (noNumeros):
        for j in range (0, noNumeros-i-1): #7-i-1, o sea 7-0-1: 6 ejecuciones;
            if lista_desordenada[j] > lista_desordenada[j+1]:
                lista_desordenada[j], lista_desordenada[j+1] = lista_desordenada[j+1], lista_desordenada[j]

# noNumeros = 7
# i = 0
# j = 0
# for j: 0, 1, 2, 3, 4, 5, 6
#     if lista_desordenada[0] > lista_desordenada[1]:
#         lista_desordenada[0], lista_desordenada[1] = lista_desordenada[1], lista_desordenada[0]
#     if 64 > 34:
#         lista_desordenada[0], lista_desordenada[1] = 34, 64


lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista_desordenada)
print("Lista ordenada:", lista_desordenada)

lista_desordenada_2 = [85, 90, 65, 75, 78, 100, 95, 80, 70, 60, 50, 40, 30, 20, 10]
bubble_sort(lista_desordenada_2)
print("Lista ordenada 2:", lista_desordenada_2)

lista_strings = ["Angel", "Juan", "Pedro", "Maria", "Jose", "Luis", "Carlos"]
bubble_sort(lista_strings)
print("Lista strings:", lista_strings)
