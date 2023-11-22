from lector import *
from Top_down import *



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

        cadenas=[]
        for i in range(k):
            cadena=str(input())
            cadenas.append(cadena)
        lector=Lector(noTerminals,grammar,cadenas,{},{})
        # Top-down parsing
        top_down=Top_down(lector.First,lector.followResultado,grammar,noTerminals,cadenas)
        # Botton-up parsing

        #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------
        # Llamada al método para eliminar la recursividad por la izquierda
        #top_down.detect_and_eliminate_left_recursion()

        # Opcionalmente, imprimir la gramática después de eliminar la recursividad por la izquierda
        print("Gramática sin recursividad por la izquierda:")
        for nt in lector.grammar:
            rules = ' | '.join(' '.join(prod) for prod in lector.grammar[nt])
            print(f"{nt} -> {rules}")
        #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------

        #---------------------------VERIFICAR LL(1)---------------------------
        top_down.verifyLL1()
        #---------------------------VERIFICAR LL(1)---------------------------
        
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