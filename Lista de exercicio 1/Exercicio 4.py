
## Exercício 4

##Crie uma função **recursiva** com o seguinte nome: **retornaMenor**. Essa função deve receber uma lista como parâmetro e retornar o menor número. 

def retornaMenor(lista, idx=0):
    
    # se esta no ultimo elemento da lista
    # vamos dizer que o menor é esse elemento
    if idx==len(lista)-1:
        return lista[idx]
    
    else:
        menor = retornaMenor( lista, idx+1 )
        
        # se o menor elemento é maior que o atual, retorna o atual
        if menor > lista[idx]:
            return lista[idx]
        else:
            return menor


##########################################################################

# testando a função criada
lista = [10,6,2,9,8,23,5]
menor = retornaMenor(lista)

print('Resultado esperado: 2')

print('\n' + 20*'-')
print('Resultado retornado: %d' %(menor) )

