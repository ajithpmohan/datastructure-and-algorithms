from linked_list_node import Node

class UnorderedList:

  def __init__(self):
    self.head = None


  def is_empty(self):
    return self.head == None

 
  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp


  def append(self,item):
    temp     = Node(item)
    current  = self.head
    previous = None
    while current != None:    
      previous = current
      current  = current.get_next()
    previous.set_next(temp)


  def show_list(self):
    current=self.head
    while current != None:
      yield current.get_data()
      current=current.get_next()


  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.get_next()
    return count


  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found


  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.get_data() == item:
        found = True
      else:
        previous = current
        current = current.get_next()
    if previous == None:
      self.head = current.get_next()
      
    elif current.get_next()==None:
      previous.set_next(None)
      
    else:
      previous.set_next(current.get_next())
   

   
mylist=UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.append(11)
mylist.add(93)
mylist.add(26)
mylist.append(44)
mylist.add(54)
mylist.append(88)
show=mylist.show_list()
print 'Linked List:'
for s in show:  
   print s
print 'Size is now', mylist.size()
print '\n'
mylist.remove(54)
mylist.remove(88)
mylist.remove(17)
mylist.remove(11)
pent=mylist.show_list()
print 'After Item removals'
for s in pent:  
   print s
print 'Size is now',  mylist.size()

