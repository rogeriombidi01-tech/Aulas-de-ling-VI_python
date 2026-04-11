"""pessoas = [ 
{"nome": "Ana", "idade": 30}, 
{"nome": "Bruno", "idade": 25}, 
{"nome": "Carla", "idade": 30}, 
{"nome": "Daniel", "idade": 25}, 
{"nome": "Eduardo", "idade": 35} 
] 
# Ordenar usando uma função lambda com múltiplos critérios 
pessoas_ordenadas = sorted(pessoas, key=lambda p: (p["idade"], 
p["nome"])) 
print("\n--- Pessoas Ordenadas ---") 
for pessoa in pessoas_ordenadas: 
    print(pessoa)"""
# Saída esperada: 
# {"nome": "Bruno", "idade": 25} 
# {"nome": "Daniel", "idade": 25} 
# {"nome": "Ana", "idade": 30} 
# {"nome": "Carla", "idade": 30} 
# {"nome": "Eduardo", "idade": 35}''' 

#Resolução aplicada, usando interações 
pessoas=[]
n=int(input("\nInfome o número de pessoas a constar na lista: "))
for i in range (n):
  novas_pessoas={
    "nome":input("\nDigite o nome: "),
    "Idade":int(input("\nDigite a idade: ")),
  }
pessoas.append(novas_pessoas)

#Ordenação usando a função lambda com múltiplos critérios 

pessoas_ordenadas = sorted(pessoas, key=lambda p: (p["Idade"], 
p["nome"])) 
print("\n PESSOAS ORDENADAS") 
for pessoa in pessoas_ordenadas: 
  print(pessoas)