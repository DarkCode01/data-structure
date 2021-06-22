"""
Es un arbol binario extendido.

Un arbol binario sera de busqueda si:
-> si iene una subraiz izquierdo, la raiz del subarbol ixquierdo
es menor a R, y a la vez el subarbol izquierdo tambien es de busqueda.

-> si tiene un subarbol derecho, la raiz del subarbol derecho es
mayor a R y a la vez el subarbol derecho tambien es de busqueda.

Ejemplo:
                     ┌────┐
                     │ 16 ├───┐
               ┌─────┴────┘   │
               │              │
            ┌──┴─┐        ┌───┴──┐
            │ 8  │        │   24 │
        ┌───┴───┬┘        └─┬────┘
        │       │           │
        │       │           │
    ┌───┴─┐   ┌─┴──┐    ┌───┴──┐
    │  3  │   │ 13 │    │  19  │
    └──┬──┘   └────┘    │      ├─────┐
       │                └──────┘     │
       │                             │
       │                          ┌──┴────┐
       ├──────┐                   │       │
       │      │                   │  21   │
       │  7   │                   │       │
       └──────┘                   └───────┘

Ejemplos de uso:
-> Almacenar enteros de menor a mayor: 5 < 12
-> almacenar cadenas de caracteres por orden lexicografico: "Alicia" < "Benito"
-> Almacenar objetos siempre que se identifiquen por alguna clave que si sea
ordenable: libros usando como clave el ISBN; personas usando como clave el
codigo de empleado.

Search:
-> exists?
-> get
-> insert
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert(node, value):
  if not node:
    return Node(value)
  
  if value > node.value:
    node.right = insert(node.right, value)
  if value < node.value:
    node.left = insert(node.left, value)

  return node
