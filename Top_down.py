from lector import *
import numpy as np

class Top_down:
    
    def __init__(self,First,Follow,Grammar,NoTerminals,cadenas):
        self.First=First
        self.Follow=Follow
        self.Grammar=Grammar
        self.NoTerminals=NoTerminals
        self.cadenas=cadenas
        self.Terminals=set()
        self.terminals()
        self.Terminals=list(self.Terminals)
        # Suponiendo que self.NoTerminals y self.Terminals son listas de strings
        self.TableM = [["" for _ in range(len(self.Terminals))] for _ in range(len(self.NoTerminals))]
        self.dicRows={}
        self.dicColumns={}
        self.Error=False
        self.dicAsing()
        self.predictiveParsingTable()
        
        for clom in self.TableM:
            print(clom)
        for cadena in self.cadenas:
            self.predictiveParsing(cadena)
        
        
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
                        if self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminal]]=="":
                            self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminal]]=noTerminal+"->"+produccion
                            #print(noTerminal,terminal," = ",noTerminal," -> ",produccion)
                        else:
                            self.Error=True
                    elif terminal == "e":
                        for terminalf in self.Follow[noTerminal]:
                            if self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=="":
                                self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=noTerminal+"->"+produccion
                                #print(noTerminal,terminalf," = ",noTerminal," -> ",produccion)
                                               
    def predictiveParsing(self,cadena):
        posicion=0
        TStack=['$',self.NoTerminals[0]]
        wString=cadena+'$'
        a=wString[posicion]
        xTop=TStack[-1]
        while(xTop!='$'):
            if xTop==a:
                #print("top=a")
                TStack.pop()
                xTop=TStack[-1]
                posicion+=1
                a=wString[posicion]
            elif xTop in self.Terminals:
                self.Error=True
                #print("top is a terminal")
                break
            elif self.TableM[self.dicRows[xTop]][self.dicColumns[a]] == "":
                #print("Error")
                self.Error=True
                break
            elif self.TableM[self.dicRows[xTop]][self.dicColumns[a]] != "":
                print(wString,TStack,xTop,"antes")
                TStack.pop()
                regla=self.TableM[self.dicRows[xTop]][self.dicColumns[a]]
                regla=regla.split("->")
                producion=regla[1]
                #print(producion)
                for valor in reversed(producion):
                    if valor!="e":
                        TStack.append(valor)
                xTop=TStack[-1]
                print(wString,TStack,xTop,"despues")
                input()
            else:
                print("Error")
                break
        if self.Error != False:
            print("si")
        else: 
            print("Error")
                
                
            
    def getFirst(self,cadena):
        for i in range(len(cadena)):
            if cadena[i] not in self.NoTerminals:
                return cadena[i]
            else:
                return self.First[cadena[i]]