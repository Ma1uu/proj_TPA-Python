class Pessoa:
    #classes do cadastro
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    #Chama o nome
    def get_nome(self):
        return self.nome
    
    def set_nome(self,nome):
        self.nome = nome

    #Chama a idade
    def get_idade(self):
        return self.idade
    
    def set_idade(self,idade):
        self.idade = idade

    #Chama o cargo
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self,cargo):
        self.cargo = cargo

    #Chama o salario
    def get_salario(self):
        return self.salario
    
    def set_salario(self,salario):
        self.salario = salario
