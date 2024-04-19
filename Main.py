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
    return [NewGrammar, NewNoTerminals]


if __name__ == "__main__":
    # Guarda las reglas de la gramatica
    grammar = {
        'E': ['E + T', 'E - T', 'T'],
        'T': ['T * F', 'T / F', 'F'],
        'F': ['(E)', 'id']
    }

    # Guarda los no terminales de la gramatica
    noTerminals = grammar.keys()

    print(grammar)
    result = eliminateLeftRecursion(grammar, noTerminals)
    print("new grammar ", result[0], "new noTerminals ", result[1])
