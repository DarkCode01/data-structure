"""
Listas Enlazadas(LinkedList): Permiten representar un grupo de elementos
presentados como una secuencia.
  -> head(primer elemento del la lista)

Nodes(Node): Elementos de una lista enlazada.
  -> value(body)
  -> pointer(next)

Esquema: [32](head) -> ([21] -> [19] -> [72] -> [24])(tail)

En una forma recursiva se representaria de la siguiente forma:
[1] -> [2, 3]; [2] -> [3]; [3] -> []||Null

Desventajas:
  -> No tienen noción de indice, por lo que no podemos hacer accesos
    aleatorio.
  -> Necesitan mas espacio en memoria ya que tienes que almacenar
    los punteros.

metodos:
-> append
-> append_by
-> preppend
-> prepend_by
-> pop
-> pop_by
-> search
-> reverse
"""


class Node:
  def __init__(self, value, _next=None):
    self.value = value
    self.next = _next
  
  def __str__(self):
    return f"Node({self.value})"

class LinkedList:
  def __init__(self):
    self.head = None
  
  def __repr__(self):
    return self.__str__()

  def __str__(self):
    nodes = "LinkedList["
    current = self.head

    while current:
      nodes += f"{str(current)}, "
      current = current.next
  
    nodes += "]"

    return nodes

  def __len__(self):
    _len = 0
    current = self.head

    while current:
      _len += 1
      current = current.next
    
    return _len

  def _get_last(self):
    current = self.head

    while current.next:
      current = current.next
    
    return current

  def append(self, node):
    if self.head:
      last = self._get_last()
      last.next = node
    else:
      self.head = node

  def append_middle(self, node):
    middle = (self.__len__() // 2)
    count = 0
    current = self.head
    temp = None

    while True:
      if count == middle:
        temp = current.next
        current.next = node
        node.next = temp
        break

      count += 1

  def append_by(self, node, reference):
    if self.head and reference:
      node.next = reference.next
      reference.next = node
    elif self.head and not reference:
      self.append(node)
    elif not self.head and reference:
      self.head = reference
      reference.next = node
    else:
      self.head = node

  def prepend(self, node):
    if self.head:
      prev = self.head
      node.next = prev
      self.head = node
    else:
      self.head = node

  def prepend_by(self, node, reference=None):
    if self.head and reference:
      prev = self.head

      while prev.next.value != reference.value:
        prev = prev.next
      
      prev.next = node
      node.next = reference

    elif self.head and not reference:
      self.prepend(node)
    elif not self.head and reference:
      self.head = node
      node.next = reference
    else:
      self.head = node

  def pop(self):
    prev = None
    current = self.head # [1, 2]

    while current.next:
      prev = current
      current = current.next
    
    if prev == None:
      self.head = None
    else:
      prev.next = None

    del current

  def pop_by(self, node):
    current = self.head
    prev = None

    if current.value != node.value:
      while True:
        if current.value == node.value:
          prev.next = current.next
          del current
          break
        
        prev = current
        current = current.next
    else:
      prev = current.next
      self.head = prev
      del current

  def reverse(self):
    # null [1, 2, 3, null]
    prev = None
    current = self.head
    temp = None

    while current:
      temp = current.next
      current.next = prev
      prev = current
      current = temp

    self.head = prev

  def search(self, node):
    current = self.head
    index = 1

    while current:
      if current.value == node.value:
        break

      current = current.next
      index += 1
    
    return index
