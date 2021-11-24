# Exemplificando a imutabilidade
print("\nExemplificando imutabilidade: ")
variavel = 10  # tipo int
print(variavel)
print(id(variavel))
print()

variavel = "20"  # tipo str
# variavel[0] = "2" # não é possível alterar o valor de uma variavel imutável
print(variavel)
print(id(variavel))
print()

variavel = 30.5  # tipo float
print(variavel)
print(id(variavel))
print()

variavel = (1, 2, 3)
# variavel[1] = 4 # não é possível alterar o valor de uma variavel imutável
print(variavel)
print(id(variavel))
print()
