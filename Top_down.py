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
        self.TableM=np.zeros((len(self.NoTerminals),len(self.Terminals)))
        self.dicRow={}
        self.dicColumns={}
        self.dicAsing()
        
    def terminals(self):
        for nt,produccions in self.Grammar.items():
            for produccion in produccions:
                for item in produccion:
                    if item not in self.NoTerminals:
                        self.Terminals.add(item)
        self.Terminals.add('$')
        
    def dicAsing(self):
        contRows=0
        contColums=0
        for terminal in self.Terminals:
            self.dicRow[terminal]=contRows
            contRows+=1
        for noTerminal in self.NoTerminals:
            self.dicColumns[noTerminal]=contColums
            contColums+=1
    
    def predictiveParsingTable(self):
        for noTerminal in self.NoTerminals:
            for produccion in self.Grammar[noTerminal]:   
                return
    
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
        
        top_down=Top_down(lector.First,lector.followResultado,grammar,noTerminals)
        numGramatica+=1