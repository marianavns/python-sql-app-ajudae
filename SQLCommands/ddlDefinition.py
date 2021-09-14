import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database='aplicativoajudae')

cursor = cnx.cursor()

#1 Tabela Programador
def createTableProgramador() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS programador(
            Username VARCHAR(45) NOT NULL,
            Email VARCHAR(45) NOT NULL UNIQUE,
            Primeiro_Nome VARCHAR(45) NOT NULL,
            Ultimo_Nome VARCHAR(45) NOT NULL,
            Senha VARCHAR(45) NOT NULL,
            Ano_de_Nascimento INT(4) NULL,
            Linkedin VARCHAR(100) NULL,
            PRIMARY KEY (Username)
        )
        """
    )


#2 Tabela Linguagem
def createTableLinguagem() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS linguagem(
            pk_Nome VARCHAR(45) NOT NULL,
            PRIMARY KEY (pk_Nome)
        )
        """
    )


#3 Tabela Programador_Linguagem
def createTableProgramadorLinguagem() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS programador_linguagem (
            Username VARCHAR(45) NOT NULL,
            Linguagem VARCHAR(45) NOT NULL,
            Nivel_De_Conhecimento ENUM(
                "Iniciante",
                "Intermediário",
                "Avançado"
            ) NULL,
            FOREIGN KEY (Username) REFERENCES programador(Username),
            FOREIGN KEY (Linguagem) REFERENCES Linguagem(pk_Nome)
        )
        """
    )



#4 Tabela Desafio
def createTableDesafio() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS desafio (
            idDesafio INT NOT NULL AUTO_INCREMENT,
            Titulo VARCHAR(45) NOT NULL,
            Descricao LONGTEXT NOT NULL,
            Erro VARCHAR(45) NULL,
            Solucionado TINYINT DEFAULT 0 NOT NULL,
            Linguagem_Do_Desafio VARCHAR(45) NOT NULL,
            Criado_Por VARCHAR(45) NOT NULL,
            PRIMARY KEY (idDesafio),
            FOREIGN KEY (Linguagem_Do_Desafio) REFERENCES linguagem(pk_Nome),
            FOREIGN KEY (Criado_Por) REFERENCES programador(Username)
        )
        """
    )


#5 Tabela Encontro
def createTableEncontro() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS encontro (
            idEncontro INT NOT NULL AUTO_INCREMENT,
            Desafio_Origem INT NOT NULL,
            Horario DATETIME(6) NOT NULL,
            Solicitado_Por VARCHAR(45) NOT NULL,
            Aceito_Por VARCHAR(45) NOT NULL,
            PRIMARY KEY (idEncontro),
            FOREIGN KEY (Solicitado_Por) REFERENCES programador(Username),
            FOREIGN KEY (Desafio_Origem) REFERENCES desafio(idDesafio),
            FOREIGN KEY (Aceito_Por) REFERENCES programador(Username)
        )
        """
    )


#6 Tabela Encontro_Programador
def createTableEncontroProgramador() :
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS encontro_programador(
            id_Encontro INT NOT NULL,
            Username VARCHAR(45) NOT NULL,
            FOREIGN KEY (Username) REFERENCES programador(Username),
            FOREIGN KEY (id_Encontro) REFERENCES encontro(idEncontro)
        )
        """
    )
