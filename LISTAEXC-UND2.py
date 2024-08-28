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
#3
soma=0
n=0
for i in range(5):
  n=int(input("Insira uma idade:"))
  soma+=n
media=soma/5
print(f"A média das idades inseridas é {media}")
