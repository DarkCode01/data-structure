class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return f"Node({self.value})"

class Queue:
  def __init__(self, capacity):
    self.front = None
    self.rear = None
    self.size = 0
    self.capacity = capacity

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    nodes = "Queue("
    current = self.front

    while current:
      nodes += f"[{str(current)}] -> "
      current = current.next
  
    nodes += ")"

    return nodes

  def __len__(self):
    return self.size

  def create_node(self, value):
    return Node(value)

  def is_full(self):
    return self.size == self.capacity
  
  def is_empty(self):
    return self.size <= 0

  def enqueue(self, value):
    if not self.is_full():
      node = self.create_node(value)

      if not self.front:
        self.front = node
        self.rear = node
      else:
        self.rear.next = node
        self.rear = node
      
      self.size += 1
    else:
      print("Error: Queue is full")

  def dequeue(self):
    if not self.is_empty():
      to_process = self.front 
      self.front = to_process.next
      to_process.next = None
      self.size -= 1

      if not self.front:
        self.rear = None

      return to_process
    else:
      print("Error: Queue is empty")

  def peek(self):
    return self.front
