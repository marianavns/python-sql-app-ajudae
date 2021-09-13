def returnInsertProgramador () :
    insertProgramador = (
            """INSERT INTO programador(
                pk_Username, 
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
            "INSERT programador_linguagem (Username, Linguagem, Nivel_de_Conhecimento) VALUES (%s)"
        )
    return insertProgramadorLinguagem 