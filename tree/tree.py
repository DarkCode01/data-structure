"""
Tree:
  -> Son estructuras no lineales.
  -> En un tree los nodos pueden apuntar a un numero indefinido de elementos.
  -> No deben de ser circular.

Teoria:
  * Los elementos seran un Node
  * Los Nodes pueden apuntar a otros nodes.
  * Parent Node: Node que apunta a nuestro Node.
  * Child Node: Nodes a los que apunta nuestro node.
  * Root Node: No tiene Parent Node.
  * Leaf Node: No tiene Child Nodes

Propiedades:
  -> Nivel: distancia del Root Node al Leaf Node.
  -> Altura/Profundidad: maximo nivel de un Tree

Tipos de Tree:
  -> Tree Binary

Operaciones:
  -> insert
  -> delete
  -> location
  -> path

Ojo: Es bueno tener un numero reducido de hijos.

Hemos dicho que los árboles son un tipo de grafo,
de hecho son grafos acíclicos dirigidos y mínimamente conectados.

Full Binary Tree:
  -> Tienen hijos o hojas;
  -> 
Complete Binary Tree:
  -> El ultimo nivel puede permitirse el prescindir de algunos de sus hijos.
  -> El padre del nodo hoja solo tiene un hijo.
  -> El nodo hoja debe ser el de la izquierda.
Degenerate Tree:
  -> Los padres solo tienen un hijo.
Balanced Tree:
  -> Inetnta mantener la profundidad de sus dos subarboles al menor posible.
  -> El balanceo o equilibrio de un arbol hace que algunas operaciones sean mas eficientes.
  -> Algunos arboles especiales se aprovechan del balanceo. Dependiendo de que tipo de balanceo intentemos
  user se usa una regla u otra distinta.


Depth-Firts Search (DFS)
Es un algoritmo para atravesar o buscar en un tree. Empieza desde el root y explora todos
los nodos posibles, tiene diferentes tipos:
- pre-order: raiz, izquierdo, derecho.
- in-order: izquierdo, raiz, derecho.
- post-order: izquierdo, derecho, raiz.


Bradth-Firts Search (BFS):
Algoritmo para atravesar o buscar en un tree empezando desde el root y explorando 
cada unos de los nodos del mismo nivel, es decir, atravieza el tree nivel por nivel.
"""

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def insert_left(self, value):
    if self.left_child == None:
      self.left_child = BinaryTree(value)
    else:
      new_node = BinaryTree(value)
      new_node.left_child = self.left_child
      self.left_child = new_node

  def insert_right(self, value):
    if self.right_child == None:
        self.right_child = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.right_child = self.right_child
        self.right_child = new_node

  def pre_order(self):
    print(self.value)

    if self.left_child:
      self.left_child.pre_order()
    
    if self.right_child:
      self.right_child.pre_order()

  def in_order(self):
    if self.left_child:
      self.left_child.in_order()
    
    print(self.value)

    if self.right_child:
      self.right_child.in_order()

  def post_order(self):
    if self.left_child:
      self.left_child.post_order()
    
    if self.right_child:
      self.right_child.post_order()

    print(self.value)


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child
