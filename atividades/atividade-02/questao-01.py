
## 1. Escreva uma função que receba uma lista de números e retorne outra lista
## com os números ímpares.

def impar(lista_numeros):
    return [num for num in lista_numeros if num %2 != 0]
 
lista_de_numeros = [5, 6, 7, 11, 2, 3]
numeros_impares = impar(lista_de_numeros)

print(numeros_impares)