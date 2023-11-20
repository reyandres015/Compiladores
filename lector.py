# Clase Lector para hacer el analisis up and down
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
        print("first:",self.First)
        print("follow", self.followResultado)
        
        """
        # Ahora que tenemos First, podemos calcular Follow
        for noTerminal in self.noTerminals:
            self.follow(noTerminal)
        print("Follow:", self.followResultado)"""

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
        for noTerminal,ruleNonTerminal in grammar.items():
            for regla in ruleNonTerminal:
                for i in range(len(regla)-1):
                    if regla[i] in self.noTerminals:
                        if regla[i+1] in self.noTerminals:
                            for first in self.First[regla[i+1]]:
                                self.followResultado[regla[i]].add(first)
                        else:
                            self.followResultado[regla[i]].add(regla[i+1])
        
        #tercera Regla A → αB Follow(B) = Follow(A)
        for noTerminal,ruleNonTerminal in grammar.items():
            for regla in ruleNonTerminal:
                if regla[len(regla)-1] in noTerminals:
                    for fo in self.followResultado[noTerminal]:
                        self.followResultado[regla[len(regla)-1]].add(fo)

                    
    #-------------------------------ESTO ES EL INTENTO DE ANTES, el de arriba tiene modificaciones hechas con GPT4-------------------------------
    # def follow(self, nT):
    #     #print("inside follow({})".format(nT))
    #     follow_ = set()
    #     #La funcion .items() es para que sea la llave y el valor
    #     prods = productions_dict.items()
    #     if nT==starting_symbol:
    #         follow_ = follow_ | {'$'}
    #     for nt,reglasDelNT in prods:
    #         #nt, reglasDelNT son simbolos 
    #         print("soy reglasDelNT:",reglasDelNT)
    #         print("soy nt:",nt)
    #         for regla in reglasDelNT:
    #             print("soy regla:",regla)
    #             for simbolo in regla:
    #                 if simbolo==nT:
    #                     following_symbol = regla[regla.index(simbolo) + 1:]
    #                     #segunda regla. Si el simbolo es nT y no hay nada despues de el, entonces follow(nT) = follow(nt)
    #                     if following_symbol=='':
    #                         if nt==nT: #si el no teminal es el mismo que le mandamos a la función Follow
    #                             continue
    #                         else:
    #                             follow_ = follow_ | follow(nt)
    #                     else:
    #                         follow_2 = self.first(following_symbol)
    #                         if '@' in follow_2:
    #                             follow_ = follow_ | follow_2-{'@'}
    #                             follow_ = follow_ | follow(nt)
    #                         else:
    #                             follow_ = follow_ | follow_2
                                
    #     print("returning for follow({}) ".format(nT),follow_)
    #     return follow_
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
if __name__=="__main__":
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
        Lector(noTerminals,grammar,cadenas,{},{})
        #print(n,m,k,'n m k')
        #print(noTerminals,'no terminales')
        #print (grammar)
        #print(cadenas)
        
        numGramatica+=1

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
