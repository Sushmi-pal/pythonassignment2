myinfo=('Sushmita','Palikhe',22)
liofpeople=[]
liofpeople.append(myinfo)
moreinfo=('Sanima','Palikhe',25)
liofpeople.append(moreinfo)
more=('Sabin','Palikhe',20)
liofpeople.append(more)
print('sorting by age')
liofpeople.sort(key=lambda x:x[2])
print(liofpeople)
print('sorting by firstname')
liofpeople.sort(key=lambda x:x[0])
print(liofpeople)

