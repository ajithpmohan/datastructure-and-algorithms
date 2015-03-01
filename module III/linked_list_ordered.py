from linked_list_node import Node

class OrderedList:

  def __init__(self):
    self.head = None


  def is_empty(self):
    return self.head == None


  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.get_next()
    return count


  def show_list(self):
    current=self.head
    while current != None:
      yield current.get_data()
      current=current.get_next()


  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.get_data() == item:
        found = True
      else:
        if current.get_data() > item:
          stop = True
        else:
          current = current.get_next()
    return found


  def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.get_data() > item:
        stop = True
      else:
        previous = current
        current = current.get_next()
    temp = Node(item)
    if previous == None:
      temp.set_next(self.head)
      self.head = temp
    else:
      temp.set_next(current)
      previous.set_next(temp)


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

      

mylist=OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
show=mylist.show_list()
print 'Ordered Linked List:'
for s in show:  
   print s
print 'Size is now', mylist.size()
print '\n'
mylist.remove(26)
mylist.remove(93)
pent=mylist.show_list()
print 'After Item removals'
for s in pent:  
   print s
print 'Size is now',  mylist.size()


