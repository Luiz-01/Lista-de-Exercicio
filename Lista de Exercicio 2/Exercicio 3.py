
## Exercício 3

##Modifique o código da Pilha Estática para criar uma variação da pilha chamada de PilhaDupla.
##Nessa estrutura de dados, duas pilhas A e B devem compartilhar o mesmo vetor (list), conforme mostrado na seguinte figura:

##A estrutura de dados deverá ter as seguintes funções:
 ##- pushA(): insere um valor no topo da pilha A 
 ##- pushB(): insere um valor no topo da pilha B
 ##- popA(): remove o valor do topo da pilha A 
 ##- popB(): remove o valor do topo da pilha A 
 ##- clearA(): remove os valores da pilha A 
 ##- clearB(): remove os valores da pilha B 
 ##- __str__(): imprime a pilha completa, contendo as pilha A e B.
 
##Só deve ser emitida uma mensagem de pilha cheia se todas as posições do vetor estiverem ocupadas. 
##Você **não** deve reservar metade do vetor para a PilhaA e metade para a PilhaB. 
##Elas podem crescer enquanto houver espaço vazio no vetor e podem ter tamanhos diferentes ao longo da execução do algoritmo.

        
class PilhaDupla:
    def __init__(self, capacity):
        self.capacity = capacity
        self.topA = -1
        self.topB = capacity
        self.counterSizeA = 0
        self.counterSizeB = 0
        self.freeSize = capacity

        # inicializa a pilha com o tamanho desejado
        self.pilha = [None] * capacity

    def pushA(self, data):
        """
        Adiciona um elemento no topo da pilha A
        """
        if self.freeSize == 0:
            print("Erro! A pilha está cheia")
            return

        if self.capacity == self.topA + 1:
            print("Estouro de pilha")
            return

        self.topA = self.topA + 1
        self.pilha[self.topA] = data
        self.freeSize = self.freeSize - 1
        self.counterSizeA += 1

    def pushB(self, data):
        """
        Adiciona um elemento no topo da pilha B
        """
        if self.freeSize == 0:
            print("Erro! A pilha está cheia")
            return

        if self.topB == -1:
            print("Estouro de pilha")
            return
        
        self.pilha[self.topB-1] = data
        self.topB = self.topB - 1
        self.freeSize = self.freeSize - 1
        self.counterSizeB += 1

    def popA(self):
        """
        Retorna e remove o elemento do topo da pilha A
        """
        if self.topA == -1:
            print("Pilha vazia")
            return
    
        temp = self.pilha[self.topA]
        self.pilha[self.topA] = None
        self.topA = self.topA - 1
        self.freeSize += 1
        self.counterSizeA -= 1

        return temp
    
    def popB(self):
        """
        Retorna e remove o elemento do topo da pilha
        """
        if self.topB == self.capacity:
            print("Pilha vazia")
            return
    
        temp = self.pilha[self.topB]
        self.pilha[self.topB] = None
        self.topB = self.topB + 1
        self.freeSize += 1
        self.counterSizeB -= 1

        return temp
    
    def clearA(self):
        """
        Limpa a pilha A
        """
        while self.topA != -1:
          self.popA()

    def clearB(self):
        """
        Limpa a pilha B
        """
        while self.topB != self.capacity:
          self.popB()


    def __str__(self):
        stringHelper = '['

        # se tem itens na pilha A, adiciona o parenteses no inicio
        if self.counterSizeA > 0:
          stringHelper += '('

        for index, value in enumerate(self.pilha):
          # se o valor atual no loop for none, coloca uma string vazia no lugar
          # se não, insere o valor atual
          stringHelper += '' if value is None else str(value)
          
          # adiciona o - apenas se não for o topo da pilha A e não for o último
          if index != self.topA and index != self.capacity - 1: 
            stringHelper += ' - '

          # se for o ultimo item da pilha A, fecha os parenteses da pilha A
          if index == self.topA:
            stringHelper += ') - '

          # se a pilha B tem itens e o index for o topo da pilha B
          if self.counterSizeB > 0 and index == self.topB - 1:
            stringHelper += '('
        
        # se tem itens na pilha B, adiciona o parenteses no final
        if self.counterSizeB > 0:
          stringHelper += ')'
        
        stringHelper += ']'
        
        return stringHelper
        
    
##########################################################################

# testando a classe criada
pilha = PilhaDupla(capacity = 5)

pilha.pushA(5)
print(pilha)

pilha.pushB(7)
print(pilha)

pilha.pushA(6)
print(pilha)

pilha.pushB(9)
print(pilha)

pilha.pushA(15)
print(pilha)

pilha.pushB(14)
print(pilha)

pilha.popA()
print(pilha)

pilha.pushB(14)
print(pilha)

pilha.clearA()
print(pilha)

pilha.pushA(6)
print(pilha)

pilha.clearB()
print(pilha)