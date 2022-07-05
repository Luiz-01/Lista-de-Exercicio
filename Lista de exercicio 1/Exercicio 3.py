
## Exercício 3

##Faça uma função chamada **contaPalavras**. Essa função deve receber uma lista como entrada. 

##Cada elemento da lista recebida pela função é uma outra lista de palavras. 

##A função deve retornar o total de palavras sem contar as repetições, a palavra que mais se repetiu e a palavra que menos repetiu.

def retornaMaximo(lista):
    """
    Retorna o índice do maior valor de uma lista
    """
    maior = lista[0]
    idxMaior = 0
    for i in range(1, len(lista) ):
        if maior < lista[i]:
            maior = lista[i]
            idxMaior = i
            
    return idxMaior

def retornaMinimo(lista):
    """
    Retorna o índice do menor valor de uma lista
    """
    menor = lista[0]
    idxMenor = 0
    for i in range(1, len(lista) ):
        if menor > lista[i]:
            menor = lista[i]
            idxMenor = i
            
    return idxMenor

def getIndex(lista, word):
    """
    Retorna o indice em que uma palavra aparece na lista
    Se a palavra nao estiver na lista, retorna -1
    """

    # percorre a lista para achar a palavra buscada
    for i in range(len(lista)):
        if word == lista[i]:
            return i
        
    return -1
    
def contaPalavras(lista):
    """
    Retorna a qtd. de palavras, a palavra que mais se repetiu
    e a que menos se repetiu
    """
    
    listaSemRepeticao = []
    qtdRepeticoes = []
    
    # percorre as linhas da lista
    for i in range( len(lista) ):
        
        # percorre as palavras da lista de indice i
        for j in range( len(lista[i]) ):
        
            word = lista[i][j]
            
            # obtem o indice onde a palavra aparece na lista sem repeticao
            # se ela nao existir, irá retornar -1
            idx = getIndex( listaSemRepeticao, word )
            
            # se a palavra não estiver na lista, insere e inicia a qtd de repeticoes daquela palavra em zero
            if idx == -1:
                listaSemRepeticao.append( word )
                qtdRepeticoes.append(1)
                
            else:
                # incrementa a qtd de vezes que a palavra se repetiu
                qtdRepeticoes[idx] += 1
      
    # total de palavras sem repeticao
    qtdPalavras = len( listaSemRepeticao ) 
    
    # palavra que menos se repete
    idxMin = retornaMinimo(qtdRepeticoes)
    palavraMenosRepetida = listaSemRepeticao[idxMin] 
    
    # palavra que menos se repete
    idxMax = retornaMaximo(qtdRepeticoes)
    palavraMaisRepetida = listaSemRepeticao[idxMax] 
                   
    return qtdPalavras, palavraMaisRepetida, palavraMenosRepetida

##########################################################################

# testando a função criada
lista = [
    ['Angola','Chade','Gana'],
    ['Chade','Angola','Gana','Togo'],
    ['Togo','Gana','Chade','Eritreia'],
    ['Chade','Togo','Angola']
]

total, maisRepetida, menosRepetida = contaPalavras(lista)

print('\n' + 20*'-')
print('Resultado retornado:')
print('\tTotal: %d' %(total)) 
print('\tPalavra que mais repetiu: %s' %(maisRepetida)) 
print('\tPalavra que menos repetiu: %s' %(menosRepetida))

