#from funcionario import listar_funcionarios
#from funcionario import cadastrar_funcionario
#from funcionario import atualizar_cargo
#from funcionario import deletar_funcionario

#from setor import criar_setor
#from setor import listar_setor
#from setor import deletar_setor


'''cadastrar_funcionario(
    "Fernando",
    "Auxiliar de Produção",
    2,
    "00000000455",
    2900.00,
    "2022-08-03"
)'''

'''atualizar_cargo(
    "Gerente",
    7
)'''

#deletar_funcionario(4)

#========================================================================================

#listar_funcionarios()
#criar_setor('Manutenção', 'Norte')
#deletar_setor(2)
#listar_setor()

#===================================================================================

from funcionario import (
    listar_funcionarios,
    cadastrar_funcionario,
    atualizar_cargo,
    deletar_funcionario
)

while True:
    
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar salário")
    print("4 - Remover funcionário")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")
    
    #listar 
    if opcao == "1":
        lista = listar_funcionarios()
        print(lista)
    
    #cadastrar    
    elif opcao == "2":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        cargo = input("Cargo: ")
        salario = input(float("Salario: "))
        data_admissao = input("Data de admissão (AAA-MM-DD): ")
        id_setor = int(input("ID setor: "))
        
        print("Funcionário cadastrado com sucesso!")
        #print(cadastrar_funcionario(nome, cargo, id_setor, cpf, salario, data_admissao))
    
    #atualizar
    elif opcao == "3":
        id_funcionario = input("ID funcionário: ")
        novo_cargo = input("Cargo: ")
        
        atualizar_cargo(novo_cargo, id_funcionario)
        
    #deletar
    elif opcao == "4":
        id_funcionario = input("ID Funcionário: ")
        
        deletar_funcionario(id_funcionario)
        
    #sair
    elif opcao == "0":
        print("tchau!")
        break
    
    else:
        print("Tente novamente...")