"""estudantes = [ 
{"nome": "Ana", "idade": 21, "curso": "Eng. Informática"}, 
{"nome": "Bruno", "idade": 19, "curso": "Gestão"}, 
{"nome": "Carla", "idade": 22, "curso": "Eng. Civil"}, 
{"nome": "Daniel", "idade": 20, "curso": "Eng. Informática"} 
] 
# Usando compreensão de lista para filtrar e transformar 
nomes_estudantes_maiores_20 = [estudante["nome"].upper()  
for estudante in estudantes  
if estudante["idade"] > 20] 
print(f"Nomes dos estudantes com mais de 20 anos: 
{nomes_estudantes_maiores_20}")"""
estudantes =[]
n=int(input("Digite numero de estudadntes que desejas cadatrar"))

for i in range (n):
    novos_estudantes={
        "Nome": input("informe o nome do estudante"),
        "Idade": int(input("digite a idade")),
        "Curso": input("Digite o curso do estudante"),
    }

    estudantes.append(novos_estudantes)

for e in estudantes:
    if e["Idade"]>20:
        print(e)