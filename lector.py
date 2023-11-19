# Clase Lector para hacer el analisis up and down
class Lector:
    # Constructor de la clase
    def __init__(self, noTerminals, grammar, strings,First,followResultado):
        self.noTerminals=noTerminals
        self.grammar=grammar
        self.strings=strings
        self.First=First
        self.followResultado=followResultado
        for noTerminal in self.noTerminals:
            self.first(noTerminal,self.grammar)
        print("first:",self.First)

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
                self.first(regla[0],grammar)
                for a in self.First[regla[0]]:
                    if a not in self.First[noTerminal]:
                        self.First[noTerminal].append(a)
    
    def follow(self,noTerminal,grammar):
        follow_ = set()

    def follow(nT):
        #print("inside follow({})".format(nT))
        follow_ = set()
        #La funcion .items() es para que sea la llave y el valor
        prods = productions_dict.items()
        if nT==starting_symbol:
            follow_ = follow_ | {'$'}
        for nt,reglasDelNT in prods:
            #nt, reglasDelNT son simbolos 
            print("soy reglasDelNT:",reglasDelNT)
            print("soy nt:",nt)
            for regla in reglasDelNT:
                print("soy regla:",regla)
                for simbolo in regla:
                    if simbolo==nT:
                        following_symbol = regla[regla.index(simbolo) + 1:]
                        #segunda regla. Si el simbolo es nT y no hay nada despues de el, entonces follow(nT) = follow(nt)
                        if following_symbol=='':
                            if nt==nT: #si el no teminal es el mismo que le mandamos a la función Follow
                                continue
                            else:
                                follow_ = follow_ | follow(nt)
                        else:
                            follow_2 = first(following_symbol)
                            if '@' in follow_2:
                                follow_ = follow_ | follow_2-{'@'}
                                follow_ = follow_ | follow(nt)
                            else:
                                follow_ = follow_ | follow_2
                                
        print("returning for follow({}) ".format(nT),follow_)
        return follow_

                    
    #-------------------------------ESTO ES EL INTENTO DE ANTES---------------------------------------------
    # def ponerEnFollow(self,noTerminals):
    #     self.Follow[noTerminals]=[]
        
    # def follow1(self,noTerminal):    
    #     primerTerminal = noTerminal[0]    
    #     if primerTerminal[0] == noTerminal[0]:     
    #         if '$' not in self.Follow[noTerminal]:
    #             self.Follow[noTerminal].append('$')
    
    # def follow(self,noTerminal,grammar):        
    #     reglas = grammar[noTerminal]
    #     for regla in reglas:
    #         if regla not in noTerminal: 
    #             for i in range(len(regla)):
    #                 print('regla[i]:',regla[i])
    #                 if regla[i] in noTerminal:
    #                     # Cambiar el argumento de la llamada recursiva por el símbolo no terminal que corresponda
    #                     if i == len(regla): # Si el símbolo no terminal es el último de la regla
    #                         # print("ME ESTOY CUMPLIENDO")
    #                         self.Follow[noTerminal].append(self.Follow[noTerminal]) # Llamar a la función Follow con el mismo símbolo no terminal
    #                         break
    #                     # Si el símbolo no terminal no es el último de la regla
    #                     if i == self.Follow[noTerminal]:
    #                         self.Follow[noTerminal].append(self.Follow[noTerminal])

    #                     else: 
    #                         print("El no terminal NO es el ultimo de la regla")
    #                         self.Follow[noTerminal].append(regla[i+1]) # Llamar a la función Follow con el siguiente símbolo no terminal
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
        print(n,m,k,'n m k')
        print(noTerminals,'no terminales')
        print (grammar)
        print(cadenas)
        
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


'''
def follow(self, noTerminal, grammar):
    # Inicializar el conjunto de seguimiento vacío para el símbolo no terminal
    self.Follow[noTerminal] = []
    # Obtener el primer símbolo del símbolo no terminal
    primerterminal = noTerminal[0]
    print("La regla:", primerterminal)
    # Aplicar la primera regla: si el símbolo inicial de la gramática aparece en algún lado derecho, entonces el final de la entrada ($) pertenece al conjunto de seguimiento de ese símbolo no terminal
    if primerterminal == 'S':
        if '$' not in self.Follow[noTerminal]:
            self.Follow[noTerminal].append('$')
    # Aplicar las otras dos reglas: recorrer todas las producciones de la gramática
    for key in grammar:
        for value in grammar[key]:
            # Buscar el símbolo no terminal en el lado derecho de la producción
            if noTerminal in value:
                # Obtener la posición del símbolo no terminal en el lado derecho
                pos = value.index(noTerminal)
                # Verificar si el símbolo no terminal es el último de la cadena
                if pos == len(value) - 1:
                    # Aplicar la segunda regla: si hay una producción A -> αB, entonces todo lo que esté en FOLLOW (A) está en FOLLOW (B)
                    if key != noTerminal:
                        # Calcular el conjunto de seguimiento del símbolo no terminal del lado izquierdo, si no se ha calculado antes
                        if not self.Follow.get(key, False):
                            self.follow(key, grammar)
                        # Unir el conjunto de seguimiento del símbolo no terminal del lado izquierdo con el del símbolo no terminal actual, sin repetir elementos
                        self.Follow[noTerminal] = list(set(self.Follow[key]) | set(self.Follow[noTerminal]))
                else:
                    # Aplicar la tercera regla: si hay una producción A -> αBβ, donde B es un símbolo no terminal y α y β son cadenas de símbolos terminales y no terminales, entonces todo lo que esté en FIRST (β), excepto ε, está en FOLLOW (B)
                    # Obtener la subcadena que sigue al símbolo no terminal en el lado derecho
                    next_str = value[pos + 1:]
                    # Calcular el conjunto de first de la subcadena, si no se ha calculado antes
                    if not self.First.get(next_str, False):
                        self.first(next_str, grammar)
                    # Verificar si el conjunto de first de la subcadena contiene ε
                    if 'e' in self.First[next_str]:
                        # Si contiene ε, se debe eliminar de first y se debe aplicar también la segunda regla
                        self.First[next_str].remove('e')
                        if key != noTerminal:
                            if not self.Follow.get(key, False):
                                self.follow(key, grammar)
                            self.Follow[noTerminal] = list(set(self.Follow[key]) | set(self.Follow[noTerminal]))
                    # Unir el conjunto de first de la subcadena con el de seguimiento del símbolo no terminal actual, sin repetir elementos
                    self.Follow[noTerminal] = list(set(self.First[next_str]) | set(self.Follow[noTerminal]))
    # Devolver el conjunto de seguimiento del símbolo no terminal
    return self.Follow[noTerminal]
'''