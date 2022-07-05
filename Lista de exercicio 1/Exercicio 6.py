
## Exercício 6 

##Cria uma função chamada **buscaBinaria**. 
##Essa função deve modificar o algoritmo de busca binária para que retorne o índice da primeira e da última ocorrência de um número em uma lista. 
##Por exemplo, se você informar a lista [1,2,3,3,3,4,5,6] e pedir para buscar o número 3, ele deverá retornar como resultado os valores 2 e 4, que correspondem respectivamente a posição da primeira e última posição onde o número 3 ocorreu. 
##Se o número buscado não for encontrado, o algoritmo deverá retornar -1 e -1.
def buscaBinaria(lista, valorBusc, primeiroIndice=0, ultimoIndice=-1, menorEncontrado = -1, maiorEncontrado=-1):

  # inicializa qual o último índice da lista
  if ultimoIndice==-1:
        ultimoIndice = len(lista)-1
        
  # obtem o indice do meio da lista
  meio = int( (primeiroIndice+ultimoIndice)/2 )

  # primeiro caso base da recursao
  # se o índice do inicio da lista for maior que o último
  # significa que toda a lista ja foi analisada
  if primeiroIndice > ultimoIndice:  
    return menorEncontrado, maiorEncontrado
        
  # se o elemento do meio foi igual ao buscado
  # atualiza o menor valor encontrado e o maior valor encontrado
  # e busca na primeira metade e na segunda metade pois pode haver 
  # valores repetidos 
  elif lista[meio] == valorBusc:
    
    if menorEncontrado == -1 or meio <= menorEncontrado:
       menorEncontrado = meio

    if meio >= maiorEncontrado:
      maiorEncontrado = meio
    
    # se existir algum elemento antes do indice do meio, 
    # procura por valores repetidos na primeira metade da lista
    if meio-1 >= primeiroIndice:
        auxMenor, auxMaior = buscaBinaria(lista, valorBusc, primeiroIndice, meio-1, menorEncontrado, maiorEncontrado)

        # se o menor indice for diferente de -1 e menor que o atual, atualiza
        if auxMenor != -1 and (auxMenor < menorEncontrado or menorEncontrado==-1):
            menorEncontrado = auxMenor
    
        # se o maior indice for maior que o atual, atualiza
        if auxMaior > maiorEncontrado:
            maiorEncontrado = auxMaior

    # se existir algum elemento após do indice do meio,         
    # procura por valores repetidos na segunda metade da lista
    if meio+1 <= ultimoIndice:
        auxMenor, auxMaior = buscaBinaria(lista, valorBusc, meio+1, ultimoIndice, menorEncontrado, maiorEncontrado)
        
        # se o menor indice for diferente de -1 e menor que o atual, atualiza
        if auxMenor != -1 and (auxMenor < menorEncontrado or menorEncontrado==-1):
            menorEncontrado = auxMenor
    
        # se o maior indice for maior que o atual, atualiza
        if auxMaior > maiorEncontrado:
            maiorEncontrado = auxMaior
            
    return menorEncontrado, maiorEncontrado
  

  else:
      
    if valorBusc <= lista[meio]:
    
      # atualiza o ultimo indice para a proxima busca analisar 
      # só o que estiver antes do meio
      ultimoIndice = meio-1
      
    else:
      # atualiza o primeiro indice para a proxima busca analisar 
      # só o que estiver depois do meio
      primeiroIndice = meio+1
    
    auxMenor, auxMaior = buscaBinaria(lista, valorBusc, primeiroIndice, ultimoIndice, menorEncontrado, maiorEncontrado)
 
    # se o menor indice for diferente de -1 e menor que o atual, atualiza
    if auxMenor != -1 and (auxMenor < menorEncontrado or menorEncontrado==-1):
        menorEncontrado = auxMenor

    # se o maior indice for maior que o atual, atualiza
    if auxMaior > maiorEncontrado:
        maiorEncontrado = auxMaior

    # se o menor encontrado for -1, faz ele receber o maior
    if menorEncontrado==-1:
        menorEncontrado = maiorEncontrado
        
    # se o maior encontrado for -1, faz ele receber o menor
    elif maiorEncontrado==-1:
        maiorEncontrado = menorEncontrado
        
    return menorEncontrado, maiorEncontrado


##########################################################################

# testando a função criada
lista = [1,2,3,4,5,5,5,5,5,6,7,8,8,8,9,10]

print('\n' + 30*'=' + '\nPrimeiro teste')
numBuscado = 5
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)

print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))

print('\n' + 30*'=' + '\nSegundo teste')
numBuscado = 50
firstIndex, lastIndex = buscaBinaria(lista, numBuscado)


print('\n' + 20*'-')
print('Resultado retornado:' )
print('\tPrimeiro índice: %d' %(firstIndex))
print('\tÚltimo índice: %d' %(lastIndex))



