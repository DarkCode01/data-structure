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
  
  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return f"Node({self.value})"

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
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
    return self.size

  def _get_last(self):
    current = self.head

    while current.next:
      current = current.next
    
    return current

  def _create_node(self, value):
    return Node(value)
  
  def is_empty(self):
    return self.size == 0

  def value_at(self, index):
    current = self.head
    _index = 0

    while _index != index:
      current = current.next
      _index += 1
    
    return current

  def push_front(self, value):
    node = self._create_node(value)

    if not self.head:
      self.head = node
      return
    
    old_head = self.head
    node.next = old_head
    self.head = node
    
    self.size += 1

  def push_back(self, value):
    node = self._create_node(value)

    if not self.head:
      self.head = node
      return

    last = self._get_last()
    last.next = node
  
  def pop_front(self):
    old_head = self.head
    new_head = old_head.next
    self.head = new_head

    return old_head

  def pop_back(self):
    current = self.head
    prev = None

    while current.next:
      prev = current
      current = current.next
    
    if prev == None:
      self.head = None
    else:
      prev.next = None

    self.size -= 1

    return  current

  def front(self):
    return self.head

  def back(self):
    return self._get_last()

  def insert(self, index, value):
    node = self._create_node(value)
    current = self.head
    prev= None
    _index = 0

    while _index < index:
      prev = current
      current = current.next
      _index += 1

    prev.next = node
    node.next = current
    self.size += 1

  def erase(self, index):
    current = self.head
    temp = None
    prev= None
    _index = 0

    while _index < index:
      prev = current
      current = current.next
      _index += 1

    if prev:
      prev.next = current.next
    elif not prev and current.next:
      self.head = current.next
    else:
      self.head = None

    self.size -= 1
    temp = current
    del temp

  def reverse(self):
    prev = None
    current = self.head
    temp = None

    while current:
      temp = current.next
      current.next = prev
      prev = current
      current = temp

    self.head = prev

  def remove_value(self, value):
    current = self.head
    prev = None

    if current.value != value:
      while True:
        if current.value == value:
          prev.next = current.next
          del current
          break
        
        prev = current
        current = current.next
    else:
      current = self.erase(0)
      del current
