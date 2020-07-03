text=input('Enter a paragraph')
li=text.split(' ')
l=[]
lis=[]
b=dict()
for i in li:
    i=i.lower()
    sortchar=sorted(i)
    s="".join(sortchar)
    l.append(s)
    inpu = l.index(s)


for i in range(len(l)):
    word=l[i]
    for alt in l:
        if word == alt:
            lis.append(word)

# print(lis)
for a in range(len(lis)):
    c=lis.count(lis[a])
    if c==1:
        continue
    b[lis[a]]=c
print('Anagrams are: ')
print(','.join(b))


