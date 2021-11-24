import os

# Tipos numéricos
print("\nTipos numéricos: ")

# Tipo int
# declarações equivalentes
variavel = 10
variavel = int(10)
variavel = int('1010', 2)  # base 2
variavel = int('A', 16)  # base 16
print(type(variavel))  # <class 'int'>
print(variavel)  # 10

# Tipo float
# declarações equivalentes
variavel = 10.0
variavel = float(10.5)
variavel = float("10.5")
print(type(variavel))  # <class 'float'>
print(variavel)  # 10.5

# Tipo complex
# declarações equivalentes
variavel = 10 + 5j
variavel = complex(10, 5)
variavel = complex("10+5j")
print(type(variavel))  # <class 'complex'>
print(variavel)  # (10+5j)
print("Parte real: ",
      variavel.real,
      " Parte imaginaria: ",
      variavel.imag)  # Parte real:  10  Parte imaginaria:  5
print()

# Outros tipos
print("\nOutros tipos: ")

# Tipo bool
print("\nTipo bool: ")
# declarações equivalentes
variavel = True
variavel = bool(True)
variavel = bool(10)
variavel = bool([1, 2, 3])  # lista preenchida
print(type(variavel))  # <class 'bool'>
print(variavel)
# declarações equivalentes
variavel = False
variavel = bool(False)
variavel = bool(0)
variavel = bool(())  # tupla vazia
variavel = bool([])  # lista vazia
print(variavel)  # False
print()

# Tipo str
print("\nTipo str: ")
# declarações equivalentes
variavel = "Python é super interessante"
variavel = str("Python é super interessante")
print(type(variavel))  # <class 'str'>
print(variavel)  # Python é super interessante
print(variavel.upper())  # PYTHON É SUPER INTERESSANTE
print(variavel.lower())  # python é super interessante
print(variavel.title())  # Python É Super Interessante
print()

# Tipo bytes
print("\nTipo bytes: ")
variavel = bytes("Python e super interessante", "utf-8")
print(type(variavel))  # <class 'bytes'>
print(variavel)  # b'Python e super interessante'
variavel = bytes(5)  # 5 bytes de 0
print(variavel)  # b'\x00\x00\x00\x00\x00'
print()

# Tipo frozenset
print("\nTipo frozenset: ")
# decalarações equivalentes
variavel = frozenset([1, 2, 3])  # utilizando lista
variavel = frozenset((1, 3, 3, 3, 5))  # utilizando tupla
print(type(variavel))  # <class 'frozenset'>
print(variavel)  # frozenset({1, 2, 3})
print(variavel)  # frozenset({1, 3, 5})
print()

# Tipo range
print("\nTipo range: ")
# declarações equivalentes
variavel = range(5)  # 0, 1, 2, 3, 4
variavel = range(0, 5)  # range(inicio, fim)
variavel = range(0, 5, 1)  # range(inicio, fim, passo)
print(type(variavel))  # <class 'range'>
print(variavel)  # range(0, 5)
for n in variavel:
    print(n)  # 0 1 2 3 4
print()

# Tipo NoneType
print("\nTipo NoneType: ")
variavel = None
print(type(variavel))  # <class 'NoneType'>
print(variavel)  # None
print()

# Tipo tupla
print("\nTipo Tupla: ")
variavel = (1, 2, 2, [1, 2, 3], (1, 2, 3))
estado = ("MG", "Minas Gerais")
print(type(estado))  # <class 'tuple'>
print(estado)  # ('MG', 'Minas Gerais')
print(variavel)  # (1, 2, 2, [1, 2, 3], (1, 2, 3))
print()
