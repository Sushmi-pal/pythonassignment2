import csv

info=[('Name','Address','Age'),('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

f=open('info.csv','w')
with f:

    writer=csv.writer(f)

    writer.writerows(info)
    f.close()





