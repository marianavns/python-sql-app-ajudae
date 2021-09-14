def returnQueryLinguagens ():
    queryLinguagens = "SELECT pk_Nome FROM aplicativoajudae.linguagem"
    return queryLinguagens

def returnQueryLinguagem ():
    queryLinguagem = "SELECT idDesafio, Linguagem_Do_Desafio, Titulo, Criado_Por FROM aplicativoajudae.desafio WHERE Linguagem_Do_Desafio LIKE '%{}%' AND Solucionado = 0"
    return queryLinguagem


