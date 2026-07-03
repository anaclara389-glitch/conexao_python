#Agora esse arquivo é um módulo
#responsável por funcionalidades referentes a funcionário
#listar funcionarios

from database import conectar

def listar_funcionarios():
    #abrir conexao
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #SQL da consulta
    sql ='''
    select
        f.id_funcionario, 
        f.nome,
        f.cargo,
        s.nome as setor,
        f.data_admissao,
        f.cpf,
        f.salario
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    '''
    #executa sql
    cursor.execute(sql)

    #recuperar dados
    dados = cursor.fetchall()


    #exibir resultados
    for funcionario in dados:
        print(funcionario)

    #fechar a conexao
    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cargo, id_setor, cpf, salario, data_admissao):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    insert into funcionario
        (nome, cargo, id_setor, cpf, salario, data_admissao)
    values
    (%s, %s, %s, %s, %s, %s)
    '''

    valores = (nome, cargo, id_setor, cpf, salario, data_admissao)
    cursor.execute(sql, valores)
    conexao.commit()


    print("funcionario ok")
    cursor.close()
    conexao.close()

def atualizar_cargo(cargo, id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    update funcionario
    set cargo = %s
    where id_funcionario = %s
    '''
    valores = (cargo, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()

    print("funcionario ok")

    cursor.close()
    conexao.close()
    
    
def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    delete from funcionario 
    where id_funcionario = %s
    '''
    
    valores = (id_funcionario,)
    cursor.execute(sql, (valores))
    conexao.commit()
    
    print("funcionario deletado")
    
    cursor.close()
    conexao.close()
    