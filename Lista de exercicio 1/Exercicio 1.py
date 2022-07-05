
## Exercício 1

##Crie uma classe chamada **CalcCientifica** que tenha o seguinte atributo: 
 ##- numero -> guarda um número 
 
##O método construtor da classe deverá receber como argumento de entrada o atributo indicado acima. 

##A classe também deve ter is seguintes métodos: 

##- potencia -> retorna o atributo **numero** da classe elevado a um expoente.

     ##- esse método deve receber um parâmetro chamado **expoente** que deve ser opcional e possui valor **default** igual a 2.  Esse parâmetro receberá o expoente da potenciação. No Python, para você fazer b elevado a c, você pode usar ```b**c```. 
     
 ##- raiz -> retorna a raiz do atributo **numero** da classe. 

     ##- esse método deve receber um parâmetro chamado **indice** que deve ser opcional e possui valor **default** igual a 2.  Esse parâmetro receberá o índice da raiz. Lembre-se que para fazer o cálculo da raiz, você pode usar potenciação: $\sqrt[b]{a}$ é o mesmo que $a^{\frac{1}{b}}$.  

 ##- fatorial -> retorna o fatorial do atributo **numero** da classe. O código de método pode ser igual ao código mostrados na aula de recursividade da disciplina. 

class CalcCientifica:
    
    def __init__(self,numero):
        self.numero = numero
        
    def raiz(self, indice = 2):
        return self.numero**(1/indice)

    def potencia(self, expoente = 2):
        return self.numero**(expoente)
    
    def fatorial(self, n=-1):
        """
        fatorial com recursao
        """
        
        if n==-1:
            n = self.numero
            
        if n < 2:
            return 1
        else:
            return n * self.fatorial(n-1)        
        
    

##########################################################################

# testando a classe criada
num1 = 9
num2 = 8

# cria dois objetos - um para cada numero
calc1 = CalcCientifica(num1)
calc2 = CalcCientifica(num2)

# calcula a raiz quadra 
raiz1 = calc1.raiz()
raiz2 = calc2.raiz(indice=3)

# calcula a raiz quadra 
potencia1 = calc1.potencia()
potencia2 = calc2.potencia(expoente=4)

# calcula o fatorial
fact1 = calc1.fatorial()
fact2 = calc2.fatorial()

print('\n' + 20*'-')
print('Resultado retornado: ' )
print('\tRaiz quadrada de %d: %d' %(num1,raiz1))
print('\t%d elevado a 2: %d' %(num1,potencia1))
print('\tFatorial de %d: %d' %(num1,fact1))

print('\n\tRaiz cubica de %d: %d' %(num2,raiz2))
print('\t%d elevado a 4: %d' %(num2,potencia2))
print('\tFatorial de %d: %d' %(num2,fact2))

