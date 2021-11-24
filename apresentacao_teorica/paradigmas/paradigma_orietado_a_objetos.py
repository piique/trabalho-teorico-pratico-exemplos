import pessoa


class Funcionario(pessoa.Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def printFuncionario(self):
        print("------------------------------")
        super().printPessoa()
        print(f'Salário: {self.salario}', end="\n")
        print("------------------------------")


primeiro_funcionario = Funcionario("João", 20, "913.921.338-99", 2000)
segundo_funcionario = Funcionario("Maria", 25, "913.921.444-75", 3000)

primeiro_funcionario.printFuncionario()
segundo_funcionario.printFuncionario()
