def getFirstResponse () :
    firstResponse = int(input("""
    \n # # # # # # APLICATIVO AJUDAÊ # # # # # # 
    \n\t O que você deseja fazer? 
    \t[1] Cadastrar informações
    \t[2] Editar informações
    \t[3] Visualizar informações
    \t-> """))

    return firstResponse

def getInsertResponse () :
    InsertResponse = int(input("""
    \n\t Digite o número correspondente à sua solicitação 
    \t[1] Criar seu cadastro como programador
    \t[2] Criar um novo desafio
    \t-> """))

    return InsertResponse

def getLinguagens (i) :
    linguagemText = "\t\tLinguagem 0" + str(i) +" (ou FIM para encerrar): "
    return linguagemText

def getNivelDeConhecimento (i) :
    nivelDeConhecimentoText = "\t- Nível de conhecimento na linguagem 0" + str(i) +": "
    return nivelDeConhecimentoText

def getQueryResponse () :
    queryResponse = int(input("""
    \n\t Digite o número correspondente à sua solicitação 
    \t[1] Visualizar todas as linguagens cadastradas na plataforma
    \t[2] Visualizar desafios não solucionados por linguagem
    \t-> """))

    return queryResponse  

def getQueryLinguagemEntry () :
    queryLinguagemEntry = input("Você quer ver desafios de que linguagem? ")

    return queryLinguagemEntry   




