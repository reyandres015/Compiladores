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
        #print(self.dicColumns,self.dicRows)
        self.predictiveParsingTable()
        for i in self.TableM:
            print(i)
        
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
                return self.First[cadena[i]]