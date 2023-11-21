# Clase Lector para hacer el calculo de First and Follow
class Lector:
    # Constructor de la clase
    def __init__(self, noTerminals, grammar, strings,First,followResultado):
        self.noTerminals=noTerminals
        self.grammar=grammar
        self.strings=strings
        self.First=First
        self.followResultado=followResultado
        # Primero calculamos First para cada no terminal
        for noTerminal in self.noTerminals:
            self.first(noTerminal,self.grammar)
        # Ahora Calculamos Follow
        self.follow()
        

    def first(self,noTerminal,grammar):
        reglas=grammar[noTerminal]
        
        for regla in reglas:
            if regla[0] not in self.noTerminals:
                if noTerminal not in self.First:
                    self.First[noTerminal]=[]
                if regla[0] not in self.First[noTerminal]:
                    self.First[noTerminal].append(regla[0])
                else: continue
            else:
                if regla[0] != noTerminal:
                    self.first(regla[0],grammar)
                    for a in self.First[regla[0]]:
                        if a not in self.First[noTerminal]:
                            self.First[noTerminal].append(a)

    def follow(self):
        for nonTerminal in self.noTerminals:
            if nonTerminal not in self.followResultado:
                self.followResultado[nonTerminal]=set()
            
            #primera Regla Follow(A)={$}
            if nonTerminal==self.noTerminals[0]:
                self.followResultado[nonTerminal].add('$')
        
        #segunda Regla A → αBβ First(β) ∈ Follow(B)
        # nt = no terminal
        for noTerminal,ruleNonTerminal in self.grammar.items():
            for regla in ruleNonTerminal:
                for i in range(len(regla)-1):
                    if regla[i] in self.noTerminals:
                        if regla[i+1] in self.noTerminals:
                            for first in self.First[regla[i+1]]:
                                self.followResultado[regla[i]].add(first)
                        else:
                            self.followResultado[regla[i]].add(regla[i+1])
        
        #tercera Regla A → αB Follow(B) = Follow(A)
        for noTerminal,ruleNonTerminal in self.grammar.items():
            for regla in ruleNonTerminal:
                if regla[len(regla)-1] in self.noTerminals:
                    for fo in self.followResultado[noTerminal]:
                        self.followResultado[regla[len(regla)-1]].add(fo)