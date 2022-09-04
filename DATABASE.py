import mysql.connector
from mysql.connector import Error


def dados_local(id):

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select nome, nivel,idLocal from local where idLocal = (" \
                               "select Local_idLocal from personagem where idPersonagem = "+ str(id) + ")"
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            if connection.is_connected():
                connection.close()
                cursor.close()
            for row in records:
                return row[0], row[1], row[2]


    except Error as e:
        print("Error while connecting to MySQL", e)


def dados_jogador(id):

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select nome, nivel from personagem where idPersonagem = "+ str(id)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                Nome = row[0]
                Nivel = row[1]

            sql_select_query = "select a.nome, a.defesa, a.ataque, r.nome, r.defesa, r.ataque from arma a, roupa r where " \
                               "idArma = (select ArmaEquipada_idArma from personagem where idPersonagem = " + str(id) + ") "\
                               "and idRoupa = (select RoupaEquipada_idRoupa from personagem where idPersonagem = " + str(id) + ") "
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

def dados_monstro(id):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select nome, defesa, ataque, id from monstro where idMonstro = (" \
                               "select Monstro_idMonstro from local where idLocal = (" \
                               "select Local_idLocal from personagem where idPersonagem = "+str(id)+"))"
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

def itens_usando(id):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select Roupa.Nivel,Arma.Nivel from Roupa,Arma where idArma = (" \
                               "select ArmaEquipada_idArma from Personagem where idPersonagem = "+str(id)+")" \
                               " and idRoupa = (" \
                               "select RoupaEquipada_idRoupa from Personagem where idPersonagem = "+str(id)+")"
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

def armas_que_possui(id):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select COUNT(*) from personagem_has_arma where Personagem_idPersonagem = "+str(id)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()

            for row in records:
                Numero_Itens = row[0]
                break

            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Arma where idArma = (" \
                               "select Arma_idArma from personagem_has_arma where Personagem_idPersonagem =" + str(id) +")"
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

def roupas_que_possui(id):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        if connection.is_connected():
            sql_select_query = "select COUNT(*) from personagem_has_roupa where Personagem_idPersonagem = "+str(id)
            cursor = connection.cursor()
            cursor.execute(sql_select_query)
            # get all records
            records = cursor.fetchall()

            for row in records:
                Numero_Itens = row[0]
                break

            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Roupa where idRoupa = (" \
                               "select Roupa_idRoupa from personagem_has_roupa where Personagem_idPersonagem =" + str(id) +")"
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


