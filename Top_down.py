from lector import *
import numpy as np

class Top_down:
    
    def __init__(self,First,Follow,Grammar,NoTerminals):
        self.First=First
        self.Follow=Follow
        self.Grammar=Grammar
        self.NoTerminals=NoTerminals
        self.Terminals=set()
        self.terminals()
        self.Terminals=list(self.Terminals)
        # Suponiendo que self.NoTerminals y self.Terminals son listas de strings
        self.TableM = [["" for _ in range(len(self.Terminals))] for _ in range(len(self.NoTerminals))]
        self.dicRows={}
        self.dicColumns={}
        self.dicAsing()
        print(self.First,self.Follow)
        #print(self.dicColumns,self.dicRows)
        #self.predictiveParsingTable()
        ## print(i)
        
    def terminals(self):
        for nt,produccions in self.Grammar.items():
            for produccion in produccions:
                for item in produccion:
                    if item not in self.NoTerminals and item != "e":
                        self.Terminals.add(item)
        self.Terminals.add('$')
        
    def dicAsing(self):
        contRows=0
        contColumns=0
        for terminal in self.Terminals:
            self.dicColumns[terminal]=contColumns
            contColumns+=1
        for noTerminal in self.NoTerminals:
            self.dicRows[noTerminal]=contRows
            contRows+=1
    
    def predictiveParsingTable(self):
        for noTerminal in self.NoTerminals:
            for produccion in self.Grammar[noTerminal]:
                first=self.getFirst(produccion)
                for terminal in first:
                    if terminal != "e":
                        #print(self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminal]])
                        if self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminal]]=="":
                            self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminal]]=noTerminal+"->"+produccion
                            print(noTerminal,terminal," = ",noTerminal," -> ",produccion)
                        else:
                            error=False
                    elif terminal == "e":
                        for terminalf in self.Follow[noTerminal]:
                            if self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=="":
                                self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=noTerminal+"->"+produccion
                            
                            
                
        #recorrer para casillas vacias hacerlas error                   
                
                
            
    def getFirst(self,cadena):
        for i in range(len(cadena)):
            if cadena[i] not in self.NoTerminals:
                return cadena[i]
            else:
<<<<<<< HEAD
                return self.First[cadena[i]]
    
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

        cadenas=[]
        for i in range(k):
            cadena=str(input())
            cadenas.append(cadena)
            
        lector=Lector(noTerminals,grammar,cadenas,{},{})
        lector.verifyLL1()

        #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------
        # Llamada al método para eliminar la recursividad por la izquierda
        lector.detect_and_eliminate_left_recursion()

        # Opcionalmente, imprimir la gramática después de eliminar la recursividad por la izquierda
        print("Gramática sin recursividad por la izquierda:")
        for nt in lector.grammar:
            rules = ' | '.join(' '.join(prod) for prod in lector.grammar[nt])
            print(f"{nt} -> {rules}")
        #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------

        #---------------------------VERIFICAR LL(1)---------------------------
        lector.verifyLL1()
        #---------------------------VERIFICAR LL(1)---------------------------
        
        top_down=Top_down(lector.First,lector.followResultado,grammar,noTerminals)
        numGramatica+=1
=======
                return self.First[cadena[i]]
>>>>>>> 4057a4f50553a539cf5fc01a0e45fe01bc1111c7
