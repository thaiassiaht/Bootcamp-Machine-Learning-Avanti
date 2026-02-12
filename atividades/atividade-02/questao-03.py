#3. Escreva uma função que receba duas listas e retorne outra lista com os
# elementos que estão presentes em apenas uma das listas.

def elementos_exclusivos(lista1, lista2):

    set1 = set(lista1)
    set2 = set(lista2)
    
    resultado = list(set1 ^ set2)
    
    return resultado

l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7, 8, 9]

resultado = elementos_exclusivos(l1, l2)
print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
print(f"Elementos exclusivos: {resultado}") 

