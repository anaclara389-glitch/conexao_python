from database import conectar

def listar_fornecedor():
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    select razao_social, id_fornecedor, telefone, cnpj, cidade  from fornecedor
    '''
    
    cursor.execute(sql)
    dados = cursor.fetchall()
    
    for fornecedor in dados:
        print(fornecedor)
        
    cursor.close()
    conexao.close()


def criar_fornecedor(razao_social, id_fornecedor, telefone, cnpj, cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    insert into fornecedor
        (razao_social, id_fornecedor, telefone, cnpj, cidade)
    values
    (%s, %s, %s, %s, %s)
    '''

    valores = (razao_social, id_fornecedor, telefone, cnpj, cidade)
    cursor.execute(sql, valores)
    conexao.commit()


    print("fornecedor novo ok!")
    cursor.close()
    conexao.close()

def atualizar_fornecedor(razao_social, id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    update fornecedor
    set razao_social = %s
    where id_fornecedor = %s
    '''
    valores = (razao_social, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Fornecedor atualizado ok")

    cursor.close()
    conexao.close()

def deletar_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    delete from fornecedor 
    where id_fornecedor = %s
    '''
    
    valores = (id_fornecedor,)
    cursor.execute(sql, (valores))
    conexao.commit()
    
    print("fornecedor deletado")
    
    cursor.close()
    conexao.close()