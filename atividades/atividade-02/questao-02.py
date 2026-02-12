# 2. Escreva uma função que receba uma lista de números e retorne outra lista
#com os números primos presentes.

import math

def ePrimo(lista):
    
    primos = []
    
    for num in lista:
        if num < 2:
            continue
        is_primo = True
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    return primos
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
resultados = ePrimo(numeros)
print(resultados)