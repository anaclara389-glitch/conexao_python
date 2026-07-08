#from funcionario import listar_funcionarios
#from funcionario import cadastrar_funcionario
#from funcionario import atualizar_cargo
#from funcionario import deletar_funcionario

#from setor import criar_setor
#from setor import listar_setor
#from setor import deletar_setor
#from setor import atualizar_setor

#from fornecedor import listar_fornecedor
#from fornecedor import criar_fornecedor
#from fornecedor import atualizar_fornecedor
#from fornecedor import deletar_fornecedor

#from produto import listar_produto
#from produto import criar_produto
#from produto import atualizar_preco_produto
#from produto import deletar_produto



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
#deletar_setor(4)
#atualizar_setor('Pintura', 3)
#listar_setor()

#========================================================================================

#criar_fornecedor('Orkestria.Tech', 6, '(47)87883-0765', '84536499856745', 'Jaraguá do Sul')
#atualizar_fornecedor('Metal unique', '6')
#deletar_fornecedor(1)
#listar_fornecedor()

#===================================================================================
#criar_produto('9', 'torneira', 'torneira de aço inoxidável', 29.99, 44, 4, 2)
#atualizar_preco_produto(888.80, 5)
#deletar_produto(6)
#listar_produto()
#==========================================================================================

'''from funcionario import (
    listar_funcionarios,
    cadastrar_funcionario,
    atualizar_cargo,
    deletar_funcionario
)

while True:
    
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar cargo")
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
        cargo = input("Cargo: ")
        id_setor = int(input("ID setor: "))
        cpf = input("CPF: ")
        salario = float(input("Salario: "))
        data_admissao = input("Data de admissão (AAA-MM-DD): ")

        print(cadastrar_funcionario)
        
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
        print("Tente novamente...")'''