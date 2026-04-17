
"""def permutar(lista): 
    if len(lista) == 0: 
        yield [] 
    elif len(lista) == 1: 
        yield lista 
    else: 
        for i in range(len(lista)): 
            elemento_atual = lista[i] 
            elementos_restantes = lista[:i] + lista[i+1:] 
            for p in permutar(elementos_restantes): 
                yield [elemento_atual] + p
print("\n--- Gerador de Permutações ---") 
lista_exemplo = [1, 2, 3] 
print(f"Permutações de {lista_exemplo}:") 
for p in permutar(lista_exemplo): 
    print(p) 
# Saída esperada: 
# [1, 2, 3] 
# [1, 3, 2] 
# [2, 1, 3] 
# [2, 3, 1] 
# [3, 1, 2] 
# [3, 2, 1] 
lista_letras = ["A", "B"] 
print(f"Permutações de {lista_letras}:") 
for p in permutar(lista_letras): 
    print(p) 
# Saída esperada: 
# ["A", "B"] 
# ["B", "A"]"""

# Em Poucas lihas este codigo faz a permutação de de valores de entradas
def permutar(lista):
    if len(lista) <= 1:
        yield lista
    else:
        for i in range(len(lista)):
            atual = lista[i]
            restantes = lista[:i] + lista[i+1:]
            for p in permutar(restantes):
                yield [atual] + p

# Interface direta
entrada = input("\nDigite o que deseja permutar (letras ou números separados por espaço): ").split()

print(f"\nPermutações de {entrada}:")
for p in permutar(entrada):
    print(" ".join(p))