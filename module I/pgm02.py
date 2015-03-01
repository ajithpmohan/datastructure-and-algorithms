# Modify the given code using list comprehensions.For an extra challenge, see if you can figure out how to remove the duplicates.

'''
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
  for a_letter in a_word:
    if a_letter not in letter_list:      
      letter_list.append(a_letter)
'''

letter_list = []
[(letter_list.append(a_letter)) for a_word in ['cat','dog','rabbit']  for a_letter in a_word ]


print letter_list
