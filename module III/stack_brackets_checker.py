from stack import Stack

def brackets(symbols):
  
  a=Stack()
  balanced=True
  index=0

  def matches(open,close):
    opens='([{'
    closes=')]}'
    return opens.index(open)==closes.index(close)
  
  while (index<len(symbols)) and (balanced):
    symbol=symbols[index]
    if symbol in '({[':
      a.push(symbol)
    else:
      if a.is_empty():
        balanced=False
      else:
        top=a.pop()
        if not matches(top,symbol):
          balanced=False
            
    index+=1

  if balanced and a.is_empty():
    return True
  else:
    return False
  
print brackets('{({[{}]})}')
print brackets('({[}{]})')
