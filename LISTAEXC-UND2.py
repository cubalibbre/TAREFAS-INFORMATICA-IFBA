# 1
n=0
for i in range(10):
  n2=int(input("Digite um número:"))
  n+=n2
print(f"A soma de todos os números é {n}")
# 2
n=0
pares=0
for i in range(20):
  n=int(input("Insira um numero:"))
  if n%2==0:
    pares+=1
  n=0
print(f"Foram inseridos {pares} números pares")
# 2.1
import random
n=0
pares=0
for i in range(20):
  #n=int(input("Insira um numero:"))
  n = random.randint
  if n%2==0:
    pares+=1
  n=0
print(f"Foram inseridos {pares} números pares")
# 3
soma=0
n=0
for i in range(5):
  n=int(input("Insira uma idade:"))
  soma+=n
media=soma/5
print(f"A média das idades inseridas é {media}")
# 4
n=int(input("Insira um número inteiro e positivo:"))
fatorial=1
for i in range(n):
    fatorial=fatorial*(n-i)
print(f"O fatorial de {n} é {fatorial}")
# 5
produto=1
for i in range(10):
    if i%2==1:
        produto=produto*i
print(f"O produto é {produto}")
# 6
palavra = input("Digite uma palavra: ")
As = 0
for i in palavra:
    if i == 'A' or i == 'a':
        As += 1
print(f"A letra 'A' aparece {As} vezes na palavra {palavra}.")
# 7
soma=0
for i in range(6):
    soma+=i*i
print(f"A soma dos quadrados dos 5 primeiros números inteiros é {soma}")
# 8
import random
aprovados=0
for i in range(10):
    #nota=float(input("Insira uma nota:"))
    nota= random.uniform (0,10)
    print(round(nota,2))
    if nota>=7.0:
        aprovados+=1
print(f"Foram aprovados {aprovados} alunos")
# 9
soma=0
for i in range(31):
    if i%3==0:
        soma+=i
print(f"A soma de todos os multiplos de 3 entre 1 e 30 é {soma}.")
# 10
import random
maior=0
for i in range(10):     
    #n=int(input("Insira um número:"))
    n=random.randint (0,100000)
    if n>maior:
        maior=n
print(f"O maior número inserido foi {maior}")
# 11
idade=int(input("Insira uma idade:"))
menor=idade
for i in range (4):
    idade = int(input("Insira uma idade:"))
    if idade<menor:
        menor=idade
print(f"A menor idade inserida foi {menor}")
# 12
import random
#n=int(input("Insira um número:"))
num= random.randint(-10000,10000)
maior=menor=num
for i in range(7):
    # num=int(input("Insira um número:"))
    num=random.randint(-10000,10000)
    if num > maior:
        maior=num
    elif num<menor:
        menor=num
dif= maior-menor
print (f"A diferença entre o maior ({maior}) e o menor ({menor}) número inseridos é {dif}")
# 13 INCOMPLETA
n=float(input("Insira um número:"))
pertode0=n
for i in range(7):
    n = float(input("Insira um número:"))
    if n


    print(pertode0)
print(f"O número mais perto de 0 é {pertode0}")
# 14
import random
# nota=float(input("Insira a nota:"))
nota=round(random.uniform(0,10),2)
print(nota)
maior=nota
for i in range(14):
    # nota=float(input("Insira a nota:"))
    nota=round(random.uniform(0,10),2)
    print(nota)
    if nota>maior:
        maior=nota
print(f"A maior nota da turma foi {maior}")
# 15
num=float(input("Insira um número:"))
menor=num
for i in range (11):
    num = float(input("Insira um número:"))
    if num<menor:
        menor=num
print(f"O menor valor inserido foi {menor}")
# 16
import random
num= round(random.uniform(-20,45),2)
maior=menor=num
for i in range(7):
    num=round(random.uniform(-20,45),2)
    if num > maior:
        maior=num
    elif num<menor:
        menor=num
print(f"A menor temperatura foi {menor} e a maior foi {maior}.")
# 17
somasalarios=0
somafilhos=0
numentrevistados=0
maiorsalario=0
salariosbaixo=0
for i in range(int(10e8)): #inicia as entradas
    salario = float(input("Digite o valor do salário (ou um salário negativo para encerrar):"))
    num_filhos = int(input("Digite o número de filhos:"))
    if salario < 0: #condição para que termine a leitura das entradas
        break
    if num_filhos > 100: #considerando que isso é impossível, se acontecer, pula o resto dos testes e vai pra próxima execução do loop
        continue
    somasalarios += salario
    somafilhos += num_filhos
    numentrevistados += 1
    if salario > maiorsalario:
        maiorsalario = salario
    if salario < 150:
        salariosbaixo +=1
if numentrevistados == 0:
    print("Não houveram entrevistados.")
else:print(f"A média salarial foi: {mediasalarial}")
    mediafilhos= somafilhos/numentrevistados    
    porcentagemsalbaixo = salariosbaixo/numentrevistados * 100
    print(f"A média salarial foi: {mediasalarial}")
    print(f"A média de filhos foi: {mediafilhos}")
    print(f"O maior salário foi: {maiorsalario}")
    print(f"A porcentagem de salários abaixo de R$150,00 foi: {porcentagemsalbaixo}")
