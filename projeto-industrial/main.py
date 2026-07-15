from fornecedor import(
    listar_fornecedor,
    cadastrar_fornecedor,
    atualizar_cidade,
    remover_fornecedor
)

from funcionario import (
    listar_funcionarios,
    cadastrar_funcionario,
    atualizar_cargo,
    deletar_funcionario
    )

from produto import(
    listar_produto,
    criar_produto,
    atualizar_preco_produto,
    deletar_produto
)

from setor import(
    listar_setor,
    criar_setor,
    deletar_setor,
    atualizar_setor
)

from relatorios import(relatorio_producao_por_setor)
#-------------------------------------------------------------------------------------------

# ================= MENU PRINCIPAL =================
while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Gerenciar Funcionários")
    print("2 - Gerenciar Fornecedores")
    print("3 - Gerenciar Setores")
    print("4 - Gerenciar Produtos")
    print("5 - Visualisar relatórios")
    print("0 - Sair")

    opcao_principal = input("\nEscolha uma área de gestão: ")

    # ================= SUBMENU: FUNCIONÁRIOS =================
    if opcao_principal == "1":
        while True:
            print("\n--- GESTÃO DE FUNCIONÁRIOS ---")
            print("1 - Listar funcionários")
            print("2 - Cadastrar funcionário")
            print("3 - Atualizar cargo")
            print("4 - Remover funcionário")
            print("0 - Voltar ao Menu Principal")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "1":
                listar_funcionarios()
            elif op == "2":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                data_admissao = input("Data de admissão: ")
                id_setor = int(input("ID do setor: "))
                cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor)
                print("Funcionário cadastrado com sucesso!")

            elif op == "3":
                id_funcionario = int(input("ID do funcionário: "))
                novo_cargo = input("Novo Cargo: ")
                atualizar_cargo(id_funcionario, novo_cargo)
                print("Cargo atualizado!")

            elif op == "4":
                id_funcionario = int(input("ID do funcionário: "))
                deletar_funcionario(id_funcionario)
                print("Funcionário removido!")

            elif op == "0":
                break

            else:
                print("Opção inválida!")

    # ================= SUBMENU: FORNECEDORES =================
    elif opcao_principal == "2":
        while True:
            print("\n--- GESTÃO DE FORNECEDORES ---")
            print("1 - Listar fornecedores")
            print("2 - Cadastrar fornecedor")
            print("3 - Atualizar cidade do fornecedor")
            print("4 - Remover fornecedor")
            print("0 - Voltar ao Menu Principal")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "1":
                listar_fornecedor()
            elif op == "2":
                nome = input("Nome do Fornecedor: ")
                cnpj = input("CNPJ: ")
                cidade = input("Cidade: ")
                cadastrar_fornecedor(nome, cnpj, cidade) 
                print("Fornecedor cadastrado com sucesso!")

            elif op == "3":
                id_fornecedor = int(input("ID do fornecedor: "))
                nova_cidade = input("Nova Cidade: ")
                atualizar_cidade(id_fornecedor, nova_cidade)
                print("Cidade do fornecedor atualizada!")

            elif op == "4":
                id_fornecedor = int(input("ID do fornecedor: "))
                remover_fornecedor(id_fornecedor)
                print("Fornecedor removido!")

            elif op == "0":
                break

            else:
                print("Opção inválida!")

    # ================= SUBMENU: SETORES =================
    elif opcao_principal == "3":
        while True:
            print("\n--- GESTÃO DE SETORES ---")
            print("1 - Listar setores")
            print("2 - Criar setor")
            print("3 - Atualizar nome do setor")
            print("4 - Deletar setor")
            print("0 - Voltar ao Menu Principal")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "1":
                listar_setor()

            elif op == "2":
                nome = input("Nome do novo setor: ")
                localizacao = input("Localização do setor: ")
                criar_setor(nome, localizacao)
                print("Setor criado com sucesso!")

            elif op == "3":
                id_setor = int(input("ID do setor: "))
                novo_nome = input("Novo nome para o setor: ")
                atualizar_setor(id_setor, novo_nome)
                print("Setor actualizado!")

            elif op == "4":
                id_setor = int(input("ID do setor a deletar: "))
                deletar_setor(id_setor)
                print("Setor deletado!")

            elif op == "0":
                break

            else:
                print("Opção inválida!")

    # ================= SUBMENU: PRODUTOS =================
    elif opcao_principal == "4":
        while True:
            print("\n--- GESTÃO DE PRODUTOS ---")
            print("1 - Listar produtos")
            print("2 - Cadastrar produto")
            print("3 - Atualizar produto")
            print("4 - Remover produto")
            print("0 - Voltar ao Menu Principal")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "1":
                listar_produto()
            elif op == "2":
                nome_produto = input("Nome do Produto: ")
                preco = float(input("Preço: "))
                estoque = int(input("Quantidade em Estoque: "))
                id_fornecedor = int(input("ID do Fornecedor: "))
                criar_produto(nome_produto, preco, estoque, id_fornecedor)
                print("Produto cadastrado com sucesso!")

            elif op == "3":
                id_produto = int(input("ID do produto a atualizar: "))
                novo_preco = float(input("Novo preço do produto: "))
                atualizar_preco_produto(id_produto, novo_preco)
                print("Produto atualizado com sucesso!")

            elif op == "4":
                id_produto = int(input("ID do produto a remover: "))
                deletar_produto(id_produto)
                print("Produto removido com sucesso!")

            elif op == "0":
                break

            else:
                print("Opção inválida!")

    # ================= RELATÓRIOS =================
    elif opcao_principal == "5":
        relatorio_producao_por_setor()

    # ================= SAÍDA DO SISTEMA =================
    elif opcao_principal == "0":
        print("\nSistema encerrado.")
        break
    else:
        print("\nOpção inválida! Selecione uma opção válida do menu.")