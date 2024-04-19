class Grammar:
    recursiveGrammar = {},
    noTerminals = [],
    grammar = {},
    first = [],
    follow = [],


def eliminateLeftRecursion(grammar, noTerminals):
    possibleTerminals = []

    # Define los no terminales posibles
    for noTerminal in noTerminals:
        possibleTerminals.append(noTerminal+"'")

    NewGrammar = {}
    NewNoTerminals = []

    needEliminate = False
    for noTerminal in noTerminals:
        if noTerminal not in NewNoTerminals:
            NewNoTerminals.append(noTerminal)
        if noTerminal not in NewGrammar:
            NewGrammar[noTerminal] = []
        for produccion in grammar[noTerminal]:
            # Si tiene Recursividad Izquierda
            if produccion[0] == noTerminal:
                needEliminate = True
                break
            else:
                needEliminate = False
        # Eliminar Recursividad directa
        if needEliminate:
            auxiliarTerminal = ''
            for posibleNoTerminal in possibleTerminals:
                if posibleNoTerminal not in noTerminals and posibleNoTerminal not in NewNoTerminals:
                    auxiliarTerminal = posibleNoTerminal
                    NewNoTerminals.append(auxiliarTerminal)
                    NewGrammar[auxiliarTerminal] = []
                    break
            for produccion in grammar[noTerminal]:
                if produccion[0] == noTerminal:
                    NewGrammar[auxiliarTerminal].append(
                        produccion[1:]+auxiliarTerminal)
                else:
                    NewGrammar[noTerminal].append(produccion+auxiliarTerminal)
        else:
            NewGrammar[noTerminal] = grammar[noTerminal]
    return {'grammar': NewGrammar, 'noTerminals': NewNoTerminals}


def first(grammar, s):
    firsts = []
    for production in grammar[s]:  # Para cada produccion de la regla
        #Eliminar espacios en blanco de production
        production = production.replace(" ", "")
        if production[0] not in noTerminals:
            firsts.append(production[0])
        else:
            firstTemp = first(grammar, production[0])
            if 'ε' in firstTemp:
                if production[1]:
                    firstTemp.remove('ε')
                    firstTemp += first(grammar, production[1])
            firsts += firstTemp
    return firsts


def imprimirGrammar(grammar, new):
    for key in grammar:
        print(key, " --> ", grammar[key])
    print('No terminales: ', list(new))


# Guarda las reglas de la gramatica
grammar = {
    'E': ['E + T', 'E - T', 'T'],
    'T': ['T * F', 'T / F', 'F'],
    'F': ['( E )', 'id']
}

# Guarda los no terminales de la gramatica
noTerminals = grammar.keys()

print('Gramatica inicial')
imprimirGrammar(grammar, noTerminals)

print('Gramatica final')
result = eliminateLeftRecursion(grammar, noTerminals)
imprimirGrammar(result["grammar"], result["noTerminals"])

print('Primeros')
for nont in result['noTerminals']:
    print(f'P({nont}) ={first(result["grammar"],nont)}')
