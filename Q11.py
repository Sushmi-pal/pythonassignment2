checktext='readme.txt'
countdot=checktext.count('.')
b=checktext.find('.')
l=list(checktext)
# finding extensions
if countdot==1:
    s=l[b+1:]
    print('Extension:')
    print(''.join(s))

if countdot==2:
    c=checktext.find('.',b+1)
    l=list(checktext)
    s=l[b+1:c]
    t=l[c+1:]
    print('Extension:')
    print(''.join(s))
    print(''.join(t))


# finding filename
splitlist=l[0:b]
listjoin=''.join(splitlist)
print('Filename',listjoin)

