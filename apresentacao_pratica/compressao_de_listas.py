from math import pi
# https://docs.python.org/3/tutorial/datastructures.html


# Exemplo 1
print("\nExemplo 1")
lista_quadrados = []
for x in range(10):
    lista_quadrados.append(x**2)
print(lista_quadrados)

lista_cubos = [x**3 for x in range(10)]
print(lista_cubos)


# Exemplo 2
print("\nExemplo 2")
pares = [(x, y) for x in [1, 2, 3, 4, 5, 6, 7, 8] for y in [1, 4, 7] if x == y]

outro_pares = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            outro_pares.append((x, y))

print(pares)
print(outro_pares)


# Exemplo 3
print("\nExemplo 3")
pi_list = [str(round(pi, i)) for i in range(1, 6)]
print(pi_list)
