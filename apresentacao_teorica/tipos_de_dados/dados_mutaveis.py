

array = bytearray(10)  # cria um array de 10 bytes preenchido com 0 em todas a posições
conjunto = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 7}  # {1, 2, 3, 4, 5, 7}
lista = [1, 2, 3, 4, 5, "Python", True, array, conjunto]
dicionario = {'a': 1, 'b': 2, 'c': 3, 'bytearray': array, "conjunto": conjunto, 'lista': lista}

print("\nbytearray:", array)
print("\nconjunto:", conjunto)
print("\nlista:", lista)
print("\ndicionario:", dicionario)

input()

# bytearray é um array de bytes:
print("\nbytearray: ")
print("\nExemplo 1: ")
array = bytearray(10)  # cria um array de 10 bytes preenchido com 0 em todas a posições
print(type(array))
print(array)

print("\nExemplo 2: ")
string = "Python é interessante."
# string with encoding 'utf-8'
array = bytearray(string, 'utf-8')
print(array)
print(array.decode('utf-8'))

input()

# list é um array de objetos:
print("\nlist: ")
lista = [1, 2, 3, 4, 5]
print(type(lista))
print(lista)
lista[0] = 10
print(lista)
lista.append(6)
print(lista)
lista.remove(3)
print(lista)

input()

# dict é um dicionário que apresenta chave e valor:
print("\ndict: ")
dicionario = {'a': 1, 'b': 2, 'c': 3, 'array': array, 'lista': lista}
print(type(dicionario))
print(dicionario)

input()

# set é um conjunto de objetos, similar a lista, mas não tem índice e não pode ter repetições:
print("\nset: ")
conjunto = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 7, "frutas", "carros", "palavras", array}
print(type(conjunto))
print(conjunto)
# print(conjunto[0]) # erro
