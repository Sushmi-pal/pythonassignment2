def conv(data,sign):
    a=''
    a=data[0].lower()
    for i in data[1:]:
        if i==i.capitalize():
            a=a+sign
            a=a+i.lower()
        else:
            a=a+i
    print(a)

conv('ThisIsCamelCaseString','_')
conv('ThisIsCamelCaseString','-')