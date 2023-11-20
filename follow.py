noTerminals=['S', 'T', 'E']
grammar={'S': ['iEtST', 'a'], 'T': ['cS', 'e'], 'E': ['b']}
First={'S': ['i', 'a'], 'T': ['c', 'e'], 'E': ['b']}
followResultado={}

def follow():
    for nonTerminal in noTerminals:
        if nonTerminal not in followResultado:
            followResultado[nonTerminal]=set()
        
        #primera Regla Follow(A)={$}
        if nonTerminal==noTerminals[0]:
            followResultado[nonTerminal].add('$')
    
    #segunda Regla A → αBβ First(β) ∈ Follow(B)
    # nt = no terminal
    for noTerminal,ruleNonTerminal in grammar.items():
        for regla in ruleNonTerminal:
            for i in range(len(regla)-1):
                if regla[i] in noTerminals:
                    if regla[i+1] in noTerminals:
                        for first in First[regla[i+1]]:
                            followResultado[regla[i]].add(first)
                    else:
                        followResultado[regla[i]].add(regla[i+1])
    
    
    #tercera Regla A → αB Follow(B) = Follow(A)
    for noTerminal,ruleNonTerminal in grammar.items():
        for regla in ruleNonTerminal:
            if regla[len(regla)-1] in noTerminals:
                for fo in followResultado[noTerminal]:
                    followResultado[regla[len(regla)-1]].add(fo)
    return

follow()
    
print(followResultado)