lioftuples=[('Sabin','Palikhe',20),('Shruti','Sinha',22),('Neha','Mahto',23)]
l=[]
total=0
for i in range(len(lioftuples)):
    li=lioftuples[i][2]
    l.append(li)
print(l)
for ele in range(0, len(l)):
    total = total + l[ele]
avg=total/len(l)
print(avg)

for i in lioftuples:
    if i[2]>avg:
        print(i[0]+' '+i[1]+' is older')
    else:
        print(i[0]+' '+i[1]+' is younger')