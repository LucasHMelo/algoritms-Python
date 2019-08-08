# coding: utf-8
valor = int(input("\nOla!!! Bem vindo ao caixa bancario.\n\n Digite A qtd para retirada: "))
print("\n\nA qtd eh", valor)
cem = valor//100
valor = valor - 100*cem
cinq = valor//50
valor = valor - 50*cinq
vinte = valor//20
valor = valor - 20*vinte
dez = valor//10
valor = valor - 10*dez
cinco = valor//5
valor = valor - 5*cinco
dois = valor//2
valor = valor - 2*dois
um = valor//1
valor = valor - 1*um

print("\n\nA qtd de notas de 100 eh", cem,"A qtd de notas de 50 eh", cinq,"A qtd de notas de 20 eh", vinte)
print("\nA qtd de notas de 10 eh", dez,"A qtd de notas de 5 eh", cinco,"A qtd de notas de 2 eh", dois)
print("\nA qtd de notas de 1 eh", um)



#Loteria
# from collections import Counter
# import random


# d = Counter()

# for i in range(1,10000000):
# 	n = random.randint(1, 60)
# 	d[n] += 1

# x = Counter(d).most_common(6)

# print(u'Números da sorte: ')
# for k, v in sorted(x):
# 	print(k)