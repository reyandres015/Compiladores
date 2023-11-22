from Lector import *

class Top_down:
    def __init__(self,First,Follow,Grammar,NoTerminals,cadenas):
        self.First=First
        self.Follow=Follow
        self.Grammar=Grammar
        self.NoTerminals=NoTerminals
        self.cadenas=cadenas
        self.Terminals=set()
        self.Resultados=[]
        self.terminals()
        self.Terminals=list(self.Terminals)
        #self.verifyLL1()
        #self.detect_and_eliminate_left_recursion()
        self.TableM = [["" for _ in range(len(self.Terminals))] for _ in range(len(self.NoTerminals))]
        self.dicRows={}
        self.dicColumns={}
        self.Error=False
        self.dicAsing()
        self.predictiveParsingTable()
        for cadena in self.cadenas:
            self.Resultados.append(self.predictiveParsing(cadena))
        for valores in self.Resultados:
            print(valores)
        
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
                        else:
                            self.Error=True
                    elif terminal == "e":
                        for terminalf in self.Follow[noTerminal]:
                            if self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=="":
                                self.TableM[self.dicRows[noTerminal]][self.dicColumns[terminalf]]=noTerminal+"->"+produccion
                                #print(noTerminal,terminalf," = ",noTerminal," -> ",produccion)
                
                                               
    def predictiveParsing(self,cadena):
        posicion=0
        TStack=['$','S'] #pila
        wString=cadena+'$'
        a=wString[posicion]
        xTop=TStack[-1]
        while(xTop!='$'):
            #print(wString,a,TStack)
            if xTop==a:
                TStack.pop()
                xTop=TStack[-1]
                posicion+=1
                a=wString[posicion]
            elif a not in self.Terminals and a!="e":
                self.Error=True
                #print("Error caracter desconocido")
                break
            elif a in self.Terminals and xTop in self.NoTerminals: 
                if self.TableM[self.dicRows[xTop]][self.dicColumns[a]] == "":
                    #print("Error tabla error")
                    #self.Error=True
                    break
                else:
                    TStack.pop()
                    regla=self.TableM[self.dicRows[xTop]][self.dicColumns[a]]
                    regla=regla.split("->")
                    producion=regla[1]
                    for valor in reversed(producion):
                        if valor!="e":
                            TStack.append(valor)
                    xTop=TStack[-1]
            else:
                self.Error=True
                break
            #input()
        #print(wString,a,TStack)
        if a == TStack[-1]:
            return "si"
        elif a != TStack[-1] or self.Error: 
            return "no"
                
            
    def getFirst(self,cadena):
        for i in range(len(cadena)):
            if cadena[i] not in self.NoTerminals:
                return cadena[i]
            else:
                return self.First[cadena[i]]
            
    #---------------------------ELIMINAR RECURSIVIDAD POR IZQUIERDA---------------------------
    def detect_and_eliminate_left_recursion(self):
        print("eliminar recursividad por la izquierda")
        new_grammar = {}
        for noTerminal in self.NoTerminals:
            reglas = self.Grammar[noTerminal]
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
                self.NoTerminals.append(new_noTerminal)
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
        interseccion=False
        for noTerminal in self.NoTerminals:
            for alpha in self.Grammar[noTerminal]:
                for beta in self.Grammar[noTerminal]:
                    if alpha!=beta and alpha!="e" and beta!="e":
                        firstAlpha=self.getFirst(alpha)
                        firstBeta=self.getFirst(beta)
                        if len(firstAlpha) == 1 and firstAlpha[0]=="e":
                            for firstB in firstBeta:
                                for followTerminal in self.Follow[noTerminal]:
                                    if firstB==followTerminal:
                                        interseccion=True
                                        return interseccion
                        elif len(firstBeta)==1 and firstBeta[0]=="e":
                            for fisrtA in firstAlpha:
                                for followTerminalA in self.Follow[noTerminal]:
                                    if fisrtA==followTerminalA:
                                        interseccion=True
                                        return interseccion
                        else:
                            for firstA in firstAlpha:
                                for firstB in firstBeta:
                                    if firstA==firstB:
                                        interseccion=True
                                        return interseccion
        return interseccion
