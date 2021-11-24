
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def printPessoa(self):
        # print("\nNome: ", self.nome, "Idade: ", self.idade, "CPF: ", self.__cpf, sep='\n')
        print("Nome: ", self.nome, sep=" ", end="\n")
        print("Idade: ", self.idade, sep=" ", end="\n")
        print("CPF: ", self.__cpf, sep=" ", end="\n")


if __name__ == '__main__':
    pessoa = Pessoa("João", 20, "123.456.789-10")
    pessoa.printPessoa()
