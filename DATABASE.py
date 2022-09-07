import mysql.connector
from mysql.connector import Error
import random


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
            sql_select_query = "select nome, ataque, defesa, nivel from monstro where idMonstro = (" \
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
            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Arma INNER JOIN personagem_has_arma " \
                               "where idArma = Arma_idArma and Personagem_idPersonagem = " + str(id)

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

            sql_select_query = "select Nome,Nivel,Ataque,Defesa from Roupa INNER JOIN personagem_has_roupa " \
                               "where idRoupa = Roupa_idRoupa and Personagem_idPersonagem = " + str(id)

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

def prox_drop(id):
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')

        #tipo_drop = 0, arma
        #tipo_drop = 1, roupa
        tipo_drop = random.randrange(0, 2)
        args = (id, tipo_drop, 0)

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
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')

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
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
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
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
        idArma = 0
        idRoupa = 0
        if connection.is_connected():
            sql_select_query = "select idArma, idRoupa from ARMA, ROUPA inner join personagem_has_arma,personagem_has_roupa " \
                               "where idArma = Arma_idArma and idRoupa = Roupa_idRoupa and " \
                               "roupa.nivel = "+str(nivel_roupa)+" and arma.nivel = " + str(nivel_arma)
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
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
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
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='projetobd',
                                             user='root',
                                             password='password',
                                             port='3307')
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


