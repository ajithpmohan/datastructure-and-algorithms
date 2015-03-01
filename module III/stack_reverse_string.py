#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.

class Stack:
  
  def __init__(self):
    self.item=[]
  
  def push(self,item):
    self.item.insert(0,item)

  def __str__(self):
    return str(''.join(self.item))


def rev_string(my_str):
  reverse=Stack()
  for i in my_str:
    reverse.push(i)
  return reverse

print rev_string('helloworld')














