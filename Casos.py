# Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno.

aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

print("Nome do aluno:", aluno["nome"])

# Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade"

aluno["nota"] = 9.5         
del aluno["idade"]          

print("Dicionário atualizado:", aluno)

# Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

# Dado o dicionário aluno, verifique se existe a chave "curso"

if "curso" in aluno:
    print("A chave 'curso' existe no dicionário aluno.")
else:
    print("A chave 'curso' NÃO existe no dicionário aluno.")

# Crie um dicionário chamado turma que contenha dois alunos, cada um com nome e nota.
# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno

turma = {
    "aluno1": {"nome": "Ana", "nota": 8.7},
    "aluno2": {"nome": "Carlos", "nota": 9.2}
}

print("Nome do primeiro aluno:", turma["aluno1"]["nota"])
print("Nota do segundo aluno:", turma["aluno2"]["nota"])

# Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# Adicione ao dicionário do carro a chave 'cor'.
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022
}

carro["cor"] = "Prata"  
print("Dicionário do carro:", carro)

# Crie um dicionário de notas de 3 alunos (nome como chave, nota como valor).

notas = {
    "Ana": 8.5,
    "Bruno": 7.9,
    "Clara": 9.3
}

# Acesse a nota de um dos alunos e exiba

print("Nota da Clara:", notas["Clara"])

# Remova um aluno do dicionário de notas.

del notas["Bruno"]
print("Notas após remoção:", notas)
