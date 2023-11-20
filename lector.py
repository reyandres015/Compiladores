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
   
"""if __name__=="__main__":
    #entrada numero de gramaticas
    gramarticas=int(input())
    numGramatica=0
    while(numGramatica<gramarticas):
        # Guarda valores de n m y k
        n,m,k = map(int,input().split())
        # Guarda los no terminales de la gramatica
        noTerminals=input().split(' ')
        # Guarda las reglas de la gramatica
        grammar={}
        # Asignar reglas a terminalesclear
        for i in range(m):
            rule=input().split('-')
            if len(rule)!=2:
                print(f"Error in rule: {rule}")
                continue
            if rule[0] not in grammar:
                grammar[rule[0]]=[]
            grammar[rule[0]].append(rule[1])
        # Guardar las cadenas a evaluar
        cadenas=[]
        for i in range(k):
            cadena=str(input())
            cadenas.append(cadena)
        lector=Lector(noTerminals,grammar,cadenas,{},{})
        
        print("first",lector.First,"Follow",lector.followResultado)
        numGramatica+=1"""
        
        
        
        
'''
CASO DE PRUEBA INICIAL
1
1 2 3
S
S-aSb
S-c
aacbb
acb
ab
'''

'''
Segundo caso de prueba.
1
2 4 4
S A
S-aSb
S-A
A-aA
A-a
aaabb
aabb
aaaaaaaaaabbbb
ab
'''

'''
Tercer caso de prueba.
1
1 2 3
S
S-aSb
S-c
aacbb
acb
ab
'''

'''
3
1 2 3
S
S-aSb
S-c
aacbb
acb
ab
2 4 4
S A
S-aSb
S-A
A-aA
A-a
aaabb
aabb
aaaaaaaaaabbbb
ab
3 5 1
S T E
S-iEtST
S-a
T-cS
T-e
E-b
ibta
'''
