#conexao com o banco de dados

#1 - instalar o drive conector
#Mysqlconnector

#o drivee um tradutor python --> mysql

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
    # o drive tenta abrir uma conexao
    host = 'localhost', 
    user = 'root',
    password = '',
    database = 'metalsul_industrial',
    port = 3306
)
    return conexao



