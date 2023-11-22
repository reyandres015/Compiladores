from lector import *

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
        self.verifyLL1()
        self.detect_and_eliminate_left_recursion()
        self.TableM = [["" for _ in range(len(self.Terminals))] for _ in range(len(self.NoTerminals))]
        self.dicRows={}
        self.dicColumns={}
        self.Error=False
        self.dicAsing()
        self.predictiveParsingTable()
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
            elif a in self.Terminals: 
                if self.TableM[self.dicRows[xTop]][self.dicColumns[a]] == "":
                #print("Error")
                    self.Error=True
                    break
                elif self.TableM[self.dicRows[xTop]][self.dicColumns[a]] != "":
                    #print(wString,TStack,xTop,"antes")
                    TStack.pop()
                    regla=self.TableM[self.dicRows[xTop]][self.dicColumns[a]]
                    regla=regla.split("->")
                    producion=regla[1]
                #print(producion)
                    for valor in reversed(producion):
                        if valor!="e":
                            TStack.append(valor)
                    xTop=TStack[-1]
                #print(wString,TStack,xTop,"despues")
            else:
                print("Error")
                break
        if self.Error != False:
            self.Resultados.append("si")
        else: 
            self.Resultados.append("Error")
                
            
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
        for noterminales in self.Grammar.keys():
            interseccion = set()
            for produccion in self.Grammar[noterminales]:
                if produccion[0] == 'e':
                    interseccion=(interseccion & set('e'))
                    print("if j[0] == 'e'")
                else:
                    print("else de --> if j[0] == 'e'")
                    # interseccion=(interseccion & set(self.First[j[0]]))
                    interseccion=(interseccion & set(produccion[0]))
            print("interseccion ",len(interseccion))
            if len(interseccion) != 0:
                #return False 
                print("No es LL(1)") 
                break
