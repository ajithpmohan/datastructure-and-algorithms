#In HTML tags exist in both opening and closing forms(<html>,</html>) and must be balanced to properly describe a web document. Write a program that can check an HTML document for proper opening and closing tags.

import re

from stack import Stack

def tags(file):

  tag=Stack()
  balanced=True
  index=0
  f=open(file,'r')
  strings=f.readlines()
  
  while (index<len(strings)) and (balanced):
    matches=re.findall('<[/\w]*>',strings[index])
    for match in matches:
      if '/' not in match:
        tag.push(match)
      elif (not tag.is_empty()) and (tag.peek()==(match[:1]+match[2:])):
        tag.pop()
      else:
        balanced=False 
    index+=1

  if balanced and tag.is_empty():
    return True
  else:
    return False


print tags('html.txt') 
