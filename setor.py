from database import conectar

def listar_setor():
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    select nome, id_setor, localizacao from setor
    '''
    
    cursor.execute(sql)
    dados = cursor.fetchall()
    
    for setor in dados:
        print(setor)
        
    cursor.close()
    conexao.close()
    

def criar_setor(nome, localizacao):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    insert into setor (nome, localizacao)
    values
    (%s, %s)
    '''
    
    valores = (nome, localizacao)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Setores adicionados")
    
    cursor.close()
    conexao.close()
    
    
def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    delete from setor
    where id_setor = %s
    '''
    
    valores = (id_setor,)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("setor deletado")
    
    cursor.close()
    conexao.close()
    
    
def atualizar_setor(nome, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    update setor
    set nome = %s
    where id_setor = %s
    '''
    valores = (nome, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Setor atualizado com sucesso!")

    cursor.close()
    conexao.close()
    
    