"""
Hash Table- Estrucutra de datos asociatiba relaciona una llave y un valor,
usando una funcion de hash.

* slots, bacekts
"""
import sys

class HashNode:
  def __init__(self, data, key):
    self.data = data
    self.next = None
    self.key = key

class HashTable:
  def __init__(self):
    self.bucket = []
    self.len = 0

  def set(self, key, value):
    index = HashTable.hash(key, self.len)
  
  def search(self, key):
    

  @staticmethod
  def hash(key, length):
    return len(key) & (sys.maxsize * lenght)
