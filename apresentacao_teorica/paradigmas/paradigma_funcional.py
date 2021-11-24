
import functools

numeros = [1, 2, 3, 4, 5]
potencia = lambda x, y=2: x ** y
lista = list(map(potencia, numeros))  # [1**2, 2**2, 3**2, 4**2, 5**2]
print(lista)  # [1, 4, 9, 16, 25]

# Somar todos os valores
lista = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, lista)  # ((((1+2)+3)+4)+5)
print(sum)  # 15
