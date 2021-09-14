def returnInsertProgramador () :
    insertProgramador = (
            """INSERT INTO programador(
                Username, 
                Email, 
                Primeiro_Nome, 
                Ultimo_Nome, 
                Senha, 
                Ano_de_Nascimento, 
                Linkedin)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        )
    return insertProgramador 


def returnValueProgramador (username, email, primeiroNome, ultimoNome, senha, anoDeNascimento, linkedin) :
    value = (username, email, primeiroNome, ultimoNome, senha, anoDeNascimento, linkedin)
    return value

def returnInsertProgramadorLinguagem () :
    insertProgramadorLinguagem = (
            """INSERT INTO programador_linguagem (
                Username, 
                Linguagem, 
                Nivel_de_Conhecimento
            ) 
            VALUES {}"""
        )
    return insertProgramadorLinguagem 

def returnQueryLinguagens ():
    queryLinguagens = "SELECT pk_Nome FROM aplicativoajudae.linguagem"
    return queryLinguagens

def returnQueryLinguagem ():
    queryLinguagem = "SELECT idDesafio, Linguagem_Do_Desafio, Titulo, Criado_Por FROM aplicativoajudae.desafio WHERE Linguagem_Do_Desafio LIKE '%{}%' AND Solucionado = 0"
    return queryLinguagem
