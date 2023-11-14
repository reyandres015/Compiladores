#Librerias

# Clase Lector para hacer el analisis up and down
class Lector:
    # Constructor de la clase
    def __init__(self, noTerminals, grammar, strings,First,Follow):
        self.noTerminals=noTerminals
        self.grammar=grammar
        self.strings=strings
        self.First=First
        self.Follow=Follow
        for noTerminal in self.noTerminals:
            self.first(noTerminal,self.grammar)
        print(self.First)
        print("first:",self.First)

        for noTerminal in self.noTerminals:
             self.follow(noTerminal,grammar)
        print('Follow:',self.Follow)
        

    # Metodo para calcular el first
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
                    else: continue  

    def follow(self,noTerminal, grammar):
        primerterminal = noTerminal[0]
        self.Follow[noTerminal] = []
        print("La regla:",primerterminal)
        if primerterminal == 'S':
            if '$' not in self.Follow[noTerminal]:
                self.Follow[noTerminal].append('$')
                print("gracias a diosito")
        
                


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
