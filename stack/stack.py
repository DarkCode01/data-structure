"""
  LIFO -> Last in, firts out

  -> push
  -> pop
  -> peek
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return f"Node({self.value})"

class Stack:
  def __init__(self, capacity):
    self.peek = None
    self.capacity = capacity
    self.size = 0

  def __len__(self):
    return self.size

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    nodes = "Queue("
    current = self.peek

    while current:
      nodes += f"<- [{str(current)}]"
      current = current.next
  
    nodes += ")"

    return nodes

  def create_node(self, value):
    return Node(value)

  def is_overflow(self):
    return self.size == self.capacity

  def is_empty(self):
    return self.size == 0

  def push(self, value):
    if not self.is_overflow():
      node = self.create_node(value)

      if not self.peek:
        self.peek = node
      else:
        temp = self.peek
        node.next = temp
        self.peek = node
      
      self.size += 1
    else:
      print(f'Error: Stack-Overflow exceded max call ({self.capacity})')

  def pop(self):
    if not self.is_empty():
      if self.peek.next:
        temp = self.peek
        new_peek = temp.next
        self.peek = new_peek
        del temp
      else:
        self.peek = None

      self.size -= 1
    else:
      print("Error: Non value on stack")
