class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def push_first(self, item):
    self.items.insert(0, item)
  
  def pop_first(self):
    return self.items.pop(0)
  
  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

