def returnQueryLinguagens ():
    queryLinguagens = "SELECT * FROM aplicativoajudae.linguagem"
    return queryLinguagens

def returnQueryLinguagem ():
    queryLinguagem = "SELECT idDesafio, Linguagem_Do_Desafio, Descricao, Criado_Por FROM aplicativoajudae.desafio WHERE Linguagem_Do_Desafio LIKE '%{}%' AND Solucionado = 0"
    return queryLinguagem
