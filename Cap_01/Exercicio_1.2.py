"""Exercício 1.2: Decorador para Validação de Argumentos 
Problema: Crie um decorador que valide se os argumentos de uma função são do tipo 
esperado. Se os tipos não corresponderem, deve lançar um TypeError. 
Solução: 
def validar_tipos(*expected_types): 
def decorator(func): 
def wrapper(*args, **kwargs): 
if len(args) != len(expected_types): 
raise TypeError(f"Esperava {len(expected_types)} 
argumentos posicionais, mas recebeu {len(args)}.") 
for arg, expected_type in zip(args, expected_types): 
if not isinstance(arg, expected_type): 
raise TypeError(f"Argumento '{arg}' deve ser 
do tipo {expected_type.__name__}, mas é {type(arg).__name__}.") 
return func(*args, **kwargs) 
return wrapper 
return decorator 
@validar_tipos(int, int) 
def somar(a, b): 
return a + b 
@validar_tipos(str, list) 
def adicionar_item(lista_str, item): 
lista_str.append(item) 
return lista_str 
print("\n--- Teste Somar ---") 
print(f"Soma (2, 3): {somar(2, 3)}") 
try: 
somar(2, "3") 
except TypeError as e: 
print(f"Erro ao somar: {e}") 
print("\n--- Teste Adicionar Item ---") 
minha_lista = ["a", "b"] 
print(f"Lista após adicionar 'c': {adicionar_item(minha_lista, 
'c')}") 
try: 
adicionar_item("string", "d") 
except TypeError as e: 
print(f"Erro ao adicionar item: {e}")"""

def validar_tipos(*expected_types): 
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            # Verifica se a quantidade de argumentos passados é igual à esperada
            if len(args) != len(expected_types): 
                raise TypeError(f"Esperava {len(expected_types)} argumentos posicionais, mas recebeu {len(args)}.") 
            
            #valida o tipo de cada argumento
            for arg, expected_type in zip(args, expected_types): 
                if not isinstance(arg, expected_type): 
                    raise TypeError(f"Argumento '{arg}' deve ser do tipo {expected_type.__name__}, mas é {type(arg).__name__}.") 
            
            # return da função original fora do ciclo for
            
            return func(*args, **kwargs) 
            
        return wrapper 
    return decorator 

# funções decoradas

@validar_tipos(int, int) 
def somar(a, b): 
    return a + b 
#  
@validar_tipos(list, str) 
def adicionar_item(lista_str, item): 
    lista_str.append(item) 
    return lista_str 

# testes e execuções das funções 
print("\n Teste somar") 
try:
    resultado_soma = somar(2, 3)
    print(f"Soma (2, 3): {resultado_soma}") 
    
    # Teste de erro proposital
    somar(2, "3") 
except TypeError as e: 
    print(f"Erro esperado ao somar: {e}") 

print("\n Teste Adicionar Item") 
try:
    minha_lista = ["a", "b"] 
    
    print(f"Lista após adicionar 'c': {adicionar_item(minha_lista, 'c')}") 

    # Testes  de erros propositadas 
    adicionar_item("isso_e_uma_string", "d") 
except TypeError as e: 
    print(f"Erro esperado ao adicionar item: {e}") 

print("\n--- Fim da Execução ---")