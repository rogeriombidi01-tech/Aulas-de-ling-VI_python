def verificar_parenteses_balanceados(expressao): 
    pilha = [] 
    mapeamento = {")": "(", "]": "[", "}": "{"} # Mapeia 
fechamento para abertura 

    for char in expressao: 
        if char in mapeamento.values(): # É um parêntese de 
abertura 
            pilha.append(char) 
        elif char in mapeamento.keys(): # É um parêntese de 
fechamento 
            if not pilha or mapeamento[char] != pilha.pop(): 
                return False # Pilha vazia ou não corresponde ao 
topo 
    return not pilha # Retorna True se a pilha estiver vazia no 
final 
# Exemplos de uso 
print("\n--- Verificação de Parênteses Balanceados ---") 
print(f"{{[()]}}: {verificar_parenteses_balanceados("{[()]}")}") 
# Saída: True 
print(f"{{[(])}}: {verificar_parenteses_balanceados("{[(])}")}") 
# Saída: False 
print(f"((())) : {verificar_parenteses_balanceados("((()))")}") # 
Saída: True 
print(f"(()    : {verificar_parenteses_balanceados("(()")}")    
Saída: False 
print(f"}}     
# 
: {verificar_parenteses_balanceados("}")}")      
Saída: False