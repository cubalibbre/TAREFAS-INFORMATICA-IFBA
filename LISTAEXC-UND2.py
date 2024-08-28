#1
n=0
for i in range(10):
  n2=int(input("Digite um número:"))
  n+=n2
print(f"A soma de todos os números é {n}")
#2
n=0
pares=0
for i in range(20):
  n=int(input("Insira um numero:"))
  if n%2==0:
    pares+=1
  n=0
print(f"Foram inseridos {pares} números pares")
#2.1
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
#3
soma=0
n=0
for i in range(5):
  n=int(input("Insira uma idade:"))
  soma+=n
media=soma/5
print(f"A média das idades inseridas é {media}")
#4
n=int(input("Insira um número inteiro e positivo:"))
fatorial=1
for i in range(n):
    fatorial=fatorial*(n-i)
print(f"O fatorial de {n} é {fatorial}")
#5
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
menor=9999999
for i in range (5):
    idade = int(input("Insira uma idade:"))
    if idade<menor:
        menor=idade
print(f"A menor idade inserida foi {menor}")
