import time 
import random
"""
def retry(max_tentativas=3, atraso_segundos=1): 
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            for tentativa in range(1, max_tentativas + 1): 
                try: 
                    print(f"Tentativa {tentativa} de 
{max_tentativas} para {func.__name__}...") 
                    return func(*args, **kwargs) 
                except Exception as e: 
            print(f"Falha na tentativa {tentativa}: {e}") 
                if tentativa < max_tentativas: 
            time.sleep(atraso_segundos) 
                raise Exception(f"Função {func.__name__} falhou após 
{max_tentativas} tentativas.") 
return wrapper 
return decorator 
@retry(max_tentativas=4, atraso_segundos=0.5) 
def operacao_instavel(): 
if random.random() < 0.7: # 70% de chance de falhar 
raise ValueError("Erro simulado na operação!") 
return "Operação bem-sucedida!" 
print("\n--- Teste de Operação Instável com Retry ---") 
try: 
resultado = operacao_instavel() 
print(f"Resultado final: {resultado}") 
except Exception as e: 
print(f"Erro fatal: {e}")"""

import time 
import random

def retry(max_tentativas=3, atraso_segundos=1): 
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            for tentativa in range(1, max_tentativas + 1): 
                try: 
                    print(f"-> Tentativa {tentativa} de {max_tentativas}...") 
                    return func(*args, **kwargs) 
                except Exception as e: 
                    print(f"   [!] Erro: {e}") 
                    if tentativa < max_tentativas: 
                        time.sleep(atraso_segundos) 
                    else:
                        raise Exception(f"Função {func.__name__} falhou após {max_tentativas} tentativas.") 
            return None
        return wrapper 
    return decorator 

def executar_teste_interativo():
    print("=== Simulador de Resiliência (Retry Decorator) ===")
    
    try:
        tentativas = int(input("Defina o máximo de tentativas (ex: 3-5): "))
        atraso = float(input("Defina o tempo de espera entre falhas (ex: 0.5): "))
        chance_falha = float(input("Defina a chance de erro (0.0 a 1.0, ex: 0.7 para 70%): "))

        # Criamos a função instável dentro para usar a chance_falha definida pelo usuário
        @retry(max_tentativas=tentativas, atraso_segundos=atraso) 
        def operacao_instavel(): 
            if random.random() < chance_falha: 
                raise ValueError("Conexão instável!") 
            return "Sucesso Total!" 

        print(f"\n--- Iniciando Operação com {chance_falha*100}% de chance de erro ---")
        resultado = operacao_instavel() 
        print(f"\nFINALIZADO: {resultado}") 

    except ValueError as e:
        print(f"\nERRO DE ENTRADA: Por favor, use números válidos.")
    except Exception as e: 
        print(f"\nERRO FATAL: {e}")

# Executa o programa
if __name__ == "__main__":
    while True:
        executar_teste_interativo()
        denovo = input("\nQuer testar novamente? (s/n): ").lower()
        if denovo != 's':
            print("Encerrando simulador.")
            break