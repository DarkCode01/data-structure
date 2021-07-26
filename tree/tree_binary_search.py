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


class BTS:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def insert_node(self, value):
    if value <= self.value and self.left_child:
      self.left_child.insert_node(value)
    elif value <=self.value:
      self.left_child = BTS(value)
    elif value >= self.value and self.right_child:
      self.right_child.insert_node(value)
    else:
      self.right_child = BTS(value)

  def find_node(self, value):
    if value < self.value and self.left_child:
      return self.left_child.find_node(value)
    if value > self.value and self.right_child:
      return self.right_child.find_node(value)
    
    return value == self.value

  def remove_node(self, value, parent):
    if value < self.value and self.left_child:
        return self.left_child.remove_node(value, self)
    elif value < self.value:
        return False
    elif value > self.value and self.right_child:
        return self.right_child.remove_node(value, self)
    elif value > self.value:
        return False
    else:
        if self.left_child is None and self.right_child is None and self == parent.left_child:
            parent.left_child = None
            self.clear_node()
        elif self.left_child is None and self.right_child is None and self == parent.right_child:
            parent.right_child = None
            self.clear_node()
        elif self.left_child and self.right_child is None and self == parent.left_child:
            parent.left_child = self.left_child
            self.clear_node()
        elif self.left_child and self.right_child is None and self == parent.right_child:
            parent.right_child = self.left_child
            self.clear_node()
        elif self.right_child and self.left_child is None and self == parent.left_child:
            parent.left_child = self.right_child
            self.clear_node()
        elif self.right_child and self.left_child is None and self == parent.right_child:
            parent.right_child = self.right_child
            self.clear_node()
        else:
            self.value = self.right_child.find_minimum_value()
            self.right_child.remove_node(self.value, self)

        return True

  def clear_node(self):
    self.value = None
    self.left_child = None
    self.right_child = None

  def find_minimum_value(self):
    if self.left_child:
        return self.left_child.find_minimum_value()
    else:
        return self.value
