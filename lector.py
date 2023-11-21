# Clase Lector para hacer el calculo de First and Follow
class Lector:
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
                                if first != "e":
                                    self.followResultado[regla[i]].add(first)
                        elif regla[i+1] != "e":
                            self.followResultado[regla[i]].add(regla[i+1])
        
        #tercera Regla A → αB Follow(B) = Follow(A)
        for noTerminal,ruleNonTerminal in self.grammar.items():
            for regla in ruleNonTerminal:
                if regla[len(regla)-1] in self.noTerminals:
                    for fo in self.followResultado[noTerminal]:
                        self.followResultado[regla[len(regla)-1]].add(fo)

    #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------
    def detect_and_eliminate_left_recursion(self):
        new_grammar = {}
        for noTerminal in self.noTerminals:
            reglas = self.grammar[noTerminal]
            recursive_rules = []
            non_recursive_rules = []
            
            # Separa las reglas recursivas de las no recursivas
            for regla in reglas:
                if regla[0] == noTerminal:
                    recursive_rules.append(regla)
                else:
                    non_recursive_rules.append(regla)
            
            # Si hay reglas recursivas, realiza la eliminación
            if recursive_rules:
                print(f"Recursion found in {noTerminal} -> {recursive_rules}")
                # Crear nuevo no terminal (por ejemplo: A -> A', donde A' es el nuevo no terminal)
                new_noTerminal = noTerminal + "'"
                self.noTerminals.append(new_noTerminal)
                new_grammar[new_noTerminal] = []

                # Elimina la recursividad por la izquierda
                for regla in recursive_rules:
                    # Crear nueva regla (A -> B A')
                    new_rule = regla[1:]  # Copia la regla desde el segundo símbolo
                    new_rule.append(new_noTerminal)  # Añade el nuevo no terminal al final
                    new_grammar[new_noTerminal].append(new_rule)
                
                # Actualiza las reglas no recursivas (A -> B A')
                new_grammar[noTerminal] = []
                for regla in non_recursive_rules:
                    new_rule = regla[:]  # Copia la regla completa
                    new_rule.append(new_noTerminal)  # Añade el nuevo no terminal al final
                    new_grammar[noTerminal].append(new_rule)

                # Agrega la regla 'e' a las nuevas reglas de A'
                new_grammar[new_noTerminal].append(['e'])  # 'e' representa la producción vacía

            else:
                # Si no hay recursividad, simplemente copia las reglas originales
                new_grammar[noTerminal] = reglas[:]

        self.grammar = new_grammar
    #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------

    #---------------------------VERIFICAR LL(1)---------------------------
    def verifyLL1(self):
        for i in self.grammar.keys():
            interseccion = set()
            for j in self.grammar[i]:
                if j[0] == 'e':
                    interseccion=(interseccion & set('e'))
                else:
                    #aqui hay que hacer que sea el primer first que tenemos
                    interseccion=(interseccion & set(self.First[j[0]]))
            if len(interseccion) != 0:
                #no sé que poner aqui
                #return False 
                print("No es LL(1)") 
                break

   
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

VERIFICAR SI ES LL(1) (debe dar error)
3 5 1
S T E
S-iEtST
S-a
T-cS
T-e
E-b
ibta

RECURSIVIDAD POR IZQUERDA:
1
2 4 1
S A
S-Sa
S-b
A-c
A-d
a
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
