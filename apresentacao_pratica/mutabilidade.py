teste = {True, 'string', 4.0}


variavel = "Uma string"
print(id(variavel))
print(variavel)

variavel = "outra string"
print(id(variavel))

variavel[0] = 'O'
print(variavel[1])

print(variavel)  # {False, 'string', 4.0}
