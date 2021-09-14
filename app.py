from Views.index import getFirstResponse, getInsertResponse, getQueryLinguagemEntry, getQueryResponse
from Controller.controller import controllerPrintTableOne, controllerPrintTableFour, controllerProgramadorLinguagem
from SQLCommands.dmlManipulation import returnInsertProgramador, returnValueProgramador, returnInsertProgramadorLinguagem
from SQLCommands.ddlDefinition import createTableDesafio, createTableEncontro, createTableEncontroProgramador, createTableLinguagem, createTableProgramador, createTableProgramadorLinguagem
from SQLCommands.dqlQuery import returnQueryLinguagem, returnQueryLinguagens

import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database='aplicativoajudae')

cursor = cnx.cursor()

createTableProgramador()
createTableLinguagem()
createTableProgramadorLinguagem()
createTableDesafio()
createTableEncontro()
createTableEncontroProgramador()

# # 0 TELA DE INTRODUÇÃO
firstResponse = getFirstResponse()

# # 1 INSERÇÃO DE DADOS
if firstResponse == 1:
    insertResponse = getInsertResponse()

# a) Cadastrar novo programador
    if insertResponse == 1:
        print("\t\nInsira suas informações")  
        firstName = input("\tPrimeiro Nome: ")
        lastName = input("\tÚltimo Nome: ")
        email = input("\tE-mail: ")
        password = input("\tSenha: ")
        username = input("\tUsername: ")
        yearOfBirth = int(input("\tAno de nascimento: "))
        linkedin = input("\tLinkedin: ")

        insertProgramador = returnInsertProgramador ()
        valueProgramador = returnValueProgramador(username, email, firstName, lastName, password, yearOfBirth, linkedin)
        cursor.execute(insertProgramador,valueProgramador)
        cnx.commit()

        insertProgramadorLinguagem = returnInsertProgramadorLinguagem()
        languagesKnowledgesValues = controllerProgramadorLinguagem(username)
        cursor.execute(insertProgramadorLinguagem, languagesKnowledgesValues)
        cnx.commit()

# b) Cadastrar novo desafio        
    if insertResponse == 2:
        createTableDesafio()
        createTableLinguagem()
        description = input("\tDescreva seu problema. Se necessário, insira o trecho de código: ")
        title = input("\tInsira um breve título que descreva seu problema: ")
        errorIDE = input("\tSua IDE retorna algum erro? Se sim, insira: ")
        challengeLanguage = input("\tQual a linguagem de programação? ")
        pk_Username = input("\tInsira seu username: ")

        insertquery = (
            """INSERT INTO desafio(
                Titulo, 
                Descricao, 
                Erro, 
                Linguagem_do_Desafio, 
                Criado_Por)
                VALUES (%s, %s, %s, %s, %s)"""
        )
        value = (title, description, errorIDE, challengeLanguage, pk_Username)
        cursor.execute(insertquery, value)
        cnx.commit()


# # 2 EDIÇÃO DE DADOS
#if firstUserResponse == 2:

# # 3 VISUALIZAR INFORMAÇÕES:
if firstResponse == 3:
    queryResponse = getQueryResponse()

# 4.1 Visualizar todas as linguagens cadastradas na plataforma
    if queryResponse == 1:
        queryLinguagens = returnQueryLinguagens()
        cursor.execute(queryLinguagens)
        controllerPrintTableOne(cursor, "# Linguagens cadastradas na plataforma #")
        cnx.commit()
    
# 4.2 Visualizar desafios por linguagem
    if queryResponse == 2:
        queryLinguagemEntry = getQueryLinguagemEntry()
        queryLinguagem = returnQueryLinguagem()
        cursor.execute(queryLinguagem.format(queryLinguagemEntry))
        controllerPrintTableFour(cursor, "Id Desafio", "Linguagem", "Título", "Criado Por")
        cnx.commit()



cnx.close

