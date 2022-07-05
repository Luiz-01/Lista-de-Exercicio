

## Exercício 5

##A empresa “Organizações Tabajaras” precisa de um sistema que faça o controle da folha de pagamento de seus funcionários. 

##Para isso, você deve criar uma classe chamada **Funcionario** que tenha os seguintes atributos: 
 ##- nomeFuncionario -> guarda o nome do funcionário
 ##- departamento -> guarda o departamento
 ##- salarioBruto -> guarda o salário bruto
 ##- anoEntrada -> guarda o ano de entrada na empresa
 ##- anoSaida -> guarda o ano atual ou o ano em que o funcionário saiu da empresa 
 ##- rg -> guarda o RG
 ##- statusEmprego -> valor booleano que indica se o funcionário ainda está trabalhando na empresa ou se já foi demitido
 ##- dependentes -> quantos dependentes o funcionário possui.
 
##O método construtor da classe deverá receber como argumento de entrada todos os atributos indicados acima. Todos eles deverão ser recebidos como atributo obrigatório, exceto os atributos **statusEmprego** e **anoSaida**. O parâmetro associado ao atributo **statusEmprego** deve ser opcional e ter valor *default* igual a **True**. O parâmetro associado ao atributo **anoDemissao** deve ser opcional e ter valor *default* igual a **0**. Na função construtora, caso o parâmetro associado ao atributo **anoDemissao** seja diferente de 0, o atributo **anoDemissao** deve receber o valor informado; senão, deve receber o ano atual.  Para obter o ano atual, você pode usar a biblioteca **datetime** do Python. Veja um exemplo onde a biblioteca **datetime** é usada para calcular o ano em que estamos:

##```
##import datetime

##date = datetime.date.today()
##year = date.strftime("%Y")
##year = int(year)

##print("Ano atual: ", year)
##```

##A classe também deve ter is seguintes métodos: 

 ##- calcSalarioLiquido -> cálcula o salário líquido do funcionário (recebe R\\$ 20,00 por dependente; depois, é descontado um imposto de 3\% para funcionários que ganham até R$ 1000,00 e 5% acima deste valor);

 ##- calcTempoServico -> cálcula o tempo de serviço do funcionário na empresa com base no ano de entrada na empresa e ano atual.

 ##- calcAumento -> calcula o aumento de salário. O cálculo de aumento de salário (com base no salário bruto) é realizado de acordo com os seguintes dados:
 
  ## - Tempo de Serviço menor que 5 anos – o percentual equivale a 5%
    
   ##- Tempo de Serviço maior que 5 anos – o percentual equivale a 8%
   
 ##- retornaInfo -> retorna uma string com os valores de todos dos atributos da classe. Essa string deve conter também o tempo de serviço, salário líquido e aumento de salário obtidos por meio da chamada das respectivas funções. 

 import datetime

class Funcionario:
    
    def __init__(self, nomeFuncionario, departamento, salarioBruto, 
                 anoEntrada, rg, dependentes, statusEmprego = True, anoSaida = 0):
    
        self.nomeFuncionario = nomeFuncionario
        self.departamento = nomeFuncionario
        self.salarioBruto = salarioBruto
        self.anoEntrada = anoEntrada
        self.rg = rg
        self.dependentes = dependentes
        self.statusEmprego = statusEmprego
        
        # se o ano informado for 0, troca pelo ano atual
        if anoSaida == 0:
            date = datetime.date.today()
            anoSaida = date.strftime("%Y")
            self.anoSaida = int(anoSaida)   
            
        else:
            self.anoSaida = anoSaida
        
    def calcSalarioLiquido(self):
        
        valorDependentes = self.dependentes * 20
        
        salario = self.salarioBruto + valorDependentes
        
        if salario<=1000:
            salario = salario - (salario*0.03)
            
        else:
            salario = salario - (salario*0.05)
            
        return salario
    
    def calcTempoServico(self):
        return self.anoSaida - self.anoEntrada
    
    def calcAumento(self):
        
        tempo = self.calcTempoServico()
        
        if tempo<=5:
            return self.salarioBruto*0.05
        else:
            return self.salarioBruto*0.08
    
    def retornaInfo(self):
        
        info = 'Nome: ' + self.nomeFuncionario
        info += '\nRG: ' + self.rg
        info += '\nDepartamento: ' + self.departamento
        info += '\nSalario Bruto: %1.2f' %(self.salarioBruto)
        info += '\nAno entrada: %d' %(self.anoEntrada)
        info += '\nNumero de dependentes: %d' %(self.dependentes)
        info += '\nO funcionário está empregado?: ' + ('sim' if self.statusEmprego == True else "não")
        info += '\nSalario Liquido: %1.2f' %(self.calcSalarioLiquido() )
        info += '\nTempo de serviço: %d' %(self.calcTempoServico() )
        info += '\nAumento: %1.2f' %(self.calcAumento() )
        
        return info


  
##########################################################################

# testando a classe criada
nome = "Pedro Cardoso"
departamento = "TI"
salarioBruto = 5000
anoEntrada = 2000
rg = '192528'
dependentes = 5

func1 = Funcionario(
    nome, departamento, salarioBruto, 
    anoEntrada, rg, dependentes 
    )

salario = func1.calcSalarioLiquido()
tempo = func1.calcTempoServico()
aumento = func1.calcAumento()
info = func1.retornaInfo()
statusFunc = func1.statusEmprego



print('\n\tString retornada pelo método imprimir(): ')

print('\n' + 20*'-')
print('Resultado retornado: ')
print('\t O funcionário está empregado?: %s' %(statusFunc))
print('\t Salario Liquido: %1.2f' %(salario))
print('\t Tempo de serviço: %d anos' %(tempo))
print('\t Aumento: %1.2f' %(aumento))

print('\nInformacoes da classe retornadas pela método retornaInfo: \n%s' %(info))

if not isinstance(info, str):
    print('\nAtenção. O valor retornado pelo método retornaInfo()')
    print('da classe Funcionário deveria ser uma string')