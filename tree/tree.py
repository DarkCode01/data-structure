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
"""
