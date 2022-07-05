
## Exercício 2 

##Crie uma função **recursiva** com o seguinte nome: **retornaImpares**. 
##Essa função deve receber um número digitado como parâmetro e retornar uma **string** com todos os números ímpares de 0 até o número digitado separados por um espaço em branco. 
##Por exemplo, ser for passado o número 8 como entrada, deve retornar: "1 3 5 7".
def retornaImpares(num, aux=1):
    
    if aux==num: 
        
        if (aux%2)==0:
            return ""
        else:
            return str(aux)
    
    elif (aux%2)==0:
        return retornaImpares(num, aux+1) 
    
    else:
        return str(aux) + " " + retornaImpares(num, aux+1)


##########################################################################

# testando a função criada
impares = retornaImpares(8)

print('Resultado esperado:')
print('\t1 3 5 7')

print('\n' + 20*'-')
print('Resultado retornado:')
print('\t'+impares)

if impares != '1 3 5 7' and impares != '1 3 5 7 ':
    print('\nAtenção! Seu resultado foi diferente do que era esperado')

