import mysql.connector
from mysql.connector import Error
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

host = '127.0.0.1'
database = 'projetobd'
user = 'root'
password = 'password'
port = '3307'

"""
def RodaScriptSQL(NameScript):
    fd = open(NameScript, 'r')
    sqlFile = fd.read()
    fd.close()
    CommandsSQL = sqlFile.split(';')
    for Command in CommandsSQL:
        try:
            cursor.execute(Command)
            connection.commit()
        except Error as e:
            print("comando pulado: ",e)
"""

def ChamaCamadaPersistenciaCriaPersonagem(ListaChaves,param1,param2):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT * FROM Personagem WHERE Nome = '" + param1 + "'AND Servidor_NomeServidor = '" + ListaChaves[1] + "' AND ContaUsuario_Login = '" + ListaChaves[0] + "'"

            cursor.execute(Comando)
            record = cursor.fetchall()
            if not record:
                Comando = "SELECT idClasse FROM Classe WHERE Nome = '"+param2+"'"
                cursor.execute(Comando)
                record = cursor.fetchone()
                param2, = record
                if param1 and param2:
                    param2 = str(param2)
                    Comando = "SELECT idArma,idRoupa FROM Classe,Arma,Roupa WHERE Arma.Nivel = 1 AND Roupa.Nivel = 1 AND Classe.idClasse = Arma.Classe_idClasse AND Classe.idClasse = Roupa.Classe_idClasse AND Classe.idClasse ="+param2+";"
                    cursor.execute(Comando)
                    record = cursor.fetchone()
                    param3,param4 = record
                    param3 = str(param3)
                    param4 = str(param4)
                    Comando = "select min(idLocal) from Local"
                    cursor.execute(Comando)
                    record = cursor.fetchone()
                    param5 = record[0]
                    param5 = str(param5)

                    Comando = "INSERT INTO Personagem(Nome,Nivel,Servidor_NomeServidor,ContaUsuario_Login,ArmaEquipada_idArma,RoupaEquipada_idRoupa,Local_idLocal,Classe_idClasse) VALUES ('"+param1+"',1,'"+ListaChaves[1]+"','"+ListaChaves[0]+"','"+param3+"','"+param4+"',"+param5+","+param2+");"
                    cursor.execute(Comando)
                    Comando = "Select idPersonagem from Personagem where Nome='"+param1+"' and ContaUsuario_Login='"+ListaChaves[0]+"' and Servidor_NomeServidor='"+ListaChaves[1]+"'"
                    cursor.execute(Comando)
                    record = cursor.fetchone()
                    param6 = record[0]
                    param6 = str(param6)
                    Comando = "INSERT INTO personagem_has_arma VALUES ("+param6+",'"+ListaChaves[1]+"','"+ListaChaves[0]+"',"+param3+");"
                    cursor.execute(Comando)
                    Comando = "INSERT INTO personagem_has_roupa VALUES (" + param6 + ",'" + ListaChaves[1] + "','" +ListaChaves[0] + "'," + param4 + ");"
                    cursor.execute(Comando)
                    connection.commit()
                    connection.close()
                    cursor.close()
                    return True
                else:
                    return False
            else:
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaLogin(param1,param2):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT * FROM ContaUsuario WHERE Login = '" + param1 + "' AND Senha = '" + param2 + "';"
            cursor.execute(Comando)
            record = cursor.fetchone()
            connection.close()
            cursor.close()
            if record:
                return True
            else:
                return False

    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaRegistro(param1,param2,param3,param4,param5):

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT * FROM ContaUsuario WHERE Login = '" + param1 + "';"
            cursor.execute(Comando)
            record = cursor.fetchone()
            if not record and (param1 and param2 and param3 and param4 and param5):
                Comando = "INSERT INTO ContaUsuario(Login,Senha,Telefone,Email,Endereço) VALUES ('"+param1+"','"+param2+"','"+param3+"','"+param4+"','"+param5+"');"
                cursor.execute(Comando)
                connection.commit()
                connection.close()
                cursor.close()
                return True
            else:
                connection.close()
                cursor.close()
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaUpdateConta(ListaChaves,param1,param2,param3):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "UPDATE ContaUsuario SET Telefone = '" + param1 + "', Email = '" + param2 + "' Endereço = '" + param3 + "' WHERE Login = '" + ListaChaves[0] + "';"

            if(param1 and param2 and param3):
                cursor.execute(Comando)
                connection.commit()
                connection.close()
                cursor.close()
                return True
            else:
                connection.close()
                cursor.close()
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaServidor():
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT NomeServidor FROM Servidor"
            cursor.execute(Comando)
            record = cursor.fetchall()
            connection.close()
            cursor.close()
            if record:
                return record
            else:
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaEscolhePersonagem(ListaChaves):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT Nome FROM Personagem WHERE ContaUsuario_Login = '" + ListaChaves[0] + "' AND Servidor_NomeServidor = '" + ListaChaves[1] + "';"
            cursor.execute(Comando)
            record = cursor.fetchall()
            connection.close()
            cursor.close()
            if record:
                return record
            else:
                return []
    except Error as e:
        print("erro na execução do script: ",e)
    return False
    
def ChamaCamadaPersistenciaExcluiPersonagem(ListaChaves,param1):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "DELETE FROM Personagem_has_Arma WHERE Personagem_idPersonagem = (" \
                  "SELECT idPersonagem FROM PERSONAGEM WHERE Nome = '"+param1+"' AND ContaUsuario_Login = '"+ListaChaves[0]+"' AND Servidor_NomeServidor = '"+ListaChaves[1]+"');"
            cursor.execute(Comando)
            Comando = "DELETE FROM Personagem_has_Roupa WHERE Personagem_idPersonagem = (" \
                      "SELECT idPersonagem FROM PERSONAGEM WHERE NOME = '"+param1+"' AND ContaUsuario_Login = '"+ListaChaves[0]+"' AND Servidor_NomeServidor = '"+ListaChaves[1]+"');"
            cursor.execute(Comando)
            Comando ="DELETE FROM Personagem WHERE Nome = '"+param1+"' AND ContaUsuario_Login = '"+ListaChaves[0]+"' AND Servidor_NomeServidor = '"+ListaChaves[1]+"';"
            cursor.execute(Comando)
            connection.commit()
            connection.close()
            cursor.close()
            return True

    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaEscolheClasse():

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT Nome FROM Classe;"
            cursor.execute(Comando)
            record = cursor.fetchall()
            connection.close()
            cursor.close()
            if record:
                return record
            else:
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaExcluiConta(ListaChaves):

    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "DELETE FROM Personagem WHERE ContaUsuario_Login = '" + ListaChaves[0] + "';"
            cursor.execute(Comando)
            Comando = "DELETE FROM ContaUsuario WHERE Login = '"+ListaChaves[0]+"';"
            cursor.execute(Comando)
            connection.commit()
            connection.close()
            cursor.close()
            return True
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaUpdateNome(ListaChaves,param1):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "SELECT * FROM Personagem  WHERE Nome = '"+param1+"' AND ContaUsuario_Login = '"+ListaChaves[0]+"' AND Servidor_NomeServidor = '"+ListaChaves[1]+"';"
            cursor.execute(Comando)
            record = cursor.fetchone()
            if(not record and param1):
                Comando = "UPDATE Personagem SET Nome = '"+param1+"' WHERE Nome = '"+ListaChaves[2]+"' AND ContaUsuario_Login = '"+ListaChaves[0]+"' AND Servidor_NomeServidor = '"+ListaChaves[1]+"';"
                cursor.execute(Comando)
                connection.commit()
                connection.close()
                cursor.close()
                return True
            else:
                connection.close()
                cursor.close()
                return False
    except Error as e:
        print("erro na execução do script: ",e)
    return False

def ChamaCamadaPersistenciaRecuperaImagem(tela, nome_monstro):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            cursor = connection.cursor()
            sql_fetch_blob_query = "SELECT image from monstro where Nome = '"+nome_monstro+"'"
            cursor.execute(sql_fetch_blob_query)
            data = cursor.fetchone()
            tela.pixmap = QPixmap()
            if tela.pixmap.loadFromData(data[0]):
                tela.label_image.setPixmap(tela.pixmap)
                # Optional, resize label to image size

                tela.label_image.resize(tela.pixmap.width(),
                                  tela.pixmap.height())
            connection.close()
            cursor.close()

    except mysql.connector.Error as error:
        print("erro na execução do script: ",error)


"""
def Fechaconexao():
    if connection.is_connected():
        cursor.close()
        connection.close()
"""
def RecuperaIDpersonagem(ListaChaves):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "Select idPersonagem from personagem where ContaUsuario_Login = '" + ListaChaves[0] + "' AND Servidor_NomeServidor = '" + ListaChaves[1] + "' AND Nome = '" + ListaChaves[2] + "';"
            cursor.execute(Comando)
            record = cursor.fetchone()
            id, = record
            connection.close()
            cursor.close()
            return int(id)
    except Error as e:
        print("erro na execução do script: ",e)
    return 0

def ChamaCamadaPersistenciaDeletaItens(idPersonagem):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            cursor = connection.cursor()
            Comando = "select min(Arma_idArma) into @ids from personagem_has_arma INNER join Arma where idArma = Arma_idArma " \
                      "and Personagem_idPersonagem = "+str(idPersonagem)+";"
            cursor.execute(Comando)
            Comando = "DELETE FROM personagem_has_arma where Personagem_idPersonagem = "+str(idPersonagem)+" and Arma_idArma > @ids;"
            cursor.execute(Comando)
            Comando = "select min(Roupa_idRoupa) into @ids from personagem_has_roupa INNER join Roupa where idRoupa = Roupa_idRoupa " \
                      "and Personagem_idPersonagem = " + str(idPersonagem) + ";"
            cursor.execute(Comando)
            Comando = "DELETE FROM personagem_has_roupa where Personagem_idPersonagem = " + str(idPersonagem) + " and Roupa_idRoupa > @ids;"
            cursor.execute(Comando)
            Comando = "SELECT min(idLocal) into @idL from Local"
            cursor.execute(Comando)
            Comando = "UPDATE Personagem SET Nivel = 1, Local_idLocal = @idL where idPersonagem = " + str(idPersonagem)
            cursor.execute(Comando)
            connection.commit()
            connection.close()
            cursor.close()
            return True

    except Error as e:
        print("erro na execução do script: ",e)
    return False


######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################



def dados_local(idPersonagem):

    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select nome, nivel from local where idLocal = (" \
                               "select Local_idLocal from personagem where idPersonagem = "+ str(idPersonagem) + ")"
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            for row in records:
                return row[0], row[1]


    except Error as e:
        print("Error while connecting to MySQL", e)

def dados_jogador(idPersonagem):

    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select nome, nivel from personagem where idPersonagem = "+ str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                Nome = row[0]
                Nivel = row[1]

            sql_select_query = "select a.nome, a.defesa, a.ataque, r.nome, r.defesa, r.ataque from arma a, roupa r where " \
                               "idArma = (select ArmaEquipada_idArma from personagem where idPersonagem = " + str(idPersonagem) + ") "\
                               "and idRoupa = (select RoupaEquipada_idRoupa from personagem where idPersonagem = " + str(idPersonagem) + ") "
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            for row in records:
                Nome_Arma = row[0]
                Nome_Roupa = row[3]
                Defesa = row[1] + row[4]
                Ataque = row[2] + row[5]

            return Nome, Nivel, Nome_Arma, Nome_Roupa, Defesa, Ataque

    except Error as e:
        print("Error while connecting to MySQL", e)

def dados_monstro(idPersonagem):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select nome, ataque, defesa, nivel from monstro where idMonstro = (" \
                               "select Monstro_idMonstro from local where idLocal = (" \
                               "select Local_idLocal from personagem where idPersonagem = "+str(idPersonagem)+"))"
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                return row[0], row[1], row[2], row[3]
            if connection.is_connected():
                connection.close()
                cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)

def itens_usando(idPersonagem):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select Roupa.Nivel,Arma.Nivel from Roupa,Arma where idArma = (" \
                               "select ArmaEquipada_idArma from Personagem where idPersonagem = "+str(idPersonagem)+")" \
                               " and idRoupa = (" \
                               "select RoupaEquipada_idRoupa from Personagem where idPersonagem = "+str(idPersonagem)+")"
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            for row in records:
                return row[0], row[1]


    except Error as e:
        print("Error while connecting to MySQL", e)

def armas_que_possui(idPersonagem):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select COUNT(*) from personagem_has_arma where Personagem_idPersonagem = "+str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()

            for row in records:
                Numero_Itens = row[0]
                break
            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Arma INNER JOIN personagem_has_arma " \
                               "where idArma = Arma_idArma and Personagem_idPersonagem = " + str(idPersonagem)

            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            return Numero_Itens, records

    except Error as e:
        print("Error while connecting to MySQL", e)

def roupas_que_possui(idPersonagem):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select COUNT(*) from personagem_has_roupa where Personagem_idPersonagem = "+str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()

            for row in records:
                Numero_Itens = row[0]
                break

            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Roupa INNER JOIN personagem_has_roupa " \
                               "where idRoupa = Roupa_idRoupa and Personagem_idPersonagem = " + str(idPersonagem)

            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            return Numero_Itens, records

    except Error as e:
        print("Error while connecting to MySQL", e)

def prox_drop(idPersonagem):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)

        #tipo_drop = 0, arma
        #tipo_drop = 1, roupa
        tipo_drop = random.randrange(0, 2)
        args = (idPersonagem, tipo_drop, 0)

        if connection.is_connected():
            cursor = connection.cursor()
            result_args = cursor.callproc('busca_drops_monstro', args)
            id_drop = result_args[2]
            # print results
            if tipo_drop == 0:
                sql_select_query = "select nome, nivel, ataque, defesa from Arma where idArma = " + str(id_drop)
            else:
                sql_select_query = "select nome, nivel, ataque, defesa from Roupa where idRoupa = " + str(id_drop)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()

        if connection.is_connected():
            connection.close()
            cursor.close()
        for row in records:
            return row[0], row[1], row[2], row[3], tipo_drop, id_drop

    except Error as e:
        print("Error while connecting to MySQL", e)

def inserir_drop(idPersonagem, idDrop, tipoDrop):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)

        if connection.is_connected():
            #Arma
            if tipoDrop == 0:
                sql_select_query = "select Personagem_idPersonagem from personagem_has_arma where Arma_idArma = " +str(idDrop)+" " \
                                   "and Personagem_idPersonagem = " +str(idPersonagem)
                cursor = connection.cursor()
                cursor.execute(sql_select_query)
                # get all records
                records = cursor.fetchall()
                temItem = None
                for row in records:
                    temItem = row[0]
                    break

                if temItem == None:
                    args = (idPersonagem, idDrop)
                    cursor = connection.cursor()
                    cursor.callproc('insere_dados_inventario_arma', args)

            #Roupa
            elif tipoDrop == 1:
                sql_select_query = "select Personagem_idPersonagem from personagem_has_roupa where Roupa_idRoupa = " + str(idDrop) + " " \
                                   "and Personagem_idPersonagem = " + str(idPersonagem)
                cursor = connection.cursor()
                cursor.execute(sql_select_query)
                # get all records
                temItem = None
                records = cursor.fetchall()
                for row in records:
                    temItem = row[0]
                    break

                if temItem == None:
                    args = (idPersonagem, idDrop)
                    cursor = connection.cursor()
                    cursor.callproc('insere_dados_inventario_roupa', args)

        if connection.is_connected():
            connection.close()
            cursor.close()
        return 0
    except Error as e:
        print("Error while connecting to MySQL", e)

def nivel_up(idPersonagem):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select p.nivel, l.nivel from personagem p inner join local l where Local_idLocal = idLocal and idPersonagem =" + str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            nivel_atual = 1
            nivel_local = 1
            for row in records:
                nivel_atual = row[0]
                nivel_local = row[1]
                break
            if nivel_atual == nivel_local:
                sql_update_query = "update personagem set nivel = " +str(nivel_atual+1)+ " where idPersonagem = " +str(idPersonagem)
                cursor = connection.cursor()
                cursor.execute(sql_update_query)
                connection.commit()
            if connection.is_connected():
                connection.close()
                cursor.close()
            return 0
    except Error as e:
        print("Error while connecting to MySQL", e)

def atualizar_armas(idPersonagem, nivel_arma, nivel_roupa):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)

        idArma = 0
        idRoupa = 0
        if connection.is_connected():
            sql_select_query = "select idArma, idRoupa from ARMA, ROUPA  inner join personagem_has_arma pa,personagem_has_roupa pr " \
                               "where idArma = Arma_idArma and idRoupa = Roupa_idRoupa and " \
                               "roupa.nivel = "+str(nivel_roupa)+" and arma.nivel = " + str(nivel_arma) + " " \
                               "and pa.Personagem_idPersonagem = "+ str(idPersonagem) + " and pr.Personagem_idPersonagem = " + str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                idArma = row[0]
                idRoupa = row[1]
                break
            sql_update_query = "update personagem SET ArmaEquipada_idArma = "+str(idArma)+ ", RoupaEquipada_idRoupa = " +str(idRoupa) + " " \
                               "where idPersonagem = " + str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_update_query)
            connection.commit()

        if connection.is_connected():
            connection.close()
            cursor.close()
        return 0

    except Error as e:
        print("Error while connecting to MySQL", e)

def voltar_local(idPersonagem, nivel_local):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select idLocal from Local where nivel =" + str(nivel_local-1)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            novo_local = 1
            for row in records:
                novo_local = row[0]
            sql_update_query = "update personagem set Local_idLocal = " +str(novo_local)+ " where idPersonagem = " +str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_update_query)
            connection.commit()
            if connection.is_connected():
                connection.close()
                cursor.close()
            return 0
    except Error as e:
        print("Error while connecting to MySQL", e)

def avancar_local(idPersonagem, nivel_local):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password,
                                             port=port)
        if connection.is_connected():
            sql_select_query = "select idLocal from Local where nivel =" + str(nivel_local+1)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            novo_local = 1
            for row in records:
                novo_local = row[0]
            sql_update_query = "update personagem set Local_idLocal = " +str(novo_local)+ " where idPersonagem = " +str(idPersonagem)
            cursor = connection.cursor()
            cursor.execute(sql_update_query)
            connection.commit()
            if connection.is_connected():
                connection.close()
                cursor.close()
            return 0
    except Error as e:
        print("Error while connecting to MySQL", e)
"""
try:
    connection = mysql.connector.connect(
        host = host,
        database = database,
        user = user,
        password = password,
        port = port
    )
    if connection.is_connected():
        cursor = connection.cursor()
        
        RODAR ISSO AQUI NO INICIO DE TODO CÓDIGO TEM CARA DE SER O PIOR DOS CRIMES
        RodaScriptSQL('CriaBanco.sql')
        RodaScriptSQL('Inserir_Servidor.sql')
        RodaScriptSQL('Inserir_Classe.sql')
        RodaScriptSQL('Inserir_Arma.sql')
        RodaScriptSQL('Inserir_Roupa.sql')
        RodaScriptSQL('Inserir_Monstro.sql')
        RodaScriptSQL('Inserir_Local.sql')
        RodaScriptSQL('Inserir_Monstro_Arma.sql')
        RodaScriptSQL('Inserir_Monstro_Roupa.sql')
        connection.close()
        cursor.close()
        
except Error as e:
    print("Erro ao tentar conectar com o banco de dados: ",e)

"""
