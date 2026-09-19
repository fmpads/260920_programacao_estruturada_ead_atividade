'''
20/9/26
Faculdade Municipal da Palhoça
Análise e Desenvolvimento de Sistemas
Turma: 2026/2
Disciplina: Prática de Programação Estruturada
Docente: Prof.ª Daniela Amorim
Discente: Jean Douglas Toledo Rodrigues Junior

Exercícios Extra

Exercício 1:

Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.
'''
idadeHomem1 = int(input("\nExercício 1 - Digite a idade do primeiro homem: "))
idadeHomem2 = int(input("Digite a idade do segundo homem: "))
idadeMulher1 = int(input("Digite a idade da primeira mulher: "))
idadeMulher2 = int(input("Digite a idade da segunda mulher: "))
if idadeHomem1 > idadeHomem2:
    homemMaisVelho = idadeHomem1
    homemMaisNovo = idadeHomem2
else:
    homemMaisVelho = idadeHomem2
    homemMaisNovo = idadeHomem1

if idadeMulher1 > idadeMulher2:
    mulherMaisVelha = idadeMulher1
    mulherMaisNova = idadeMulher2
else:
    mulherMaisVelha = idadeMulher2
    mulherMaisNova = idadeMulher1

print(f"\nSoma das idades do homem mais velho com a mulher mais nova: {homemMaisVelho + mulherMaisNova}")
print(f"Produto das idades do homem mais novo com a mulher mais velha: {homemMaisNovo * mulherMaisVelha}")
'''
Exercício 2:

Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário.
Calcular e escrever o total (total = quantidade adquirida * preço unitário) e o total a pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <=10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%

'''
nomeProduto = input("\nExercício 2 - Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
precoUnitario = float(input("Digite o preço unitário: R$ "))
total = quantidade * precoUnitario
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

totalAPagar = total - desconto
print(f"\nTotal: R$ {total:.2f}")
'''
Exercício 3:

Imagina que você consegue atender entre 20 e 30 cães durante a semana no seu Pet Shop.
Se atender menos do que 20 cães, o pet shop ficou ocioso, se você atendeu mais do que 30 significa que o cliente foi até o local mas não pode ser atendido. Faça um algoritmo para verificar quantos cães foram atendidos e informar se a petshop ficou ocioso, se está normal ou se está com carga alta de demanda.
'''
quantidade = int(input("\nExercício 3 - Digite a quantidade de cães atendidos durante a semana: "))
if quantidade < 20:
    print("\nO pet shop ficou ocioso.")
elif quantidade > 30:
    print("\nO pet shop está com carga alta de demanda.")
else:
    print("\nO pet shop está normal.")
'''
Exercício 4:

Elabore um algoritmo que leia dois números inteiros e mostre o resultado da diferença do maior valor pelo menor;
'''
num1 = int(input("\nExercício 4 - Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))
if num1 > num2:
    diferenca = num1 - num2
else:
    diferenca = num2 - num1
print(f"\nA diferença do maior número pelo menor é: {diferenca}")
'''
Exercício 5:

A escola “APRENDER” faz o pagamento de seus professores por hora/aula.
Faça um algoritmo que calcule e exiba o salário de um professor.
Sabe-se que o valor da hora/aula segue a tabela abaixo:
Professor Nível 1 R$12,00 por hora/aula
Professor Nível 2 R$17,00 por hora/aula
Professor Nível 3 R$25,00 por hora/aula.
'''
nivel = int(input("\nExercício 5 - Digite o nível do professor (1, 2 ou 3): "))
horasAula = int(input("Digite a quantidade de horas/aula (números inteiros):"))
if nivel == 1:
    salario = horasAula * 12
elif nivel == 2:
    salario = horasAula * 17
elif nivel == 3:
    salario = horasAula * 25
else:
    print("\nNível inválido. O nível do professor deve ser 1, 2 ou 3.")
    salario = 0

print(f"\nO salário do professor é: R$ {salario:.2f}")