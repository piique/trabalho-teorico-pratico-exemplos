# pip install numpy

# importando biblioteca e confirmando a versão
import numpy as np
print("Versão Numpy:", np.version)
print()
input()

# criando um vetor a partir de uma lista em python
lista = [0, 5, 10, 15, 20]  # Criando a Lista
# Transformando a lista em vetor, utilizando 'np.array'
vetor = np.array(lista)
print("Vetor:", vetor)
print()
input()

# o vetor produzido pelo np.array é do tipo ndarray enquanto a lista 'lista' é do tipo list
print(type(vetor))
print(type(lista))
print()
input()

# ...
print(dir(list))
print(dir(np.array))
print()
input()

# obtendo a média dos valores inseridos no vetor
media_vetor = vetor.mean()
print("Média:", media_vetor)
print()
input()

soma_acumulada_vetor = vetor.cumsum()
print("Vetor:", vetor)
print("Soma:", soma_acumulada_vetor)
print()
input()

maximo = vetor.max()
minimo = vetor.min()
print("Maximo:", maximo)
print("Minimo:", minimo)
print()
input()


# Sendo:
# vetor = [0, 5, 10, 15, 20]
# soma_acumulada_vetor = [0, 5, 15, 30, 50]
#
# o que será que acontece se eu somar 'vetor + soma_acumulada_vetor'?
# a) os vetores serão concatenados em um só
# b) será somado os elementos dos vetores (primeiro com primeiro, segundo com segundo, etc..)
# c) N.d.a.
vetorzao = vetor + soma_acumulada_vetor
print("Vetozao:", vetorzao)
print()
input()


vetor_concatenado = np.concatenate((vetor, soma_acumulada_vetor, vetorzao))
print("Arrays concatenados:", vetor_concatenado)
print()
input()

# ---------------------------------------------------------

# Array unidimensional com 6 numero aleatorio entre 1 e 60
vetor = np.random.randint(1, 61, size=6)
print("Array unidimensional:", vetor)
print()
input()

# Array bidimensional com 9 numero aleatorio entre 1 e 20
vetor = np.random.randint(1, 21, size=(3, 3))
print("Array bidimensional:")
print(vetor)
input()
