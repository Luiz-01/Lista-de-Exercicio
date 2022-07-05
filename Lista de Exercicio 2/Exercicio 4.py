

##Acrescente a função *verificaBalanceamento* na **árvore binária de busca** ensinada na disciplina. Essa função deve retornar duas saídas:
 ##- a primeira deve ser um valor *booleano*: *true* indica que a árvore está balanceada e *false* indica que a árvore está desbalanceada. 
 ##- a segunda deve ser uma *string*. Essa string deve conter o fator de balanceamento de cada nó da árvore. Para preencher a string, deve ser usado o percurso pré-ordem. 
   ##- Exemplo: suponha que tenham sido inseridos os seguintes elementos na árvore, respectivamente: 17, 6, 35, 4, 2, 48.
##A string retornada pela função deve conter: 1( 2( -1( 0( ) ) ) -1( 0( ) ) ).


class Node:
  def __init__(self, data = None):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, data, node = None):
    if self.root == None:
      self.root = Node(data)
      return
        
    if node is None: 
      node = self.root
    if data < node.data:
      if node.left is None:
        node.left = Node(data)
      else:
        self.insert( data, node.left )
    else:
      if node.right is None:
        node.right = Node(data)
      else:
        self.insert( data, node.right )   

  # function to find height of binary tree
  def height(self, root):
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(self.height(root.left), self.height(root.right)) + 1

  def verificaBalanceamento(self):
    # Uma árvore binária vazia é balanceada.
    if self.root is None:
        return [True, 0]

    root = self.root
    isBalanced = True
    
    while root is not None:
      # pega em loop a altura da esquerda e direita para verificar se esta balanceado
      leftHeight = self.height(root.left)
      rightHeight = self.height(root.right)
      
      # se o valor absoluto for maior que 1, nao esta balanceada.
      if abs(leftHeight - rightHeight) > 1:
        isBalanced = False

      # altera para o valor disponivel na esquerda ou direita
      if root.left is not None:
        root = root.left
      elif root.right is not None:
        root = root.right
      else:
        root = None

    info = self.strPreorder(self.root)
    return [isBalanced, info]


  # Retorna recursivamente o balanceamento da árvore, utilizando pre ordem
  def strPreorder(self, node = -1, info = ''):
    if self.root is None:
      return ' '
            
    if node == -1:
      node = self.root
          
    leftHeight = self.height(node.left)
    rightHeight = self.height(node.right)
    if node.data is not None:
      info += ' ' + str(leftHeight - rightHeight)
      info += '('
                
      if node.left is not None: 
        info += self.strPreorder(node.left)
                
      if node.right is not None:
        info += self.strPreorder(node.right)
      info += ' )'            
      return info
    return info        
        

##########################################################################



#---------------------    
# testando a arvore

tree = Tree()
tree.insert(17)
tree.insert(6)
tree.insert(35)
tree.insert(4)
tree.insert(5)
tree.insert(48)

estaBalanceada, balanceamento = tree.verificaBalanceamento()

print('Resultado retornado:' )
print('\tEstá balanceada: ', estaBalanceada)
print('\tBalanceamento: %s' %(balanceamento))