'''
13/10/26
Faculdade Municipal de Palhoça
Tecnologia em Análise e Desenvolvimento de Sistemas
Turma: 93. ADS - ADS/MAT - 2026/2 - MATURINO
Disciplina: Prática de Programação Estruturada
Docente: Prof.ª Daniela Amorim
Discente: Jean Douglas Toledo Rodrigues Junior

EaD 03

'''

# Questão 1

soma = 0 # declaração das variáveis que serão utilizadas
print(f"\nQuestão 1. Faça um programa que calcule e escreva a seguinte soma: soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.\n")
for i in range (1, 101): # intervalo entre 1 e 100
    if i % 2 == 0: # se o número for par, entra nesta condição
        numerador = i - 1 # define o numerador como o número ímpar anterior
        denominador = i // 2 # define o denominador como a metade do número par
        soma += numerador / denominador # define a somatória das divisões das frações
        if i < 100: # condição pra imprimir o sinal de + entre as frações (exceto depois da última)
            print(f"{numerador}/{denominador} + ", end="")
        else: # condição para imprimir o sinal de = depois da última fração
            print(f"{numerador}/{denominador} =", end="")
print(f"\n\nsoma = {soma}\n")

# Questão 2

numeros = 0 # declaração das variáveis que serão utilizadas
print(f"Questão 2. Liste os números de 1 até 500.\n")
for i in range(1, 501): # intervalo entre 1 e 500
    if i < 500: # condição pra imprimir a vírgula entre os números (exceto depois do último)
        print(f"{i},", end=" ")
    else: # condição para imprimir o sinal de = depois do último número
        print(f"{i}", end="\n")
    numeros += 1 # incremento do contador de números

#Questão 3

print(f"\nQuestão 3. Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura e sexo (0=masc, 1=fem) das pessoas.")
print(f"\nFaça um programa que leia 50 dados diferentes e informe:")
print(f"\n- a maior e a menor altura encontradas;")
print(f"\n- a média de altura das mulheres;") 
print(f"\n- a média de altura da população;") 
print(f"\n- o percentual de homens na população.")

# declaração de todas as variáveis que serão utilizadas
contadorHomens = 0
contadorMulheres = 0
maiorAlturaHomens = 0
maiorAlturaMulheres = 0
menorAlturaHomens = 0
menorAlturaMulheres = 0
somaAlturaHomens = 0
somaAlturaMulheres = 0
mediaAlturaHomens = 0
mediaAlturaMulheres = 0
maiorAltura = 0
menorAltura = 0
mediaPopulacao = 0

for i in range (1, 2): # intervalo entre 1 e 50
    sexo = int(input(f"\nQual o sexo da {i}ª pessoa (0=masc, 1=fem)? ")) # pede os sexos de todas as pessoas
    altura = float(input(f"Qual a {i}ª altura? ")) # pede as alturas de todas as pessoas

    if sexo == 0: # se o sexo for masculino entra nesta condição
        if i == 1: # se o contador for 1, ou seja, o primeiro homem, entra nesta condição
            maiorAlturaHomens = altura # define a maior altura dos homens
            menorAlturaHomens = altura # define a menor altura dos homens
            somaAlturaHomens += altura # inicia a somatória das alturas dos homens
            contadorHomens += 1 # inicia a contagem dos homens
        else: # se for homem e não for a primeira pessoa, entra nesta condição
            if altura >= maiorAlturaHomens: # se a altura for maior ou igual que a maior altura dos homens, entra nesta condição
                maiorAlturaHomens = altura # define a maior altura masculina
                somaAlturaHomens += altura # continua a somatória das alturas dos homens
                contadorHomens += 1 # continua a contagem dos homens
            else:
                menorAlturaHomens = altura # define a menor altura masculina
                somaAlturaHomens += altura # continua a somatória das alturas dos homens
                contadorHomens += 1 # continua a contagem dos homens
    else: # se o sexo for feminino entra nesta condição
        if i == 1: # se o contador for 1, ou seja, a primeira mulher, entra nesta condição
            maiorAlturaMulheres = altura # define a maior altura das mulheres
            menorAlturaMulheres = altura # define a menor altura das mulheres
            somaAlturaMulheres += altura # inicia a somatória das alturas das mulheres
            contadorMulheres += 1 # inicia a contagem das mulheres
        else: # se for mulher e não for a primeira pessoa, entra nesta condição
            if altura >= maiorAlturaMulheres: # se a altura for maior ou igual que a maior altura das mulheres, entra nesta condição
                maiorAlturaMulheres = altura # define a maior altura feminina
                somaAlturaMulheres += altura # continua a somatória das alturas das mulheres
                contadorMulheres += 1 # continua a contagem das mulheres
            else: # se a altura não for maior ou igual à maior altura, entra nesta condição
                menorAlturaMulheres = altura # define a menor altura feminina
                somaAlturaMulheres += altura # continua a somatória das alturas das mulheres
                contadorMulheres += 1 # continua a contagem das mulheres

if (contadorHomens != 0): # se tiver homem, entra nesta condição
    mediaAlturaHomens = somaAlturaHomens / contadorHomens # calcula a média das alturas dos homens
    if maiorAlturaHomens > maiorAlturaMulheres: # se a maior altura dos homens for maior que a maior altura das mulheres, entra nesta condição
        maiorAltura = maiorAlturaHomens # define a maior altura vindo das alturas dos homens
    else: # se a maior altura dos homens não for maior que a maior altura das mulheres, entra nesta condição
        maiorAltura = maiorAlturaMulheres # define a maior altura vindo das alturas das mulheres
else: # se não tiver homem, entra nesta condição
    mediaPopulacao = mediaAlturaMulheres # define a média das alturas vindo da média das alturas das mulheres
    menorAltura = menorAlturaMulheres # define a menor altura vindo da menor altura das mulheres

if (contadorMulheres != 0): # se tiver mulher, entra nesta condição
    mediaAlturaMulheres = somaAlturaMulheres / contadorMulheres # calula a média das alturas das mulheres
    if maiorAlturaMulheres > maiorAlturaHomens: # se a maior altura das mulheres for maior que a maior altura dos homens, entra nesta condição
        maiorAltura = maiorAlturaMulheres # define a maior altura vindo das alturas das mulheres
    else: # se a maior altura das mulheres não for maior que a maior altura dos homens, entra nesta condição
        maiorAltura = menorAlturaHomens # define a maior altura vindo das alturas dos homens
else: # se não tiver mulher, entra nesta condição
    mediaPopulacao = mediaAlturaHomens # define a média das alturas vindo da média das alturas dos homens
    menorAltura = menorAlturaHomens # define a menor altura vindo da menor altura dos homens

if (contadorMulheres != 0 and contadorHomens != 0): # se tiver mulher e homem, entra nesta condição
    mediaPopulacao = (somaAlturaHomens + somaAlturaMulheres) / (contadorHomens + contadorMulheres) # define a média das alturas da população

percentualHomens = contadorHomens * 100 / (contadorHomens + contadorMulheres) # define o percentual de homens na população

print(f"\nA maior altura é: {maiorAltura} metros")
print(f"\nA menor altura é: {menorAltura} metros")
print(f"\nA média de altura das mulheres é: {mediaAlturaMulheres} metros")
print(f"\nA média de altura da população é: {mediaPopulacao} metros")
print(f"\nO percentual de homens da população é: {percentualHomens} %")

# Questão 4

print(f"\nQuestão 4. Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório.")
print(f"\nSuponha que os números digitados são um intervalo crescente.")
print(f"\nExemplo:")
print(f"\n- Limite inferior: 3")
print(f"\n- Limite superior: 12")
print(f"\n- Saída: 4 6 8 10")
print(f"\n- Soma: 28")

soma = 0 # declaração das variáveis que serão utilizadas
inferior = int(input("\nQual o limite inferior do intervalo? "))
superior = int(input("Qual o limite superior do intervalo? "))

for i in range (inferior + 1, superior): # Intervalo Aberto, ou seja, não entra o inferior, nem o superior
    if i % 2 == 0: # verifica se o i é par
        if i < superior: # condição pra imprimir o sinal de + entre os números pares (exceto depois do último)
            print(f"{i} + ", end="")
        else: # condição pra imprimir o = depois do último
            print(f"{i} = ", end="")
        soma += i # define a somatória dos números pares

print(f"\nSoma: {soma}")