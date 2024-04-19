class Grammar:
    recursiveGrammar = {},
    noTerminals = [],
    grammar = {},
    first = [],
    follow = [],


def eliminateLeftRecursion(grammar, noTerminals):
    """
    Eliminates left recursion from a given grammar.

    Args:
        grammar (dict): The original grammar.
        noTerminals (list): List of non-terminal symbols.

    Returns:
        dict: A dictionary containing the modified grammar and the updated list of non-terminals.
    """
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
                        produccion[1:] + ' ' + auxiliarTerminal)
                else:
                    NewGrammar[noTerminal].append(
                        produccion + ' ' + auxiliarTerminal)
        else:
            NewGrammar[noTerminal] = grammar[noTerminal]
    return {'grammar': NewGrammar, 'noTerminals': NewNoTerminals}


def first(grammar, s):
    firsts = []
    for production in grammar[s]:  # Para cada produccion de la regla
        # Eliminar espacios en blanco de production
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

# Algoritmo de siguientes


def findSymbol(s):
    results = {}
    for nont in grammar:  # Por NT de la gramatica
        for production in grammar[nont]:  # Por produccion del simbolo
            for symbol in production:
                if s in production:
                    try:
                        results[nont] += [production]
                    except KeyError:
                        results[nont] = [production]
    return results


def follow(s):
    follows = []
    if s == next(iter(grammar)):  # Si el NT es el estado inicial, el siguiente sera $
        follows.append("$")
    # Buscamos las producciones donde se encuentra nuestro NT
    found = findSymbol(s)
    for nont in found:  # Por cada NT de las reglas encontradas
        for production in found[nont]:
            if (production.index(s) < len(production)-1):
                # El simbolo despues del NT
                nxt = production[production.index(s)+1]
                if (nxt not in noTerminals):  # Si el simbolo es terminal
                    # Agregamos ese simbolo a la lista de siguientes
                    follows.append(nxt)
                elif (nxt in noTerminals):  # Si el simbolo es no terminal
                    # Buscamos los primeros del siguiente
                    nxt = first(grammar, nxt)
                    if ("ε" in nxt):  # Si existe epsilon en los primeros
                        # Se añaden los siguientes del padre
                        nxt += follow(nont)
                    follows += nxt
            else:
                if (s != nont):
                    follows += follow(nont)
    follows = list(set(follows))
    if ("ε" in follows):
        follows.remove("ε")
    return follows

# Algoritmo de predicción


def conjunto_prediccion(grammar, primeros, siguientes):
    conjuntos_prediccion = {}

    for no_terminal, producciones in grammar.items():
        conjuntos_prediccion[no_terminal] = {}
        for produccion in producciones:
            primeros_de_produccion = set()

            for simbolo in produccion:
                if simbolo in grammar:
                    primeros_de_produccion |= primeros[simbolo] - {'ε'}
                    if 'ε' not in primeros[simbolo]:
                        break
                elif simbolo != 'ε' and simbolo != '$':
                    primeros_de_produccion.add(simbolo)
                    break
            else:
                primeros_de_produccion |= siguientes[no_terminal] - {'$', 'ε'}

            conjuntos_prediccion[no_terminal][" ".join(
                produccion)] = primeros_de_produccion

    return conjuntos_prediccion

# funcion para comprobar que la gramatica es LL(1)


def isLL1(grammar, conjuntos_prediccion):
    for no_terminal, producciones in grammar.items():
        for produccion, conjunto in conjuntos_prediccion[no_terminal].items():
            for no_terminal2, producciones2 in grammar.items():
                for produccion2, conjunto2 in conjuntos_prediccion[no_terminal2].items():
                    if no_terminal != no_terminal2 and produccion == produccion2 and conjunto & conjunto2:
                        return False
    return True


def imprimirGrammar(grammar, new):
    for key in grammar:
        print(key, " --> ", grammar[key])
    print('No terminales: ', list(new))


def convert_grammar(grammar):
    new_grammar = {}
    for key, productions in grammar.items():
        new_productions = []
        for production in productions:
            new_productions.append(production.split())
        new_grammar[key] = new_productions
    return new_grammar


# Guarda las reglas de la gramatica
grammar = {
    'A': ['B C', 'ant A all'],
    'B': ['big C', 'bus A boss', 'ε'],
    'C': ['cat', 'cow']
}

# Guarda los no terminales de la gramatica
noTerminals = grammar.keys()

print('Gramatica inicial')
imprimirGrammar(grammar, noTerminals)

# Elimina la recursividad izquierda
print('Gramatica final')
result = eliminateLeftRecursion(grammar, noTerminals)
grammar = convert_grammar(result["grammar"])
imprimirGrammar(grammar, result["noTerminals"])

# Algoritmo de primeros
print('Primeros')
primeros = {}
for nont in result['noTerminals']:
    primeros[nont] = set(first(grammar, nont))
    print(f'P({nont}) ={first(grammar,nont)}')

# Algoritmo de siguientes
print('Siguientes')
siguientes = {}
for nont in result['noTerminals']:
    siguientes[nont] = set(follow(nont))
    print(f'S({nont}) ={follow(nont)}')

# Algoritmo de prediccion
print('Conjuntos de prediccion')
conjuntos_prediccion = conjunto_prediccion(grammar, primeros, siguientes)

print(conjuntos_prediccion)

# Comprobacion de LL(1)
if isLL1(grammar, conjuntos_prediccion):
    print('La gramatica es LL(1)')
else:
    print('La gramatica no es LL(1)')
    
# funcion para cada no terminal en un ASDR
def asdr(noTerminal,grammar):
    # extraemos la gramatica
    reglas=grammar[noTerminal]
    #añadimos el terminal al diccionario del First
    if noTerminal not in Grammar.first:
                Grammar.first[noTerminal]=[]
    # Recorremos las reglas
    for regla in reglas:
        #si el primer caracter es un Terminal, lo añadimos al first del no terminal
        if regla[0] not in Grammar.noTerminals:
            # verificamos que no exista ya el terminal en el First del terminal
            if regla[0] not in Grammar.first[noTerminal]:
                Grammar.first[noTerminal].append(regla[0])
            else: continue
        else: # si el primer caracter es un no terminal
            # verificamos que el caracter no sea el mismo no terminal 
            if regla[0] != noTerminal:
                # hallamos el first del no terminal
                asdr(regla[0],grammar)
                # Recorremos el first del caracter no terminal
                for a in Grammar.first[regla[0]]:
                    # verificamos que no exista ya el terminal en el First del terminal
                    if a not in Grammar.first[noTerminal]:
                        Grammar.first[noTerminal].append(a)
