# O que é falso para Python?
variavel = False
print(variavel)  # False

variavel = bool('')
print(variavel)  # False

variavel = bool(0)
print(variavel)  # False

variavel = bool(())  # tupla vazia
print(variavel)  # False

tupla_elemento = 10,
# tupla_elemento = (10,)
print(tupla_elemento)  # (10,)

tuple([10, 10])  # tupla com 2 elementos
print(tuple((10, 10)))  # (10, 10)
