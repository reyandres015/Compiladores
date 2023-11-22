#Clase botom up.


class Bottom_up:

    def __init__(self,First,Follow,Grammar,NoTerminals,cadenas):
        self.First=First
        self.Follow=Follow
        self.Grammar=Grammar
        self.NoTerminals=NoTerminals
        self.cadenas=cadenas
        self.Terminals=set()
        self.extenderGramatica()



    #Extender la gramatica
    def extenderGramatica(self):
        extend =  self.NoTerminals[0]+"'"
        self.Grammar[extend]=[self.NoTerminals[0]]
        print(self.Grammar)
        
  
    def goTo(self,Items):
        for non_terminal, production_rules in new_grammar.items():
            if non_terminal not in self.Grammar:
                self.Grammar[non_terminal] = []  # Initialize the list if non-terminal is not in the grammar

            # Add each production rule to the grammar
            self.Grammar[non_terminal].extend(production_rules)