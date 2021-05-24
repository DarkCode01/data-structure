class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

  def __repr__(self):
    return self.__str__()
  
  def __str__(self):
    return f"Node({self.value})"


class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    nodes = "DoublyLinkedList["
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

  def create_node(self, value):
    return Node(value)
  
  def get_last(self):
    current = self.head

    while current.next:
      current = current.next
    
    return current

  def append(self, value):
    node = self.create_node(value)
    current = self.head
    prev = None
    
    if not current:
      self.head = node
      return

    while current.next:
      current = current.next

    current.next = node
    node.prev = current

  def prepend(self, value):
    node = self.create_node(value)
    current = self.head

    if current:
      current.prev = node
      node.next = current

    self.head = node

  def add(self, value, position=None):
    current = self.head
    node = self.create_node(value)
    index = 1

    if not current:
      self.head = node

    if not position:
      self.append(value)
      return

    if position == index:
        current.prev = node
        node.next = current
        self.head = node

    while current.next:
      if index == position:
        current.prev.next = node
        current.prev = node
        node.next = current

      current = current.next
      index += 1

  def pop_beginning(self):
    old_head = self.head

    if not old_head.next:
      self.head = None
      del old_head
      return

    new_head = self.head.next
    old_head.next = None
    new_head.prev = None

    self.head = new_head
    del old_head

  def pop(self):
    last = self.get_last()

    if not self.head.next:
      self.head = None
    else:
      last.prev.next = None
    
    del last

  def pop_position(self, position):
    current = self.head
    temp = None
    index = 1

    if position <= index:
      self.pop_beginning()
      return

    if position >= self.__len__():
      self.pop()
      return

    while index != position:
      current = current.next
      index += 1

    temp = current
    temp.prev.next = current.next
    temp.next.prev = temp.prev
  
    del current

  def max(self):
    current = self.head
    _max = current.value

    while current:
      if current.value >= _max:
        _max = current.value
    
      current = current.next

    return _max

