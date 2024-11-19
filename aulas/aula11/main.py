from Pessoa import *
import os
def limpar(): os.system('clear')

limpar()
def pergunta():
    res = int(input("deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÂO: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salario da pessoa: "))

    cadastro.append(Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("N°", "Nome", "Idade", "Cargo", "Salário"))
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format (y,
                       x.get_nome(),
                       x.get_idade(),
                       x.get_cargo(),
                       x.get_salario()))
        y=+1
        
mostrar()


def alterar(x, op, valor):
    if(op == 0): cadastro[x].set_nome(valor)
    if(op == 1): cadastro[x].set_idade(valor)
    if(op == 2): cadastro[x].set_cargo(valor)
    if(op == 3): cadastro[x].set_salario(valor)

alterar(0,0,"Maria")
mostrar()



        


    