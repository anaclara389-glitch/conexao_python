from database import conectar

def listar_produto():
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    select P.id_produto, 
    P.nome, 
    P.descricao, 
    P.preco_fabricacao, 
    P.quantidade_estoque, 
    C.nome, 
    F.razao_social  
    from produto as P
    join categoria_produto as C on C.id_categoria = P.id_categoria
    join fornecedor as F on F.id_fornecedor = P.id_fornecedor
    '''
    
    cursor.execute(sql)
    produtos = cursor.fetchall()
    
    for produto in produtos: 
        print(f"\n ID:{produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Descrição: {produto[2]}")
        print(f"Preço fabricação: {produto[3]}")
        print(f"Estoque: {produto[4]}")
        print(f"Categoria: {produto[5]}")
    
        print("-" * 40)
        
    cursor.close()
    conexao.close()

def criar_produto(id_produto, nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    insert into produto
        (id_produto, nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor)
    values
    (%s, %s, %s, %s, %s, %s, %s)
    '''

    valores = (id_produto, nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()


    print("Produto novo ok!")
    cursor.close()
    conexao.close()

def atualizar_preco_produto(preco_fabricacao, id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    update produto
    set preco_fabricacao = %s
    where id_produto = %s
    '''
    valores = (preco_fabricacao, id_produto)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Preço do produto atualizado ok")

    cursor.close()
    conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = '''
    delete from produto 
    where id_produto = %s
    '''
    
    valores = (id_produto,)
    cursor.execute(sql, (valores))
    conexao.commit()
    
    print("produto deletado com sucesso!")
    
    cursor.close()
    conexao.close()