#from Views.index import getLinguagens, getNivelDeConhecimento


def controllerProgramadorLinguagem (a) :
    print("\t\t-> Digite as linguagens que você conhece ")
    linguagens = []
    levels = []

    linguagem = input("\t\tInsira a linguagem ou digite FIM: ")
    while linguagem != "FIM":
        linguagens.append(linguagem)
        level = input("\t\tNível de Conhecimento: Iniciante, Intermediário ou Avançado? ")
        levels.append(level)
        linguagem = input("\t\tInsira a linguagem ou digite FIM: ")

    values = []
    for x in range(len(levels)):
        values.append("('{}', '{}', '{}')".format(a, linguagens[x], levels[x]))
    return values

def controllerPrintTableOne (x, columnA) :
    print("\t\n%s" % columnA)
    for columnA in x:
        print("%s" % columnA)

def controllerPrintTableFour(x, columnA, columnB, columnC, columnD) :
    print("\n{:<15} {:<15} {:<25} {:<6}".format(columnA, columnB, columnC, columnD))
    for (columnA, columnB, columnC, columnD) in x:
        print("{:<15} {:<15} {:<25} {:<6}".format(columnA, columnB, columnC, columnD))
