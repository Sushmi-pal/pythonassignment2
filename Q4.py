'''4.

    The id of list while appending my friends name is the same.'''

li=[]
print(id(li))
li.append('Sushmita')
print(id(li))
li.append('Sanima')
print(id(li))
li.append('Sabin')
print(id(li))
# sorting
li.sort()
print(li)
print('First item on the list is {}'.format(li[0]))
print('Second item on the list is {}'.format(li[1]))