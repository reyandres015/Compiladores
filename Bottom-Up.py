#Clase botom up.


class Bottom_up:

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
        # Suponiendo que self.NoTerminals y self.Terminals son listas de strings
        self.TableM = [["" for _ in range(len(self.Terminals))] for _ in range(len(self.NoTerminals))]
        self.dicRows={}
        self.dicColumns={}
        self.Error=False
        self.dicAsing()
        self.predictiveParsingTable()
        for cadena in self.cadenas:
            self.predictiveParsing(cadena)


    def extenderGramatica(self, grammar):
        pass