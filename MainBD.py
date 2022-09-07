import mysql.connector
from mysql.connector import Error

def RodaScriptSQL(NameScript):
    fd = open(NameScript, 'r')
    sqlFile = fd.read()
    fd.close()
    CommandsSQL = sqlFile.split(';')
    for Command in CommandsSQL:
        try:
            cursor.execute(Command)
        except Error as e:
            print("comando pulado: ",e)

def ChamaCamadaPersistenciaLogin(param1,param2):
    Comando = "SELECT * FROM ContaUsuario WHERE Login = \'"+param1+"\' AND Senha = \'"+param2+"\';"
    try:
        cursor.execute(Comando)
        record = cursor.fetchall()
        if record:
            return True
        else:
            return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaRegistro(param1,param2):
    Comando = "SELECT * FROM ContaUsuario WHERE Login = '"+param1+"';"
    try:
        cursor.execute(Comando)
        record = cursor.fetchall()
        if not record and (param1 and param2):
            Comando = "INSERT INTO ContaUsuario(Login,Senha) VALUES ('"+param1+"','"+param2+"');"
            cursor.execute(Comando)
            return True
        else:
            return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaServidor():
    Comando = " SELECT Nome FROM Servidor"
    try:
        cursor.execute(Comando)
        record = cursor.fetchall()
        if record:
            return record
        else:
            return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        database = 'ProjetoBD',
        user = 'root',
        password = 'zedes123'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        RodaScriptSQL('CriaBanco.sql')
except Error as e:
    print("Erro ao tentar conectar com o banco de dados: ",e)
#finally:  
    #if connection.is_connected():
    #    cursor.close()
    #    connection.close()
    #    print("conexão com o MYSQL foi fechada")
