from Views.index import getLinguagens, getNivelDeConhecimento


def controllerProgramadorLinguagem (pk_Username) :
    print("\t\t -> Digite as linguagens que você conhece: ")
    languages = []
    knowledge = []

    i = 1
    end = False
    while end == False:
        languages.append(input(getLinguagens (i)))
        lastElement = languages[-1]
        if lastElement != "FIM":
            knowledge.append(input(getNivelDeConhecimento(i)))
        if lastElement == "FIM":
            end = True
            del languages[-1]
            languageValues = '%s' %'\'), (\''.join(map(str, languages))
            knowledgeValues = '%s' %'\'), (\''.join(map(str, knowledge))
        i += 1
    languageKnowledge = ""
    for x in range(len(languages)):
        languageKnowledge+=("(\'%s\', \'%s\', \'%s\'), " %(pk_Username, str(languages[x]), str(knowledge[x])))
    languagesKnowledgesValues = languageKnowledge[:-2]

    return languagesKnowledgesValues

def controllerPrintTableOne (x, columnA) :
    print("\t\n%s" % columnA)
    for columnA in x:
        print("%s" % columnA)

def controllerPrintTableFour(x, columnA, columnB, columnC, columnD) :
    print("\n{:<15} {:<15} {:<25} {:<6}".format(columnA, columnB, columnC, columnD))
    for (columnA, columnB, columnC, columnD) in x:
        print("{:<15} {:<15} {:<25} {:<6}".format(columnA, columnB, columnC, columnD))