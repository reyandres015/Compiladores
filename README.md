# Compiladores

## ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿ Análizador sintactico ( ＾◡＾)っ ♡


Este proyecto es una implementación de dos algoritmos de análisis sintáctico para lenguajes libres de contexto, un analizador descendente (top-down parser) y un analizador ascendente (bottom-up parser). El analizador descendente está diseñado para gramáticas LL(1) y utiliza análisis predictivo para determinar si una cadena dada forma parte del lenguaje descrito por la gramática proporcionada. Por otro lado, el algoritmo ascendente está diseñado para gramáticas LR(0).

# Forked repo 🧑‍💻

Los cambios realizados en esta rama 'changes' solo se aplicaron en Main.py. Los demás archivos ahora no estan haciendo nada. Esto esta funcionando asi debido a que solo se necesitaba:

- Eliminar recursividad por izquierda.
- Calcular conjunto de primeros.
- Calcular conjunto de siguientes.
- Calcular conjuntos de predicción.
- Definir si es una gramatica LL(1)
- Implementar una funcion por cada no terminal en un ASDR.

## Uso

Para ejecutar el código simplemente hay que clonarlo 

```
git clone https://github.com/Pokloskaya/Compiladores.git
```

y luego ejecutar el archivo main 

```
python Main.py
```
El input debe cumplir la siguiente estructura:


![image](https://github.com/Pokloskaya/Compiladores/assets/83888452/a1df718e-5087-418a-b354-be7d95825e34)






            ._                                            ,
             (`)..                                    ,.-')
              (',.)-..                            ,.-(..`)         
               (,.' ,.)-..                    ,.-(. `.. )                    
                (,.' ..' .)-..            ,.-( `.. `.. )                     
                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                   ( ,.' ,.'    _== ==_     `.. `.. )                        
                    ( ,.'   _==' ~  ~  `==_    `.. )                     
                     \  _=='   ----..----  `==_   )                     
                  ,.-:    ,----___.  .___----.    -..                        
              ,.-'   (   _--====_  \/  _====--_   )  `-..                 
          ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
      ,.-'.'   .'      (          |  |          )      `.   `.-..  
 
